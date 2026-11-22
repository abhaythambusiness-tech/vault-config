---
title: 'Harness: principios de movimiento y migración de hooks a Go'
date: '2026-11-12'
type: meta/sesion
origen: mixto
proyecto: ''
sesion_id: 2070ddd3-f951-4aa4-907d-8f2b8969da19
tags:
- sesion
- cierre-nocturno
---

> [!resumen] En cristiano
> Se añadieron a la skill de diseño los principios de animación y las leyes de UX. Luego se aplicaron ideas de un repo de «harness engineering» y se fijó una regla nueva: todo script nuevo va en Go. Los hooks y scripts existentes de `~/.claude` se migraron a binarios Go con tests.

## Qué se hizo
- `~/.claude/skills/diseno-central/reference/principios-motion-ux.md`: 12 principios de Disney y leyes de UX (Hick, Miller, Doherty, Postel, Jakob, Fitts) con checklist.
- Del repo awesome-harness-engineering: `rules/harness.md`, `run-silent`, `guard-secretos` (antes de `git push`).
- Regla «scripts siempre en Go» en memoria y `CLAUDE.md` §3 (`GEMINI.md` sincronizado).
- Migrados a Go, código en `~/.claude/tools-go/` (módulo `claude-tools`), binarios en `~/.claude/bin/`: run-silent, guard-secretos, guard-destructive, guard-read-grande, guard-web, guard-proyecto, guard-ui-commit, format-web, recordar-diseno, log-skill, log-mcp, informe-uso-skills, sync-gemini, check-mcps. 42 tests en 14 paquetes; comparados caso a caso con los Python originales (mismo resultado).
- Quitados de `settings.json` los 5 hooks de `vault-os/presencia.mjs`.
- `Sistema Claude Code - Configuracion Completa.md` actualizada a los binarios Go (incluidas líneas 32 y 372).

## Decisiones tomadas
- Los scripts viejos no se reescriben sin petición; los originales quedan en `~/.claude/_backups/*.bak`.
- Webs siguen en TypeScript.

## Aprendizajes
- El test del port a Go halló un fallo del Python: `git -C ruta push` no se reconocía.
- Los hooks nuevos se aplican al abrir sesión nueva.

## Pendientes y próximos pasos
- Alguna referencia a scripts Python no migrados (panel.py, index_vault.py, scripts de diseno-central) sigue vigente.
- Nada commiteado.

## Relacionado
- [[03_Resources/Sistema Claude Code - Configuracion Completa]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

