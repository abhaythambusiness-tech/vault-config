---
type: doc-software
doc: prd
proyecto: 01_Projects/Bot de Tendencia
status: borrador
date: '2026-10-21'
origen: mixto
---


# 1 · PRD — Bot de Tendencia (papel, cripto spot, varias frecuencias)

> [!resumen]
> Bot de **seguimiento de tendencia** en papel sobre 12 criptomonedas líquidas de Binance spot, con **tres carteras** que operan a distinta frecuencia: **T** (diaria, la que respalda la evidencia), **M** (4 h) y **F** (1 h, "operar bastante"). Antes de desplegar se mide cada una con datos históricos reales y costes, con el criterio de la sección 4 fijado por escrito. Las tres operan en papel **hoy** (las no validadas se marcan como experimentales). Sin dinero real. Corre en el servidor Zorin. Sucede a las pruebas de Laya con texto ([[01_Projects/Mercados Laya/1 - PRD|Mercados Laya]]) y a [[01_Projects/Scalper Memecoins]].

## 1. Investigación (2026-10-21): qué dice la evidencia
| Hallazgo | Fuente | Fiabilidad |
|---|---|---|
| **Momentum de series temporales**: la tendencia a 12 meses es rentable en 58 futuros (acciones, divisas, materias primas, bonos); Sharpe bruto ~1,17 en 1985-2017 | Moskowitz, Ooi y Pedersen; AQR "Trends Everywhere" | Revisado por pares |
| **Cripto**: un conjunto (ensemble) de 9 rupturas Donchian con volatilidad objetivo del 25 %, lookbacks de 5 a 360 días, sobre ~20 monedas líquidas, Sharpe > 1,5 neto de costes y alfa del 10,8 % sobre Bitcoin | Zarattini, Pagani y Barbon, SSRN 5209907 (2025) | Preprint; solo he podido leer un resumen secundario, **no verifiqué las tablas de resultados** |
| **Descomposición reciente**: el Sharpe neto de tendencia diversificada en 1974-2025 baja a ~0,6-0,95 según la construcción; solo 2 de 7 pares de forex superan 0,5 en 2003-2025 | repos y blogs de investigación | **Baja fiabilidad**: no revisado por pares |
| **Dimensionado por volatilidad** equivale a Kelly fraccionado y reduce la dispersión de resultados; Kelly completo da caídas de ~90 % | literatura de gestión de riesgo (Carver y otros) | Teoría sólida, evidencia de rendimiento mixta |
| **Carry de financiación/base en cripto**: 15-40 % anual en euforia, 3-8 % en mercados bajistas; atractivo solo ~8 % de los días de 2025; riesgo de liquidación en cascada (octubre de 2025) | informes de proveedores (Amberdata, Sharpe) | Datos de proveedores, sin Sharpe verificado; **descartado** (requiere derivados y capital grande) |
| **Sentimiento con LLM**: sin estudio limpio post-2023; hay inversiones de signo y sesgo de anticipación; la alfa "copiable" se acorta | arXiv, Interactive Brokers (2026) | Coincide con mis pruebas de Laya: **fuera** |
| **Metodología**: probabilidad de sobreajuste, Sharpe deflactado (corrige por número de pruebas y por la no normalidad), registrar todas las variantes probadas, validación fuera de muestra | Bailey y López de Prado, SSRN 2460551 | Revisado por pares |

**Conclusión de la investigación**: lo que mejor respaldan las fuentes para un bot minorista es **tendencia sencilla, diversificada y con riesgo dimensionado por volatilidad**, a frecuencia baja. **No hay evidencia sólida de que más operaciones mejoren el resultado**; mis pruebas previas (memecoins, indicador de 5 min) mostraron que los costes se comen la ventaja bruta. Aun así, Haytham quiere que opere bastante cada día: se mide en una cartera aparte (F) y se publica cuánto cuesta.

## 2. Diseño (todos los parámetros fijados; no se optimiza nada)
- **Universo**: BTC, ETH, BNB, XRP, SOL, DOGE, ADA, TRX, AVAX, LINK, LTC y DOT frente a USDT en Binance spot. Cada activo entra cuando tenga historia suficiente.
- **Solo largo o fuera, sin apalancamiento.** Capital de papel: **10.000 USDT por cartera**.
- **Señal por activo (Donchian con histéresis)**: para un lookback *N*, el estado es "largo" si el cierre supera el máximo de las *N* barras anteriores y pasa a "fuera" si cae por debajo del mínimo de las *N* barras anteriores; si no, mantiene el estado. La señal del activo es la **media de los estados** de 7 lookbacks (0 a 1).
- **Tres carteras**:
  | Cartera | Barras | Lookbacks (en barras) | Equivale a |
  |---|---|---|---|
  | **T** | 1 día | 5, 10, 20, 40, 80, 160, 320 | 5 a 320 días |
  | **M** | 4 horas | 6, 12, 24, 48, 96, 192, 384 | 1 a 64 días |
  | **F** | 1 hora | 6, 12, 24, 48, 96, 192, 384 | 6 h a 16 días |
- **Peso objetivo del activo** = (1/nº de activos con datos) × señal × min(1, 70 % / volatilidad anualizada de 30 días), con un mínimo de 0,25 del escalado. La suma queda ≤ 100 % del capital (el resto, en efectivo).
- **Rebalanceo**: en cada cierre de barra; se opera solo si el cambio de peso es ≥ 0,5 % del capital.
- **Ejecución simulada**: al **precio de apertura de la barra siguiente**. **Costes**: 0,10 % de comisión más 0,05 % de deslizamiento por lado, sobre el valor operado (0,15 % por lado).

## 3. Datos
Velas de Binance spot (API pública, sin clave), 1 d, 4 h y 1 h desde 2019-01-01 (los primeros meses solo calientan los indicadores). **Periodo de evaluación: desde 2020-01-01** (así el lookback más largo, 320 días, ya tiene datos). Periodo 1: 2020-01-01 a 2023-12-31; periodo 2: 2024-01-01 a hoy. Como no se ajusta ningún parámetro con los datos, las dos mitades son independientes de verdad.

## 4. Criterio de validación (fijado ANTES de medir; no se cambia después)
Una cartera es **VALIDADA** solo si cumple TODO, con costes incluidos:
1. **Sharpe neto ≥ 0,8** en toda la muestra y **≥ 0,5 en cada uno de los dos periodos**.
2. **Caída máxima ≤ 45 %** (Bitcoin ha caído ~75 % en ese periodo).
3. **Probabilidad de que el Sharpe real > 0 ≥ 95 %** (bootstrap por bloques de 20 días).
4. **Sharpe deflactado ≥ 0,90** con 3 pruebas (T, M y F).
5. **Supera al "comprar y mantener" equiponderado en Sharpe** en el periodo 2.
Las no validadas **siguen operando en papel como experimentales**, con la etiqueta visible. Como "operar bastante" también es objetivo, F debe hacer **≥ 10 operaciones al día de media**; si no, se informa.

## 5. Cartera de papel hoy
- Servicio en el servidor Zorin que, cada hora (`cron`, minuto 2), baja las velas nuevas, recalcula las tres carteras y simula las órdenes.
- Se ejecuta **una primera vez hoy**: las posiciones iniciales equivalen a las que tendría la estrategia ya en marcha, abiertas al precio actual con costes.
- Registro en SQLite de cada orden con motivo, precios, costes y equidad; informe de estado por línea de comandos.

### 5.1 Resultado del backtest (2020-01-01 a 2026-10-21) y despliegue (2026-10-21)
Backtest con 12 monedas, costes del 0,15 % por lado, ejecución a la apertura siguiente, parámetros fijos del PRD. Código y resultados: `~/Proyectos/trend-bot-paper/` del servidor, commit `04b7e92`.
| | Sharpe total | 2020-23 | 2024-26 | CAGR | Caída máx. | Ops/día | Costes/año | ¿Validada? |
|---|---|---|---|---|---|---|---|---|
| **T** diaria | 1,10 | 1,55 | **0,42** | 35 % | **−49 %** | 1,7 | 7,6 % | **No** |
| **M** 4 h | 1,22 | 1,71 | **0,43** | 40 % | **−48 %** | 6,8 | **44 %** | **No** |
| **F** 1 h | 0,65 | 1,14 | **−0,13** | 16 % | −64 % | 26 | **74 %** | **No** |
| BTC comprar y mantener | 0,91 | 1,00 | 0,75 | 43 % | −77 % | | | |
| Equiponderado de las 12 | 1,09 | 1,45 | 0,41 | 71 % | −79 % | | | |
**Veredicto: ninguna cartera cumple el criterio.** T y M lo incumplen por el Sharpe de 2024-26 (< 0,5) y por la caída (> 45 %); F lo incumple en casi todo. Lo que sí cumplen T y M: probabilidad de Sharpe > 0 del 99 % y Sharpe deflactado > 0,98 (con solo 3 pruebas, la deflación casi no penaliza).
- **El Sharpe > 1,5 del preprint no se replica** con estas reglas y costes: 1,10 en toda la muestra y 0,42 desde 2024.
- **Más operaciones es peor**: de T a M y a F los costes pasan del 7,6 % al 44 % y al 74 % del capital al año; M y F rotan la cartera 296 y 494 veces al año por los cambios continuos de peso (volatilidad y media de señales), lo que apunta a un fallo de diseño (umbral de 0,5 % demasiado pequeño). **No se ha corregido hoy**: cualquier variante nueva cuenta como otra prueba y exige deflactar con 4 o más.
- **Contra Bitcoin**: en 2024-26 comprar y mantener BTC (Sharpe 0,75) supera a T y M (0,42-0,43) en rentabilidad ajustada al riesgo; la ventaja de la tendencia fue una caída máxima menor (T −43 % frente a −53 % de BTC en 2024-26, y −49 % frente a −77 % en toda la muestra), no una mayor rentabilidad.
- **Sesgos favorables al bot**: monedas que sobreviven hoy; mercados alcistas en 2020-21 y 2023-25.

**Despliegue en papel (hoy, 2026-10-21 16:49 UTC)**: las tres carteras operan **como EXPERIMENTALES** (el PRD ya lo preveía para las no validadas), 10.000 USDT cada una. Primera pasada: 12 órdenes por cartera (36 en total) al precio actual con costes; luego `cron` cada hora (minuto 2). F ejecuta ~26 operaciones/día en el backtest, cumpliendo el deseo de "operar bastante", pero con el peor resultado. Informe: `venv/bin/python scripts/estado.py` en el servidor.

### 5.2 Mejora de la rotación (variante «umbral 3 %»), regla fijada ANTES de medirla (2026-10-21)
> [!resumen] En cristiano
> Las carteras de 4 horas y de 1 hora compran y venden **demasiadas veces por movimientos minúsculos** y las comisiones se comen la ganancia (44 % y 74 % del capital al año). La mejora más sencilla: **no tocar nada si el cambio es pequeño** (menos de un 3 % del dinero, antes un 0,5 %). Se mide **una sola vez**; si cumple la regla de abajo, se aplica a las carteras reales de papel; si no, se queda como estaba.

- **Qué cambia**: solo el umbral de rebalanceo, de 0,5 % a **3 %** del capital. Todo lo demás (señal, volatilidad, costes, datos, periodo) igual que en §5.1.
- **Regla de aceptación** (todo debe cumplirse, por cartera): (a) costes anuales **al menos 40 % menores**, (b) Sharpe total **no baja más de 0,10**, (c) Sharpe de 2024-26 **no baja más de 0,10**. T se adopta si no empeora en (b) y (c). Si una cartera no cumple, conserva su umbral de 0,5 %.
- **Contabilidad de pruebas**: cuenta como prueba nueva a efectos del Sharpe deflactado (T, M, F, K y esta variante en T, M y F).
- **No es una promesa**: reducir costes no crea ventaja; solo evita regalar dinero a las comisiones.

**Resultado (2026-10-21), aplicando la regla tal como se escribió** (código `scripts/correr_variante.py`, datos en `docs/variante_umbral.json`):
| Cartera | Comisiones al año | Sharpe total | Sharpe 2024-26 | Caída máx. | ¿Se adopta? |
|---|---|---|---|---|---|
| T diaria | 7,6 % → 2,7 % | 1,10 → 1,12 | 0,42 → 0,51 | −48,8 % → −47,9 % | **Sí** |
| M 4 horas | 44,4 % → 18,7 % | 1,22 → 1,35 | 0,43 → 0,53 | −47,9 % → −41,6 % | **Sí** |
| F 1 hora | 74,2 % → 44,6 % | 0,65 → 1,21 | −0,13 → 0,39 | −63,6 % → −44,3 % | **No** |
F baja las comisiones un 39,9 % y la regla exigía un 40 %: **no se adopta, aunque mejora**; no se cambia la regla después de ver el número. Se mantiene a propósito como la hucha «que opera mucho» para medir cuánto cuesta. T y M operan en vivo con umbral del 3 % desde el 2026-10-21 (`estrategia.UMBRAL_CARTERA`). **Contabilidad de pruebas**: con las 3 variantes y las dos de Kronos, el Sharpe deflactado de cualquier resultado nuevo debe contar al menos 8 pruebas; ninguna de estas cifras es todavía evidencia de que ganen: siguen siendo resultados sobre el pasado en un mercado alcista.

## 6. Fuera de alcance
Dinero real; apalancamiento y cortos; derivados (carry, basis); texto, noticias y Laya (descartados por las pruebas); optimización de parámetros; control y escritura desde el panel. **El panel web de solo lectura SÍ se hizo el 2026-10-21 a petición de Haytham**, aunque ninguna cartera validara: ver [[01_Projects/Bot de Tendencia/3 - Panel web|3 - Panel web]] (`http://192.168.0.100:8060`).

## 7. Riesgos
> [!riesgo]
> - **Fiabilidad de la cifra de Zarattini**: preprint con resultados que no he podido verificar contra el original.
> - **Mercado alcista 2019-2026**: casi cualquier regla de tendencia con exposición larga gana; por eso se compara con "comprar y mantener" y se exige el segundo periodo por separado.
> - **Costes**: 0,15 % por lado es un supuesto; Binance con BNB baja la comisión, pero el deslizamiento real en monedas pequeñas puede ser mayor.
> - **Supervivencia**: el universo son monedas que existen hoy; las que murieron no están. Sesgo favorable, que se declara.
> - **Sobreajuste**: aunque no se optimice, las tres carteras son tres pruebas y se deflactan.
> - **Operar a 1 h**: se espera que F pierda por costes; se mide para saber cuánto.

---
Relacionado: [[01_Projects/Mercados Laya/1 - PRD|Mercados Laya]] · [[01_Projects/Scalper Memecoins]]

