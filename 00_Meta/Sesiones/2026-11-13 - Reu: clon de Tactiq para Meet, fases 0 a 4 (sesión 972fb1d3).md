---
title: 'Reu: clon de Tactiq para Meet'
date: '2026-11-13'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/Reu/1 - PRD]]'
sesion_id:
- 972fb1d3-4e68-4b46-94ad-ae2f24e832b8
tags:
- sesion
- reu
---

> [!resumen] En cristiano
> Haytham preguntó si se podía copiar gratis Tactiq (guarda las transcripciones de Google Meet). Se decidió una versión mínima: solo Meet, sin resumen con IA, con exportación y un panel con las reuniones. Se aprobaron PRD y Plan y se construyeron las primeras tareas de la extensión de Chrome «Reu». Aún no se ha probado en un Meet real.

## Qué se hizo
- Repo `~/Proyectos/reu/` (Node 22, TypeScript, Vite, Preact), documentos en `01_Projects/Reu/` (PRD y Plan de Implementación).
- T-00 a T-02: scaffold, `src/db.ts` (IndexedDB con borrado en cascada) y `src/merge.ts` (une las reescrituras parciales de cada frase).
- T-03 y T-04 (commit `b6dc616`): `captions.ts`, `content.ts`, `background.ts`, selectores de Meet aislados en `selectors.ts` con plan B por estructura; pastilla indicadora (verde, ámbar si no hay subtítulos, roja si se recargó la extensión).
- 11 pruebas Vitest, typecheck y build limpios; probado con una página de Meet simulada en Chromium.

## Decisiones
- Alcance: solo Meet, sin resumen, exportación y panel de reuniones.

## Problemas y límites
- Meet real no se probó (pide cuenta de Google); las clases `.nMcdL`, `.KcIKyf`, `.ygicle` vienen de lo conocido, no vistas en pantalla.
- Si alguien repite la misma frase seguida («Sí»), la segunda se pierde.
- Una llamada a herramienta se interrumpió al final.

## Pendientes
- `npm run build` y cargar `dist/` en `chrome://extensions`; probar en una reunión con subtítulos.
- Panel, búsqueda, exportación y pulido; origen de la ficha de proyecto (§0.8) y `resumen.html`.

## Relacionado
[[01_Projects/Reu/1 - PRD]] · [[01_Projects/Reu/6 - Plan de Implementacion]]

