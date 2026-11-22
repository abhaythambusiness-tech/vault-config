---
type: proyecto
status: pausado
date: '2026-10-21'
repo: ssh@192.168.0.100:~/Proyectos/trend-bot-paper (git local, sin remoto)
tags:
- crypto
- trading
- bot
- tendencia
- papel
origen: mixto
---


# Bot de Tendencia

> [!resumen] En cristiano
> Es un **simulador** que compra y vende criptomonedas como si fuera real, pero con **dinero inventado** (10.000 USDT por cartera). Hay cinco «carteras» que prueban formas distintas de decidir: el *Seguidor diario*, el *de 4 horas* y el *de 1 hora* siguen las tendencias del mercado (el de 1 hora opera muchísimo y se come muchas comisiones); *Kronos diario* compra las 4 monedas que un modelo de IA llamado Kronos cree que más subirán en 5 días; y *Kronos scalper* mira cada 15 minutos y compra y vende muy rápido lo que Kronos prevé que subirá en la próxima media hora (lo más arriesgado). El panel enseña **velas de precio** con flechas donde el bot compró y vendió. **Ninguna ha demostrado que gane dinero**; por eso llevan la etiqueta «experimental» o «sin probar». Se comprueba con `scripts/estado.py` en el servidor.

> [!resumen]
> Bot de **seguimiento de tendencia en papel** (sin dinero real) sobre 12 criptomonedas de Binance spot, en el servidor Zorin. Tres carteras de 10.000 USDT virtuales con distinta frecuencia: **T** (diaria), **M** (4 h) y **F** (1 h, "operar bastante"). Operan desde el **2026-10-21 16:49 UTC** como **EXPERIMENTALES**: ninguna superó el criterio de validación fijado antes de medir. Proyecto personal de Haytham.

## Documentos
[[01_Projects/Bot de Tendencia/1 - PRD|PRD]] (investigación con fuentes, diseño, criterio y resultado del backtest).

## Qué dice la investigación (resumen)
La evidencia que mejor se sostiene para un bot minorista es **tendencia sencilla, diversificada y con riesgo dimensionado por volatilidad**, a frecuencia baja (Moskowitz-Ooi-Pedersen, AQR; un preprint de cripto con Donchian en conjunto reporta Sharpe > 1,5 que **no he podido verificar**). No hay evidencia de que operar más rentabilice; el carry de financiación y el sentimiento con LLM no se sostienen con los datos públicos disponibles. Metodología: parámetros fijados antes de medir, validación por periodos, Sharpe deflactado (Bailey y López de Prado) y registro de todas las variantes.

## Resultado del backtest (2020-2026, costes incluidos)
| | Sharpe total | 2024-26 | CAGR | Caída máx. | Ops/día | Costes/año |
|---|---|---|---|---|---|---|
| T diaria | 1,10 | 0,42 | 35 % | −49 % | 1,7 | 7,6 % |
| M 4 h | 1,22 | 0,43 | 40 % | −48 % | 6,8 | 44 % |
| F 1 h | 0,65 | −0,13 | 16 % | −64 % | 26 | 74 % |
| BTC comprar y mantener | 0,91 | 0,75 | 43 % | −77 % | | |
Más operaciones = más costes y peor Sharpe reciente. La ventaja de la tendencia fue una caída máxima menor, no mayor rentabilidad que BTC.

## Operativa
- Servidor: `~/Proyectos/trend-bot-paper/`, `cron` cada hora (minuto 2). `venv/bin/python scripts/estado.py` da equity, posiciones, órdenes de hoy y costes.
- Primera pasada: 36 órdenes (12 por cartera). Equity inicial 10.000 USDT por cartera; los costes de entrada fueron ~8-10 USDT cada una.
- **Panel web en vivo** (rediseñado el 2026-10-21 para que se entienda sin saber nada: fondo claro, frases sencillas, una página por estrategia y velas de precio con las compras y ventas del bot): `http://192.168.0.100:8060` (solo lectura, red local): cuánto llevan ganado o perdido las 4 huchas, qué tienen comprado, lo último que hizo el bot y si todo funciona. Detalle, verificación y límites en [[01_Projects/Bot de Tendencia/3 - Panel web]]. Código en `trend-bot-paper/src/panel_api.py` y `panel/static/`; lo vigila un `cron`.

## Cartera K: Kronos-small, SIN PROBAR (añadida el 2026-10-21 a petición de Haytham)
- **Qué hace**: cada noche (00:10 UTC) Kronos-small (sin ajuste fino) predice el retorno a 5 días de las 12 monedas; K compra a partes iguales las 4 con mejor previsión y rebalancea como mucho cada 5 días, con costes del 0,15 % por lado.
- **Primera selección (2026-10-21)**: BTC, AVAX, BNB y TRX, 25 % cada una; 4 órdenes y 14,98 USDT de costes.
- **Se puso en papel sin esperar a su prueba**; la prueba offline sigue calculándose en segundo plano (`~/Proyectos/kronos-test/`, criterio en [[01_Projects/Bot de Tendencia/2 - Prueba Kronos]]). Si el resultado no cumple el criterio, K se queda como experimento marcado, no como estrategia.
- Seguridad: si la previsión falta o tiene más de 3 días, K no opera y lo anota. Es dinero falso: no hay claves ni conexión a ninguna cuenta.

## Resultado de Kronos y lo que se hizo después (2026-10-21, noche)
- **Examen de Kronos-small con datos del pasado: NO APORTA.** Su acierto al ordenar las monedas fue del 2 %, indistinguible de la suerte (ver [[01_Projects/Bot de Tendencia/2 - Prueba Kronos]]). El modelo grande sigue calculándose.
- **Kronos scalper (hucha S, sin probar)**: cada 15 minutos Kronos-small prevé la subida a 30 minutos de las 12 monedas; S mantiene comprada (10 % del dinero, máximo 5) cada una que prevé subir ≥ 0,15 % y la vende en cuanto deja de verlo. Desde las 19:14 UTC hizo ya 2 operaciones (compró Cardano y la vendió 2 minutos después, ≈3 $ de comisiones). Casi todo lo ve en bajada, así que compra poco. **Sin ninguna prueba previa** y con el examen de Kronos sin resultados a su favor, lo esperable es que pierda en comisiones.
- **Mejora de rotación**: el umbral de 3 % redujo las comisiones de la diaria (7,6 → 2,7 % al año) y de la de 4 horas (44 → 19 %) y se aplica en vivo; la de 1 hora no cumplió la regla por una décima (39,9 % frente a 40 %) y se queda igual a propósito. Detalle en [[01_Projects/Bot de Tendencia/1 - PRD]] §5.2.

## PAUSADO el 2026-10-21 (noche), a petición de Haytham
> [!aviso] En cristiano
> Está todo **apagado**: ya no compra ni vende nada (ni siquiera de mentira), el panel no se abre y la prueba larga de Kronos está detenida. No se ha borrado nada: los datos, el código y las posiciones de las 5 huchas siguen guardados tal cual. Las huchas «se quedan congeladas» con lo que tenían comprado y su valor deja de actualizarse.

- **Qué se paró**: las 6 tareas de `cron` (bot cada hora, scalper cada 15 min, previsión diaria de Kronos, vigilante del panel con su arranque al reiniciar, recolector de titulares de cripto), el panel web (puerto 8060) y el examen del modelo grande de Kronos (265 líneas, unas 22 de 95 fechas hechas).
- **Cómo se reanuda** (en el servidor, usuario `ssh`): `crontab ~/crontab_activo_2026-10-21.txt` (copia del calendario original) y, para el examen de Kronos, `cd ~/Proyectos/kronos-test && nohup nice -n 15 venv/bin/python scripts/pedir_previsiones.py base > logs/base.log 2>&1 &` (continúa donde se quedó). El panel lo levanta solo el cron al minuto de reactivarlo.
- **RAM del servidor**: de 2,9 GB usados a 1,6 GB; libres 6,1 GB de 7,6; intercambio a 0.
- **Al reanudar**: las huchas retomarán con precios nuevos; T, M, F y K actúan en cuanto haya una vela nueva, y el scalper necesita una previsión de menos de 55 minutos (la primera tarda ~1 min).

## Pendiente
- Dejar correr al menos 4 semanas y comparar en vivo con el backtest.
- Rotación de M y F (296 y 494 veces al año) sugiere un umbral de rebalanceo demasiado pequeño; probar variantes cuenta como pruebas nuevas para el Sharpe deflactado.

## Relacionado
[[01_Projects/Mercados Laya/1 - PRD|Mercados Laya]] · [[01_Projects/Scalper Memecoins]] · [[00_Meta/Sesiones/2026-10-21 - Scalper Memecoins, arranque del flujo de software]]

