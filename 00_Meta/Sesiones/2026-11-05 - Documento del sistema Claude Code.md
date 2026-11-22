---
title: "Sesión - 2026-11-05 - Documento del sistema Claude Code"
date: 2026-11-05
type: meta/sesion
origen: mixto
proyecto: ""
tags:
  - sesion
aliases: []
---

# Sesión — 2026-11-05: Documento del sistema Claude Code

> [!resumen] En cristiano
> Haytham pidió un solo archivo que explique toda la configuración de Claude Code: reglas, skills (con su enlace a GitHub y cuándo se usa), diseño, hooks, MCPs y plugins. Se escribió en `03_Resources`. Los orígenes que no se pudieron comprobar están marcados «por confirmar», no inventados.

## Contexto
Petición directa de Haytham. Nota resultante: [[Sistema Claude Code - Configuracion Completa]].

## Qué se hizo
- Leídos `CLAUDE.md` global, `rules/`, `reference/`, `known_marketplaces.json`, `settings.json` y hooks.
- Escrita la nota única con 16 secciones (capas, reglas duras, hooks, skills por situación, diseño completo, GTM, plugins→repo, agentes, MCP, herramientas base, routing, proyectos, mantenimiento, seguridad, honestidad de orígenes).
- Enlazada desde `CLAUDE.md` del vault; `GEMINI.md` regenerado con `sync-gemini.py`.

## Auditoría aplicada (2026-11-05)
- Puerta de diseño en 2 fases (Macro `design-taste-frontend` / Micro `impeccable`) en `rules/diseno.md` y routing global; `GEMINI.md` regenerado.
- Skills redundantes de diseño marcadas como archivadas en `reference/skills-diseno-seleccion.md` (ya lo estaban en disco).
- `guard-destructive.py`: bloquea `git push --force`/`-f`; los `deny` de `settings.json` se mantienen.
- Creado `scripts/check-mcps.sh` (solo informa).
- Desviaciones: el hook de impeccable no está instalado ni bloquea (se activa por proyecto); `taste-skill` es `design-taste-frontend`.
- Falso positivo visto: `guard-destructive.py` bloquea comandos Bash que solo mencionan palabras como TRUNCATE en texto; escribir el contenido con Write.

## Decisiones tomadas
- Un único archivo, en `03_Resources` (no en `00_Meta`), para que sea recurso reutilizable.
- Origen de skills no verificable → «por confirmar».

## Aprendizajes (para futuras sesiones)
- Fallos de MCP vistos hoy: `zorin-ssh`, `shadcn-registries`, `roblox-studio` (timeout); muchos MCP de plugin piden autorización.
- Revisión de uso de skills/MCP prevista el 2026-12-04; actualizar la nota entonces.

## Próximos pasos
- Confirmar los orígenes marcados «por confirmar».
- Mantener la nota al día tras cambiar plugins, skills o MCPs.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[Sistema Claude Code - Configuracion Completa]]
