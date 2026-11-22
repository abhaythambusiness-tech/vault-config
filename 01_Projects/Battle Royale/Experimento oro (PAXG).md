---
type: informe
date: '2026-10-23'
proyecto: '[[01_Projects/Battle Royale]]'
status: cerrado
tags:
- trading
- oro
- servidor-zorin
origen: mixto
---

> [!resumen] En cristiano
> Se probaron las 4 estrategias de un manual de trading de oro, cada una con 4 formas de gestionar la salida (16 combinaciones), con 6 años de velas de PAXG (la moneda de Binance respaldada por oro). **Ninguna pasa: con comisiones todas pierden (entre −0,14 % y −0,33 % por operación) y ninguna le gana al azar.** Sin comisiones están alrededor de cero. Las salidas «sofisticadas» (stop a la entrada, cierre parcial, trailing) no ayudan: empeoran o no cambian. Esto no demuestra que el oro no se pueda operar, sino que estas reglas, con los costes de PAXG, no tienen ventaja.

## Qué se probó
Criterio fijado antes de medir en `~/Proyectos/battle-royale/docs/criterio_oro.md` (no se tocó después): examen = último 40 % de la historia, comisión 0,1 % + deslizamiento 0,05 % por lado, azar con la misma gestión (300 repeticiones), pasa solo si cumple a la vez ≥30 operaciones, media > 0, p < 0,05/16 y media > 0 en cada mitad del examen.

| Estrategia (solo compras) | Marco | Operaciones | Neta por operación | Sin costes | Probabilidad de azar |
|---|---|---|---|---|---|
| Tendencia EMA + RSI | 1 h | 205 | −0,136 % | +0,133 % | 0,26 |
| Retroceso Fibonacci + divergencia | 1 h | 80 | −0,315 % | −0,048 % | 0,92 |
| Ruptura del rango asiático | 15 min | 309 | −0,274 % | +0,017 % | 0,43 |
| Scalping por cruce de medias | 5 min | 1.844 | −0,307 % | −0,007 % | 0,68 |

(Variante «base»; las 16 están en `logs/experimento_oro.json` del servidor y se ven con `scripts/ver_oro.py`.)

## Lectura
- **Los costes lo deciden todo**: una operación completa cuesta 0,3 % y las ventajas brutas son de 0,0-0,13 %. El azar con la misma gestión también pierde (−0,18 % a −0,30 %).
- **La mejor, tendencia EMA + RSI, sin costes gana +0,13 % por operación** y con costes pierde −0,14 %; es mejor que el azar (−0,18 %) pero sin significación (p = 0,26) y con 205 operaciones es una pista, no una prueba.
- **Gestión de salida**: el trailing bajó el acierto (del 40 % al 24 % en tendencia) y empeoró el resultado neto; el cierre parcial y el stop a la entrada apenas cambian nada; en Fibonacci y scalping son idénticos a la base (el nivel del 1,5R no llega a alcanzarse o coincide con el objetivo).
- **Scalping**: acierto del 5 % porque el objetivo (≈0,15 %) es menor que los costes (0,3 %).

## Límites (importante)
- PAXG no es el XAU/USD de un bróker: spread y comisión mucho más altos, mercado 24/7 y sin sesión asiática real. En un bróker con spread bajo las cifras «sin costes» (tendencia +0,13 %) serían la referencia, **pero eso no está probado**.
- Solo compras (PAXG es spot). No se midieron noticias, cierre de fin de semana, límite de pérdida diaria ni apalancamiento.
- La estrategia de Fibonacci pide muchas condiciones a la vez (solo 80 operaciones en el examen).
- Parámetros del manual sin ajustar; no se buscó «rescatar» ninguna.

## Lo construido (reutilizable)
- `motor.Gestion` y `cerrar_gestion`: stop a la entrada con costes, cierre parcial y trailing por ATR en el simulador (sin gestión el resultado es idéntico al de siempre; 12 pruebas).
- `estrategias/oro.py` (4 estrategias, no incluidas en el torneo real), `indicadores.rsi`, `experimento_oro.py` y velas de PAXG en `data/velas_oro/` (1 h, 15 min, 5 min).
- 350 pruebas pasan.

## Siguiente paso posible
Solo tendría sentido con datos reales de XAU/USD de un bróker (exportar velas de MetaTrader 5) y sus costes reales. Si con ellos tampoco gana al azar, el manual no aporta ventaja.
