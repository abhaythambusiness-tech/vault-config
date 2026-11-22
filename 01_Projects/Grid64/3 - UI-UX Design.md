---
type: doc-software
doc: ui-ux
proyecto: "Grid64"
status: aprobado
date: 2026-11-08
origen: mixto
---

# 3 · UI/UX Design — Grid64

> [!resumen] En cristiano
> Propuesta de cara de la app: un tablero oscuro y cálido donde cada acción es una «piedra» (como en el juego de Go) que pasa de hueca a rellena al hacerla. El cuadro 9×9 es la pantalla, no un adorno. Sin referencias externas, por tu decisión.
> **Decisión que te toca:** aprobar la identidad (§2, §5, §7), o decir qué cambiar, y contestar la pregunta del icono en §5.

## 1. Principios de experiencia
- Una mano, pulgar: controles en el tercio inferior; objetivo táctil ≥ 48 dp.
- Un pilar a la vez (3×3); el panorama 9×9 solo para orientarse.
- Marcar una acción: 1 toque + háptico. Capturar una idea: ≤ 3 toques.
- Nunca una pantalla vacía muda: cada estado vacío dice el siguiente paso.

## 2. Identidad visual
- **Idea visual central**: «Grid64 es un tablero de Go y lo demuestra la piedra: cada acción es una piedra hueca que se rellena y se asienta al completarla; cuando las 8 de un pilar están puestas, el pilar se enciende.»
- **El producto como diseño**: el propio cuadro 9×9 con progreso real (anillos y piedras); sin ilustraciones ni stock.
- **Composición firma**: rejilla 3×3 de pilares con la meta central como núcleo más grande; el pilar activo ocupa la pantalla y los vecinos asoman por los bordes (swipe).
- **Anti-referencias**: app de productividad infantil o gamificada con confeti; dashboard corporativo gris; azul noche + ámbar, grafito + hielo y tinta + naranja (ya usados en Los Apuntes de Liyo, ComandAi y TopLeads).
- **2 referencias reales**: no se piden (decisión de Haytham). Referencia conceptual propia: el tablero de Go (piedras sobre rejilla), no un producto.

| Elemento | Valor |
|---|---|
| Paleta | Obsidiana cálida `#12100E` / `#1B1815` / `#26211C` (fondos), hueso `#ECE6DA` (texto), acento jade `#3FBF8F` (único acento de interfaz). 8 tonos de pilar, uno por pilar: `#E07A5F`, `#E0A458`, `#C9C45A`, `#6FBF73`, `#4FB3BF`, `#6A8FE0`, `#A47FD6`, `#D678A9`; solo se ven en piedras y anillos |
| Tipografías | Figtree (interfaz; redondeada y legible en pantalla pequeña) + Martian Mono (cifras y porcentajes; el cuadro es un instrumento) — motivo: calidez de tablero sin parecer juego |
| Radio / sombras / espaciado | Radio 18 px tarjetas, piedras circulares; sin sombras duras, solo capa de luz interior; rejilla de 4 px, gutters de 12 |
| Tono y voz | Tú, breve, tranquilo («Hoy: 3 piedras»), sin exclamaciones ni emojis |
| Referencias | Ninguna externa |

### 2.1 Tokens primero
```css
:root{
  --bg:#12100E; --surface:#1B1815; --surface-2:#26211C;
  --text:#ECE6DA; --text-dim:#A39B8E; --brand:#3FBF8F;
  --radius:18px; --ease-stone:cubic-bezier(.34,1.3,.64,1);
  --p1:#E07A5F; --p2:#E0A458; --p3:#C9C45A; --p4:#6FBF73;
  --p5:#4FB3BF; --p6:#6A8FE0; --p7:#A47FD6; --p8:#D678A9;
}
```
Modo claro: no en v1 (oscuro por defecto según PRD; `prefers-color-scheme` se revisa en Pulido).

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base | Estados a diseñar |
|---|---|---|---|---|
| Inicio | Usuario | US-06, US-07, US-11 | dashboard móvil | vacío (sin mandala) · hoy sin prioridades · éxito (todo hecho) |
| Mandalas: panorama 9×9 | Usuario | US-04, US-12 | cuadrícula | vacío · cargando · parcial |
| Mandalas: enfoque 3×3 | Usuario | US-02, US-03, US-05 | detalle por swipe | pilar vacío · completo |
| Hoja inferior de acción | Usuario | US-10 | sheet | sin notas · con fecha vencida |
| Crear mandala (asistente) | Usuario | US-01 | asistente 3 pasos | error de validación |
| Ideas | Usuario | US-08, US-09 | lista/grid | vacío · convertida |
| Exportar / copia | Usuario | US-13, US-14 | sheet | éxito · error |

## 4. Slots por pantalla
App con Alpine y CSS propio, **sin React ni registries**; no aplica la Paleta de Componentes de shadcn/magicui. Piezas propias:
| Pantalla | Slot | Componente propio | Dato | Estado vacío |
|---|---|---|---|---|
| Inicio | cabecera | Saludo + racha + barra global | racha, % | «Crea tu primer mandala» |
| Inicio | cuerpo | Tarjeta de objetivo activo + lista de hoy | % y días restantes | «Elige hasta 5 piedras para hoy» |
| Mandalas | cabecera | Selector horizontal de mandalas | títulos | botón crear |
| Mandalas | cuerpo | Cuadrícula de piedras (9×9 o 3×3) | progreso | piedras huecas |
| Todas | pie | Barra inferior de 3 pestañas + `+` flotante | n/a | n/a |

### 4.1 Componentes clave
| Componente | Librería | Variantes |
|---|---|---|
| Piedra (acción) | CSS + Alpine | hueca · rellena · prioridad de hoy · vencida |
| Anillo de pilar | SVG propio | 0-100 % |
| Hoja inferior | Alpine + CSS | media · completa |

## 5. Imágenes e ilustración contextual
Cero imágenes inventadas. La app no necesita ilustraciones: los estados vacíos usan el propio tablero.
- **Estilo de imagen**: ninguna; solo geometría (piedras, anillos).
- **Bloque de estilo para Gemini**: solo si Haytham decide generar el icono.
- Prohibido: texto dentro de imagen, estética genérica de IA.

| Vista / hueco | Qué imagen | Origen decidido por Haytham | Estado |
|---|---|---|---|
| Icono de la app (Android, 512×512, adaptativo) | Tablero 3×3 con una piedra rellena | SVG propio (decidido 2026-11-08) | entregada: `~/Proyectos/grid64/assets/icon.svg` |

## 6. Responsive y accesibilidad
- Base 360-430 px vertical; el mismo HTML se prueba a 375/768/1280 en navegador.
- Objetivo táctil ≥ 48 dp, contraste AA (hueso sobre obsidiana ≈ 14:1), foco visible, etiquetas en piedras («Acción 3 del pilar Salud, pendiente»), `prefers-reduced-motion` desactiva el rebote.
- No depender solo del color: la piedra rellena difiere de la hueca por forma.

## 7. Movimiento y dinamismo
- **Nivel**: 1-2. Solo responde al gesto; el progreso es el protagonista.
- **Cómo evita parecer estático**: escala entre núcleo y pilares, piedras con profundidad (luz interior), anillos de progreso.
- **Curva propia**: `cubic-bezier(.34,1.3,.64,1)` («asentarse»). **Elemento vivo firma**: la piedra que se asienta con rebote al marcar y, al cerrar un pilar, un pulso de su color en el anillo (máx. uno por pantalla).
- **Motor**: CSS + Web Animations API, 0 librerías (coincide con TRD §1.2).

## 8. Checklist de marca
- [ ] Prueba del intercambio: cambiando logo y textos no vale para otro negocio
- [ ] Prueba de lejos: se reconoce por la rejilla de piedras y el jade
- [x] No repite combinación de [[Registro de Identidades Visuales]] (fila añadida 2026-11-08)
- [ ] No parece plantilla genérica
- [ ] Contraste verificado
- [ ] Señales de confianza: «Tus datos no salen de este móvil», visible en Ajustes

## 9. Inspiración: interfaces de Airtable (añadido 2026-11-08, petición de Haytham)
Se toma el **vocabulario de estructura** de Airtable Interfaces (tipos de página y elementos: dashboard, record detail, record review, gallery, list, kanban, number, form), no su aspecto: la identidad (§2, oscuro, piedras, jade) no cambia.

| Pantalla Grid64 | Equivalente Airtable | Qué se adopta |
|---|---|---|
| Inicio | Dashboard | Fila de «Number»: racha, progreso global, días restantes. Debajo, elemento «List» con Acciones de hoy y checkbox |
| Mis Mandalas: selector | Gallery | Tarjetas con título, anillo de % y fecha; scroll horizontal |
| Mis Mandalas: enfoque 3×3 | Record review | Pasar de un pilar al siguiente (swipe) con contador «3 / 8» arriba |
| Hoja inferior de acción | Record detail (panel lateral) | Campos en lista vertical: título, estado, notas Markdown, fecha tope, idea vinculada |
| Ideas | Kanban / List | Vista por defecto lista con filtros de estado como pestañas (Bandeja · Vinculadas · Archivadas); conversión como acción de fila |
| Crear mandala | Form | Asistente de 3 pasos con campos etiquetados y validación en línea |

Reglas: densidad compacta de listas, filas tocables ≥ 48 dp, etiquetas de campo en `--text-dim` sobre el valor. Revisar con `diseno-central` antes de maquetar (T-10).

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
