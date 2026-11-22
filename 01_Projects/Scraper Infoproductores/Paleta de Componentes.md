---
type: plantilla
status: aprobada
proyecto: Scraper Infoproductores
date: 2026-11-01
origen: mixto
---

# Paleta de componentes — Scraper Infoproductores

> [!resumen] En cristiano
> Antes de maquetar, se elige qué piezas de las librerías de componentes usa **esta** web y por qué. Aquí la marca es un «libro mayor» sobrio, así que casi todo es shadcn limpio y las piezas distintivas son gráficas pequeñas y datos vivos (de Bklit), no efectos vistosos. El movimiento se hace con CSS. Sin esta nota aprobada no se escribe interfaz.

## 1. Insumo
Idea visual central y dinamismo (UI-UX §2 y §7): libro mayor que responde al instante; nivel 1, solo CSS, saldo con «tic».
Adjetivos de marca (PRD §11): preciso, rápido, fiable. Anti: guru chillón.

## 2. Registries buscados
El buscador MCP `shadcn-registries` no tiene registries configurados aquí (devolvió lista vacía, la trampa conocida) y el repo aún no tiene `components.json`. Se buscó con la CLI (`npx shadcn@latest search @ns -q ...`, Node 22), que resuelve los espacios de nombres sin configurar.
- [x] @shadcn  - [x] @magicui  - [ ] @aceternity (la CLI falla: `self-signed certificate`; no se usa)  - [x] @bklit  - [x] @componentry  - [x] @spaceui  - [x] @uiarc  - [x] @skiper-ui  - [ ] 21st (sin clave)  - [ ] otros

Consultas (palabra → registry → resultados): table → magicui 29 (sin tabla útil), bklit 19; number ticker → magicui 4; animated list → magicui 49; blur → magicui 23; sparkline → bklit 8; line chart → bklit 37; timeline → bklit 7; number/table → componentry 0; metric/table → uiarc 0 en la CLI; input → spaceui 0; search → skiper-ui 0; data table → shadcn 5; command → shadcn 3; pricing → shadcn 0.

## 3. Elección por sección
Base shadcn (botón, input, tarjeta, tabla, formulario) no cuenta como distintivo.

| Sección / pantalla | Componente | Registry | Por qué encaja con la marca | Peso / motor de animación | Alternativa descartada |
|---|---|---|---|---|---|
| Landing: buscador en vivo | `sparkline` (curva diminuta de lanzamientos en cada ficha de ejemplo) + `command` base para la caja de búsqueda | @bklit + @shadcn | Dato real como imagen: cada resultado trae su curva, precisión de libro mayor | Por medir al instalar; sin motor extra si Bklit lo permite | `animated-list` de Magic UI: es un efecto de escaparate con motor `motion`, choca con «solo CSS» |
| Registro / entrada | Formulario shadcn base (excepción: pantalla de un paso, nada distintivo que aporte) | @shadcn | Sobriedad: menos elementos, mejor ejecutados | Ninguno | `shimmering-text` de Bklit: decorativo |
| Búsqueda y resultados | Tabla shadcn (`data-table`) + `sparkline` en columna «lanzamientos» | @shadcn + @bklit | Densa y alineable con cifras mono; la curva da lectura rápida | Ninguno / por medir | `dashboard-01` de shadcn: trae barra lateral y demasiado paquete |
| Ficha de infoproductor | `composed-chart` (lanzamientos y anuncios en una línea de tiempo) | @bklit | Es el «historial» de la persona, mismo lenguaje de libro mayor | Por medir | `line-chart` simple: no mezcla series |
| Mis contactos | Tabla shadcn + exportación | @shadcn | Una lista de trabajo no necesita adorno | Ninguno | — |
| Planes y créditos | `stat-card-line-01` (saldo en el tiempo) + tarjetas de plan shadcn | @bklit + @shadcn | El saldo como libro de movimientos visible | Por medir | `number-ticker` de Magic UI: motor `motion` para un efecto que se hace con CSS |
| Baja de ficha (pública) | Formulario shadcn base | @shadcn | Claridad legal ante todo | Ninguno | — |
| Admin: fuentes y bajas | `heatmap-chart` (actividad de recogida por fuente y día) + `sparkline` | @bklit | Salud de las fuentes de un vistazo | Por medir | Tablas planas sin señal visual |

## 4. Control anti-parecido
Proyectos recientes comparados: Cauce y el CRM usan gráficas y KPI; este usa Bklit solo en pequeño (sparkline/heatmap), con identidad clara y mono. Componentes distintivos repetidos con otros proyectos: `sparkline`/`stat-card` de Bklit (probado en reto-30 según el Catálogo). Máx. 1 de cada 3: **se cumple de forma justa**; la diferencia la pone la composición y la tipografía, no el componente.
Una sola librería de animación y de iconos: **sí, ninguna de animación** (CSS) y una de iconos (a fijar al instalar, `lucide`). Si Bklit exige `motion`/`d3`, se declara en el TRD §1.2 antes de instalar.

## 5. Instalación
Con Node 22 y uno por uno, tras crear el repo desde `starter-saas` y su `components.json` con `@bklit`:
`npx shadcn@latest add @bklit/sparkline` · `@bklit/composed-chart` · `@bklit/stat-card-line-01` · `@bklit/heatmap-chart` · `@shadcn/command` · `@shadcn/table`. Medir el JS inicial tras cada uno (presupuesto ≤ 150 kB gzip) y anotar trampas en `librerias.md` y el Catálogo.

## Aprobación
`status: aprobada` solo con visto bueno de Haytham.
