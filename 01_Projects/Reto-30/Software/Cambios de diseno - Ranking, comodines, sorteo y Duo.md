---
type: referencia
status: aprobado
date: '2026-10-17'
proyecto: Reto 30 (app real)
tags:
- reto-30
- cambios
- ranking
- sorteo
- duo
origen: mixto
---


# Cambios de diseño — Ranking, comodines, sorteo y plan Dúo

> [!resumen]
> Ideas nuevas de Haytham y Pedro del 2026-10-17, recogidas en conversación. **Los 6 documentos aprobados el 2026-10-14 no se han tocado**: esta nota lista qué cambia en cada uno. Hasta que se apruebe, el [[1 - PRD]], [[2 - TRD]], [[4 - AppFlow]], [[5 - Backend Schema]] y [[6 - Plan de Implementacion]] siguen vigentes.

## 1. Lo acordado

### Niveles y racha
- Tres niveles: básico, medio y avanzado (equivalen a Fácil, Medio y Avanzado del PRD).
- **Comodines:** el básico y el medio ganan uno cada 7 días del reto (4 en total: días 7, 14, 21 y 28). El avanzado gana uno cada 10 días (3 en total: días 10, 20 y 30).
- Gastar un comodín en un día fallado **cuenta ese día como cumplido** y la racha sigue. Sin comodines, un día fallado reinicia la racha a cero.

### Ranking por nivel
- Un ranking para cada nivel, ordenado por racha.
- Cada fila muestra: **nombre, racha, comodines gastados y retos extra cumplidos**.
- Desempate: primero **menos comodines gastados** (criterio que más penaliza), después **más retos extra cumplidos**.

### Reto extra
- Un reto extra **cada 3 días** (días 3, 6, 9… 30; 10 en total). Es opcional y cuenta para el desempate.
- Los días con reto extra, el correo diario lo avisa.

### Sorteo
- **Un único premio** compartido por los tres niveles; entran los clasificados de cualquier nivel.
- Para clasificar hace falta una **racha** de 21 días (básico), 26 (medio) o 30 (avanzado).
- **Mismas papeletas para todos** los clasificados, sin importar el nivel: quien elige avanzado asume el riesgo.

### Seguimiento por correo
- Correo diario con: reto del día, racha, comodines que quedan, puesto en el ranking y, si toca, aviso de reto extra.
- Además, seguimiento día a día dentro de la app.

### Ejercicios y cronómetro
- La app lleva un **cronómetro** por ejercicio (ejemplo: "10 flexiones, tienes 2 minutos") y también para los **descansos**.
- Repeticiones, tiempos y descansos los **programan Haytham y Pedro**.
- **Vídeos:** se usa primero la librería de vídeos ya hechos ([[Fuentes de Ejercicios y Multimedia Fitness]]); solo se graba el ejercicio que no exista en ella.

### Plan Dúo (dos personas)
- **Misma app, dos cuentas independientes**: cada uno tiene su usuario, su racha, sus comodines y su puesto en el ranking (aparecen por separado).
- Lo propio del Dúo es una **pestaña de pareja** con la racha del otro, aviso si tu pareja aún no ha entrenado hoy y una **racha conjunta** (solo suma los días en que ambos cumplen). La racha conjunta **no cuenta para el sorteo**.
- *Decisión de Claude, no de Haytham:* no se construye una app aparte para el Dúo. Es la misma base de código con una pestaña extra.

### Premio, precio y nivel (decidido el 2026-10-17, segunda tanda)
- **Premio:** **50 € + merchandising de Factory Training**. Sustituye al 25 % del beneficio (importe fijo, ya no depende del número de plazas).
- **Fecha del sorteo:** no se fija hasta que se lance la app.
- **Precio del plan Dúo:** **30 €** por la pareja (el individual sigue en 20 €).
- **Sin cambio de nivel a mitad del reto:** el nivel se elige al empezar y no se puede cambiar.

### Sorteo y reparto (decidido el 2026-10-17, tercera tanda)
- **Quién paga el premio:** Haytham y Pedro.
- **Factory Training cobra el 15 % de la facturación total**, sea cual sea el plan (20 € individual o 30 € Dúo).
- **Cómo se hace:** se anuncia **un día** y se sortea **al azar** entre los clasificados. **El dueño de Factory Training avisa en persona al ganador**; la app no envía ese aviso.
- **Si nadie clasifica:** gana la persona con **más racha** de todos los niveles. Si hay empate, **al azar entre los empatados**.

## 2. Choques con lo aprobado

> [!riesgo]
> Estos puntos contradicen o amplían documentos aprobados. Hay que decidirlos antes de actualizar nada.

| Tema | Lo aprobado | Lo nuevo | Efecto |
|---|---|---|---|
| Ranking | PRD §7: "ranking entre participantes" **fuera de alcance v1** | Ranking por nivel con nombre visible | Pasa a v1. Hay que pedir consentimiento para mostrar el nombre (RF-14, política de privacidad) |
| Sorteo | RF-13 y US-11: 30 días **consecutivos sin fallar** | Racha de 21/26/30 según nivel, con comodines | Cambia el criterio de elegibilidad. El requisito "sin fallar" de las bases deja de ser cierto |
| Bases legales | [[Borrador - Bases del sorteo]]: cláusula 4 y preguntas al abogado | Elegibilidad por nivel y comodines | Reescribir la cláusula 4 y añadir la pregunta de si los comodines o los tres umbrales afectan al encaje legal |
| Correo | TRD/Plan: correo solo al activar la plaza (RF-12); proveedor de correo pendiente en las 6 decisiones previas | Correo **diario** a todos los participantes | Hace falta proveedor, programación diaria, plantilla y baja de las comunicaciones (RGPD) |
| Racha | RF-05 y RF-13: racha simple | Comodines por nivel que cumplen días fallados | Nueva regla de racha y nueva tabla de comodines gastados |
| Cronómetro | No existe | Cronómetro de ejercicio y descanso | Nuevo modelo de datos por ejercicio (repeticiones, tiempo, descanso) |
| Plan Dúo | No existe | Cuentas emparejadas | Nueva relación entre usuarios y nuevo tipo de plaza |
| Precio | 20 € por persona | Plan Dúo a 30 € | Nuevo tipo de plaza con precio propio. El 15 % de Factory Training se calcula sobre la facturación total, también la del Dúo |
| Premio | PRD, RF-13 y bases: 25 % del beneficio, importe variable | 50 € + merchandising | Se simplifica: importe fijo. Reescribir la cláusula 2 de las bases y quitar la fórmula del beneficio; sigue pendiente de la consulta legal |
| Cambio de nivel | US-02 y RF-02: se puede cambiar de nivel sin perder lo completado | Nivel fijo durante todo el reto | Retirar el cambio de nivel del PRD y del AppFlow. Simplifica comodines y ranking |

## 3. Impacto por documento

- **[[1 - PRD]]:** nuevas historias (ranking, comodines, reto extra, cronómetro, correo diario, Dúo). Retirar "ranking" de fuera de alcance. Reescribir RF-13 y US-11. Añadir el plan Dúo a usuarios y precio.
- **[[2 - TRD]]:** proveedor de correo diario y programación, cálculo de racha con comodines, consulta del ranking, fuente de vídeos (librería de ejercicios) y reproducción en la app.
- **[[3 - UI-UX Design]]:** pantallas de ranking por nivel, cronómetro con cuenta atrás y descansos, comodines visibles, pestaña de pareja del Dúo.
- **[[4 - AppFlow]]:** flujo "completar el día" con cronómetro, uso automático del comodín, reto extra opcional y flujo de alta del Dúo. Revisar la regla R15 (sorteo desactivado por defecto).
- **[[5 - Backend Schema]]:** tablas o campos nuevos para comodines (ganados y gastados), retos extra cumplidos, repeticiones/tiempo/descanso por ejercicio, vínculo de pareja y vista del ranking con el desempate. Mantener RLS: el ranking solo expone nombre y cifras, nunca el correo.
- **[[6 - Plan de Implementacion]]:** tareas nuevas para cada punto anterior; revisar T-39 y T-40 (sorteo).

## 4. Preguntas abiertas

1. ~~Premio~~ **Decidido:** 50 € + merchandising de Factory Training, pagado por Haytham y Pedro. Falta saber qué merchandising concreto. *(parcial)*
2. ~~Fecha y forma del sorteo~~ **Decidido:** sin fecha hasta lanzar la app; se anuncia un día y se sortea al azar; el dueño de Factory Training avisa al ganador. Si nadie clasifica, gana la persona con más racha y los empates se sortean. Falta saber si ese sorteo es en directo o solo con acta, lo que depende de la consulta legal. *(parcial)*
3. ~~Precio del Dúo~~ **Decidido:** 30 €. Factory Training cobra el 15 % de la facturación total, sea cual sea el plan.
4. ~~Cambio de nivel~~ **Decidido:** no se puede cambiar de nivel a mitad del reto.
5. **Comodín automático o elegido:** lo dicho fue "al gastar un comodín ese día ya está cumplido". Se asume que se gasta solo al fallar un día; confirmar. *(suposición de Claude)*
6. **Qué cuenta como "completar el día"** ahora que hay cronómetro: ¿basta con terminar el tiempo o hay que marcarlo a mano? *(sin decidir)*
7. **Reto extra:** qué es (otro ejercicio, un hábito) y cuántos hay que programar. *(sin decidir)*
8. **Visibilidad del ranking:** nombre completo o solo nombre de pila o apodo, y qué pasa con quien no quiera aparecer. *(sin decidir)*
9. **Consulta legal:** el sorteo sigue pendiente de abogado o DGOJ; este cambio no la sustituye. Hay que añadir a las preguntas del abogado la regla "si nadie clasifica, gana quien tenga más racha" y el aviso al ganador por el dueño de Factory Training (protección de datos del nombre y contacto).

## 5. Estado (2026-10-17)
Los seis documentos y el [[Borrador - Bases del sorteo]] **ya están actualizados** con estos cambios. Tres valores por defecto de esta nota los aprobó Haytham el 2026-10-17: completar el día se marca a mano tras el cronómetro, el reto extra es un ejercicio opcional que programáis vosotros, y el ranking muestra nombre de pila + inicial con opción de ocultarse.

**Decisiones de Claude que conviene revisar** (están en el [[4 - AppFlow]], R15 a R22): el sorteo usa la **racha más larga** y no la actual; un comodín cubre el primer día sin completar y no da insignia; el reto extra se marca desde que completas ese día hasta las 07:00 siguientes; el correo diario sale a las 07:00; el Dúo se une con un código de 6 caracteres y los dos pueden tener niveles distintos; el nivel `Fácil` pasa a llamarse `Básico`.

**Pendiente**: el SQL **se probó en local el 2026-10-18 (102 comprobaciones) pero aún no se ha aplicado a Supabase** (T-07 del [[6 - Plan de Implementacion]]); merchandising concreto; sorteo en directo o con acta; fecha del sorteo; consulta legal.

