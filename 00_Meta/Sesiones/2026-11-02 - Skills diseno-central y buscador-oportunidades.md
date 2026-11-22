---
title: "Sesión - 2026-11-02 - Skills diseno-central y buscador-oportunidades"
date: 2026-11-02
type: meta/sesion
proyecto: ""
sesion_id: f852ec34-b0fc-4c51-9e73-138ff83c9740
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-11-02: Skills diseno-central y buscador-oportunidades

> [!resumen] En cristiano
> Haytham quería usar todas sus skills de diseño en cada proyecto sin invocarlas una a una. Se creó una skill central de diseño (con un candado que impide editar interfaces sin pasar por ella) y otra para cazar ideas y problemas de negocio.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `f852ec34`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Skill `diseno-central`: mide primero el tamaño del trabajo (retoque, componente, pantalla, proyecto); cada fase tiene «hecho cuando» (p. ej. verificar 375/768/1280 px, axe a cero, Lighthouse).
- Hook `recordar-diseno.py`: bloquea editar `.tsx/.css/.html` hasta invocar la skill; deja pasar subagentes, `.obsidian/` y `.claude/`. Probado con 8 casos.
- Skill `buscador-oportunidades` (cazar problemas, ideas desde cero, funciones nuevas, marketing) y `03_Resources/Registro de Oportunidades.md`.
- Aplicados 7 puntos de mejora; reglas replicadas en CLAUDE.md global, `rules/diseno.md` y los dos GEMINI.md.

## Decisiones tomadas
- Una skill orquestadora única para diseño en vez de muchas invocaciones sueltas.

## Archivos y proyectos afectados
- `~/.claude/skills/diseno-central/SKILL.md`
- `~/.claude/hooks/recordar-diseno.py`
- `~/.claude/skills/buscador-oportunidades/SKILL.md`

## Problemas
- Ninguna de las dos skills se ha probado con un caso real.

## Mejoras propuestas
- Probarlas con un proyecto real y ajustar.

## Pendientes y próximos pasos
- Ninguno registrado.

## Relacionado
- [[2026-11-02 - NeoZeler Web, marketing con IA, modulo de venta y embudo hairline]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
