---
type: doc-software
doc: prd
proyecto: 01_Projects/Eventos Bolsa
status: pausado
date: '2026-10-21'
origen: mixto
---


# 1 · PRD — Eventos Bolsa (confluencia híbrida, prueba offline primero)

> [!resumen]
> Estrategia elegida por Haytham: **confluencia híbrida**. Una señal técnica de compra (ruptura de máximos con volumen) solo se ejecuta si **Laya**, leyendo las noticias de la empresa, la respalda. Objetivo: filtrar falsas rupturas sin fundamento. Antes de construir bot o panel hay una **Puerta 0** offline con datos históricos. Si no pasa, el cambio de mercado se cierra. Si pasa, se abre el flujo de 6 documentos para un bot en **papel** (sin dinero real) con panel en vivo. Proyecto personal de Haytham; sucede a [[01_Projects/Scalper Memecoins]].

## 1. Problema
- Haytham quiere un bot que opere en papel acciones con una señal técnica **filtrada por noticias** y un panel en vivo con decisiones y ganancias, con Laya como "Sistema 1" local en el servidor Zorin.
- **Por qué es una pregunta abierta**: tres proyectos de cripto no hallaron ventaja tras costes, y Laya con estados numéricos falló (AUC 0,31-0,39, al revés). Con **texto** no se ha probado. Además, el tono de un comunicado lo explotan los fondos en milisegundos; aquí se opera a **barras diarias** (decisión tras el cierre, orden en la apertura siguiente), donde la latencia de Laya (~0,6 s) deja de importar, pero también se pierde el primer movimiento.

## 2. Diseño de la prueba (Puerta 0)
**Universo**: acciones del S&P 500 (lista actual; periodo corto para limitar el sesgo de supervivencia). **Periodo**: 2025-01-01 a 2026-10-15.

**Señal técnica (única, fijada)**: al cierre del día *t*, `Close_t` supera el máximo de los 20 días anteriores **y** `Volumen_t ≥ 1,5 ×` la media de volumen de los 20 días anteriores. Un solo aviso por acción cada 10 sesiones.

**Catalizador (fuente de noticias v1)**: 8-K de la propia empresa aceptados por la SEC entre *t*−4 y el cierre de *t* (anexo EX-99.1 si existe; si no, el cuerpo del 8-K). Es la única fuente histórica completa y gratuita con hora exacta. Limitación asumida: no son noticias de prensa general.

**Lo que ve Laya**: titular y primeros ~1.000 tokens del texto. Preguntas: `tono` (choice: buena / mala / neutra) y `catalizador` (noul: ¿describe un hecho de negocio concreto —resultados, guía, contrato, adquisición, producto— y no un trámite administrativo?). Puntuación = P(buena) − P(mala).

**Brazos comparados** (mismas señales técnicas, mismo periodo):
| Brazo | Qué ejecuta |
|---|---|
| A | todas las rupturas |
| B | rupturas con algún 8-K reciente |
| **C** | **B más aprobación de Laya** (puntuación por encima de la mediana de B y `catalizador` = sí) |
| D | B más aprobación por léxico simple (palabras de resultados), mismo tamaño que C |
| E | B más selección aleatoria del mismo tamaño que C (1.000 repeticiones) |

**Entrada**: apertura de la sesión siguiente a *t*. **Salida**: cierre a +5 y +10 sesiones. Sin stops. Solo largos. **Retorno anormal** = retorno de la acción − retorno de SPY. **Costes**: 0,10 % de deslizamiento y 0,05 % de comisión por lado (supuesto; se medirá con spreads reales si pasa). Se informa también el retorno bruto.

**Análisis secundario (no decide)**: tono de Laya frente al retorno a 1 y 5 días en los 8-K de resultados (Item 2.02), con los mismos textos.

## 3. Criterio de aprobación (fijado ANTES de medir; no se cambia después)
La Puerta 0 **pasa** solo si se cumple TODO:
1. **n(C) ≥ 400** señales aprobadas por Laya y **n(B) ≥ 800**.
2. Retorno anormal medio **neto** del brazo C con **IC95 inferior > 0** a +5 o a +10 sesiones.
3. **C − A** con IC95 inferior > 0 (el filtro aporta frente a operar todas las rupturas).
4. **C − E** > 0 con p < 0,05 (Laya selecciona mejor que azar con el mismo tamaño).
5. **C − D** con IC95 inferior > 0 (Laya supera al léxico simple).
6. La media de C es **> 0 en las dos mitades temporales**.
7. Se mantiene positivo **quitando las 3 mejores señales** de C.
Los intervalos se calculan con **bootstrap por día** (las señales del mismo día están correlacionadas). Si falla cualquiera, **se cierra el cambio de mercado**. Cambiar el criterio después de ver resultados queda prohibido.

## 4. Datos y fuentes (a verificar)
| Dato | Fuente | Estado |
|---|---|---|
| Universo S&P 500 | lista pública (a descargar) | pendiente |
| 8-K y hora de aceptación | SEC EDGAR `data.sec.gov/submissions` | verificado: responde desde el servidor |
| Texto del comunicado | anexo EX-99.1 / cuerpo del 8-K | verificado en un 8-K real |
| Precios diarios OHLCV | Yahoo Finance (como `stock-copy-bot`); plan B Stooq | verificado: responde |
| Calendario de sesiones | `market_calendar.py` de `stock-copy-bot` | por revisar |
Cabecera de la SEC: se necesita un contacto real; `stock-copy-bot` usa uno falso (`contact@stockcopybot.local`).

## 5. Fuera de alcance
- Dinero real; forex, materias primas y cripto; operar fuera de horario; fuentes de noticias de pago; reentrenar Laya; cortos.
- Bot y panel hasta que la Puerta 0 pase.

## 6. Riesgos y supuestos
> [!riesgo]
> - **Ventaja inexistente o ya descontada**: una ruptura con noticia positiva suele estar ya reflejada en el precio del día *t*; entrar a la apertura siguiente llega tarde.
> - **Muchas decisiones de diseño** (umbrales, ventana de noticias, horizonte): se fijaron arriba para no ajustar después; aun así hay riesgo de falsos positivos por probar varios horizontes (+5 y +10) y varios brazos, que el criterio de 7 condiciones compensa.
> - **8-K ≠ noticias**: sin prensa, rumores ni redes. Un 8-K de resultados se publica el día del evento, antes o después de la ruptura, y puede ser lo que la causa (sesgo de causalidad inversa si se publica tras la ruptura del día).
> - **Muestra**: si hay pocas rupturas con 8-K, no se llega a n(C) ≥ 400 y la prueba termina como "no concluyente".
> - **Datos**: Yahoo no es oficial; la SEC pide un contacto real en la cabecera.
> - **Desconocido**: con qué datos se entrenó Laya (por eso solo 2025-2026).
> - **Memoria y tiempo**: unos 2-3 s por texto de 1.024 tokens; 2.000 textos ≈ 1-2 h en segundo plano en el servidor.

## 7. Siguientes pasos
1. Aprobar este PRD y el criterio de la sección 3.
2. Construir en `~/Proyectos/eventos-bolsa/` (sandbox del servidor): universo, precios, señales técnicas, 8-K y textos.
3. Puntuar con Laya, analizar y dar el veredicto.
4. **Pasa** → abrir TRD, UI/UX, AppFlow, Schema y Plan para el bot en papel. **No pasa** → cerrar.

---
Relacionado: [[01_Projects/Scalper Memecoins]] · [[00_Meta/Sesiones/2026-10-21 - Scalper Memecoins, arranque del flujo de software]]

