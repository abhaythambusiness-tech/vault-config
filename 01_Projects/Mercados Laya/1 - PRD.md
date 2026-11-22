---
type: doc-software
doc: prd
proyecto: 01_Projects/Mercados Laya
status: forex-no-pasa
date: '2026-10-21'
origen: mixto
---


# 1 · PRD — Mercados Laya (forex y oro ahora; cripto cuando haya datos)

> [!resumen]
> Dos frentes con una sola regla: **medir antes de construir**. (1) **Puerta 0 de forex y oro**: ¿predice el tono de Laya sobre los comunicados de la Fed y del Banco de Inglaterra el movimiento de EURUSD, GBPUSD, USDJPY y oro a 1 y 5 días, ya descontados costes? (2) **Recolector de titulares de cripto** (BTC y ETH) en el servidor, para probar a Laya cuando haya 8 semanas de datos propios. Todo en **papel**, sin dinero real, en el servidor Zorin. Sustituye a [[01_Projects/Eventos Bolsa/1 - PRD|Eventos Bolsa]] (pausado) y sucede a [[01_Projects/Scalper Memecoins]] (cerrado: Laya no aporta con estados numéricos).

## 1. Problema
- Haytham quiere un bot que lea texto de mercado con Laya ("Sistema 1" local) y opere en papel con panel en vivo. Las pruebas previas con **números** fallaron; con **texto** no se ha probado.
- **Aviso honesto**: con barras diarias se entra mucho después del comunicado (la Fed publica a las 14:00 de Nueva York y los fondos lo descuentan en milisegundos). Esta prueba **no mide la reacción instantánea**, sino si queda deriva a 1-5 días. Lo esperable es "sin ventaja". Se acepta como validación de deriva, no de reacción.

## 2. Puerta 0 de forex y oro: diseño (fijado el 2026-10-21 antes de descargar ningún comunicado)
**Eventos**: declaraciones de política monetaria de la **Fed** (FOMC, 2010-01-01 a 2026-10-15) y resúmenes del **Banco de Inglaterra** (MPC, 2016-01-01 a 2026-10-15). El **BCE queda pendiente**: su listado se carga con JavaScript y no hay enlaces estáticos; se añade si se resuelve sin adivinar URLs.

**Activos y signo** (hawkish = endurecimiento):
| Evento | Activo | Posición si el tono es más hawkish que el habitual |
|---|---|---|
| Fed | EURUSD, USDJPY, oro (GC=F) | corto EURUSD, largo USDJPY, corto oro |
| BoE | GBPUSD | largo GBPUSD |

**Texto que ve Laya** (`typed-decisions`, ≤ 1.024 tokens): el texto íntegro de la declaración o su resumen. Pregunta: `tono` (choice: hawkish / dovish / neutral). **Señal** = P(hawkish) − P(dovish).

**Cambio de tono, no nivel**: la señal se compara con la **mediana de las 8 declaraciones anteriores del mismo banco** (ventana móvil, sin mirar al futuro; se saltan las 8 primeras). Posición = signo de (señal − mediana) × signo del activo.

**Entrada y salida**: al **cierre del día del comunicado**; salida al cierre de **+1 y +5 sesiones**. **Costes**: 0,03 % ida y vuelta en forex y 0,08 % en oro (supuesto razonable de spread más comisión).

**Líneas base**: (a) **léxico**: palabras hawkish (inflation, tighten, raise, elevated, strong) menos dovish (accommodative, patient, lower, weak, downside), también frente a su mediana previa; (b) **azar**: signo permutado, 2.000 repeticiones.

## 3. Criterio de aprobación (no se cambia después de ver resultados)
La Puerta 0 **pasa** solo si se cumple TODO:
1. **≥ 150 declaraciones** puntuadas y **≥ 300 pares evento-activo** tras el calentamiento.
2. Retorno medio **neto** de la estrategia de Laya con **IC95 inferior > 0** a +1 o a +5 sesiones.
3. Positivo en **las dos mitades temporales**.
4. **Supera al léxico**: IC95 de la diferencia > 0.
5. **Supera al azar**: p < 0,05 con la permutación.
6. Sigue positivo **quitando los 3 mejores eventos**.
Los intervalos usan **bootstrap por fecha de evento** (EURUSD, USDJPY y oro reaccionan al mismo comunicado de la Fed). **Si falla cualquiera: se detiene todo desarrollo de Laya en trading hasta que el recolector de cripto tenga suficientes datos.**

## 4. Recolector de titulares de cripto (activo desde 2026-10-21)
- 6 fuentes RSS públicas (CoinDesk, Cointelegraph, Decrypt, BeInCrypto, The Block, Bitcoin Magazine), una consulta por fuente cada **30 min** vía `cron`, guardadas en SQLite (`~/Proyectos/mercados-laya/data/titulares.db`), cada titular una sola vez con su hora de publicación y de recogida. Primera pasada: 133 titulares, 0 fallos. Código con 4 pruebas, `ruff` y `mypy` limpios.
- **Prueba de cripto (pendiente, no antes de 8 semanas)**: Laya puntúa cada titular (tono sobre BTC o ETH) y se compara con el retorno de BTC y ETH a +1 h, +1 d y +5 d. Criterio propio que se fijará **antes** de mirarlo.

## 5. Datos y fuentes
| Dato | Fuente | Estado |
|---|---|---|
| Declaraciones de la Fed | `federalreserve.gov` (páginas históricas por año con enlaces `monetaryAAAAMMDDa.htm`) | verificado (2012: 8 enlaces) |
| Resúmenes del BoE | `bankofengland.co.uk/monetary-policy-summary-and-minutes/AAAA/mes-AAAA` | verificado 2019; 2012 da 404, por eso se parte de 2016 |
| BCE | declaración de política monetaria | **pendiente** (listado dinámico) |
| Precios diarios EURUSD, GBPUSD, USDJPY, oro | Yahoo Finance (`=X`, `GC=F`) | verificado: responde |
| Titulares de cripto | 6 RSS | verificado y recolectando |

### 5.1 Hallazgo de datos antes de puntuar (2026-10-21)
Corpus bajado: **132 declaraciones de la Fed (2011-01-26 a 2026-09-16) y 78 del BoE (2017-02-02 a 2026-09-17)**; no hay declaraciones de 2010 ni de 2016 porque las páginas históricas o los resúmenes no se localizaron con enlaces estáticos. En las barras diarias de Yahoo la fila con fecha *D* contiene el cierre del día *D*−1: el movimiento absoluto medio salta en la fila *D*+1 (oro 1,45 % frente a 0,65 % en *D*; EURUSD 0,54 % frente a 0,34 %; GBPUSD 0,64 % frente a 0,42 %; USDJPY 0,53 % frente a 0,38 %) y es tranquilo en *D* y *D*−1. **Regla fijada**: el cierre del día del comunicado es el de la fila siguiente a *D*; la salida a +1 y +5 sesiones se cuenta desde ahí. Se decidió mirando solo el tamaño del movimiento, sin usar la señal de Laya.

## 6. Fuera de alcance
Dinero real; bot y panel hasta que alguna puerta pase; acciones (PRD pausado); datos de pago; reentrenar Laya; operar intradía.

## 7. Riesgos y supuestos
> [!riesgo]
> - **Ventaja ya descontada**: lo más probable. Un "sin ventaja" aquí no demuestra que Laya lea mal el tono.
> - **Fuga de entrenamiento**: las declaraciones de la Fed son famosas y Laya puede haberlas visto; si pasa, hay que desconfiar y repetir con textos posteriores a su entrenamiento.
> - **Muestra pequeña**: ~135 declaraciones de la Fed y ~90 del BoE; los IC serán anchos.
> - **Hora de publicación vs cierre diario**: la entrada al cierre del día llega 2-10 horas tarde según el banco; no es la reacción inmediata.
> - **Yahoo no es oficial**; el BCE está sin resolver; la descarga de la Fed y del BoE debe ser pausada y educada.

## 7.1 Resultado de la Puerta 0 de forex y oro (2026-10-21): NO PASA
Criterio aplicado tal como estaba fijado: 210 declaraciones (132 Fed + 78 BoE), 194 eventos con señal tras el calentamiento y 442 pares evento-activo.
| Horizonte | Media neta de Laya | IC95 | Mitades temporales | Léxico | Diferencia Laya − léxico (IC95) | Azar (p) | Sin 3 mejores |
|---|---|---|---|---|---|---|---|
| +1 día | −0,04 % | [−0,14, +0,05] | +0,04 / −0,15 | −0,07 % | [−0,13, +0,16] | 0,50 | −0,07 % |
| +5 días | −0,13 % | [−0,33, +0,06] | +0,00 / −0,32 | +0,08 % | [−0,47, +0,03] | 0,85 | −0,19 % |
**Ninguna** de las condiciones 2 a 6 se cumple en ningún horizonte; solo la 1 (muestra). Con p = 0,50 a +1 día, la estrategia de Laya es indistinguible de permutar el signo al azar.
- **Laya sí lee el tono**: su puntuación media sobre la Fed pasa de ~0 en 2011-2021 a +0,22 en 2022 y +0,18 en 2023 (la subida de tipos), y baja a +0,07 en 2024-2025. La confianza interna es baja (media 0,02), igual que con memecoins.
- **El mercado ya lo ha pagado**: a cierre del día del comunicado y a +1 y +5 sesiones no queda deriva por encima de costes. Era el resultado más probable (§1).
- **Lo que esta prueba NO descarta**: la reacción en minutos u horas (necesita datos intradía gratuitos que no tengo) ni el BCE (no incluido).
- **Cómo se comprobó la alineación de fechas**: ver §5.1. El análisis completo está en `~/Proyectos/mercados-laya/docs/resultado_bancos.json` del servidor (commit `f20d987`).
- **Regla de parada (de Haytham)**: se detiene todo desarrollo de Laya en trading hasta que el recolector de cripto tenga suficiente histórico.

## 8. Siguientes pasos
1. Construir el corpus (Fed y BoE) y los precios; guardar el commit antes de puntuar.
2. Puntuar con Laya y analizar con el mismo método que en memecoins.
3. Veredicto: **pasa** → abrir TRD, UI/UX, AppFlow, Schema y Plan para un bot en papel. **No pasa** → parar hasta que el recolector de cripto tenga 8 semanas.

---
Relacionado: [[01_Projects/Scalper Memecoins]] · [[01_Projects/Eventos Bolsa/1 - PRD|Eventos Bolsa (pausado)]]

