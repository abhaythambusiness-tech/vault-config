---
type: sesion
status: completada
fecha: '2026-10-07'
proyecto: '[[04_Archive/goat-trading]]'
tags:
- crypto
- trading
- bot
- backtest
- decision
origen: mixto
---


# Sesión — 2026-10-07: goat-trading, del diseño al veredicto del Gate 1

> [!abstract] Resumen
> Tercer intento de bot cripto tras cerrar Memecoin-LSTM y rediseñar AVAX. Se diseñó la plataforma completa (spec + plan), se implementó el Plan 1 (datos y validación, 9 tareas, TDD) y **el Gate 1 salió NO PASA**: 100 € → 59,70 € en papel, con la cuenta muerta el 21-mar-2025. Según la spec, no entra dinero real y el Plan 2 no se escribe.

## Contexto
Haytham pidió "el plan definitivo" con tres piezas: elegir las criptos de Q4, un duelo reglas-fijas contra ML, y un dashboard premium multi-bot en vivo. Presupuesto 10-100 €, objetivo 1.000 € en un mes.

## Decisiones tomadas
- **Objetivo declarado y reconfirmado**: 100 € → 1.000 €, 500 € como suelo aceptable, **sin apalancamiento**. Se le explicó apalancamiento y liquidación y lo rechazó explícitamente. Queda por escrito en la spec porque determina el diseño: sin apalancamiento la única vía a x5-x10 es rotar altcoins de alta volatilidad, lo que descarta bitcoin como motor.
- **Este mes en papel, sin dinero real** (decisión suya a mitad de sesión). Eso eliminó la dependencia del KYC y permitió arrancar el mismo día.
- **Binance como fuente única** de velas y exchange de referencia, coste modelado al 0,10 % por lado. Bitvavo queda como alternativa futura, pero cambiar de exchange obliga a repetir la validación con sus velas.
- **Cuatro planes separados, solo se escribió el primero**, porque el Gate 1 podía matar el proyecto el día 3 — y lo hizo.
- `goat-trading` como nombre.

## Resultado: Gate 1 NO PASA
| Métrica | Valor |
|---|---|
| Capital | 100,00 € → **59,70 €** |
| Operaciones | 65 |
| Trimestres en positivo | 0 de 4 |
| Peor caída | 55,6 % |
| Costes pagados | 7,57 € |
| Sin las 3 mejores operaciones | −69,49 € |
| Cuenta muerta | 2025-03-21 (bajó del suelo de 60 €) |

Universo real: 136 monedas de Binance con >2 M€/día y ≥180 días de histórico, 900 días, velas de 4 h. Informe en `~/Proyectos/archive/goat-trading/docs/reports/gate1-2026-10-06.md`.

## Aprendizajes
- **El gate escrito antes de medir volvió a ser lo único que permitió decidir.** Dos veces: para cerrar Memecoin-LSTM y ahora para no meter dinero en esta rotación. Sin él habría "faltado afinar un parámetro".
- **Un resultado negativo también hay que desmontarlo antes de creerlo.** El primer informe daba "0 de 6 trimestres en positivo" con cuatro a 0,00 €, indistinguible de un mercado plano. Al comprobarlo había 31-58 monedas elegibles en esas fechas: la cuenta estaba **muerta**, no plana — había caído por debajo del mínimo de orden y no podía comprar. Reportar ese informe como hallazgo de mercado habría sido reportar un bug.
- **Una revisión con contexto fresco encontró 5 fallos críticos que 51 tests en verde no veían.** El peor: `quarterly_pnl` solo contenía los trimestres *con* operaciones, así que un bot parado dos años pasaba el gate con "4 de 4 en positivo". Es el falso PASA más caro posible y le pasa de forma natural a cualquier estrategia de momentum con filtro de tendencia.
- **Seis tests no probaban nada** y la suite estaba verde: uno comparaba `feature_frame(df)` consigo mismo, el de fuga de datos comparaba recortar-dos-veces con recortar-una, y ninguno recorría el camino PASA. Un `passed = False` constante habría aprobado la suite entera. **Lección: después de añadir un filtro, comprobar que las aserciones del tipo "X no está en la lista" no se cumplen en vacío.**
- **Los fixtures sin ruido mienten.** Sobre una recta, la volatilidad realizada mide la curvatura de la rampa, no el nervio del precio: la serie que menos subía puntuaba 8 veces más. Ningún fixture de una métrica ajustada a volatilidad puede ser una recta lisa.
- **Un par anclado (USDC/USDT) rompe cualquier score de momentum/volatilidad**: volatilidad casi nula, puntuación alta, y ocupa una plaza sin poder dar nunca el movimiento buscado. Los cuatro pares anclados del universo estaban dentro; hace falta un suelo de volatilidad explícito.
- **Rendimiento como bloqueante de diseño**: recalcular las features en cada vela daba ~10 h de ejecución y el gate era inejecutable. Cachear es seguro solo porque todas las ventanas son causales, y eso hay que fijarlo con un test (la fila calculada sobre la serie completa debe ser idéntica a la calculada sobre la recortada).
- **Preregistrar limita el autoengaño mejor que cualquier revisión posterior.** Escribir "dos hipótesis, el gate no se toca, y si las dos fallan se para" antes de medir convirtió un +37 % en un rechazo razonado en lugar de en una excusa para seguir.
- **Un fixture uniforme esconde fallos reales.** El ML abortó con datos reales porque las monedas tienen históricos de 1.166 a 5.399 velas y pandas alinea al índice unión; todos los fixtures tenían la misma longitud. Al menos un fixture irregular por cada estructura de datos que venga del mundo.
- **La fricción es el enemigo con capital pequeño**: entre el 7,6 % y el 22,5 % del capital inicial pagado en comisiones y deslizamiento. El ML perdió más por operar más, no por elegir peor.
- **Sesgo de supervivencia**: construir el universo con `fetch_tickers()` de hoy y aplicarlo a 900 días atrás mete liquidez que no existía y deja fuera a las que murieron. La mitad se arregla midiendo el volumen de cada momento; la otra mitad (pares deslistados) no se puede recuperar de la API de Binance y hay que declararla.

## Plan 1.5: dos hipótesis más, las dos refutadas
Tras el primer NO PASA se escribió un **preregistro** con dos hipótesis y solo dos, el Gate 1 sin tocar, una ejecución por hipótesis y la decisión de parar escrita de antemano. Las dos fallaron:

| Medida | Reglas 4 h | Reglas 1 d | ML 4 h |
|---|---|---|---|
| Capital final | 59,70 € | **136,87 €** | 59,41 € |
| Sin las 3 mejores | −69,49 € | **−201,39 €** | −154,62 € |
| Trimestres positivos | 0 de 4 | 3 de 6 | 0 de 6 |
| Peor caída | 55,6 % | 74,9 % | 72,1 % |
| Costes pagados | 7,57 € | 11,04 € | **22,54 €** |

- **La hipótesis diaria dio +37 % y el gate la tumbó con razón**: sin tres operaciones pierde 201 €. Es el mismo patrón que cerró Memecoin-LSTM. Sin el criterio escrito antes, habría parecido un éxito y habría entrado dinero.
- **El ML operó más del doble (158 contra 65), pagó 22,54 € de fricción sobre 100 € de capital y acabó igual.** Más actividad, más coste, mismo sitio.
- Lo que comparten las tres: el resultado se vuelve muy negativo al quitar tres operaciones. **No hay ventaja repetible; hay una cola derecha gorda.** Eso no lleva 100 € a 1.000 € en un mes.

## Próximos pasos
- **Proyecto de bots PARADO.** No hay Plan 1.6, no se prueba una cuarta señal sobre los mismos datos, no entra dinero real. No se borra nada.
- El camino a 1.000 € es NeoZeler, no una cuenta de 100 €.
- Pendiente de Haytham: rotar los 3 webhooks de Discord antiguos (Memecoin-LSTM ×2 y AVAX), que siguen en el historial de git.
- Bot AVAX en paper parado en esta sesión (llevaba desde el 6-oct a las 19:45; cartera de 32 monedas en velas de 2 h, plana en 1.000 €).

## Relacionado
- [[04_Archive/goat-trading]]
- [[00_Meta/Sesiones/2026-10-06 - Cierre del proyecto Memecoin-LSTM]]
- [[04_Archive/AVAX-RL-Bot]]
- [[00_Meta/Registro de Sesiones]]

