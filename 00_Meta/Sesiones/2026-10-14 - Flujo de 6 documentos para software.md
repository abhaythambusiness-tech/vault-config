---
type: sesion
date: '2026-10-14'
proyecto: '[[00 - Flujo de Software]]'
status: completada
origen: mixto
---

## Contexto
Haytham pidió mejorar el sistema de creación de software: al empezar un proyecto, una carpeta en el vault con PRD → TRD → UI/UX → AppFlow → Backend Schema → Plan de Implementación.

## Qué se hizo
- 6 plantillas + guía en `00_Meta/Plantillas/Proyecto Software/` (Templater, enlazadas entre sí).
- Regla §0.10 en `CLAUDE.md` y `GEMINI.md` del vault.
- Segunda ronda ("aplica todas" las 13 ideas): `~/Proyectos/flujo-software/` con `trace_lint.py` y `schema_to_migration.py` (8 pruebas OK), plantillas ampliadas (ficha de librería, presupuesto de dependencias, tokens primero, slots por pantalla, demo provocadora, cliente simulado, SQL ejecutable), [[Catalogo de Componentes]], [[Biblioteca de Layouts]], [[Starter Kits NeoZeler]], [[Dashboard - Proyectos de Software]] y skill `/nuevo-proyecto`. Ficha: [[Flujo de Software]].

## Aprendizajes
- Orden estricto con aprobación entre documentos: el código no empieza hasta tener el plan.
- Proyectos pequeños: solo PRD + Plan, para no burocratizar.
- Se encaja con la metodología de 3 reuniones: reunión 1 alimenta el PRD, reunión 2 las reglas del Backend Schema.
- `00_Meta/GEMINI.md` es copia del global, no del vault: esta regla no se replica ahí.
- Starter Kits quedó como inventario de candidatos: no se inventó código extraído que no existe.
- Los lints se probaron con datos sintéticos; falta usarlos en un proyecto real. La skill aparece en sesión nueva.
- El gate de archivos nuevos rechaza siempre el primer intento: declarar los hechos antes y reenviar.

