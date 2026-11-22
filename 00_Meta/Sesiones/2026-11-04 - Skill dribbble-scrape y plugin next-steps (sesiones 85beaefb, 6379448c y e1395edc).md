---
title: "Sesión - 2026-11-04 - Skill dribbble-scrape y plugin next-steps"
date: 2026-11-04
type: meta/sesion
origen: mixto
proyecto: ""
sesion_id:
  - 85beaefb-1d21-40c7-99a8-2ca688e23d61
  - 6379448c-2357-4552-b8b4-2a7536a52b97
  - e1395edc-454c-4fb5-b1b0-495863631ef4
tags:
  - sesion
  - skills
  - diseno
aliases: []
---

# Sesión — 2026-11-04: skill de Dribbble y cuadro «next steps»

> [!resumen] En cristiano
> Dribbble no tiene MCP, así que se creó una skill que lo lee con Scrapling. Desde ahora, antes de diseñar una pantalla o un proyecto web, Claude buscará 5-8 referencias de Dribbble y te las enseñará para que elijas. Aparte, Haytham quería que el cuadro de «siguientes pasos» saliera siempre al final de cada turno: se activó el plugin y se guardó la regla en memoria.

Son tres sesiones cortas del mismo día.

## Qué se hizo
- **`85beaefb`**: se comprobó que Dribbble no tiene MCP; se explicó `scrapling-official`; se creó `~/.claude/skills/dribbble-scrape/` (script `scripts/dribbble.py`), se endureció para que no falle, y se añadió la **fase 0b** a `diseno-central`: obligatoria en «Pantalla» y «Proyecto», solo si la pieza es nueva en «Componente», no aplica en «Retoque». Si Dribbble falla se dice y se usa `mobbin` o `hallmark study`. Se escribió la regla en `rules/diseno.md`, el `CLAUDE.md` global y el del vault; `GEMINI.md` regenerado con `sync-gemini.py`.
- **`6379448c` y `e1395edc`**: el «mod de toma de decisiones» no se veía; Haytham aclaró que se refería a `next-steps` (plugin de `anthropics/claude-plugins-community`). Se activó con `true` en `settings.json:239` y se guardó la memoria `feedback-siempre-next-steps` (cerrar cada turno con `wrap_up`, pregunta y botones). `e1395edc` es una bifurcación de `6379448c`.

## Decisiones
- «Drip» se interpretó como Dribbble; se avisó del supuesto.
- Es una regla por instrucciones, no un hook: depende de que Claude lea `diseno-central`.

## Problemas
- El cuadro de `next-steps` solo se dibuja en un terminal normal, no en la app de escritorio; y solo sale si lleva pregunta, así que a veces será una pregunta de relleno.

## Archivos afectados
`~/.claude/skills/dribbble-scrape/`, `~/.claude/skills/diseno-central/SKILL.md`, `~/.claude/rules/diseno.md`, `~/.claude/CLAUDE.md`, `CLAUDE.md` del vault, `~/.claude/settings.json`, memoria `feedback-siempre-next-steps.md`.

## Mejoras propuestas
- Si la fase 0b se salta, añadir un hook que lo detecte (hoy depende de la disciplina).
- Abrir sesión nueva para comprobar que `next-steps` carga.

## Pendientes
- Verificar en el terminal que `next-steps` aparece; sin hacerlo, no está comprobado.

## Relacionado
- [[2026-11-04 - Rediseno del sistema de UI (diseno-central)]]
- [[2026-11-04 - Comanda Viva - construcción T-01 a T-10 (sesiones af0e72a1, 984e75fa y f0a02e92)]] (primer uso real de la fase 0b)
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
