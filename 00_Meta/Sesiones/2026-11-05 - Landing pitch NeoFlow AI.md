---
date: 2026-11-05
proyecto: "[[01_Projects/NeoFlow AI]]"
type: sesion
origen: mixto
---

# 2026-11-05 · Landing pitch NeoFlow AI

> [!resumen] En cristiano
> Se creó una landing de 10 diapositivas para el pitch de NeoFlow AI (Impulsa Startup). El fondo SVG no se veía; la causa era que el `body` tenía fondo propio y lo tapaba. Arreglado y commiteado en `~/Proyectos/neoflow-pitch/`.

## Aprendizajes
- Si `html` tiene fondo, el `body` con fondo pinta como bloque y tapa hijos `fixed` con `z-index:-1`. Fondo solo en `html`.
- `transform` CSS sobre círculos SVG con degradado grande deja un borde duro en Chromium; mover con `cx`/`cy`.
- Capturas a mitad de reveal salen vacías: desactivar transiciones para verificar.
- Hook `guard-ui-commit.py` exige capturas 375 y 1280 en `.capturas/` de las últimas 12 h.
- Repo nuevo sin identidad git: se fijó solo en local.
