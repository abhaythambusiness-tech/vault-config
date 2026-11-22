---
type: doc-software
doc: paleta-componentes
proyecto: ARM
status: aprobada
date: '2026-11-17'
origen: mixto
---

# Paleta de componentes — ARM

> [!resumen] En cristiano
> Qué piezas de librería usa ARM y cuáles hay que hacer a medida. Base shadcn para lo común; **dos piezas propias** (margen de firmas y sello de agente) que son lo que hace a ARM distinto; el resto, componentes ya hechos para el tablero y el historial. Sin aprobar no se escribe interfaz.

## 1. Insumo
Idea visual central ([[3 - UI-UX Design]] §2): libro de registro con la firma de cada agente en el margen. Dinamismo 1 (Motion, sello que se imprime). Adjetivos (PRD §11): cálido, técnico, premium.

## 2. Registries buscados
- [x] @shadcn (MCP `shadcn-ui`: 61 componentes listados)
- [x] 21st (MCP; 2 búsquedas)
- [ ] @magicui: **MCP no conectó en esta sesión** (`CONNECTION_CLOSED`); pendiente de consultar antes de instalar
- [ ] @aceternity, @bklit, @componentry, @spaceui, @uiarc, @skiper-ui: no buscados (`shadcn-registries` dio `CONNECT_TIMEOUT`); en una app Operate no hacen falta efectos de marketing

Consultas (palabra → registry → resultados): «activity timeline feed with author signature and timestamp» → 21st → 4; «kanban board drag and drop pipeline columns» → 21st → 4; lista completa → shadcn → 61.

## 3. Elección por sección
| Sección / pantalla | Componente | Registry | Por qué encaja con la marca | Peso / motor | Alternativa descartada |
|---|---|---|---|---|---|
| Ficha > Historial (margen de firmas) | **Propio** `FirmaMargen` sobre `item` + `separator` de shadcn; ritmo de filetes como «Timeline» de 21st (kuratlielia) como referencia de inserción animada | shadcn + propio | Es la idea central; ningún feed genérico pone hora y sello en mono a la izquierda | Motion (ya en stack), solo opacity/transform | «Activity Timeline» (olewandowski1): rail con avatares, parece Linear/Git |
| Sello de agente | **Propio** `SelloAgente` sobre `badge` + IBM Plex Mono | shadcn + propio | Sello tipográfico con iniciales en latón; distingue persona, agente, sistema | CSS + Motion (impresión una vez) | Avatar con foto: sin caras inventadas |
| Pipeline | Kanban de diceui | 21st (`diceui/kanban`) | Teclado + overlay de arrastre; encaja con `@dnd-kit` ya decidido | dnd-kit (comprobar versión: `@dnd-kit/core` sin publicar desde 2024-12) | Kanban de arunjdass (HTML5 drag): sin teclado ni táctil |
| Lista de leads | `table` + tanstack-table | shadcn | Densidad modo Operate | — | — |
| Inicio: KPI | Cifra serif con número animado | magicui (a confirmar cuando conecte) o Motion `animate` propio | Cifras grandes en serif | Motion | Contador de librería externa: segundo motor |
| Conexiones | `field` + `input-group` + `kbd`; campo de copia propio | shadcn | Guía paso a paso sin asustar | — | — |
| Estados vacíos | `empty` + SVG propio (libro abierto) | shadcn + propio | Sin stock | — | Ilustración generada |
| Marco (menú) | `sidebar` | shadcn | Navegación estándar, acento azul acero | — | `navigation-menu`: pensado para webs |

## 4. Control anti-parecido
Comparado con [[Registro de Identidades Visuales]]: ningún proyecto previo usa margen de firmas ni kanban con sello de agente. Distintivos repetidos: 1 de 8 (kanban, común en CRM). Una sola librería de animación (Motion) y de iconos (Lucide): sí.

## 5. Instalación
Node 22, de uno en uno, tras `components.json` con registries: `npx shadcn@latest add item badge separator empty sidebar table field input-group kbd`; kanban: `npx shadcn@latest add "https://21st.dev/r/diceui/kanban?api_key=$API_KEY_21ST"` (clave solo en variable de entorno).

## Aprobación
`status: aprobada` solo con visto bueno de Haytham.

