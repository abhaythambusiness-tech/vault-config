---
title: Auditoría del harness, cortacircuitos y hooks en Go
date: '2026-11-12'
type: meta/sesion
origen: mixto
proyecto: ''
sesion_id:
- 9e075734-f7e9-4e73-9789-323eeea5241a
- 4d6daee6-9656-4625-9ac7-3e580321123a
- 9e1cbaea-806a-49d2-b861-66a61bdf9955
- 6ba75720-946d-4abd-a0fc-f9798aba83b3
tags:
- sesion
- cierre-nocturno
---

> [!resumen] En cristiano
> Se comprobó que los hooks en Go cargan, se auditó el harness (10 puntos débiles) y se aplicaron los arreglos 1 al 10: el `rm` ya no se aprueba solo, las tareas nocturnas tienen tope y hay un aviso al cerrar sin tests. Además la revisión nocturna ahora audita el harness y propone apuestas atrevidas, y se creó un script para ordenar Descargas.

## Qué se hizo
- `9e075734`: los 14 binarios son ELF de Go y los hooks salen con exit 0. `guard-destructive` solo cubría terraform, DROP, TRUNCATE y push forzado; las pruebas fallidas eran del test. Se borró la línea falsa de `uso-mcp.jsonl`.
- Informe [[00_Meta/Informes/Auditoria del harness 2026-11-13]]. Arreglo #1: quitado `Bash(rm *)` de `vault/.claude/settings.local.json`; `guard-destructive` bloquea `rm -r` fuera de /tmp, `git reset --hard`, `git clean -f`, `git checkout .` y `git restore .` con cambios sin guardar.
- Puntos 2-10: sección «Cortacircuitos» en las dos tareas nocturnas, hook `Stop` `verificar-cierre`, `guard-secretos` también en Edit/Write, `check-hooks` (17 casos OK), rotación de logs (`logs-archivo/`), `cleanupPeriodDays: 180`, 184 `skillOverrides` (181 `plugin:skill`). 48 tests en 16 paquetes pasan (`~/.claude/tools-go`).
- `9e1cbaea`: la revisión nocturna incluye Fase 1B (auditoría de harness) y Fase 2B (3-5 apuestas atrevidas por noche, solo propuestas) en `scheduled-tasks/revision-nocturna-vault-mejoras/SKILL.md`.
- `6ba75720`: script `~/Proyectos/ordenar-descargas/` (Go, tests; clasifica `Tipo/AAAA-MM/`, simulacro por defecto, nunca sobrescribe); Haytham dijo «Sí, aplicar».
- `4d6daee6`: verificación de las claves `plugin:skill` y localización de los tests.

## Decisiones tomadas
- «No, ya reviso yo» tras los puntos 2-10: Haytham revisa los cambios.

## Pendientes y próximos pasos
- En sesión nueva: confirmar que las skills en `name-only` salen sin descripción y que `verificar-cierre` y `guard-secretos` actúan.
- Ver si se cumplen los cortacircuitos la primera noche.
- La revisión de Fase 1B/2B se estrena sin haberse probado.
- `run-silent` sin tests. Nada commiteado.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

