---
title: MCP de diseño propio
date: '2026-11-16'
type: sesion
proyecto: '[[MCP Diseno]]'
origen: mixto
tags:
- sesion
- diseno
- mcp
---

> [!resumen] En cristiano
> Se analizó skalaia.es para saber qué librerías usa (gustó mucho el efecto visual) y resultó ser código propio sobre WebGL, no una librería.
> Se apuntaron esas librerías y siete fuentes nuevas de componentes en el catálogo largo.
> Con todo eso se construyó un MCP propio de diseño en Go: pregunta qué stack toca, qué librería cubre una necesidad y qué trampas ya se pagaron.
> Las reglas de diseño y la skill `diseno-central` ahora lo invocan como primera consulta de toda tarea de interfaz.

## Qué se hizo

1. **REA sobre skalaia.es.** Las herramientas web de REA necesitan un endpoint CDP vivo y no sirven para una URL remota; se analizó con `curl` + `grep` sobre los bundles.
2. **Apunte en `~/.claude/reference/librerias.md`** (aditivo, fecha 2026-11-16): sección nueva de skalaia.es y cuatro filas nuevas de librerías (DaisyUI + Blueprint, HeroUI, KokonutUI, Skiper UI) más la fila de Vengeance UI reescrita.
3. **MCP `diseno`** creado en `~/Proyectos/mcp-diseno/`: Go 1.22, sin dependencias, catálogo JSON embebido, cinco herramientas, autotest propio de 11 comprobaciones.
4. **Reglas y skill sincronizadas**: `~/.claude/rules/diseno.md`, `skills/diseno-central/SKILL.md` y su `reference/herramientas.md`.
5. **Documentación**: `README.md`, `resumen.html`, ficha [[MCP Diseno]] y esta sesión.

## Qué usa skalaia.es

- Next.js (App Router) con Turbopack y React; archivos desde `/_next/static/immutable/`.
- Fuente Inter en 400, 500 y 600, cargada con `next/font`.
- `lucide-react` para iconos.
- Motor WebGL2 propio con shaders en `/fx/skala-fx.js` (~98 KB), dirigido por atributos `data-fx*`. Hay firmas compatibles con OGL, pero no confirmadas.

## Aprendizajes

- **Lo que gusta de una web no siempre es una librería.** Aquí el efecto es código propio; copiar la librería no habría dado el resultado. Separar «librería» de «código a medida» antes de apuntar nada.
- **El conocimiento de diseño estaba repartido en tres archivos largos** (`rules/diseno.md`, `reference/librerias.md`, la skill). Había que leerlos enteros para contestar «¿qué uso para una tabla de 5.000 filas?». Un MCP de decisión lo convierte en una pregunta.
- **Decisión frente a ejecución.** El MCP nuevo no instala ni genera: decide. Instalar sigue siendo de `shadcn-ui`, `magicui`, `boardui` y `21st`. Mezclar las dos capas habría duplicado trabajo ya hecho.
- **Catálogo en JSON embebido, no en Go.** Añadir una librería es editar un JSON y recompilar; no hay que tocar código.
- **El panel del navegador no puede manejar un archivo local**: `resize_window` falla con «This tab shows a local file, not a web page». Para capturas de un HTML suelto, Chromium en modo headless (`/home/haytham/.local/bin/chromium`).
- **daisyUI Blueprint es de pago y sus claves son secretos** (`LICENSE`, `EMAIL`, `FIGMA`): nunca a un repo; si se usan, van a `~/.claude/reference/` con `chmod 600`.

## Enlaces

- Proyecto: [[MCP Diseno]]
- Repo: `~/Proyectos/mcp-diseno/`
- Reglas: `~/.claude/rules/diseno.md` · Catálogo largo: `~/.claude/reference/librerias.md`

