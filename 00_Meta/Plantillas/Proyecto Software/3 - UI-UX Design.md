---
type: doc-software
doc: ui-ux
proyecto: "<% tp.file.folder() %>"
status: borrador
date: <% tp.date.now("YYYY-MM-DD") %>
origen: humano
---

# 3 · UI/UX Design

> [!resumen]
> Cómo se ve y se siente. Pasa antes por el gate de `rules/diseno.md` (identidad, anti-genérico, contraste, confianza). Cada pantalla traza a una historia del [[1 - PRD]].

## 1. Principios de experiencia
-

## 2. Identidad visual
> [!resumen] Este apartado es la identidad del proyecto
> Aquí se rellena lo que pide `~/.claude/rules/identidad-y-dinamismo.md` (plantilla suelta: [[Plantilla - Identidad de Proyecto]]). **Sin esta sección aprobada no se maqueta.** Al crear el repo se copia entera (§2, §5, §7) a `DESIGN-IDENTITY.md` en su raíz. Antes de decidir, mirar [[Registro de Identidades Visuales]] y no repetir combinación.

- **Idea visual central** («esta marca es ___ y lo demuestra ___»):
- **El producto como diseño** (qué del negocio se enseña en vivo en vez de ilustrarlo con stock):
- **Composición firma** (rejilla rota, escala dramática, recortes, capas…):
- **Anti-referencias** (lo que NO debe parecer) y **2 referencias reales** con qué se toma de cada una (no píxeles):

| Elemento | Valor |
|---|---|
| Paleta (escala de 8 tonos por color clave, neutros con temperatura) |  |
| Tipografías (y **motivo** del par; Inter/Geist/Space Grotesk solo con razón escrita) |  |
| Radio / sombras / espaciado |  |
| Tono y voz |  |
| Referencias (Mobbin / Figma / Canva) |  |

### 2.1 Tokens primero
Orden obligatorio: marca (Bloom o la existente) → variables CSS (`:root` + oscuro) → componentes → pantallas. No se maqueta ninguna pantalla sin tokens definidos.
```css
:root { --brand: ; --surface: ; --text: ; --radius: ; }
```

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base (ver [[Biblioteca de Layouts]]) | Estados a diseñar |
|---|---|---|---|---|
|  |  | US-01 | dashboard / lista-detalle / asistente / parte | vacío · cargando · error · éxito |

### 3.1 Top tasks y escenarios → pantallas
Las pantallas y su jerarquía salen de las **top tasks** y los **escenarios** del [[1 - PRD]] §2.1-2.3: lo que más usuarios eligieron va más prominente. Una tarea sin pantalla o una pantalla sin tarea es señal de error.
| Top task (PRD §2.3) | Persona / escenario (§2.1-2.2) | Pantalla | Qué debe verse primero | Patrón de lectura (F / Z) |
|---|---|---|---|---|
|  |  |  |  |  |

Cada pantalla clave pasa el **test del desenfoque** (`diseno-central/reference/revision.md`) con lo que debe destacar.

## 4. Slots por pantalla
Cada zona de cada pantalla con su componente asignado. Candidatos desde [[Catalogo de Componentes]] y, si falta, `search_items_in_registries` (shadcn-registries). Referencias visuales de Mobbin cuando haya sesión.
| Pantalla | Slot (zona) | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|---|
|  | cabecera · KPI |  |  |  |  |

## 4.1 Componentes clave
| Componente | Librería (shadcn / magicui…) | Variantes |
|---|---|---|

## 5. Imágenes e ilustración contextual
Cero contenedores vacíos **y cero imágenes inventadas en silencio**: por cada imagen que falte se pregunta a Haytham qué origen usar (flujo completo en la regla de identidad §3).
- **Estilo de imagen** de la marca:
- **Bloque de estilo para Gemini** (se pega entero en cada prompt, sin retocar):
  ```
  ```
- Prohibido en imagen: texto dentro, estética genérica de IA, lo que diga la anti-referencia.

| Vista / hueco | Qué imagen (tamaño, formato) | Origen decidido por Haytham | Estado |
|---|---|---|---|
| Vista X |  | Prompt Gemini · SVG propio · Foto real | pendiente · entregada |

## 6. Responsive y accesibilidad
- Breakpoints, objetivo táctil ≥ 44 px, contraste WCAG AA, foco visible, `prefers-reduced-motion`.

## 7. Movimiento y dinamismo
- **Nivel** (0 estático · 1 sutil · 2 dinámico · 3 protagonista) y por qué:
- **Cómo evita parecer estático sin animar**: ritmo, capas, escala, asimetría:
- **Curva propia del proyecto** (`cubic-bezier(...)`) y **elemento vivo firma** (máx. uno por pantalla):
- Dónde anima, con qué motor y por qué (un solo motor, el mismo que declara el [[2 - TRD]]).

## 8. Checklist de marca
- [ ] Prueba del intercambio: cambiando logo y textos no vale para otro negocio
- [ ] Prueba de lejos: sin logo, en 3 segundos se reconoce por forma, color y ritmo
- [ ] No repite combinación de [[Registro de Identidades Visuales]] (y se ha añadido la fila)
- [ ] No parece plantilla genérica
- [ ] Contraste verificado
- [ ] Señales de confianza presentes

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
