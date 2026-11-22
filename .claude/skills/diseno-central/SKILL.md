---
name: diseno-central
description: Skill de referencia (huérfana desde 2026-11-18): NO es el punto de entrada de UI; el routing vigente es Capa 0 con `impeccable init` y luego design-taste-frontend / emil-design-eng / impeccable según `rules/diseno.md`. Usar solo para consultar valores exactos (tipografía, color, espacio, motion, criterios de revisión en reference/revision.md y landing.md) o para exportar DESIGN.md con scripts/export_design_md.py.
---

# diseno-central

Un solo sitio para diseñar UI. Funde lo mejor de impeccable, design-taste-frontend, hallmark, Emil Kowalski, Jakub Krehel, garden (web-design-engineer), landing-page-design, Meng To y tastemaker. Gate y MCP: `~/.claude/rules/diseno.md` e `identidad-y-dinamismo.md`. Web/stack/verificación: `rules/web.md`.

**Por qué funciona (Reto 30):** buen diseño = brief concreto con valores + imágenes reales + **bucle de mirar y corregir** en el navegador. No salió de conceptos abstractos. Aquí manda eso.

## Paso 1: tamaño, modo y diales (una línea)

«Tamaño: X · Modo: Y · Diales v/m/d/a/b». Modo: Operate (app, dashboard) · Read · Persuade (landing) · Experience (portfolio). Diales por defecto en `reference/nucleo.md`.

| Tamaño | Qué es | Fases |
|---|---|---|
| **Retoque** | Cambio pequeño en UI existente (~20 líneas) | 1 (leer identidad), 6 mínima, 7 mínima |
| **Componente** | Pieza nueva en proyecto con identidad | 1, 2, 3 si anima, 6, 7 |
| **Pantalla** | Página o vista nueva / rediseño | 1 a 7 |
| **Proyecto** | Landing, web o app completa | 1 a 7, todas |

Duda entre dos tamaños: el mayor.

## Skills: solo estas

| Necesidad | Usar |
|---|---|
| Qué stack toca · qué librería cubre una necesidad · trampas ya pagadas · puerta de identidad | **MCP `diseno`** (propio): `stack(tipo)`, `elegir(necesidad)`, `catalogo(estado?, papel?)`, `trampas(libreria?)`, `identidad(ruta)`. Primera consulta de toda tarea de UI |
| Todo diseño nuevo | esta skill + `reference/*` (valores exactos) |
| Marketing, landing, portfolio, pantalla de app premium | `design-taste-frontend` (tipo, motion, números de app; **no** su `draw.mjs` si hay identidad) |
| UI existente: crítica, auditoría, pulido, endurecer, adaptar | `impeccable` |
| Paleta/tipografía por dominio (cantera) | `ui-ux-pro-max` |
| Animación accesible | `web-animation-skills:accessible-animation` |
| Gráficas | `dataviz` · SVG: `svg-skill` · diagrama: `diagram-design` |
| Plugins de marca | Figma, Canva, Bloom, shadcn, magicui, 21st: firmas en `rules/diseno.md` §3 |

Más archivo: `reference/herramientas.md`. Lo demás está archivado y consultable en `~/.claude/skills-archivo/`.

## Fases

**1. Identidad (puerta; sin esto no se maqueta)**
Comprobar la puerta con el MCP `diseno`: `identidad(ruta del repo)` dice si falta la identidad o el `DESIGN.md`, y `stack(tipo)` fija base, iconos y piezas antes de instalar nada.
`DESIGN-IDENTITY.md` aprobado (o UI-UX §2/§5/§7). Debe ser **concreta**: paleta con valores, 2 tipografías, escala, radio/elevación elegidos, curva de movimiento, nivel de dinamismo y qué imagen va en cada sitio. Falta identidad o una imagen: parar y preguntar (prompt Gemini, SVG o foto real). Con Figma: `get_design_context`.
Con la identidad aprobada, exportar `DESIGN.md` (formato design.md, lo leen otros agentes) a la raíz del repo: `python3 -I ~/.claude/skills/diseno-central/scripts/export_design_md.py DESIGN-IDENTITY.md DESIGN.md`. Se regenera cada vez que cambie la identidad; no se edita a mano. Si la identidad está sin rellenar, el script se niega.
*Hecho cuando*: identidad citada con sus valores y `DESIGN.md` exportado.

**2. Construir v0 temprano**
Estructura real con datos y copy reales (nunca Lorem) y componentes de la librería del proyecto (`diseno` `elegir(necesidad)` y después `shadcn-ui` `list_components`, antes de escribir a mano). Valores de `reference/nucleo.md`; landing: `reference/landing.md`. Tokens en `:root` (ningún color ni fuente literal fuera). Primera captura en el navegador **antes** de afinar nada.
*Hecho cuando*: v0 visible a 375 y 1280, sin placeholders.

**3. Movimiento**
`reference/movimiento.md`: puerta «¿animar?», tokens, tabla, scroll-storytelling solo en Persuade/Experience. Una curva propia, una librería, solo `transform`/`opacity`, reduced-motion respetado.
`reference/principios-motion-ux.md`: 12 principios de animación traducidos a UI + leyes de UX (Hick, Miller, Doherty, Postel, Jakob, frecuencia de uso) y checklist de revisión.
*Hecho cuando*: tabla aplicada y `audit_motion.py` sin avisos.

**4. Textos**
Botones con la acción real, estados vacío/error/carga escritos, sin buzzwords. Patrones, fórmulas y checklist en `reference/ux-copy.md` (variantes: `design:ux-copy`); `humanizer` fuera de textos legales. Oferta, precio y promesa de la landing vienen de `oferta-central`.
*Hecho cuando*: checklist de `reference/ux-copy.md` marcado.

**5. Imágenes y SVG**
Real o generada con prompt aprobado, con `alt`. Marca: Bloom/Canva. Vectores: `svg-skill`. Sin caras ni logos inventados.

**6. Revisión (bucle, no una vez)**
`reference/revision.md`: capturas 375/768/1280 → scripts (`anti_slop_scan.py`, `check_contrast.py`, `impeccable detect`) → autocrítica 1-5 en 6 ejes (<3 = rehacer) → tabla de hallazgos → corregir → recapturar. **Mínimo 2 rondas.** Vistas con datos: peor caso (break-ui).
*Hecho cuando*: sin H abiertos, ejes ≥3 y las señales de IA revisadas.
Guardar ≥2 capturas (375 y 1280) en `<repo>/.capturas/` (añadir a `.gitignore`): el hook `guard-ui-commit.py` bloquea `git commit` de UI sin ellas de las últimas 12 h (escape `UI_CAPTURAS=off`).

**7. Verificación y entrega**
Tres anchos revisados + 320 sin scroll horizontal; axe a cero violaciones; Lighthouse; build y type-check limpios (`rules/web.md`). Sin navegador: decirlo, no darlo por verificado.
*Hecho cuando*, y se declara con el resultado: tamaño, modo, skills usadas, MCP ejecutados, fases saltadas y por qué, rondas de revisión, resultado de la verificación.

## Choques y escape

- Identidad aprobada > brief > `reference/nucleo.md` > gusto de cualquier skill.
- Plugin desactivado necesario: activar, avisar en una línea y restaurar al terminar.
- Chrome DevTools bloqueado: usar el navegador del panel (`mcp__Claude_Browser__*`).
- Hook `bin/recordar-diseno` bloquea editar UI hasta invocar esta skill. Saltarlo solo si Haytham lo decide: `DISENO_CENTRAL=off`.
