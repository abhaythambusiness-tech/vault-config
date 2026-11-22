---
type: plantilla
status: aprobada
proyecto: Comanda Viva
date: 2026-11-04
origen: mixto
---

# Paleta de componentes — Comanda Viva

> [!resumen] En cristiano
> Antes de maquetar, se elige qué piezas ya hechas de las librerías de componentes usa **esta** app y por qué. Cada pantalla lleva al menos una pieza con personalidad (a veces hecha a mano, cuando ninguna librería encaja). Sin esta nota aprobada no se escribe interfaz. **Hallazgo:** el buscador MCP `shadcn-registries` veía 0 registries (no hay `components.json` en el vault); busqué con la línea de comandos de shadcn, que sí los ve todos.

## 1. Insumo
Idea visual central y dinamismo (de [[3 - UI-UX Design]] §2 y §7): yemas que se apagan al agotarse un plato; pegatinas giradas y bloques pastel por categoría; menú nivel 2, caja y admin nivel 1; **Motion como único motor**.
Adjetivos de marca (PRD §11): fresco, vivo, cercano.

## 2. Registries buscados
- [x] @shadcn  - [x] @magicui  - [x] @aceternity  - [x] @bklit  - [x] @componentry  - [x] @spaceui  - [x] @uiarc  - [x] @skiper-ui  - [ ] 21st (sin clave `API_KEY_21ST`)

Consultas hechas, con CLI `npx shadcn@latest search` (Node 22) sobre los 8 registries: product card 49 · badge sticker 21 · number ticker counter 17 · bottom sheet drawer 31 · kanban board order 37 · marquee 25 · receipt invoice 48 · stat card kpi 93. Dentro de un registry: @shadcn drawer 3, tabs 16, table 18, sonner 3 · @bklit stat card 34, bar chart 49, area chart 53, line chart 37 · @uiarc dashboard 3, settings 27 · @componentry card 6 · @skiper-ui card 4 · @magicui bento 46 · @aceternity counter 36. Búsqueda difusa con mucho ruido: se filtró a mano.

> [!riesgo] Descartados con motivo
> - `@aceternity/speed-counter` (dígitos que corren, encajaba con «quedan N»): **401 Unauthorized**, exige token. No disponible.
> - `@spaceui/demo-c-kanban-06` (tablero con actualización optimista): arrastrar y soltar no hace falta (caja cambia estado con un botón) y trae `@tabler/icons-react`, una segunda librería de iconos.
> - `@magicui/bento-grid`: trae `@radix-ui/react-icons` (segunda librería de iconos) y ya se usa en NeoZeler Web; la rejilla del menú se hace con CSS Grid propio.
> - `@uiarc/login-centered`: está pensado para llaves de acceso (passkey), el login de la dueña es email + contraseña.
> - `@magicui/number-ticker`: válido (`motion`), pero Bklit ya trae `@number-flow/react` para las cifras del panel; no se duplica.

## 3. Elección por sección
Mínimo **un componente distintivo por sección**. Base shadcn (botón, input, tarjeta) no cuenta. «Propio» = hecho a mano con tokens de la marca, porque ningún registry encajaba.

| Sección / pantalla | Componente | Registry | Por qué encaja con la marca | Peso / motor de animación | Alternativa descartada |
|---|---|---|---|---|---|
| C1 Menú | **Hilera de yemas** (propio) + tarjeta de plato pastel con pegatina girada (propio) | — | Es el elemento firma del PRD §11 e identidad §7: una yema se apaga al bajar la disponibilidad | `motion`, solo `transform`/`opacity` | `speed-counter` de @aceternity (401); contador numérico plano |
| C1 Menú (tira superior) | `marquee` | @magicui | Tira «Huevos del día · Café recién molido…» como la cinta del shot 5 | Sin dependencias, CSS puro; pausa con `prefers-reduced-motion` | `logo-marquee` (@uiarc, pensada para logos) |
| C2 Detalle de plato + nota | `drawer` (hoja inferior) | @shadcn | Patrón del shot 2 (detalle con extras y nota); gesto natural en móvil | `vaul` (CSS/JS propio de la librería, sin `motion`) | `demo-p-drawer-07` (@spaceui, hojas anidadas: demasiado) |
| C3 Resumen y enviar | **Ticket dentado + stepper −/+** (propio) | — | Recuerda al ticket de papel; ninguna búsqueda («receipt invoice» 48 resultados) dio nada útil, todo ruido | CSS + `motion` para el total | — |
| C4 Mi mesa | `sonner` (aviso «plato anulado/agotado») + lista propia | @shadcn | Avisos amables sin bloquear | `sonner` | — |
| K1 Comandas en vivo | `tabs` con contador + **tarjeta de comanda tintada por estado** (propio) | @shadcn | Pestañas con contador del shot 7 y tarjetas tintadas del shot 6 | `tabs` Radix; entrada de tarjeta con `motion` | `kanban-06` (@spaceui) por dnd e iconos tabler |
| K2 Cuenta y cobro | `radio-cards` (método: efectivo / tarjeta / otro) | @uiarc | Panel de pago del shot 6; anillo de selección deslizante | `motion` + `arc-motion-tokens` | Botones pill planos de shadcn |
| K3 Mesas | **Rejilla de mesas** (propio) | — | Mesa como ficha: libre / con comanda / por cobrar | CSS | — |
| A1 Panel financiero | `stat-card-area-01` + `bar-chart` + `area-chart` | @bklit | Gráficas MIT sobre `motion` (un solo motor); tarjeta con sparkline y cifra animada | `motion`, `d3-shape`, `@number-flow/react` | **Recharts** (más pesado, otro motor; ver cascada abajo) |
| A2 Inventario | `table` + `sparkline` (consumo 7 días) | @shadcn + @bklit | Mini-gráfica por ingrediente dentro de la fila; avisa de tendencia antes de agotarse | `motion`, `d3-shape` | Tabla sin gráfico |
| A3 Platos y recetas | Lista-detalle shadcn + **vista previa de yemas** (propio) | @shadcn | La dueña ve cuántas raciones salen con su receta | `motion` | — |
| A4 Mesas y QR | **Hoja de impresión de QR** (propio) con `qrcode` | — | QR A6 con marca; no existe en registries | Sin animación | — |
| A5 Acceso / A6 Ajustes | **Sin componente distintivo externo**: `form`, `input`, `switch` (@uiarc opcional) y marca | @shadcn | Pantallas funcionales de baja frecuencia; la seña es el logo y la crema | Solo shadcn base | `login-centered` (@uiarc, passkey) |

## 4. Control anti-parecido
Proyectos recientes comparados (`Registro de Identidades Visuales.md` y [[Catalogo de Componentes]]): NeoZeler Web usa `bento-grid` y `text-reveal`; Neozeler CRM, TopLeads y Scraper Infoproductores son oscuros/ledger. Distintivos repetidos con ellos: **0 de 10** (`bento-grid` descartado a propósito); `@bklit` ya está en el catálogo como «pendiente de probar».
Una sola librería de animación (Motion) y de iconos (lucide): **sí**. Excepción a vigilar: `@number-flow/react` y `vaul` traen su propio movimiento interno; medir peso en el primer build.

## 5. Instalación
Antes: `components.json` en el repo con los 7 registries de @magicui a @skiper-ui (copiado de TopLeads) y Node 22 (`~/.local/share/fnm/node-versions/v22.23.3/installation/bin`). Uno por uno:
```bash
npx shadcn@latest add @shadcn/drawer @shadcn/tabs @shadcn/table @shadcn/sonner
npx shadcn@latest add @magicui/marquee
npx shadcn@latest add @uiarc/radio-cards
npx shadcn@latest add @bklit/stat-card-area-01 @bklit/bar-chart @bklit/area-chart @bklit/sparkline
```
Revisar `shadcn view` de cada ítem antes (dependencias) y medir el peso tras instalar.

> [!riesgo] Cascada sobre el TRD (aprobado)
> El [[2 - TRD]] deja «Recharts o gráficas SVG propias». Esta paleta propone **Bklit** (sobre `motion`, que ya está en el stack) en lugar de Recharts, y añade `@number-flow/react`, `d3-shape`, `vaul` y `radix` al presupuesto de dependencias. **No he tocado el TRD**: necesito tu permiso para actualizarlo.

## Aprobación
`status: aprobada` solo con visto bueno de Haytham.
