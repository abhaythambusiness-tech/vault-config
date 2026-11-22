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
origen: mixto
---

# Sesión — 2026-10-06: Rediseño del bot AVAX

> [!abstract] Resumen
> El bot PPO de 15m llevaba la noche entera sin operar. Se auditó, se descartó el aprendizaje por refuerzo y se sustituyó por una estrategia de tendencia en velas de 4h, validada con backtest fuera de muestra. Código en `~/Proyectos/archive/AVAX-RL-Bot/` (spec en `spec.md`).

## Por qué "no hacía nada"
El modelo decidía HOLD casi siempre (83 de 96 velas) y no hay log de la noche. Además tenía fallos de diseño: normalización con fuga de datos y distinta entre entrenamiento y vivo, precios en bruto como entradas, el agente no veía si tenía posición, decisión con la vela aún incompleta, y 15m con comisiones que se comen el margen.

## Qué se decidió
- Estrategia: ruptura de máximo de 40 velas + filtro EMA300, salida por trailing stop de 4·ATR. Larga/plana, 100 % del capital.
- Backtest 2020-2026 con comisión 0,1 % + deslizamiento 0,05 % por lado: la familia con EMA300 es positiva en 4 de 6 años (Sharpe 1,2–1,5), con caídas de ~50 %.
- 1h descartado (comisiones). Tamaño por volatilidad descartado (baja el Calmar de 2,4 a 1,1). RL descartado.
- Bot nuevo en paper trading con estado persistente (`state.json`) y log en `logs/live.log`.

## Aprendizajes
- Un buen resultado de 2020-2023 en AVAX es un espejismo de mercado alcista: separar siempre un tramo de test y mirar año por año.
- Elegir parámetros por zona estable de la rejilla, no por el máximo.
- El timeframe manda: a 1h casi todo pierde por costes.
- Comprobar frescura de datos por huecos entre velas, no por antigüedad (fallaba a mitad de vela).
- El webhook de Discord estaba en el código y en git; ahora vive en `~/.claude/reference/avax-bot.env` (chmod 600). Sigue en el historial local: rotarlo.

## Próximos pasos
- Rotar el webhook de Discord.
- Dejar correr semanas en paper antes de pensar en dinero real.
- Montarlo como servicio de systemd si se quiere que sobreviva a reinicios.

## Relacionado
- [[04_Archive/AVAX-RL-Bot]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

