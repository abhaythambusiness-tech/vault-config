---
type: doc-software
doc: ui-ux
proyecto: ARM
status: aprobado
date: '2026-11-17'
origen: mixto
---

# 3 · UI/UX Design — ARM

> [!resumen] En cristiano
> ARM se ve como un **libro de registro bien encuadernado**: papel cálido, letra con carácter para los títulos y letra técnica para lo que escriben las máquinas. Cada vez que un agente (Mila, el de voz) o una persona toca un lead, deja su **firma** con la hora, como en un libro de actas. Así el cliente confía en lo que hacen los agentes. Cálido, técnico y premium; sin aspecto de CRM gris ni de «IA».

Tamaño: Proyecto · Modo: Operate · Diales 4/3/7/3/6 (variance/motion/density/assets/brand). Cada pantalla traza a una historia del [[1 - PRD]].

## 1. Principios de experiencia
1. **Lo importante primero**: lo nuevo y cualificado arriba; el resto, a un clic (top tasks hipótesis del PRD §2.3).
2. **Cada dato dice quién lo puso**: persona o agente, con firma y hora (US-09). La confianza en los agentes se gana viéndolos.
3. **Pocas cosas por pantalla**: la ficha responde «¿a quién llamo y qué le digo?» sin pestañas infinitas.
4. **Lo técnico no asusta**: claves y MCP se explican con una guía paso a paso en lenguaje llano.
5. **Rápido**: acciones frecuentes en un toque; atajos de teclado en escritorio.

## 2. Identidad visual
- **Idea visual central**: «ARM es un libro de registro que nunca duerme, y lo demuestra con la **firma de cada agente** en el margen de cada lead».
- **El producto como diseño**: el historial real de un lead (mensajes, análisis, cita, cambios de etapa) se presenta como líneas de libro de actas: margen izquierdo en mono con hora y firma, cuerpo en serif. Se enseña en vivo con datos reales, nunca con stock.
- **Composición firma**: rejilla de dos columnas con **margen de firmas** fijo a la izquierda (hora + sello del autor en mono) y contenido a la derecha; cifras grandes en serif para los KPIs; filetes finos de tinta como único adorno.
- **Anti-referencias**: CRM gris con pestañas; panel oscuro de sala de control; degradados morados, brillos «mágicos», chispas y robots; sombras grandes; tarjetas de vidrio.
- **Referencias reales** (aspecto y modelo, no código): GoHighLevel (flujo de pipeline y conversación junto a la ficha), Twenty (objetos y vistas de tabla/kanban limpias, API para agentes), Huly (densidad y velocidad). Lo que se toma: estructura y ritmo, no píxeles.
- **Marca**: **marca ARM** con **logo y color de acento del cliente** (decisión por escalabilidad: una identidad que mantener, solo cambian dos tokens por instancia). El chrome (menú, tipografía, tablas) es siempre ARM.

| Elemento | Valor |
|---|---|
| Paleta (neutros con temperatura cálida, un acento) | Neutros: `#F8F7F6` `#F2F0EE` `#E9E6E2` `#D7D1CC` `#AA9E92` `#72665A` `#39332D` `#1F1C19`. Fondo `#F6F3EE`, tinta `#211D1A`. **Acento ARM: azul acero** (del lazo del logo, oscurecido para texto) `#EEF4F7` `#D9E7EE` `#B7D0DC` `#8FB0C4` `#5F8AA3` `#3F6F89` `#2F5F78` `#1D3B4C`, uso principal `#2F5F78`. **Señal de agente: latón** `#F7F2E9` `#EBE1CB` `#DBC79F` `#CAAD72` `#B99346` `#947538` `#6F582A` `#4A3B1C`, texto `#8A6A22`. Contraste medido: tinta/fondo 15,1; acento/fondo 6,3; blanco/acento 6,9; tinta suave `#6B6259`/fondo 5,4; latón/fondo 4,6 (solo texto grande o con icono) |
| Tipografías | **Newsreader** (títulos y cifras: calidez editorial, premium) + **Onest** (interfaz y cuerpo: legible, técnica sin ser fría) + **IBM Plex Mono** (firmas, horas, IDs, claves y salida de máquinas). Motivo: serif cálido + sans claro + mono para «lo que escribe una máquina»; no se usan Inter/Geist/Space Grotesk |
| Radio / sombras / espaciado | Radio 6 px en controles y 10 px en tarjetas; sin sombras grandes, filete de 1 px `#D7D1CC` y una elevación mínima solo en menús; espaciado de 4 px (4/8/12/16/24/40) |
| Tono y voz | Cercano y claro, frases cortas; sin «IA mágica». Los agentes se llaman por su nombre (Mila) con su sello |
| Referencias (Mobbin / Figma / Canva) | Mobbin: pipelines y fichas de CRM; sin sesión por ahora, se declarará al consultarlo |

### 2.1 Tokens primero
Orden: marca → variables CSS → componentes → pantallas. El acento del cliente sustituye `--accent`; el resto es de ARM.
```css
:root {
  --bg: #F6F3EE; --surface: #FFFFFF; --ink: #211D1A; --ink-soft: #6B6259; --line: #D7D1CC;
  --accent: #2F5F78; --accent-ink: #FFFFFF; --accent-soft: #EEF4F7;
  --agent: #8A6A22; --agent-soft: #F7F2E9;
  --ok: #2F6B4F; --warn: #A15C0A; --err: #A32A2A;
  --radius-ctl: 6px; --radius-card: 10px;
  --font-title: "Newsreader", Georgia, serif; --font-ui: "Onest", system-ui, sans-serif; --font-mono: "IBM Plex Mono", ui-monospace, monospace;
  --ease: cubic-bezier(0.22, 1, 0.36, 1);
}
:root[data-theme="dark"] {
  --bg: #1B1815; --surface: #24201C; --ink: #F2EEE8; --ink-soft: #B5ABA0; --line: #3A342E;
  --accent: #8FB0C4; --accent-ink: #1B1815; --accent-soft: #1D3B4C;
  --agent: #CAAD72; --agent-soft: #2E2616;
}
```
Modo oscuro cálido y opcional (no es el defecto); sin negro puro ni lima, para no repetir Grid64.

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base ([[Biblioteca de Layouts]]) | Estados a diseñar |
|---|---|---|---|---|
| Login | Cliente, operador | US-01 | formulario centrado | cargando · error de clave · sesión caducada |
| Inicio: nuevos y cualificados | Cliente | US-01 | dashboard + lista | vacío (con guía para conectar el Setter) · cargando · error |
| Lista de leads | Cliente | US-01 | lista-detalle | vacío · filtros sin resultado · cargando |
| Pipeline | Cliente | US-08 | tablero por etapas | columna vacía · error al mover |
| Ficha del lead (con historial y notas) | Cliente | US-02, US-04, US-09 | lista-detalle con margen de firmas | sin cita · sin mensajes · error · guardando |
| Resumen semanal | Cliente | US-11 | dashboard | semana sin datos |
| Conexiones (claves y MCP) | Cliente, operador | US-05, US-06 | parte + guía | sin claves · clave recién creada (se muestra una vez) · revocada |
| Avisos | Cliente | US-10 | ajustes | desactivado · activo |
| Alta de instancia | Operador | US-07 | línea de comandos (`arm-alta`), sin pantalla | — |
| Agentes (claves de API) | Operador | US-03, US-05 | tabla | sin agentes · clave caducada |

### 3.1 Top tasks y escenarios → pantallas
Hipótesis (`sin confirmar`, PRD §2.3).
| Top task | Escenario | Pantalla | Qué debe verse primero | Patrón de lectura |
|---|---|---|---|---|
| Ver a quién llamar hoy | Recepcionista por la mañana | Inicio | Cualificados sin contactar, con la última firma | F |
| Preparar la llamada | Antes de marcar | Ficha | Qué busca, resumen del análisis, cita y última firma | F con margen de firmas |
| Cambiar etapa y dejar nota | Tras la llamada | Ficha / Pipeline | Etapa actual y campo de nota | Z |
| Preguntar a mi IA | Dueño con muchos leads | Conexiones | Pasos para conectar y copiar la URL | Z |
| Controlar qué hacen los agentes | Dueño desconfiado | Ficha > Historial | Firmas por agente con hora | F |

Cada pantalla clave pasa el test del desenfoque: en Inicio debe destacar el bloque «Cualificados», y en Ficha el nombre del lead y su estado.

## 4. Slots por pantalla
Se completa en la **Paleta de Componentes** (tras aprobar esta identidad) con `search_items_in_registries` y [[Catalogo de Componentes]]. Esqueleto:
| Pantalla | Slot | Componente (a elegir) | Librería | Dato | Estado vacío |
|---|---|---|---|---|---|
| Inicio | KPI de cabecera | cifra grande en serif | shadcn + magicui | entrados / cualificados / con cita | «Aún no hay leads: conecta el Setter» |
| Lista | tabla de leads | tabla con filtros | shadcn | nombre, etapa, última firma | texto + guía |
| Ficha | margen de firmas | componente propio sobre shadcn | shadcn | hora + sello + acción | «Sin actividad» |
| Pipeline | columnas | kanban | shadcn + dnd (por decidir) | leads por etapa | columna vacía |
| Conexiones | pasos y claves | pasos + campo de copia | shadcn | URL del MCP, clave | «Crea tu primera clave» |

## 4.1 Componentes clave
| Componente | Librería | Variantes |
|---|---|---|
| Sello de firma (hora + autor) | propio sobre shadcn | persona · agente (latón) · sistema |
| Ficha de lead con margen de firmas | propio | normal · cualificado · descartado |
| Cifra KPI | magicui (número animado, a confirmar) | normal · delta |
| Campo de copia de clave | shadcn | oculta · visible una vez |

## 5. Imágenes e ilustración contextual
Cero contenedores vacíos **y cero imágenes inventadas en silencio**.
- **Estilo de imagen**: ninguna foto ni ilustración de stock. La imagen del producto es el propio libro de registro con datos reales. Iconos de línea fina (Lucide); sellos y estados vacíos como **SVG propio** (libro abierto con un filete, sello tipográfico con iniciales).
- **Bloque de estilo para Gemini**: no se usa en v1 (no hay imágenes generadas).
- Prohibido en imagen: texto dentro, caras o logos inventados, estética genérica de IA, robots, chispas y degradados morados.

| Vista / hueco | Qué imagen | Origen decidido por Haytham | Estado |
|---|---|---|---|
| Logo de ARM | Cuadrado negro redondeado con lazo de Möbius triangular en azul hielo (material NeoZeler) | Aprobado; `~/Proyectos/arm/assets/` (1024 a 16 px y favicon). Pendiente: versión SVG plana para 24 px y lockup «ARM por NeoZeler» | aprobado |
| Estados vacíos (Inicio, Lista, Ficha) | SVG de libro abierto, 2 tonos | SVG propio | pendiente de aprobar |
| Logo del cliente | Su logo vectorial o PNG | Foto/logo real del cliente al dar el alta | por instancia |
| Sello del agente | Círculo con iniciales en mono | SVG generado por código | automático |

## 6. Responsive y accesibilidad
- Breakpoints 375 / 768 / 1280; revisión a 320 sin scroll horizontal. En móvil, el margen de firmas pasa encima del texto.
- Objetivo táctil ≥ 44 px, contraste WCAG AA (medido arriba), foco visible, `prefers-reduced-motion` respetado, navegación completa por teclado y atajos en escritorio.
- axe a cero violaciones y Lighthouse antes de dar por hecho.

## 7. Movimiento y dinamismo
- **Nivel 1 (sutil)**, porque es una herramienta de trabajo diario (modo Operate): el movimiento informa, no decora.
- **Cómo evita parecer estático sin animar**: ritmo del libro (filetes, margen de firmas, cifras grandes en serif), contraste de escala entre título y mono, y asimetría de dos columnas.
- **Curva propia**: `cubic-bezier(0.22, 1, 0.36, 1)`, 180-260 ms.
- **Elemento vivo firma** (uno por pantalla): al llegar una actividad nueva de un agente, su **sello se imprime** en el margen (opacidad + 4 px de desplazamiento, una vez). En Inicio, el contador de cualificados sube con la misma curva.
- Motor: **Motion** (un solo motor, el que declara el [[2 - TRD]]); solo `transform` y `opacity`; animación accesible primero (`web-animation-skills:accessible-animation`).

## 8. Checklist de marca
- [ ] Prueba del intercambio: cambiando logo y textos no vale para otro negocio
- [ ] Prueba de lejos: sin logo, en 3 segundos se reconoce por margen de firmas, azul acero y serif
- [ ] No repite combinación de [[Registro de Identidades Visuales]] (azul acero + latón + Newsreader no están; fila añadida)
- [ ] No parece plantilla genérica
- [ ] Contraste verificado (medido en §2)
- [ ] Señales de confianza presentes (firma de agente, historial, claves revocables)

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
