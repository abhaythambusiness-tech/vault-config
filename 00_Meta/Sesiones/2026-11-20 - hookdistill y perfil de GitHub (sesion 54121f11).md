---
title: hookdistill y perfil de GitHub
date: '2026-11-20'
type: meta/sesion
origen: maquina
proyecto: ''
sesion_id: 54121f11-b372-4f60-a263-e68f5c7317bd
tags:
- sesion
- github
- hooks
- go
---

> [!resumen] En cristiano
> Haytham quería un repo de GitHub que consiga estrellas. Se recogieron quejas de usuarios de Claude Code y se eligió una: reglas de CLAUDE.md que se incumplen.
> Se construyó `hookdistill` (Go, MIT): lee tus sesiones guardadas, detecta reglas ignoradas y las convierte en hooks (avisos que bloquean). Quedó con 17 commits y 66 tests, sin publicar.
> También se hizo una tarjeta de perfil de GitHub con tu cara en ASCII y se reescribió la autoría de los commits.

## Qué se hizo
- **`foros-claude-code`** (`~/Proyectos/foros-claude-code/`, Go): recoge quejas de GitHub Issues, Hacker News y Stack Overflow; 437 posts en `quejas.jsonl`. Reddit está en el código (OAuth) pero sin probar: faltan claves.
- **Idea elegida**: se cruzaron las quejas con lo ya construido. Había competencia (hookify, PRISM, claudecode-rule2hook); el hueco es leer el historial real y proponer hooks solo con evidencia.
- **Nombre**: `hookwise` ya existía (framework Go, npm) → renombrado a **`hookdistill`**, libre en GitHub, npm y PyPI.
- **`~/Proyectos/hookdistill`**: diseño y plan de 14 tareas (TDD) en `docs/superpowers/`; comandos `scan`, `propose`, `replay`, `promote`, `install`, `uninstall`, `run`; CI, goreleaser, instalador con checksum, README, plantillas, imagen social y borrador de Show HN.
- **`~/Proyectos/perfil-github`**: tarjeta `card.svg` (nombre en 3D, cara ASCII desde un retrato local, ciudad isométrica con 468 commits en 42 días) y README; primer commit `ac574ec`.
- **Autoría**: los 17 commits se reescribieron a `abhaythambusiness-tech`; `master` apunta a `831b928`/`77129e4`. Se conservan las ramas `old-master-haytham` y `backup-before-author-rewrite`.

## Decisiones
- `promote`: una regla solo pasa a bloquear si el replay no bloqueó nada legítimo.
- Nada se empuja a GitHub sin orden expresa; identidad git local por repo.

## Problemas
- El hook `guard-destructive` bloqueó un `rm -rf` de limpieza y cadenas en Bash; se usó `Write`.
- Reddit sin claves: sin probar.

## Pendientes / próximos pasos
- Publicar `hookdistill` (crear remoto, push, lanzamiento); no se puede prometer respuesta en menos de un día ni cero errores.
- Decidir si el `.gitignore` de `perfil-github` entra en un segundo commit y si se quita el `Co-Authored-By`.
- Sin ficha en `01_Projects/` ni `resumen.html` (regla §0.8): pendiente.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

