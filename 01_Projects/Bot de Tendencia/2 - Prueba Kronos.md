---
type: doc-software
doc: prueba
proyecto: 01_Projects/Bot de Tendencia
status: borrador
date: '2026-10-21'
origen: mixto
---


# 2 · Prueba de Kronos (sin enseñarle nada nuevo)

> [!resumen] En cristiano
> **Kronos** es un programa que ha mirado millones de velas de precios y trata de adivinar cómo seguirán. **Pregunta:** ¿acierta lo bastante como para ganar dinero **después de pagar comisiones**? **Cómo se prueba:** cada 5 días le damos las 12 monedas del bot, le pedimos que prediga cuánto subirá o bajará cada una en los próximos 5 días, y miramos si las que él pone arriba rinden de verdad más que las que pone abajo. **Reglas escritas antes de mirar nada:** si no cumple todas, Kronos no entra en el bot. Todo es en papel (dinero falso) y en el servidor.

## 1. Qué se prueba y con qué
- **Modelos** (se prueban los dos): `Kronos-small` (24,7 millones de parámetros) y `Kronos-base` (102,3 millones), con su `Kronos-Tokenizer-base`. Sin ajuste fino: se usan tal como vienen (*zero-shot*, «sin entrenarlo de nuevo»). Código: repositorio `shiyu-coder/Kronos` (licencia MIT). El código se revisa antes de ejecutarlo.
- **Datos**: velas diarias de las mismas 12 monedas de Binance que usa el bot de tendencia. Cada predicción ve las **400 velas anteriores** (el modelo admite 512).
- **Periodo de evaluación**: desde **2025-07-01** hasta 2026-10-15, una predicción **cada 5 días** (así las ventanas no se solapan): unas 95 fechas × 12 monedas por modelo. Se elige este periodo porque lo más probable es que sea posterior a lo que Kronos vio al aprenderlo; **no sé su fecha de corte**, y lo declaro como riesgo.
- **Predicción**: 5 velas por delante, parámetros por defecto del README (`T = 1,0`, `top_p = 0,9`). Predicción de la moneda = su subida prevista a 5 días. **Muestras promediadas: 2** (el plan inicial era 5, pero en la CPU del servidor tardaba 99 s por fecha con 5 muestras, 2,6 h solo para el modelo pequeño y ~10 h para el grande). Cambio decidido **antes de ver ningún resultado** (solo se midió el tiempo de las 2 primeras fechas, cuyos resultados se borraron); con menos muestras la previsión es más ruidosa, lo que juega **en contra** de Kronos.

## 2. Cómo se mide (todo fijado antes de ejecutar)
1. **RankIC** (en cristiano: «¿ordena bien las monedas de mejor a peor?»): en cada fecha se ordenan las 12 monedas según la subida prevista y se compara con el orden real (de la apertura del día siguiente a la apertura 5 días después). Se promedia entre fechas; el intervalo de confianza del 95 % se obtiene remuestreando fechas.
2. **Estrategia «Top-4»** (en cristiano: «comprar las 4 que Kronos más recomienda»): cada 5 días, 100 % invertido a partes iguales en las 4 monedas con mayor subida prevista, solo largo, **costes del 0,15 % por lado** sobre lo que se compra y se vende. Se compara con:
   - **EW-12**: las 12 monedas a partes iguales, rebalanceadas cada 5 días con los mismos costes.
   - **T**: la cartera diaria del bot de tendencia, en el mismo periodo.

## 3. Criterio de aprobación (no se cambia después de ver resultados)
Un modelo **aporta** solo si cumple TODO:
1. **RankIC medio ≥ 0,03** y límite inferior del IC95 **> 0**.
2. RankIC medio **> 0 en las dos mitades** del periodo.
3. **Exceso neto** de Top-4 sobre EW-12 (por periodo de 5 días): media > 0 y límite inferior del IC95 > 0.
4. **Sharpe neto** de Top-4 **> Sharpe de T** en el mismo periodo (Sharpe = «cuánto ganas por cada susto que pasas»).
5. El exceso sigue siendo **> 0 quitando los 3 mejores periodos**.
6. **Sharpe deflactado ≥ 0,90** contando **5 pruebas** (T, M, F, Kronos-small y Kronos-base). «Deflactado» = rebajar el resultado por haber probado varias cosas y quedarse con la mejor.
- Si cumple solo 1 y 2: «tiene información, pero no paga las comisiones». Si no cumple 1: «no aporta».
- Se informa también el RankIC por trimestre: si la señal solo aparece en el primero, sospecha de que Kronos ya conocía esos datos.

## 4. Riesgos
> [!riesgo]
> - **Fecha de corte desconocida**: si el preentrenamiento incluyó parte del periodo, el resultado sale inflado. Por eso se mira por trimestres.
> - **Solo 95 fechas**: los intervalos serán anchos; pasar es difícil, y es lo esperable.
> - **Es una prueba más**: hay que contarla al deflactar.
> - **Código de terceros**: corre con todos los permisos; se revisa antes, igual que con Laya.
> - **CPU sin GPU**: el modelo pequeño debería ir bien; el base puede tardar.

## 5. Resultado del modelo pequeño (2026-10-21): NO APORTA
> [!resumen] En cristiano
> **Kronos no demostró que acierte más que la suerte.** En 95 fechas distintas (julio de 2025 a octubre de 2026) le pedimos que ordenara las 12 monedas de la que más subiría a la que menos, y su acierto fue **casi nulo (2 %)**, con un margen de error tan grande que incluye el 0 (el azar puro). Comprar las 4 que él elegía salió **algo mejor que comprar todas**, pero esos meses fueron malos para todo el mercado y la diferencia es tan pequeña e irregular que puede ser pura suerte. **No hay razón para fiarse de él con dinero real.** Siguen en papel, con la etiqueta «sin probar», Kronos diario y Kronos scalper.

| Medida | Resultado | Necesitaba | ¿Cumple? |
|---|---|---|---|
| Acierto al ordenar las monedas (RankIC) | 0,021 [−0,043, +0,083] | ≥ 0,03 y límite inferior > 0 | **No** |
| Acierto en las dos mitades del periodo | 0,036 y 0,007 | positivo en ambas | Sí |
| Ganancia extra de «las 4 de Kronos» sobre «las 12 a partes iguales», por cada 5 días | +0,19 % [−0,19, +0,57] | límite inferior > 0 | **No** |
| Calidad (Sharpe) de «las 4 de Kronos» frente a la cartera diaria en el mismo periodo | 0,06 frente a −0,22 | mayor | Sí |
| Sigue ganando quitando los 3 mejores periodos | +0,02 % | > 0 | Sí |
| Calidad deflactada (rebajada por haber probado varias cosas) | 0,29 | ≥ 0,90 | **No** |
- Por trimestre el acierto salta de −0,065 a +0,166: es ruido, no una señal estable. No se ve un patrón claro de «solo funciona al principio», pero con tan pocas fechas no se puede descartar del todo que Kronos ya conociera parte de esos datos.
- **Modelo grande (102 millones de parámetros)**: en marcha en segundo plano con prioridad baja (17 de 95 fechas a las 19:30 UTC); su resultado se añadirá aquí. Cuenta como una prueba más.
- **Resultados completos**: `~/Proyectos/kronos-test/docs/kronos_resultado.json` en el servidor (commit `0a05c8a`).

## 6. Siguiente
Esperar al modelo grande. Mientras tanto, las huchas de Kronos siguen como experimentos: **Kronos diario** (top 4 a 5 días) y **Kronos scalper** (velas de 15 minutos, desde 2026-10-21 19:14 UTC).

---
Relacionado: [[01_Projects/Bot de Tendencia/1 - PRD|PRD del Bot de Tendencia]] · [[01_Projects/Bot de Tendencia]]

