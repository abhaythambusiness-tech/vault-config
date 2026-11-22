# Herramientas de diseño (comandos que funcionan en este equipo)

MCP `diseno` (propio, Go, 2026-11-16; capa de decisión, no instala nada): `stack(tipo)` con `web-cliente | landing | dashboard | micro-saas | saas | maqueta-estatica`; `elegir(necesidad)` en lenguaje normal; `catalogo(estado?, papel?)`; `trampas(libreria?)`; `identidad(ruta)`. Código y catálogo editable en `~/Proyectos/mcp-diseno/` (`datos/catalogo.json`; tras editarlo, `cd ~/Proyectos/mcp-diseno && go build -o mcp-diseno . && ./mcp-diseno --autotest`). Fuera de Claude Code: `./mcp-diseno` habla JSON-RPC por stdin.

Scripts propios (solo librería estándar; ejecutar con `python3 -I`): `S=~/.claude/skills/diseno-central/scripts`
- `python3 -I $S/anti_slop_scan.py <rutas>`: gradiente índigo/cian, gradient-text, `100vh`, `href="#"`, img sin alt, `transition:all`, em dash, placeholders, palabras de IA.
- `python3 -I $S/check_contrast.py "#fff" "#777"` o `--matrix text=.. bg=..`.
- `python3 -I $S/generate_palette.py --mood premium|warm|technical|playful|elegant --mode dark --seed N`.
- `python3 -I $S/extract_palette.py captura.png`: paleta real de una referencia (Pillow); sirve para "copiar el estilo" sin describir el "vibe".
- `python3 -I $S/audit_motion.py <rutas>`: curvas, `transition:all`, reduced-motion (sin probar a fondo).

Impeccable (existente, revisión y pulido): invocar la skill `impeccable` (`critique`, `audit`, `polish`, `harden`, `adapt`). Detector mecánico: `~/.impeccable/bin/0.1.18/impeccable detect --json --scope type|layout <ficheros>`. Leer su `reference/craft-floor.md` antes de editar.

Taste (marketing y pantallas de app premium): skill `design-taste-frontend`. Funciona aquí `node scripts/lint.mjs <src>`; `inspect.mjs` y `scenes` piden Node 22 + Chrome (no disponibles). Su `draw.mjs` (sorteo de dirección) **no se usa** si hay identidad aprobada.

Cantera de estilos: `python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<q>" --domain style|color|chart|landing|product|ux|typography|icons|react|web|google-fonts [--stack nextjs|shadcn] -n 3`. Devuelve hex y "SaaS oscuro": es cantera, no veredicto.

Referencias: `PY=~/.local/share/scrapling-venv/bin/python; S=~/.claude/skills/dribbble-scrape/scripts/dribbble.py; $PY -I $S search "<estilo sector>" --limit 12` y `... shot <url>`.

Reglas de interfaz de Vercel: copia local `03_Resources/web-interface-guidelines.md` (la skill `web-design-guidelines` hace WebFetch; si falla la red, usar la copia).

Archivadas (consultables, no cargan): `~/.claude/skills-archivo/` y `skills-archivo/optimizacion-20261104/` (emil-design-eng, animate, web-design-engineer, landing-page-design, tastemaker, better-*, hallmark, ...). Catálogo de estructuras y temas: `skills-archivo/hallmark/` (macrostructures, themes, genres, components).
