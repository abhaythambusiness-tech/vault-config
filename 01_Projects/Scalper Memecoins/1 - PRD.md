---
type: doc-software
doc: prd
proyecto: 01_Projects/Scalper Memecoins
status: aprobado
date: '2026-10-21'
origen: mixto
---


# 1 · PRD — Scalper Memecoins

> [!resumen]
> Bot de **scalping de memecoins en papel** (cartera virtual, precios y costes reales) que corre entero en el servidor Zorin (`ssh@192.168.0.100`) y tiene un **panel web en vivo** con ganancias y decisiones. **Laya** (clasificador de texto, `NandhaKishorM/laya`) decide comprar / mantener / vender y descarta estafas antes de entrar. Proyecto personal de Haytham (no de NeoZeler). Dinero real: **fuera de v1**.

## 1. Problema
- **Dolor**: Haytham quiere un bot que haga muchos trades pequeños al día y ver en una web, en tiempo real, cuánto gana y por qué decide cada operación.
- **Cómo se ha intentado** (y por qué falló): `Memecoin-LSTM` (cerrado 2026-10-06, Gate 1: 0 de 24 pruebas con ventaja neta), `goat-trading` (5 señales NO PASA), `crypto-copy-bot` (6 cerradas, 0 ganadas, costes = 68 % de la pérdida bruta) y `pine-cripto-5m` (ninguna regla de 5 m supera al azar tras costes). Patrón común: **la ventaja bruta (+0,03 a +0,09 R) es menor que el coste por operación (~0,22 R)**.
- **Consecuencia de diseño**: scalping = muchas operaciones = el coste se multiplica. Con ~1,4 % de ida y vuelta (mediana medida) y 3-5 % en monedas poco líquidas, cada trade necesita una ventaja bruta mayor que eso. El objetivo de v1 es **medir con honestidad si Laya aporta esa ventaja**, no prometer rentabilidad diaria.

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Operador | Haytham | Ver PnL, posiciones y razones de cada decisión; parar el bot | Varias veces al día |
| Bot | Proceso en el servidor | Señales, precios, decisión de Laya, ejecución simulada | 24/7 |

### 2.1 Las tres carteras en sombra
Las tres reciben **las mismas señales** y usan el mismo broker y los mismos costes. Cada una parte de **10 SOL virtuales**.
| Cartera | Quién decide | Para qué sirve |
|---|---|---|
| **Laya** | Laya (¿estafa?, ¿entrar?, ¿mantener o vender?) | Es el bot que se evalúa |
| **Reglas** | Umbrales fijos de liquidez, edad y momento | Línea base sin IA: ¿Laya aporta algo sobre reglas simples? |
| **Azar** | Entrada aleatoria con el mismo stop y franja horaria | Línea base de suerte: lo que se gana sin ninguna ventaja |

Un panel muestra siempre qué es cada cartera y con cuánto capital parte.

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
| Panel en vivo | Retraso entre una decisión del bot y verla en la web | n/a | ≤ 2 s |
| Muchas operaciones pequeñas | Operaciones cerradas por día (ritmo esperado; el veredicto del Gate exige un **mínimo de 300 en total** y 5 días) | 0 | ≥ 100 |
| Costes realistas | Comisión + slippage por operación, medidos del feed real | supuesto 1,37 % (mediana) | medido por moneda, nunca supuesto |
| Ventaja real (**Gate 1**) | Media neta por operación, IC90 | sin dato | **IC90 inferior > 0 en AMBAS mitades temporales y sin las 3 mejores**, con ≥ 300 operaciones y ≥ 5 días |
| Antifraude | Monedas con rug/honeypot que llegan a entrar | sin dato | < 5 % de las entradas |

> [!riesgo] Criterio de cierre fijado ANTES de medir
> Si tras 5 días y 300 operaciones el Gate 1 no se cumple, **el proyecto se cierra** (lección de Memecoin-LSTM). Cambiar el criterio después de ver resultados queda prohibido. *Pendiente de aprobación de Haytham.*

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | Operador | ver mi capital virtual, PnL del día y curva de equidad en tiempo real | saber si el bot gana | Must |
| US-02 | Operador | ver cada decisión (comprar / mantener / vender / saltar) con su razón y confianza de Laya | entender y auditar al bot | Must |
| US-03 | Operador | ver las posiciones abiertas con PnL y tiempo de tenencia | vigilar el riesgo | Must |
| US-04 | Bot | descartar monedas con señales de estafa antes de entrar | no perder capital en rugs | Must |
| US-05 | Bot | operar en papel con precio, liquidez y slippage reales | que el resultado sea extrapolable | Must |
| US-06 | Operador | botón de pausa y límites (pérdida diaria, nº de posiciones) | cortar si va mal | Must |
| US-07 | Operador | ver el informe del Gate 1 (IC90, sin top 3, mitades) | decidir seguir o cerrar | Should |
| US-08 | Operador | historial de operaciones exportable (CSV) | analizar fuera del panel | Could |

## 5. Requisitos funcionales
- RF-01: Ingesta de monedas nuevas y precios en tiempo real (fuentes del TRD: Jupiter Price v3, DexScreener, feed de alertas).
- RF-02: Laya responde por moneda preguntas tipadas: *¿parece estafa?* (sí/no), *¿entrar?* (comprar/saltar) y, con posición abierta, *¿mantener o vender?*. Umbrales **calibrados con datos propios** (`laya.calibrate`): los checkpoints vienen sobreconfiados.
- RF-03: Motor de papel con contabilidad FIFO persistente, comisiones y slippage `1 % + 20 × tamaño / liquidez`, y salida por stop, trailing y tiempo.
- RF-04: Control de riesgo aplicado de verdad. Valores por defecto (parámetros de prueba, sin optimizar; modificables en Control dentro de rangos duros): capital 10 SOL por cartera, tamaño por operación 3 % del capital (rango duro 0,5-3 %), máximo 8 posiciones abiertas, exposición máxima 24 %, corte por pérdida diaria del −20 % (rango duro −3 a −20 %; decisión de Haytham 2026-10-21). El corte pausa las entradas y **no se anula** reanudando sin confirmar el motivo; reanudar no reinicia el contador del día.
- RF-05: Panel web con tiempo real (equidad, PnL, posiciones, feed de decisiones).
- RF-06: Registro de auditoría de cada decisión y cada operación (inmutable, con la entrada y la respuesta de Laya).
- RF-07: Informe del Gate 1 generado automáticamente, con una frase en lenguaje llano ("¿Gana el bot más de lo que cuestan las comisiones, con certeza razonable?") y progreso "n/300 · día X/5".
- RF-08: Panel explicable: cuadro "Qué estoy viendo", glosario con tooltips junto a cada cifra técnica, resumen de una frase por decisión, embudo de descartes por motivo (RugCheck, estafa, límite, `laya_lenta`, Laya "saltar") y tarjeta de salud del bot (RAM, swap, cola de señales, antigüedad del precio, latencia de Laya).
- RF-09: Acciones peligrosas protegidas: "Cerrar todo a mercado" exige escribir CERRAR y muestra nº de posiciones y coste estimado; "Reanudar" tras un corte diario exige confirmación con el motivo.

## 6. Requisitos no funcionales
- **Todo dentro del servidor Zorin**: código en `~/Proyectos/scalper-memecoins/` de ese equipo, servicios `systemd`, panel solo en red local (sin abrir puertos al exterior).
- **Memoria**: 7,6 GiB totales y sin GPU (CPU). Laya ocupa ~2,3 GB de checkpoints y 150-450 ms por decisión en CPU: sirve para scalping de minutos, no de segundos. Límite de memoria del bot ≤ 3,8 GB.
- **Seguridad**: ningún secreto en el repo; claves en `.env` con `chmod 600`. Sin clave de wallet en v1.
- **Idioma**: panel en español. **Dispositivos**: escritorio y móvil.
- **Disponibilidad**: reinicio automático si muere el proceso.

## 7. Fuera de alcance (v1)
- Dinero real y ejecución on-chain (Fase posterior, solo si pasa el Gate 1 y Haytham lo pide).
- Copy trading de carteras ajenas (ya lo cubre `crypto-copy-bot`).
- Otras cadenas distintas de Solana.
- Reentrenar Laya desde cero (solo calibrar o afinar con datos propios si el Gate lo justifica).

## 8. Riesgos y supuestos
> [!riesgo]
> - **Ventaja inexistente**: tres proyectos previos no la encontraron. v1 es un experimento con criterio de cierre, no una promesa de rentabilidad.
> - **Laya no es un modelo de precios**: es un clasificador de texto. Si se le pasan números como texto puede no aportar nada sobre el azar; se mide contra una línea base aleatoria con el mismo stop y franja horaria.
> - **Costes que se comen el scalping**: más operaciones = más coste. Medir coste real por moneda.
> - **Datos retrasados**: DexScreener tarda 30-75 s en notar un vaciado de liquidez; el precio de monedas poco líquidas cambia ~1 vez cada 40 s.
> - **Memoria**: el servidor ya llegó a 1,5 GiB de swap con otros servicios; los contenedores de Supabase de `wallet-fidelidad` están parados.
> - **Supuesto**: se pueden reutilizar los datos del observador de Memecoin-LSTM (1,1 GB, otro equipo) para calibrar; hay que copiarlos al servidor.

## 9. Criterios de aceptación globales
- [ ] El bot corre 24 h seguidas en el servidor sin intervención y se reinicia solo.
- [ ] El panel muestra equidad, PnL, posiciones y decisiones con ≤ 2 s de retraso.
- [ ] Cada operación tiene su registro de auditoría con la respuesta de Laya.
- [ ] El corte de pérdida diaria detiene las entradas de verdad (probado).
- [ ] El informe del Gate 1 se genera solo y compara con una línea base aleatoria.
- [ ] Ciclo completo validado: crear → refrescar → pausar → reiniciar → refrescar, con el estado intacto.

## 10. Demo provocadora (reunión 1)
No aplica (proyecto personal, sin cliente). Equivalente: **maqueta del panel con operaciones sintéticas** para que Haytham valide qué quiere ver antes de construir el motor.
- Pantalla clave: equidad en vivo + feed de decisiones de Laya con su confianza.
- Quién la ve: solo Haytham.

---
Siguiente: [[2 - TRD]]

