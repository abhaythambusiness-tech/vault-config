---
title: Skills de mattpocock y apple-design-skill
date: '2026-11-21'
type: sesion
origen: maquina
proyecto: ''
sesion_id: 20fbb680-6b88-48b8-978a-103e6313eaeb
tags:
- sesion
- skills
- claude-code
---

> [!resumen] En cristiano
> Haytham pidió revisar dos repos de skills de GitHub. De `mattpocock/skills` se instalaron 7 skills (las 5 pedidas más 2 de apoyo) y se anotaron en la configuración. `apple-design-skill` se revisó y se descartó por encajar poco con su stack web. Hay que abrir una sesión nueva para que aparezcan.

## Qué se hizo
- Revisión de `mattpocock/skills` (MIT, ~30 skills pequeñas combinables).
- Instaladas en `~/.claude/skills/`: `grill-with-docs`, `handoff`, `wait-what`, `improve-codebase-architecture`, `codebase-design` y, como dependencias, `grilling` y `domain-modeling`. Sin pisar nada.
- Añadidas a `03_Resources/Sistema Claude Code - Configuracion Completa.md` (§5.10) y a `skills-seleccion-global.md`; contador de skills activas 149 → 156 también en el `CLAUDE.md` global.
- Revisión de `dickwu/apple-design-skill` (HIG de Apple, sin licencia declarada): encaja poco con el stack obligatorio web; no se instaló.

## Decisiones
- Solo las skills pedidas más sus dependencias; el resto de la colección no se instala.

## Pendientes
- Abrir sesión nueva para usarlas (`/grill-with-docs`, `/handoff`, `/wait-what`).
- «34 skills propias activas» sigue sin recontar (cifra de 2026-11-05).

## Relacionado
- [[03_Resources/Sistema Claude Code - Configuracion Completa]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

