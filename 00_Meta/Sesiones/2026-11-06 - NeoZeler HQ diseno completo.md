---
type: sesion
date: 2026-11-06
proyecto: "[[NeoZeler HQ]]"
origen: mixto
---

# 2026-11-06 · NeoZeler HQ: diseño completo

> [!resumen] En cristiano
> Se diseñó entero NeoZeler HQ, la herramienta compartida de Haytham y Sam: los 6 documentos del flujo quedaron aprobados. No hay código aún.

## Qué se hizo
- Vía `saas`; proyecto nuevo que absorbe ComandAi y Neozeler CRM; alojado en Zorin + Tailscale.
- PRD (19 historias), Ficha, TRD, UI-UX (identidad «Mesa de dos»), AppFlow, Backend Schema (30 tablas) y Plan (T-00..T-29) aprobados.
- `trace_lint.py` en OK tras añadir flujos breves a AppFlow y US-19 a UI-UX.
- Repo `~/Proyectos/neozeler-hq/` con `git init`, `.gitignore`, README y `.claude/COMMON_MISTAKES.md`.

## Aprendizajes
- Bun no está en la máquina local: lo que use `bun:sqlite` se prueba en el Zorin.
- `schema_to_migration.py` solo vale para Postgres; con SQLite se escribe la migración a mano.
- El lint exige que cada US aparezca en UI-UX y AppFlow, no solo en el Plan.

## Pendiente
Ver «Puertas abiertas» en [[NeoZeler HQ]]. Falta `resumen.html` (se hace con la Paleta de Componentes en la Fase 0, porque el hook bloquea `.html` sin ella).
