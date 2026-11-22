---
type: doc-software
doc: prd
proyecto: Laya Trader
status: aprobado
date: 2026-10-22
origen: mixto
---

# 1 · PRD — Laya Trader

> [!resumen] En cristiano
> Réplica fiel del bot `buberlo/jev-trader` (gist de drillan), cambiando Jev por **Laya**. Practica con **dinero de mentira** en BTC, ETH y SOL de Binance. Un programa normal mide el mercado y escribe un resumen corto; Laya contesta 6 preguntas cortas; otro programa decide con reglas y frenos de seguridad que Laya no puede saltarse; todo se apunta para ver si Laya acierta. Sin nada del Bot de Tendencia ni del bot de memecoins. Es un experimento con el criterio de cierre escrito **antes** de medir. Decisión que te toca: aprobar este PRD. Proyecto personal de Haytham, no de NeoZeler.

> [!riesgo] Aviso honesto
> En pruebas anteriores Laya sin entrenar no aportó nada leyendo cifras. Por eso el original ya trae un "juez de reserva" hecho con reglas fijas: sirve de referencia. Si Laya no lo supera, se cierra.

## 1. Problema
- Dolor: saber si un modelo de respuestas cortas (Laya) añade algo real dentro de un sistema de trading ordenado, sin arriesgar dinero.
- Hoy: no hay un banco de pruebas con el patrón "el modelo juzga, el código ejecuta".

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia |
|---|---|---|---|
| Operador | Haytham | Ver si Laya mejora al juez de reserva | Diaria |
| Servidor | Zorin (`ssh@192.168.0.100`) | Correr 24/7 | Continua |

## 3. Objetivos y métricas de éxito (congeladas hoy)
| Objetivo | Métrica | Meta |
|---|---|---|
| Laya aporta señal | Brier / log loss de sus juicios frente al juez de reserva (informe `calibrate`) | Mejor que el juez de reserva con IC90 que no cruce 0 |
| Rentabilidad neta en papel | Resultado neto por ciclo (comisiones y deslizamiento incluidos) | Límite inferior IC90 > 0 en las dos mitades temporales y sin las 3 mejores operaciones |
| Muestra | Ciclos y días | ≥ 300 operaciones y ≥ 7 días; antes: "NO CONCLUYENTE" |

**Cierre**: si falla cualquiera de las dos primeras, el proyecto se cierra. Cada ciclo se corre dos veces en paralelo con los mismos datos: juicios de **Laya** vs juicios del **juez de reserva** (réplica del `fallback judge` del original).

## 4. Historias de usuario
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | Operador | datos públicos en directo de Binance (libro de órdenes y trades) de BTC/ETH/SOL | partir de mercado real gratis | Must |
| US-02 | Operador | un motor de rasgos en código puro (precio medio, microprecio, spread, desequilibrio, volatilidad, inventario, caída acumulada, posición en cola) | que Laya no calcule nada | Must |
| US-03 | Operador | un resumen de estado de menos de 400 tokens | que la llamada a Laya sea rápida | Must |
| US-04 | Operador | una llamada a Laya con 6 juicios: régimen, dirección, flujo tóxico, estrés de liquidez, entorno de cotización, presión de inventario | alimentar la política | Must |
| US-05 | Operador | una política en código (acción, tamaño Kelly fraccional, precios Avellaneda-Stoikov) | que Laya no decida precios ni tamaños | Must |
| US-06 | Operador | vetos de riesgo duros y un interruptor de emergencia que Laya no puede saltarse | proteger la cartera | Must |
| US-07 | Operador | una escalera de reserva (confianza baja → reducir tamaño; fuera de plazo → no cotizar; Laya caída → juez de reserva; límite roto → cerrar todo) | que nunca opere con datos viejos | Must |
| US-08 | Operador | un broker de papel con órdenes post-only y ejecuciones simuladas | números honestos | Must |
| US-09 | Operador | un registro `(estado, decisión, resultado)` en JSONL y un informe de calibración (Brier, log loss, ECE, curva de fiabilidad, Platt) | medir si Laya acierta | Must |
| US-10 | Operador | ejecuciones repetibles con semilla | reproducir pruebas | Should |
| US-11 | Operador | un panel web de solo lectura con el veredicto del cierre | decidir cerrar o seguir | Should |

## 5. Requisitos funcionales
- RF-01: solo papel; sin claves de exchange; Binance spot, datos públicos.
- RF-02: una decisión por turno y moneda (plazo configurable, por defecto 4 s por moneda, no los 300 ms de Monad: Laya tarda ~3 s en CPU); Laya en CPU del servidor.
- RF-03: cada juicio con su respuesta tipada y confianza; la política usa umbrales en código.
- RF-04: el criterio de cierre se calcula automático desde el JSONL.

## 6. Requisitos no funcionales
Python 3.12 con `uv`; `systemd` en Zorin; solo LAN; sin secretos en el repo; español en documentación; el original es MIT, se cita la fuente.

## 7. Fuera de alcance (v1)
Dinero real, corto o apalancamiento, memecoins, entrenar Laya, cualquier pieza del Bot de Tendencia o de Scalper Memecoins.

## 8. Riesgos y supuestos
> [!riesgo]
> - Laya sin entrenar puede no leer cifras (probable). Mitigación: juez de reserva como control y cierre automático.
> - Crear mercado en spot paga comisiones: la métrica es siempre neta.
> - El README del original no publica las opciones de cada juicio, los campos del estado ni los umbrales: se definen en el TRD y se marcan como decisión propia, no copiada.
> - Cambiar el criterio tras ver resultados invalida el experimento.

## 9. Criterios de aceptación globales
- [ ] `paper` corre 7 días sin intervención
- [ ] Laya y juez de reserva ven los mismos datos
- [ ] `calibrate` genera el informe
- [ ] Ningún secreto en el repo

## 10. Demo provocadora
No aplica (proyecto personal). Equivalente: panel con ambos jueces compitiendo y el veredicto "NO CONCLUYENTE".

---
Siguiente: [[2 - TRD]]
