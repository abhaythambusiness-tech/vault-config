---
type: sesion
date: 2026-11-04
proyecto: sistema de reglas de diseño
origen: mixto
tags:
  - diseno
  - reglas
  - skills
---

> [!resumen] En cristiano
> Las UI nuevas salían flojas porque había demasiadas reglas y skills que se pisaban, y poco «mirar y corregir». Se dejó **una sola skill de diseño** (`diseno-central`) con lo mejor de impeccable, Taste, hallmark, las del vídeo de AI LABS (Emil Kowalski, garden, landing-page-design, Meng To, Jakub Krehel, tastemaker, designer-skills). Las reglas pasan de 7 a 3 archivos. El arranque de cada conversación pesa la mitad.

## Qué cambió
- `~/.claude/skills/diseno-central/`: SKILL.md con fases y bucle de revisión (mínimo 2 rondas con capturas a 375/768/1280); `reference/` con `nucleo.md` (valores exactos), `movimiento.md`, `revision.md`, `landing.md`, `herramientas.md`; `scripts/` (anti_slop_scan, check_contrast, generate_palette, extract_palette, audit_motion).
- Reglas: `diseno.md` (puerta + firmas MCP), `identidad-y-dinamismo.md` (intacta), `web.md` (stack + verificación + dashboards). `skills-diseno-seleccion.md` pasó a `~/.claude/reference/`.
- Skills de diseño activas: `diseno-central`, `impeccable`, `design-taste-frontend`, `dribbble-scrape`, `ui-ux-pro-max`, `web-design-guidelines`. `hallmark`, `responsive-design` y las del vídeo están en `~/.claude/skills-archivo/`.
- Copia previa: `~/.claude/_backups/ui-20261104/`.

## Decisiones
- Identidad aprobada > brief > núcleo > gusto de cualquier skill.

## Pendiente
- Hook que bloquee commits de UI sin capturas recientes (propuesto, no hecho).
- Probar el sistema en el próximo proyecto web y ajustar `nucleo.md`.
