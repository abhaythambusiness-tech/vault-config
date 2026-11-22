---
type: doc-software
doc: ui-ux
proyecto: 01_Projects/Scalper Memecoins
status: aprobado
date: '2026-10-21'
origen: mixto
---


# 3 · UI/UX Design

> [!resumen]
> Panel web de **un solo operador**, tema oscuro "carbón cálido + ámbar" (la misma identidad del panel de `crypto-copy-bot`, para que se sienta de la misma familia). Cinco pantallas: **En vivo**, **Decisiones**, **Operaciones**, **Gate 1** y **Control**. Cada pantalla traza a una historia del [[1 - PRD]]. Siempre visible: banner **PAPEL · sin dinero real**.

> [!cliente] Gate de diseño ejecutado (declaración)
> - Estilo: `ui-ux-pro-max search.py` ejecutado (dominios `product`, `style`, `color`, `typography`). Recomendó "Real-Time Monitoring" + dark data-dense para fintech/trading; **descarto** su paleta por defecto (dorado + morado sobre navy `#0F172A`) y su glassmorphism por ser el look genérico prohibido.
> - Gráfica: skill `dataviz` aplicada y paleta **validada con `validate_palette.js`** en modo oscuro sobre `#14110F`: PASS en banda de luminosidad, croma, separación para daltónicos (ΔE 12,5 protan / 25 tritan), visión normal (ΔE 21,8) y contraste ≥ 3:1.
> - MCP: ninguno de diseño aplica (no hay Figma, Canva ni shadcn en este stack; ver TRD §1). Mobbin no se usó: sin sesión. Chrome DevTools: **no disponible**; la verificación visual se hará con el navegador integrado de Claude.
> - Guideline aplicada: `03_Resources/web-interface-guidelines.md` (foco, estados, contraste, copy).

## 1. Principios de experiencia
- **La verdad primero**: lo que se ve es papel y está dicho siempre. Nada de cifras sin periodo y sin n de operaciones.
- **Una acción primaria por pantalla**: En vivo → Pausar; Control → Guardar límites.
- **El bot se explica**: cada decisión muestra qué le preguntó a Laya, qué respondió y con qué confianza.
- **Resultado del Gate sin maquillaje**: mientras n < 300 pone "NO CONCLUYENTE", nunca un verde.
- **Pérdidas con el mismo peso que ganancias**: color **más** signo **más** flecha (▲ ▼), nunca solo color.
- **Cada cifra con su n y su periodo** ("hoy · 37 operaciones") y, si es técnica, con tooltip y enlace al glosario.
- **La confianza de Laya es una puntuación, no una probabilidad de acierto**: se muestra sin porcentaje ("alta / media / baja") hasta que `calibrate` demuestre lo contrario.
- **Una decisión se explica en una frase** antes de enseñar el texto enviado a Laya y las probabilidades (que quedan plegados).

## 2. Identidad visual
| Elemento | Valor |
|---|---|
| Paleta (tokens) | Carbón cálido + ámbar (ver §2.1). Estados de PnL con verde y rojo **reservados**, siempre con ▲/▼ y signo |
| Series de la gráfica | Laya `#C97F15` ámbar · Reglas `#4F8FE0` azul · Azar = línea discontinua gris (referencia, no serie) |
| Tipografías | **IBM Plex Sans** (UI) + **IBM Plex Mono** (cifras, hashes, texto enviado a Laya), autoalojadas (OFL-1.1), sin Google Fonts en ejecución |
| Radio / sombras / espaciado | Radio 6 px (tarjetas) y 3 px (chips); sin sombras, separación por borde de 1 px y superficie; escala 4/8 px |
| Tono y voz | Español directo y sobrio. "Compra", "Venta", "Saltar", "Mantener". Sin jerga de moda ni exclamaciones |
| Referencias | Panel de `crypto-copy-bot` (ámbar sobre carbón) como base; patrón "Real-Time Monitoring" de `ui-ux-pro-max` |

### 2.1 Tokens primero
```css
:root {
  /* superficies (carbón cálido, no navy) */
  --bg:        #14110F;
  --surface:   #1C1815;
  --surface-2: #26201C;
  --border:    #352D27;
  /* texto */
  --text:      #F2EBE3;   /* ~15:1 sobre --bg */
  --text-2:    #C9BDB0;   /* ~10:1 */
  --text-3:    #A89C8F;   /* ~7:1, mínimo permitido para <14 px */
  /* marca y series (validadas con dataviz) */
  --brand:     #F5A524;   /* acción primaria, foco */
  --s-laya:    #C97F15;
  --s-reglas:  #4F8FE0;
  --s-azar:    #8F8377;   /* referencia discontinua */
  /* estados reservados (nunca como serie) */
  --gain:      #5FD38D;
  --loss:      #FF6B5B;
  --warn:      #F2C14E;
  --live:      #5FD38D;
  /* forma y movimiento */
  --radius: 6px; --radius-chip: 3px;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);   /* expo-out propia del proyecto */
  --font-ui: "IBM Plex Sans", system-ui, sans-serif;
  --font-num: "IBM Plex Mono", ui-monospace, monospace;
}
.num { font-family: var(--font-num); font-variant-numeric: tabular-nums; }
```
> Solo tema oscuro en v1 (panel de operador). Modo claro: fuera de alcance. Los contrastes se comprobarán en el navegador integrado a 375 px antes de dar nada por terminado.

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base ([[Biblioteca de Layouts]]) | Estados a diseñar |
|---|---|---|---|---|
| **En vivo** | Operador | US-01, US-03, US-05 (banner PAPEL, costes y salud), US-06 (pausa) | Dashboard (con simetría rota: feed a la derecha ocupa la altura de gráfica + posiciones) | vacío (sin operaciones aún) · cargando · error de conexión · bot pausado · éxito |
| **Decisiones** | Operador | US-02, US-04 | Lista + detalle | vacío · cargando · error · filtro sin resultados |
| **Operaciones** | Operador | US-03, US-08 | Dashboard reducido (KPI + tabla) | vacío · cargando · error · exportando |
| **Gate 1** | Operador | US-07 | Ficha de entidad (veredicto + pestañas) | "no concluyente" · cargando · error · veredicto final |
| **Control** | Operador | US-06 | Asistente simple (límites + zona de peligro + token) | guardado · validación fallida · token inválido · corte diario activo |
| **Acceso** | Operador | US-06 | Pantalla única de un campo | pedir token · token inválido · caducado |
| **Glosario** | Operador | US-02, US-07 | Lista con búsqueda (panel lateral) | vacío (término no encontrado) · cargando |

## 4. Slots por pantalla
Sin librería de componentes (decisión TRD §1: sin Node). Los "componentes" son clases CSS propias; `lightweight-charts` 5.2.1 solo para el gráfico.
| Pantalla | Slot (zona) | Componente | Librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|---|
| En vivo | A cabecera | `Topbar` (nombre, punto "en vivo", banner PAPEL, botón **Pausar** primario) | CSS propio | Estado del bot, latencia del feed | "Bot detenido" con botón Reanudar |
| En vivo | B KPI (4) | `StatTile` ×4 | CSS propio | Equidad (suma de la cartera Laya), PnL del día, operaciones hoy, coste total del día | "—" con texto "Sin operaciones hoy" |
| En vivo | C gráfica | `EquityChart` (3 líneas: Laya, Reglas, Azar discontinua) con leyenda y tooltip con cruceta | lightweight-charts | Curva de equidad por cartera, última hora/día | Ilustración vacía (§5) + "Esperando la primera operación" |
| En vivo | D posiciones | `PositionTable` | CSS propio | Moneda, entrada, precio, PnL ▲▼, tiempo, stop | Ilustración vacía (§5) |
| En vivo | E feed (columna derecha) | `DecisionFeed` (flujo SSE, más reciente arriba) | CSS propio | Hora, moneda, acción (Comprar/Mantener/Vender/Saltar), confianza de Laya | "Aún sin decisiones" |
| Decisiones | A barra | `FilterBar` (cartera, acción, buscar moneda) | CSS propio | Filtros | — |
| Decisiones | B lista | `DecisionList` | CSS propio | Fila con acción + confianza | Ilustración vacía (§5) |
| Decisiones | C detalle | `DecisionDetail` (texto enviado a Laya en mono, probabilidades, umbral aplicado, resultado de la operación) | CSS propio | Auditoría completa | "Elige una decisión" |
| Operaciones | B KPI | `StatTile` ×3 | CSS propio | Media neta, mediana, coste medio | "—" |
| Operaciones | D tabla | `TradeTable` + botón **Exportar CSV** | CSS propio | Operaciones cerradas con costes | "Aún no hay operaciones cerradas" |
| Gate 1 | A veredicto | `VerdictCard` (callout: NO CONCLUYENTE / NO PASA / PASA) | CSS propio | n, días, IC90 | "Faltan N operaciones y D días" |
| Gate 1 | C detalle | pestañas: Resumen · Mitades temporales · Sin top 3 · Contra azar | CSS propio + tabla accesible | IC90 y media neta por cartera | "Sin datos suficientes" |
| Control | A formulario | `LimitForm` (pérdida diaria −3 a −20 %, máx. posiciones, tamaño 0,5-3 %) + **Guardar límites**, con rangos duros e historial de cambios | CSS propio | Valores actuales (por defecto: −20 %, 8, 3 %) | — |
| Control | B zona de peligro | `DangerZone`: **Cerrar todo a mercado** (escribir CERRAR; muestra nº de posiciones y coste estimado) y **Reanudar** tras corte diario (muestra el motivo) | CSS propio | Estado y consecuencias | "No hay posiciones abiertas" |
| Control | C sesión | `TokenField` (cerrar sesión / renovar token) | CSS propio | Estado de la sesión | — |
| Acceso | A | `TokenGate` (un campo, mensaje de error claro) | CSS propio | Pide el token para escribir | — |
| En vivo | F qué estoy viendo | `LegendCard`: qué es cada cartera y con cuánto capital parte (10 SOL) | CSS propio | Laya · Reglas · Azar | — |
| En vivo | G embudo | `FunnelBar`: señales recibidas → descartadas por RugCheck / estafa / límite / `laya_lenta` / "saltar" → compradas | CSS propio | Conteo por motivo, hoy | "Sin señales todavía" |
| En vivo | H salud | `HealthCard`: RAM, swap, cola de señales, antigüedad del precio, latencia de Laya, estado del feed y del bot **por separado** | CSS propio | Semáforo con icono y texto | "Sin datos del bot" |
| Gate 1 | B progreso | `GateProgress`: "n/300 · día X/5" + frase en lenguaje llano + coste como % del bruto | CSS propio | Avance hacia el veredicto | "Aún sin operaciones" |
| Global | Glosario | `Term` (tooltip + enlace al panel Glosario) para Gate 1, IC90, slippage, trailing, stop, liquidez, rug/honeypot, RugCheck | CSS propio | Definición de una línea | — |

### 4.1 Componentes clave
| Componente | Librería | Variantes |
|---|---|---|
| `StatTile` | CSS propio | neutro · ganancia · pérdida (siempre con ▲/▼ y signo) |
| `EquityChart` | lightweight-charts 5.2.1 | 1 h · 24 h · todo; vista de tabla alternativa |
| `DecisionFeed` | CSS propio | comprar · mantener · vender · saltar · "descartada por estafa" |
| `VerdictCard` | CSS propio | no concluyente (ámbar) · no pasa (rojo + icono) · pasa (verde + icono) |
| `LiveDot` | CSS propio | en vivo · reconectando · caído |

## 5. Imágenes e ilustración contextual
Cero contenedores vacíos. Prompts para generar con Bloom/Canva (monocromos, trazo fino, fondo transparente, paleta de §2.1, sin personas ni logos de terceros):
- **En vivo · gráfica sin datos**: "Línea de tiempo horizontal en trazo fino ámbar sobre carbón, tres líneas discontinuas apenas esbozadas que parten de un punto único a la izquierda, sin ejes ni cifras, estilo plano técnico".
- **En vivo · sin posiciones**: "Tablero de calibres vacío en trazo fino: tres filas de rectángulos huecos con una pequeña moneda esquemática al lado, ámbar tenue sobre fondo oscuro, sin texto".
- **Decisiones · sin selección**: "Documento de auditoría esquemático con una lupa en ámbar, líneas de texto representadas por barras grises, composición asimétrica a la derecha".

## 6. Responsive y accesibilidad
- Breakpoints: ≥ 1100 px (3 columnas), 700-1099 px (2), < 700 px (1 columna: A → B desplazable → E feed → C → D → G → H). Verificar 375 px.
- Objetivo táctil ≥ 44 px; foco visible (`outline` ámbar 2 px); contraste AA; texto < 14 px nunca por debajo de `--text-3`.
- **Gráfica**: leyenda siempre presente, serie con etiqueta directa al final, tooltip con cruceta, **vista de tabla** equivalente y patrón de trazo (continua/discontinua) para no depender del color.
- `prefers-reduced-motion`: sin parpadeos ni destellos; el punto en vivo pasa a estático.
- SSE con indicador de reconexión visible y aviso `aria-live="polite"` para decisiones nuevas (limitado para no saturar lectores de pantalla).

## 7. Movimiento
- **Sin librería de animación** (presupuesto TRD: 0). CSS con la curva propia `--ease`.
- Solo donde informa: punto "en vivo" que pulsa 2 s, fila nueva del feed que entra con desplazamiento de 8 px, cifra que se resalta 600 ms al cambiar. Todo desactivado con `prefers-reduced-motion`.

## 8. Checklist de marca
- [ ] No parece plantilla genérica (carbón cálido + ámbar, sin navy/teal, sin gradiente morado, sin glassmorphism, sin Inter)
- [ ] Contraste verificado a 375 px en el navegador integrado
- [ ] Señales de confianza: banner PAPEL siempre visible, n y periodo junto a cada cifra, Gate "no concluyente" sin verde, costes visibles
- [ ] Ningún placeholder visible (todos los vacíos con ilustración y texto)
- [ ] PnL nunca solo por color (signo + ▲/▼)

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]

