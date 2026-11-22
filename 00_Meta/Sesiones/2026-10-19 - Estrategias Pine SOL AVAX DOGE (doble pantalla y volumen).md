---
type: sesion
status: cerrado
date: '2026-10-19'
proyecto: '[[Pine 5m - Indicador y Estrategia]]'
tags:
- trading
- pine-script
- scalping
origen: mixto
---


# Sesión — 2026-10-19: Estrategias Pine para SOL, AVAX y DOGE

> [!abstract] Resumen
> Se pegó el playbook de scalping con 10 € (altcoins volátiles, 15m para dirección y 5m para gatillo, 3 balas al día, killzone de Wall Street) y se crearon dos estrategias de Pine v6: una con los indicadores del playbook y otra basada en volumen. Ninguna está validada.

## Contexto
Parte de [[Trading con 10 euros - MOC]] y [[Pine 5m - Indicador y Estrategia]]. El backtest del 18 de octubre (BTC/ETH) ya había concluido que en 5m la comisión supera la ventaja bruta de los patrones. Código en `~/Proyectos/pine-cripto-5m/`.

## Qué se hizo
- `estrategia-doble-pantalla.pine`: EMA 20/50 de 15m (sin repintado) marcan la dirección; gatillo de pullback a la EMA 20 en 5m con volumen sobre la media; stop 0,8-2 %, objetivo 2R, killzone 15:30-22:00 de Madrid, máximo 3 operaciones al día, parar tras 3 pérdidas.
- `estrategia-volumen.pine`: ruptura de 20 velas con volumen relativo ≥ 2,5x, cierre en el 70 % superior, precio sobre VWAP y EMA 50, OBV a favor; mismas reglas de riesgo.
- Sección nueva en el README del repo y en la ficha del Playbook.

## Decisiones tomadas
- Stop mínimo 0,8 % y máximo 2 % (en BTC era 0,5-1,5 %) por la mayor volatilidad de las altcoins y para que la comisión pese menos.
- Solo largos por defecto (spot); el panel avisa si el activo no es SOL, AVAX o DOGE.
- Haytham pidió "no descargues nada" cuando la descarga de AVAX y DOGE ya estaba en marcha; la orden de parar llegó tarde y los dos archivos de 5m quedaron guardados en `backtest/data/` (datos públicos de Binance, regenerables). Haytham autorizó después usarlos y se hizo el backtest (ver más abajo).

## Aprendizajes (para futuras sesiones)
- La descarga en segundo plano figuraba como fallida pero había terminado; comprobar siempre el disco en vez de fiarse del estado de la tarea.
- Pendiente de comprobar: los datos de SOL de 5m ya estaban en `backtest/data/SOLUSDT-5m.parquet`, así que un backtest de SOL no necesita descargar nada.
- El hook de GateGuard exige declarar llamantes, duplicados e instrucción verbatim antes del primer `Write` de cada archivo nuevo.

## Próximos pasos
- Probar las dos estrategias en TradingView en SOL, AVAX y DOGE y mirar nº de operaciones y factor de beneficio.
- Decidir si se cierra aquí (recomendado) o se prueba algo estructuralmente distinto: marcos de 1h o más, o comisión menor.
- Commit inicial del repo `pine-cripto-5m` (sin commitear aún).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[Pine 5m - Indicador y Estrategia]]


## Backtest local (ampliación de la sesión)
Con permiso de Haytham se replicaron en Python DP 15/5 y la de volumen (`backtest/alts.py`, 10 pruebas en `test_alts.py`) y se corrieron junto a los 6 patrones en SOL, AVAX y DOGE.

> [!resumen]
> Backtest local de 2 años en SOL, AVAX y DOGE (`backtest/alts.py`, informe en `backtest/resultados_alts.md`): **ninguna de las tres estrategias supera al azar tras comisiones**. R neto entre -0,13 y -0,27 por operación, factor de ganancias 0,60-0,79; la mejor (DP 15/5 con killzone) deja -0,19 R en SOL, -0,17 en AVAX y -0,13 en DOGE frente a -0,22, -0,20 y -0,19 del azar. La ventaja bruta (+0,03 a +0,09 R) no cubre el coste de ~0,22 R por operación.

- **Fallo cazado por las pruebas:** `_day_week` asumía nanosegundos y pandas 3 usa microsegundos, así que todos los días salían iguales y los límites diarios no se reiniciaban. Registrado en `.claude/COMMON_MISTAKES.md` #46.
- **Decisión:** no optimizar parámetros; no hay ventaja que afinar. Haytham había pedido optimizar DP 15/5 tras ver 4 operaciones en TradingView: esa muestra era ruido.

## Auto ajuste con 6 años (ampliación)
Haytham pidió un sistema de auto ajuste "hasta que una de las dos estrategias funcione" y autorizó descargar unos 6 años de 5m de SOL, AVAX y DOGE (copia de los datos de 2 años guardada antes en el scratchpad).

> [!resumen]
> Auto ajuste (`backtest/tune.py`): 4 rondas de 48 candidatos por estrategia (384 en total) sobre 6 años de velas de 5m (unas 636.000 por activo, 2020-10 a 2026-10). **Ninguno logró R neto positivo en los tres activos en el periodo de entrenamiento** (2020-10 a 2023-06), así que ninguno llegó a validarse y el hold-out (2024-10 a 2026-10) sigue sin consultar. Mejor puntuación (el peor de los tres activos): DP 15/5 -0,090 R (mediana de los candidatos -0,197) y volumen -0,124 R (mediana -0,268). Veredicto: **no funciona**; la comisión de 0,1 % por lado domina cualquier ajuste de parámetros.

- **Decisión de diseño:** no buscar sin límite. Protocolo con tres periodos, criterios estrictos fijados de antemano, una validación por estrategia y ronda, y hold-out de una sola consulta con candado. Si ninguna pasa, el resultado es "no funciona".
- **Datos:** 10 huecos por mantenimientos de Binance (el mayor, 4 h 45 min); 635.900 velas por activo.
- **Prueba de humo:** 6 candidatos en 4 s sin tocar el hold-out; se borró su registro antes de la búsqueda real.
