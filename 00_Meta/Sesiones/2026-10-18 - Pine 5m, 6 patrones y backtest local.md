---
type: sesion
status: cerrado
date: '2026-10-18'
proyecto: '[[Pine 5m - Indicador y Estrategia]]'
tags:
- trading
- pine-script
- backtest
origen: mixto
---

# Sesión — 2026-10-18: Pine 5m, 6 patrones y backtest local

> [!abstract] Resumen
> Se crearon un indicador y dos estrategias de Pine v6 para cripto en 5m con los patrones del Playbook, y un backtest local de 2 años que concluyó que ninguno es rentable tras comisiones.

## Contexto
Parte de [[Trading con 10 euros - MOC]] y [[Playbook - Index]]. Primer indicador rechazado por Haytham tras ver la captura: LONG con las EMAs enredadas y SHORT al final de una caída extendida. Código en `~/Proyectos/pine-cripto-5m/`.

## Qué se hizo
- Indicador `indicador-pb5.pine` y estrategia `estrategia-pb5.pine` (pullback + fakeout) con panel de riesgo, límites diarios y tamaño de posición para 10 €.
- `estrategia-patrones-5m.pine` con los 6 patrones (doble techo/suelo, hombro-cabeza-hombro, fakeout, banderas, triángulos, pullback), cada uno con interruptor.
- Resultado en TradingView: 30 operaciones, 16,7 % de acierto, -13,9 %. Muestra de solo ~3 semanas.
- Backtest en Python (`backtest/`): 2 años de velas de 5m de BTC y ETH de Binance, remuestreo a 15m/1h/4h, comisión 0,1 % por lado, cada patrón solo y todos juntos, línea base aleatoria, 10 pruebas (incluye no mirar al futuro).
- Enfoque alternativo de tendencia de horizonte largo (`backtest/tendencia.py`): historial de 1d y 4h de BTC y ETH desde 2017, siete reglas clásicas solo largos, costes con deslizamiento, comparación con comprar y mantener y con entradas aleatorias de igual número y duración, criterios de éxito fijados antes de ver resultados, 9 pruebas.

## Decisiones tomadas
- No operar estas señales con dinero real.
- Validar cualquier estrategia con miles de operaciones y contra una línea base aleatoria antes de optimizar parámetros.

## Aprendizajes (para futuras sesiones)
- En 5m la ventaja bruta es +0,044 R frente a un coste de ~0,28 R por operación (stops de ~0,75 % y 0,2 % ida y vuelta): la comisión decide el resultado, no el patrón. Solo 1h muestra ventaja bruta clara (+0,09 R sobre el azar) y tampoco cubre 0,1 % por lado.
- Las banderas daban 0 señales por una contradicción entre condiciones (pendiente medida con la vela de ruptura). Registrado en `.claude/COMMON_MISTAKES.md` #45.
- Con 30 operaciones no se puede concluir nada; TradingView básico limita el histórico de 5m.
- Entorno: el Python de `~/Proyectos/archive/goat-trading/.venv` trae pandas, numpy y pyarrow; el del sistema no tiene pandas.
- La tendencia de horizonte largo reduce el riesgo (desplome máximo de BTC de -77 % a entre -39 % y -64 %; Calmar de 0,37 a 0,5-1,1) pero no demuestra ventaja de timing: frente a entradas aleatorias casi todas dan p entre 0,1 y 0,5, y ninguna regla cumple los 10 criterios (las mejores, 8). Con 28 pruebas, un p = 0,044 aislado es lo esperable por azar.
- Al descargar 1d y 4h se re-descargaron por error también las velas de 5m (ventana desplazada 15 min): datos regenerables de la misma fuente, sin efecto relevante en las conclusiones.

## Próximos pasos
- Decidir si se prueban los patrones del Playbook en 4h/1d con salida por trailing en vez de objetivo fijo, si se hace seguimiento en papel de un filtro de tendencia (precio sobre SMA), o si se cierra aquí.
- Commit inicial del repo `pine-cripto-5m` (sin commitear aún).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[Pine 5m - Indicador y Estrategia]]

