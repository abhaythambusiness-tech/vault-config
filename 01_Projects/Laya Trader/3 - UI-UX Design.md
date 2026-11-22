---
type: doc-software
doc: ui-ux
proyecto: "Laya Trader"
status: aprobado
date: 2026-10-22
origen: mixto
---

# 3 · UI/UX Design — Panel Laya Trader

> [!resumen] En cristiano
> Un panel web con aspecto de **cuaderno de laboratorio**, no de casino de bolsa: fondo claro cálido (con modo oscuro), números nítidos y una sola pregunta arriba del todo: **«¿sirve Laya o no?»**, contestada con un sello grande (NO CONCLUYENTE / PASA / CIERRE). Debajo, gráficos en vivo. Cinco pantallas, todas de solo lectura. Decisión que te toca: aprobar este diseño.

Gate previo ejecutado (2026-10-22): `ui-ux-pro-max` (estilos *Data-Dense Dashboard* y *Real-Time Monitoring*; pareja tipográfica *Financial Trust*), `dataviz` (colores de serie validados con su script). Descartado a propósito el "SaaS oscuro navy + verde" que devuelve la búsqueda de color: es el aspecto genérico que prohíbe el gate.

## 1. Principios de experiencia
- **El veredicto primero.** Lo que decide va arriba-izquierda; el detalle, debajo.
- **Honestidad numérica.** Siempre netos (tras comisiones); si la muestra es corta, el panel lo dice con letra grande, no con una nota pequeña.
- **Vivo pero tranquilo.** Un punto de estado y marcas de tiempo; nada parpadea sin motivo.
- **Cero pantallas vacías.** Cada hueco tiene estado de carga, vacío y error con texto útil (catálogo de seis estados en `4 - AppFlow` §4; P1 a P5 los diseñan todos).
- **Lenguaje normal, siempre (regla de Haytham, 2026-10-22).** Ninguna palabra técnica sin su frase llana **visible** al lado o debajo (no solo en un globo al pasar el ratón: en el móvil no hay ratón). Títulos como preguntas o frases cortas («¿Sirve Laya?», «¿Cómo va cada moneda?»). Los términos siguen el glosario único de `4 - AppFlow` §4.1.
- **Intuitivo sin manual.** Cada pantalla abre con una línea que dice qué se está viendo y qué hacer («Aquí ves si Laya gana al programa de reglas. No hace falta tocar nada»). Un botón «¿Cómo leo esto?» abre una ayuda de 5 líneas por pantalla.

## 2. Identidad visual
| Elemento | Valor |
|---|---|
| Paleta (tokens) | Superficies cálidas neutras (de `dataviz`); Laya = azul `#2a78d6`; Juez de reserva = naranja `#eb6834`; estados: bien `#0ca30c`, aviso `#fab219`, grave `#ec835a`, crítico `#d03b3b` (siempre con icono y texto) |
| Tipografías | IBM Plex Sans (interfaz) + IBM Plex Mono (cifras, precios, registros), autoalojadas (OFL) |
| Radio / sombras / espaciado | Radio 8 px (tarjetas) y 4 px (chips); sin sombras: aro de 1 px; escala 4/8 px; tarjetas con 12-16 px de relleno |
| Tono y voz | Español claro, frases cortas, términos traducidos en un `title`/tooltip («Brier = cuánto se equivoca en sus porcentajes») |
| Detalle firma | **Regla graduada**: una franja fina de marcas (como una regla de laboratorio) en el borde superior de cada tarjeta, y el veredicto como **sello** inclinado 2° con borde doble |
| Referencias | Mobbin no disponible (sin sesión): declarado. Referencia de estructura: `jarrodwatts/jev-trader` (panel SSE) sin copiar su estética |

### 2.1 Tokens primero
```css
:root {
  color-scheme: light;
  --page: #f9f9f7;  --surface: #fcfcfb;  --ring: rgba(11,11,11,.10);
  --ink: #0b0b0b;  --ink-2: #52514e;  --ink-3: #6b6a65;   /* ink-3 ≥ 4.5:1 en superficie clara */
  --grid: #e1e0d9; --axis: #c3c2b7;
  --laya: #2a78d6; --reserva: #eb6834;
  --good: #0ca30c; --good-text: #006300; --warn: #fab219; --serious: #ec835a; --critical: #d03b3b;
  --radius: 8px; --radius-sm: 4px; --gap: 12px;
  --ease: cubic-bezier(.16,1,.3,1);
  --font-sans: "IBM Plex Sans", system-ui, sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  color-scheme: dark; --page: #0d0d0d; --surface: #1a1a19; --ring: rgba(255,255,255,.10);
  --ink: #f0efec; --ink-2: #c3c2b7; --ink-3: #a09f98; --grid: #2c2c2a; --axis: #383835;
  --laya: #3987e5; --reserva: #d95926; --good-text: #0ca30c; } }
:root[data-theme="dark"] { /* mismos valores oscuros */ }
```
El `ink-3` claro (`#6b6a65`) y oscuro (`#a09f98`) se comprobarán con contraste ≥ 4,5:1 antes de cerrar la tarea de interfaz. Los colores de serie pasan el validador de `dataviz` (claro: ΔE 33,6 normal / 24,7 daltonismo; oscuro: 31,8 / 26,8; contraste ≥ 3:1).

## 3. Inventario de pantallas
| Pantalla | Rol | Historia | Layout base | Estados a diseñar |
|---|---|---|---|---|
| P1 Veredicto | Operador | US-11, US-09 | Dashboard | vacío (sin datos aún) · cargando · error de conexión · éxito |
| P2 Mercado (BTC · ETH · SOL) | Operador | US-01, US-02, US-04, US-08 | Dashboard (1 gráfica principal) | feed caído · sin operaciones · normal |
| P3 Calibración | Operador | US-09 | Dashboard | muestra insuficiente · normal |
| P4 Riesgo y sistema | Operador | US-06, US-07, US-10 | Dashboard | kill switch activo · escalera en reserva · normal |
| P5 Registro de decisiones | Operador | US-03, US-05, US-07, US-09 | Lista + detalle | vacío · filtrado sin resultados · normal |

Navegación: carril lateral fijo (escritorio) / barra inferior de 5 iconos con texto (móvil). Cabecera común: nombre, punto de estado en vivo, hora del último bloque, conmutador claro/oscuro.

## 4. Slots por pantalla
| Pantalla | Slot | Componente | Librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|---|
| P1 | A cabecera | Título + punto en vivo + selector de periodo | HTML/CSS propio | «Laya Trader · papel», último bloque hace Ns | «Esperando el primer bloque…» |
| P1 | B sello | Sello de veredicto grande + línea «qué falta» | propio | «TODAVÍA NO SE SABE» / «LAYA SIRVE» / «LAYA NO SIRVE: SE CIERRA» + las dos reglas con ✓/✗ + una línea tipo «Te faltan 212 operaciones y 5 días para poder decidir» | Sello gris «sin datos» |
| P1 | B KPI ×4 | Tarjetas de cifra, cada una con su frase llana | propio | «Ganancia de Laya (ya descontadas las comisiones)» · «Ganancia del programa de reglas (ya descontadas las comisiones)» · «Operaciones hechas: 88 de 300 necesarias» · «Días medidos: 2 de 7 necesarios» | `—` con texto «aún 0 operaciones» |
| P1 | C gráfica principal | Líneas de dinero acumulado | lightweight-charts 5.2.1 | Laya (azul) vs Reserva (naranja), leyenda + etiqueta directa | Línea plana con texto |
| P1 | D tabla | Últimas 10 decisiones | propio | hora, símbolo, acción, juicio, neto | Fila «Sin decisiones todavía» |
| P2 | A cabecera | Pestañas BTC/ETH/SOL | propio | símbolo activo, spread, microprecio | — |
| P2 | B tira de juicios | 6 chips con respuesta y confianza (Laya vs reserva) | propio | régimen, dirección, flujo tóxico, estrés, entorno, inventario | Chips grises «sin juicio» |
| P2 | C gráfica principal | Velas/línea de precio con marcas de entrada y salida | lightweight-charts | precio + fills de ambos carriles | «Sin ejecuciones» |
| P2 | D libro | Mini-libro (10 niveles) en barras | propio SVG | bids/asks | «Libro sin sincronizar» |
| P3 | B tarjetas | Brier · log loss · ECE · n | propio | Laya vs reserva | `—` hasta 50 juicios |
| P3 | C gráfica principal | Curva de fiabilidad | SVG propio | probabilidad dicha vs frecuencia real, diagonal de referencia | Texto «muestra insuficiente» |
| P3 | D tabla | Calibración por juicio | propio | un renglón por pregunta | — |
| P4 | B estado | Semáforo de 4 vetos + interruptor de emergencia; cada veto disparado es **clicable** y lleva a la decisión afectada (P5 detalle) | propio | «Límite de pérdida diaria: usado 20 % de lo permitido»; leyenda fija: verde = todo bien · amarillo = cerca del límite (más del 70 % usado) · naranja = el bot va con más prudencia · rojo = se ha frenado | todo verde si nada se usó |
| P4 | C escalera | Línea de 5 peldaños con el activo marcado | propio | normal · poca confianza · fuera de plazo · Laya caída · interruptor | — |
| P4 | D latencia | Histograma de la llamada a Laya | SVG propio | p50/p95, % fuera de plazo | «Sin muestras» |
| P5 | A barra | Búsqueda + filtros (símbolo, carril, acción) | propio | — | — |
| P5 | B lista | Filas con estado | propio | hora, símbolo, acción, resultado | «Aún no hay decisiones» |
| P5 | C detalle | Estado enviado, 6 juicios, política, veto, resultado | propio + `<pre>` mono | el triple `(estado, decisión, resultado)` | «Elige una decisión» |

### 4.1 Componentes clave
| Componente | Librería | Variantes |
|---|---|---|
| `Card` con regla graduada | CSS propio | normal · alerta |
| `Stamp` (veredicto) | CSS propio | gris · verde · rojo, siempre con texto e icono |
| `KpiTile` | CSS propio | con delta ▲▼ + texto, nunca solo color |
| `Chip` de juicio | CSS propio | confianza alta / media / baja (relleno, medio relleno, trazo) |
| `LiveDot` | CSS propio | conectado · reconectando · caído |
| `Chart` | lightweight-charts 5.2.1 | línea · área · velas |
| `Gauge` de veto | CSS/SVG | usado/permitido |

No se usa shadcn/magicui: el servidor no tiene Node ni React (TRD §1). Se declara; el Catálogo de Componentes se amplía al terminar.

### 4.2 Reglas de lenguaje y de pantalla añadidas tras el cliente simulado (2026-10-22)
| Tema | Regla |
|---|---|
| Diccionario de etiquetas | Se muestra la palabra llana, el término técnico queda pequeño al lado. Ej.: «Precio justo del momento» (microprecio) · «Hueco entre comprar y vender» (spread) · «Quién empuja: compradores o vendedores» (desequilibrio) · «¿Hay gente con prisa por vender?» (flujo tóxico) · «¿Cuesta comprar o vender?» (estrés de liquidez) · «¿Cuánta seguridad tiene Laya?» (confianza) · «Lo que se equivoca en sus porcentajes» (Brier, log loss, ECE: menor es mejor) · «Tiempo que tarda Laya en contestar» (latencia) · «Nivel de prudencia del bot» (escalera) |
| Selector de periodo (P1) | Afecta solo a las curvas y a la tabla; el sello y los KPI siempre usan todo el experimento. Se escribe debajo del selector. |
| Mini-libro (P2) | En escritorio 10 niveles en barras; en móvil, una lista de 3 compradores y 3 vendedores con su explicación. |
| Estados de P2, P3 y P5 | Cada una diseña los seis estados del catálogo (cargando, vacío, reconectando, error de conexión, datos parados, error 500); P5 añade «cargar más» y orden por hora. |
| Decisión sin resultado aún | «El resultado se sabrá en 8 min» en lugar de un guion. |
| Comando para reiniciar (P4) | Texto copiable con botón «Copiar»; explicación en una frase: «Pídeselo a Claude o escríbelo en la terminal». |
| Botón «¿Cómo leo esto?» | En cada pantalla; ayuda de 5 líneas escritas sin jerga. |

## 5. Imágenes e ilustración contextual
Prompts para Bloom/Haytham (estado vacío de las vistas clave; estilo: tinta sobre papel milimetrado, azul y naranja, sin personas, sin texto):
- P1 vacío: «Plano de laboratorio sobre papel milimetrado: dos péndulos idénticos, uno tinta azul y otro naranja, listos para soltarse; línea de tiempo vacía debajo; estilo grabado técnico, fondo crema, aire de cuaderno de campo.»
- P3 vacío: «Báscula de precisión con dos platillos vacíos y una regla graduada detrás; tinta azul y naranja sobre crema, estilo láminas científicas antiguas.»
- P4 error/alto: «Interruptor de emergencia rojo con tapa de seguridad levantada sobre una mesa de laboratorio milimetrada; vista cenital, trazo fino.»

## 6. Responsive y accesibilidad
- Breakpoints: 375 · 768 · 1200. Móvil: una columna, KPI en scroll horizontal, barra inferior; objetivo táctil ≥ 44 px.
- Contraste WCAG AA (texto ≥ 4,5:1; gráficos ≥ 3:1); colores de serie con **etiqueta directa + leyenda** y tabla alternativa («Ver como tabla»); estados con icono + texto, no solo color.
- Foco visible (aro de 2 px), orden de tabulación lógico, `aria-live="polite"` en el sello y en el estado del feed, `prefers-reduced-motion` respetado.
- Hover con transformación (elevación de 1 px de tarjeta, desplazamiento de fila), no solo color. `tabular-nums` en todas las cifras.

## 7. Movimiento
CSS únicamente (cero motores de animación, TRD §1.2), curva propia `--ease`: entrada de tarjetas con desplazamiento de 8 px y desvanecido en 280 ms escalonado de 30 ms; el sello «cae» una vez al cargar; el punto en vivo pulsa a 2 s; las cifras se actualizan con un cambio de fondo de 400 ms. Todo desactivado con `prefers-reduced-motion`.

## 8. Checklist de marca
- [ ] No parece plantilla genérica (regla graduada + sello + Plex; sin navy/teal ni degradado morado)
- [ ] Contraste verificado en 375 px claro y oscuro (al construir; DevTools de Chrome no disponible, se usa el navegador integrado de Claude)
- [ ] Señales de confianza presentes (netos, tamaño de muestra, «papel, sin dinero real»)
- [ ] Ningún logo ni dato inventado

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
