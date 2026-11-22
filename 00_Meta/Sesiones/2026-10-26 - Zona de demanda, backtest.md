---
type: sesion
status: cerrado
date: '2026-10-26'
proyecto: '[[Zona de Demanda - Patron y Backtest]]'
tags:
- trading
- backtest
- zona-de-demanda
origen: mixto
---

# Sesión — 2026-10-26: Zona de demanda, backtest

> [!resumen] En cristiano
> Haytham pidió probar su patrón de zona de demanda (vela grande alcista + retroceso que respeta la zona). Se programó con reglas escritas antes de medir y se probó en BTC, ETH y SOL. **NO PASA**: no gana al azar tras comisiones. Queda documentado en el Playbook.

## Contexto
Parte de [[Playbook - Index]] y [[Pine 5m - Indicador y Estrategia]]. Haytham dibujó el patrón sobre una captura y aclaró que la raya de arriba es el take profit.

## Qué se hizo
- `backtest/zona_demanda.py` y `test_zona.py` (5 pruebas) en `~/Proyectos/pine-cripto-5m/`; reutiliza las velas de `backtest/data/` (1h sale de remuestrear 5m; 4h BTC y ETH desde 2017).
- Criterio de éxito escrito en el docstring antes de ejecutar; línea base aleatoria de 1000 grupos con mismo stop y objetivo en %.
- Resultados: 1h y 4h NO PASAN (núcleo BTC+ETH, R neto -0,24 y -0,09; p azar 0,76 y 0,72). Nota: [[Zona de Demanda - Patron y Backtest]].

## Decisiones tomadas
- No operar el patrón con dinero real.
- La tabla de sensibilidad (K y objetivo) es informativa; no se elige el mejor resultado a posteriori.

## Aprendizajes (para futuras sesiones)
- Supuesto no confirmado: techo de la zona = mínimo de la vela siguiente a la impulso.
- Objetivo en el último máximo local da riesgo/beneficio de ~1,0-1,2: la comisión se lo come. El 2R fijo mejora (+0,07 a +0,15 R en 4h) pero sin significancia (p 0,15-0,22), y con 12 combinaciones probadas no vale como prueba.
- Entorno: el Python del sistema no tiene pandas; se creó un venv con uv en el scratchpad de la sesión (pandas, numpy, pyarrow, pytest).

## Próximos pasos
- Decidir si se hace una única prueba más con criterio nuevo (2R fijo, impulso >= 2 ATR, 4h, SOL/AVAX/DOGE desde 2020) o se cierra aquí.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[Zona de Demanda - Patron y Backtest]]

- 5m: NO PASA (BTC+ETH -1,01 R, p azar 0,41). Ver [[Zona de Demanda - Patron y Backtest]].
- Mismo día, segunda estrategia (transcripción de un curso): retroceso al POC del perfil de volumen. 5m, 1h y 4h NO PASAN. Ver [[Retroceso al POC - Patron y Backtest]].
- Nueva regla de Haytham: backtests solo en oro. Se descargó PAXGUSDT (5m, 2020-10 → 2026-10; sustituto del XAU/USD) y se repitieron las dos estrategias: ambas NO PASAN en 5m, 1h y 4h. Ver [[Zona de Demanda - Patron y Backtest]] y [[Retroceso al POC - Patron y Backtest]].
- Filtro de horario de persona (lun-vie 07-20 UTC, cierre al acabar la sesión; opción `--sesion` en ambos scripts): mejora algo los números pero ambas estrategias siguen en NO PASA en oro 5m/1h/4h.
