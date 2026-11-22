---
title: "Sesión - 2026-10-31 - NeoZeler Web - T-05 a T-11, plan UX v2 y medición de consumo"
date: 2026-10-31
type: meta/sesion
proyecto: "[[NeoZeler Web]]"
sesion_id: 4fd64972-e65e-4a4f-b99d-9d9f88fe2f36
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-10-31: NeoZeler Web: T-05 a T-11, plan UX v2 y medición de consumo

> [!resumen] En cristiano
> Sesión larga que siguió construyendo la web de NeoZeler (tareas 5 a 11), la desplegó en local y, al final, midió cuántos tokens se gastan antes de escribir nada: unos 98.000, casi el 10 % de la ventana. No se cambió nada.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `4fd64972`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Tareas T-05 a T-11 (saltando a T-09 por decisión de Haytham); `recomendador.tsx`, `caso-form.tsx`, `cta-links.tsx`.
- Notas `Analisis UI-UX y Plan de Mejora.md` y `Plan de Componentes UX v2.md`.
- Despliegue de la página en localhost.
- Medición de consumo: ~98k tokens siempre cargados (9,8 %), ~136k en sesiones reales; reglas ~28k, skills ~40k, CLAUDE.md ~10k, MCP ~3k.

## Decisiones tomadas
- Medir primero, recortar después: sin cambios en esta sesión.

## Archivos y proyectos afectados
- `01_Projects/NeoZeler Web/`
- `~/Proyectos/neozeler-web/src/`

## Problemas
- `librerias.md` (~36 KB) y `skills-frecuentes.md` (~24 KB) se cargan siempre.

## Mejoras propuestas
- Pasar reglas pesadas a carga bajo demanda.
- Adelantar la compactación a 300k evitaría ~55 % de lecturas de caché (~129 $ netos en 30 días, medido sobre el historial).

## Pendientes y próximos pasos
- Ninguno registrado.

## Relacionado
- [[NeoZeler Web]]
- [[2026-10-31 - Arranque NeoZeler Web]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
