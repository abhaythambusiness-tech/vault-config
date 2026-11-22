---
date: 2026-11-06
proyecto: "[[01_Projects/Vault OS]]"
origen: mixto
---

> [!resumen] En cristiano
> Se decidió construir Vault OS (sustituye a Dashboard Command AI y a Obsidian). Se archivó el dashboard, se movieron los modelos 3D, se aprobaron PRD y Plan, se eligió el estilo de ventana «Cristal» y se creó el repo.

## Hecho
- Dashboard Command AI archivado (ficha en `04_Archive/`, repo borrado, copia en `~/Proyectos/archive/dashboard-command-ai-20261106.tar.gz`).
- 15 archivos `.glb/.obj/.mtl` movidos a `99_Assets/3d/`.
- PRD y Plan en `01_Projects/Vault OS/`, aprobados.
- Repo `~/Proyectos/vault-os/` (git, `.proyecto`, workspaces, build limpio).

## Aprendizajes
- Hay que escribir en `apps/web` con `cd` y `.`: `npm create vite@5 apps/web` pregunta el nombre y se cuelga sin terminal.
- La presencia no puede salir solo del disco (no dice quién tiene un archivo abierto): evento de la UI + escritura detectada.
- Borrar el tar del dashboard solo cuando vault-os tenga la escena portada.
