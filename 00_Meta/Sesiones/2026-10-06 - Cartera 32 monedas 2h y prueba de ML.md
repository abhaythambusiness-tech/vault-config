---
type: sesion
status: completada
fecha: '2026-10-06'
proyecto: '[[04_Archive/AVAX-RL-Bot]]'
tags:
- avax
- bot
- trading
- backtest
- ml
origen: mixto
---

# Sesión — 2026-10-06 (tarde/noche): cartera 32 monedas y prueba de ML

> [!abstract] Resumen
> Continuación de [[00_Meta/Sesiones/2026-10-06 - Rediseno del bot AVAX a tendencia 4h]]. Se investigó cómo operar más veces y se desplegó una cartera de 32 monedas en velas de 2h. Se probó ML como filtro de señales: sin ventaja, descartado. Código en `~/Proyectos/archive/AVAX-RL-Bot/` (spec en `spec.md`).

## Qué se hizo
- **Intradía en AVAX solo (15m–2h)**: con comisión real casi todo pierde fuera de muestra. Largo+corto a 100 % también.
- **Auditoría del backtest**: contabilidad independiente (14.358 % vs 14.354 %). Sin error de base.
- **Misma estrategia en 13 monedas sin reoptimizar**: 11/13 positivas en 2024+, cartera Sharpe 1,42, DD −39 %.
- **Universo y timeframe**: 32 monedas a 4h → 342 trades/año; 2h × 32 monedas (N80, k4, EMA 50 días) → ~470 trades/año, Sharpe test 0,90, DD test −23 %. 1h se degrada. Combinar reglas no mejora.
- **Reoptimizar cada año**: peor que parámetros fijos (Sharpe 0,48 vs 0,79).
- **ML como filtro** (gradient boosting, reentrenado anualmente, OOS): AUC ≈ azar, empeora la cartera. Descartado.
- **Desplegado**: bot de reglas fijas, 32 monedas, 2h, 1.000 USDT virtuales, estado en `state_portfolio.json`, log en `logs/live.log`.

## Decisiones
- Parámetros congelados; no hay entrenamiento que mantener.
- ML: repetir la prueba cuando haya más datos en vivo, no antes.
- No pasar a dinero real sin semanas de paper trading.

## Aprendizajes
- Más frecuencia en una sola moneda pierde por comisiones; la frecuencia se compra con diversificación, no con timeframes cortos.
- Validar sobre monedas no usadas para decidir es la mejor prueba contra el ajuste a los datos.
- Reoptimizar parámetros con pocos datos añade ruido: el walk-forward lo midió peor que fijos.
- Un modelo de ML sobre ~2.800 señales no encuentra estructura: AUC ≈ 0,5.
- Sesgo conocido: las 32 monedas existen hoy (supervivencia).

## Próximos pasos
- Rotar el webhook de Discord (sigue en el historial local de git).
- Commit del proyecto y servicio systemd para sobrevivir a reinicios.
- Revisar el paper trading tras varias semanas y comparar con el backtest.
- Dinero real: capital suficiente (≥ ~1.000 USDT) por el mínimo de orden de Binance.

## Relacionado
- [[04_Archive/AVAX-RL-Bot]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

