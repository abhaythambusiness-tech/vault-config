---
title: "Sesión - 2026-11-03 - Reto 30: Cómo hacerlo por ejercicio y GIFs"
date: 2026-11-03
type: meta/sesion
proyecto: Reto 30
sesion_id: 93d31246-80dc-4f7d-af30-707291ba8902
tags:
  - sesion
  - cierre-automatico
aliases: []
origen: mixto
---

# Sesión — 2026-11-03: Reto 30, «Cómo hacerlo» por ejercicio y GIFs

> [!resumen] En cristiano
> Haytham tenía tres quejas de la app Reto 30: cada ejercicio debía tener sus propios pasos de «cómo hacerlo», los GIFs no se veían, y el botón «Completar el día» no aparecía hasta el final. Ahora cada ejercicio muestra sus pasos numerados y los GIFs salen en todos. El botón sigue saliendo solo tras el último ejercicio, porque se probó mostrarlo siempre y se volvió atrás.

## Contexto
Proyecto [[01_Projects/Reto-30/Reto 30 - App real|Reto 30 - App real]]. Continúa [[2026-11-02 - Reto 30 - GIFs de ejercicios y tarea de cierre nocturno (sesión a9265e7d)]].

## Qué se hizo
- «Cómo hacerlo» propio por ejercicio, con pasos numerados sacados de su texto (`GuidedWorkout.tsx`); se quitó el bloque general del día cuando hay ejercicios guiados (`[dia]/page.tsx`).
- GIFs visibles en todos los ejercicios (commit `2b6e3ef`, 28 GIFs nuevos). Se comprobó que los 390 ejercicios del seed tienen ilustración y que los 70 GIFs existen.
- Haytham pidió un commit; al principio no se hizo ninguno. Finalmente quedó subido a `main` como `b77b517`.

## Decisiones tomadas
- «Completar el día»: Haytham pidió que saliera al terminar los 4 o 5 ejercicios. Se probó mostrarlo siempre y se revirtió; queda como estaba (solo tras el último ejercicio).

## Problemas
- El primer commit no se llegó a hacer y Haytham tuvo que avisar.
- `vitest` da `ERR_REQUIRE_ESM`, así que no se ejecutó.

## Pendientes y próximos pasos
- [ ] Mirar los cambios en el navegador (no se hizo).
- [ ] Confirmar el despliegue en Vercel.
- [ ] Arreglar `vitest` (`ERR_REQUIRE_ESM`).
- [ ] Aclarar si «Completar el día» debe aparecer antes: el resultado final no coincide del todo con lo que pidió Haytham.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
