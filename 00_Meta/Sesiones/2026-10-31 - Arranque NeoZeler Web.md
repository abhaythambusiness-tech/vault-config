---
type: meta/sesion
date: 2026-10-31
proyecto: "[[01_Projects/NeoZeler Web]]"
tags:
  - sesion
origen: mixto
---

# Sesión 2026-10-31: arranque de NeoZeler Web

> [!resumen] En cristiano
> Se montó la web de NeoZeler hasta tener todos los documentos aprobados y el plan de obra. No se escribió código.

## Qué se hizo
Vía web-cliente; PRD, Ficha, UI-UX con identidad C, Paleta y Plan aprobados; `trace_lint` OK; repo `~/Proyectos/neozeler-web` con `.proyecto` y primer commit.

## Aprendizajes
- `trace_lint.py` exige AppFlow con todas las historias aunque esté `no-aplica`: se añadió una tabla historia → ruta.
- El MCP `shadcn-registries` lee el `components.json` del directorio de arranque (el vault no tiene): usar `npx shadcn@latest search` con Node 22 y quoting bash (en zsh `$R` no se parte en palabras).
- Sin librería de animación se descartan las piezas con `motion`; queda poco catálogo útil.
