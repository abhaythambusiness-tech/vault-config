---
type: doc-software
doc: ui-ux
proyecto: "Comanda Viva"
status: aprobado
date: 2026-11-04
origen: mixto
---

# 3 · UI/UX Design

> [!resumen] En cristiano
> Cómo se ve y se siente. **Esta primera entrega es solo la identidad** (§2, §5, §7) más la lista de pantallas (§3): colores, letras, el «detalle vivo» que hace especial el menú y qué fotos hacen falta. Hasta que la apruebes no se maqueta nada ni se eligen componentes (§4 queda para después de aprobar la identidad). Referencias elegidas por Haytham: **menú cliente = mezcla de los shots 2 y 5; caja y administración = mezcla de los 6 y 7**.

## 1. Principios de experiencia
- **El menú nunca miente**: lo que se ve pedible, se puede pedir. Si algo se agota mientras el cliente decide, se le dice con amabilidad y se le ofrece alternativa, no un error.
- **Pedir en 3 toques**: plato → añadir → enviar. Nota por plato opcional, nunca obligatoria.
- **Caja se mira de reojo**: en servicio, una mirada basta para saber qué mesa tiene comanda nueva y cuál espera cobro. Poco texto, estados por color y etiqueta.
- **Un solo cerebro, tres caras**: mismo carácter de marca en menú, caja y admin, pero densidad distinta (menú generoso, caja y admin funcionales).
- **Marca blanca**: nombre, logo y colores de tema por restaurante; el resto es de `Comanda Viva`.

## 2. Identidad visual
> [!resumen] Este apartado es la identidad del proyecto
> **Identidad aprobada por Haytham el 2026-11-04** (§2, §5 y §7; el resto del documento sigue en borrador). Aquí se rellena lo que pide `~/.claude/rules/identidad-y-dinamismo.md`. **Sin esta sección aprobada no se maqueta.** Al crear el repo se copia entera (§2, §5, §7) a `DESIGN-IDENTITY.md`. Revisado [[Registro de Identidades Visuales]] el 2026-11-04: no se repite ninguna combinación (ver aviso al final de la sección).

- **Idea visual central**: *«Esta carta está recién hecha y lo demuestra una hilera de yemas: cada plato que está a punto de acabarse muestra sus raciones como yemas y, cuando alguien lo pide, una desaparece.»* Desayuno de barrio, fresco y vivo, no carta fría de franquicia.
- **El producto como diseño**: la **disponibilidad real** (raciones calculadas del inventario) es el elemento gráfico: pegatina «Quedan 3» con yemas, plato «Agotado por hoy» que se apaga, y en caja el pulso de la comanda nueva. Las fotos son de los platos reales de la clienta, no de stock.
- **Composición firma**:
  - *Menú*: bloques de **color pastel por categoría** (cielo, rosa, mantequilla, menta) con la foto cenital del plato centrada, nombre en serif grande y **pegatina** de estado («Quedan 3», «Nuevo», «Lo más pedido»): la forma puede ir girada (−6°) pero el texto crítico va siempre recto y de 18 px mínimo. Rejilla de 2 columnas en móvil con un plato destacado a ancho completo cada 4.
  - *Caja y admin*: tarjetas de comanda **teñidas por estado** (nueva, en preparación, lista, por cobrar), panel de cuenta fijo a la derecha, navegación lateral compacta.
- **Anti-referencias**: carta digital fría de franquicia; app de delivery genérica (naranja + tarjetas iguales); plantilla gratuita de QR-menu; panel SaaS oscuro navy + teal.
- **2 referencias reales (qué se toma, no píxeles)**:
  1. Shot 2 *(Food Ordering UI, menú por QR)*: flujo **menú → detalle con extras y notas → resumen**; la mesa visible arriba («Mesa 9»); controles −/+ claros; botones de acción en pastilla.
  2. Shot 5 *(Mabel, brunch)*: **bloques de color por plato**, tipografía muy contundente, pegatinas de estado, fondo crema, botones con borde y sombra dura. Se toma el espíritu, no el «MABEL» gigante.
  3. *(caja/admin)* Shot 6 y 7: del 6, **panel de cuenta a la derecha con método de pago (efectivo/tarjeta/otro)** y tarjetas de pedido tintadas por estado; del 7, **navegación lateral de iconos**, **pestañas con contador** (Nuevo 1 · En cocina 2 · Listo 3 · Cobrado 38) y tarjetas limpias con «ver más».

| Elemento | Valor |
|---|---|
| Paleta (marca) | **Crema** `#FBF5E6` (fondo) · **Café** `#2A1C14` (texto y botón principal) · **Guindilla** `#C8322E` (acento único de marca: pegatinas «Quedan», alertas, precio destacado) · **Yema** `#F2B632` (las yemas y estados «pocos») · Café suave `#6B5647` (texto secundario) |
| Paleta (categorías, pasteles) | Cielo `#CFE8F7` · Rosa `#F3D6E3` · Mantequilla `#F6EDB0` · Menta `#CDEBDD` (fondo de tarjeta de plato; asignación por categoría, configurable en el tema) |
| Paleta (estados, solo caja/admin) | Nueva = rosa pastel, En preparación = mantequilla, Lista = cielo, Cobrada = menta; verde `#1F7A4D` solo para «cobrado/ok»; guindilla para anulado/agotado. El estado **nunca va solo en color**: lleva etiqueta de texto e icono |
| Contrastes medidos (WCAG) | Café/crema 15,2:1 · café/pasteles 12,2–13,9:1 · guindilla/crema 4,9:1 · blanco/guindilla 5,3:1 · café suave/crema 6,3:1 · café/yema 9,0:1 → todos ≥ AA. Guindilla sobre crema **no** vale para texto pequeño (<18 px negrita): usar solo en pegatina con texto blanco o en texto grande |
| Tipografías | **Fraunces** (display: nombres de plato, cifras grandes de «quedan», títulos; serif cálida con carácter, evoca carta de desayuno) + **Figtree** (UI y cuerpo; redonda, legible a pie de mesa, cifras tabulares con `font-variant-numeric: tabular-nums` en caja/admin). Autoalojadas con `@fontsource` (licencia OFL); verificar glifos `latin` y `tnum` al instalar. Se evita Inter/Geist/Space Grotesk por estar ya repetidas en el vault |
| Radio / sombras / espaciado | Menú: radio 20 px en tarjetas, pastilla completa en botones, **sombra dura** `0 3px 0 #2A1C14` en botones (borde 1,5 px café). Caja/admin: radio 16 px, sombra suave `0 1px 2px` y borde 1 px; sin sombra dura. Espaciado base 4/8 px; objetivo táctil ≥ 48 px en menú, ≥ 44 px en caja |
| Tono y voz | Tuteo cercano y breve, español de barrio sin caricatura: «Últimas 3», «Se acabó por hoy», «Tu pedido va para cocina», «¿Algo más?». Nada de «Procesando su solicitud». Errores con salida: «Se nos acabó el aguacate mientras pedías. ¿Te cambiamos a…?» |
| Referencias (Mobbin / Figma / Canva) | Dribbble: shots 2, 5, 6 y 7 (descargados solo como referencia interna, no se reutilizan). Mobbin: sin sesión, no usado (se declara) |

> [!riesgo] Aviso de registro
> `Scraper Infoproductores` ya usa **papel hueso + tinta + verde botella** y `TopLeads` usa un único acento naranja sobre tinta. Esta identidad se separa de ambas por: crema **cálida** con **pasteles por categoría**, serif Fraunces (no grotesca), acento **guindilla** (rojo, no naranja) y las **yemas** como elemento firma. Verde solo como estado semántico, nunca como marca. Si al verla en pantalla se parece a alguna, se cambia el acento antes de maquetar.

> [!riesgo] Cambio de dirección visual (2026-11-04, aprobado por Haytham)
> La paleta pastel, los círculos punteados, las yemas grandes y la sombra dura de esta sección se **sustituyen** por la dirección sobria: papel `#F6F2EA`, tinta `#1F1A17`, línea `#E4DCCF`, guindilla `#B5302B` solo para «Quedan N», radio 12 px, Figtree casi en todo y Fraunces solo en marca y títulos, dinamismo 1. Detalle y maqueta: `DESIGN-IDENTITY.md` y `public/maqueta.html` del repo. Lo que aquí contradiga eso queda superado.

### 2.1 Tokens primero
Orden obligatorio: marca → variables CSS → componentes → pantallas. Los tokens de marca (nombre, logo, pasteles, acento) viven en `restaurantes.tema` y se inyectan como variables en runtime (RF-13); `Monika Viva` es la primera instancia.
```css
:root {
  --crema: #FBF5E6;      --cafe: #2A1C14;        --cafe-suave: #6B5647;
  --acento: #C8322E;     --yema: #F2B632;
  --cat-1: #CFE8F7;      --cat-2: #F3D6E3;       --cat-3: #F6EDB0;   --cat-4: #CDEBDD;
  --ok: #1F7A4D;
  --radio-menu: 20px;    --radio-panel: 16px;
  --sombra-dura: 0 3px 0 var(--cafe);
  --ease-viva: cubic-bezier(.2, .9, .25, 1.15);
  --font-display: "Fraunces", Georgia, serif;
  --font-ui: "Figtree", system-ui, sans-serif;
}
/* Modo oscuro de caja: fuera de v1; los tokens ya permiten añadirlo después. */
```

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base (ver [[Biblioteca de Layouts]]) | Estados a diseñar |
|---|---|---|---|---|
| C1 Menú por categorías | Cliente | US-01, US-02 | lista con chips de categoría | cargando · plato agotado · «quedan N» · sin conexión · mesa no válida |
| C2 Detalle de plato + nota | Cliente | US-03 | lista-detalle (hoja inferior) | con/sin foto · agotado entre medias · nota larga |
| C3 Resumen y enviar pedido | Cliente | US-04 | resumen | vacío · enviando · error de stock (alternativa) · **«Enviado nº N» (pantalla propia)** · error de red con reintento |
| C4 Mi mesa (lo pedido) | Cliente | US-05 | lista | sin pedidos · varias tandas · estado de cada pedido (recibido/servido) · plato anulado por caja |
| C5 QR no válido | Cliente | US-01 | mensaje | token inválido · mesa cerrada · teléfono del local |
| K1 Comandas en vivo | Caja | US-13 | tablero con pestañas contador | vacío · nueva «sin ver» (sonido) · sin conexión en vivo |
| K2 Cuenta de mesa y cobro | Caja | US-14, US-15, US-16 | lista-detalle (panel derecho) | cuenta abierta · anular línea + deshacer · dividir iguales · entrega/cambio · mover a mesa · cobrada |
| K3 Mesas | Caja | US-14 | rejilla de mesas | libre · con comanda · pendiente de cobro |
| K4 Cobradas del día | Caja | US-15 | lista | vacío · filtro por método |
| A1 Panel financiero | Dueña | US-17, US-18 | dashboard | sin datos · sin costes cargados · rango de fechas |
| A2 Inventario | Dueña | US-06, US-11, US-12, US-21 | tabla + ajuste rápido | vacío (con oferta de plantilla de desayunos) · bajo mínimo · movimiento registrado · recuento · merma |
| A3 Platos y recetas | Dueña | US-07, US-08, US-09, US-10, US-19, US-21 | lista-detalle | plato sin receta («sin control») · «Oculto: faltan X» + «Añadir stock» · raciones calculadas · medidas caseras |
| A4 Mesas y QR | Dueña | US-19 | lista + vista de impresión | regenerar QR · imprimir |
| A5 Acceso | Dueña | US-20 | formulario | error de credenciales · sesión caducada |
| A6 Ajustes de marca y umbral | Dueña | US-19, RF-13 | formulario | vista previa del tema |

## 4. Slots por pantalla
Componentes según [[Paleta de Componentes]] (aprobada 2026-11-04). «Propio» = hecho a mano con los tokens de §2.1.
| Pantalla | Slot (zona) | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|---|
| C1 Menú | cabecera | Logo + «Mesa N» + tira `marquee` | @magicui | Nombre de restaurante, mesa, frases del día | — |
| C1 Menú | chips | Categorías con icono SVG propio | propio + lucide | Categorías activas | «Hoy no hay carta disponible» |
| C1 Menú | rejilla | Tarjeta de plato pastel + pegatina + hilera de yemas | propio + `motion` | Foto, nombre, precio, «Quedan N» | Categoría sin platos pedibles |
| C2 Detalle | hoja inferior | `drawer` + nota + alérgenos + yemas | @shadcn (vaul) | Descripción, alérgenos, nota, cantidad | Sin foto: monograma de marca |
| C3 Resumen | cuerpo | Ticket dentado + stepper −/+ | propio | Líneas, notas, total | «Aún no has añadido nada» |
| C4 Mi mesa | lista | Líneas por tanda con estado | propio + `sonner` | Pedido de la mesa y avisos de caja | «Todavía no has pedido nada» |
| K1 Comandas | cabecera | `tabs` con contador (Nueva · Preparación · Lista · Cobrada) | @shadcn | Contadores por estado | «Sin comandas ahora mismo» |
| K1 Comandas | tablero | Tarjeta de comanda tintada por estado | propio + `motion` | Mesa, líneas, notas, hora | Ilustración SVG propia |
| K2 Cuenta | panel derecho | Cuenta + `radio-cards` de método de pago | @uiarc | Líneas, total, método | Mesa sin cuenta abierta |
| K3 Mesas | rejilla | Ficha de mesa (libre/comanda/por cobrar) | propio | Estado y total de cada mesa | Sin mesas: ir a A4 |
| A1 Finanzas | KPI | `stat-card-area-01` | @bklit | Ventas, ticket medio, comandas | «Sin ventas en este rango» |
| A1 Finanzas | gráficas | `bar-chart`, `area-chart` | @bklit | Ventas por hora/día, ranking | Sin datos |
| A2 Inventario | tabla | `table` + `sparkline` | @shadcn + @bklit | Stock, mínimo, consumo 7 días | «Carga tu primer ingrediente» |
| A3 Platos | detalle | Receta + vista previa de yemas | propio | Raciones calculadas | Plato «sin control» |
| A4 Mesas y QR | impresión | Hoja QR A6 | propio + `qrcode` | QR y nombre de mesa | Sin mesas |
| A5/A6 | formulario | `form`, `input`, `switch` | @shadcn | Credenciales / tema y umbral | — |

## 4.1 Componentes clave
| Componente | Librería | Variantes |
|---|---|---|
| Hilera de yemas | propio + `motion` | N (≤ umbral), apagando, agotado, reducida (`prefers-reduced-motion`) |
| Pegatina de estado | propio | Quedan N · Nuevo · Lo más pedido · Agotado |
| Tarjeta de plato | propio | Normal, destacada (ancho completo), agotada |
| Tarjeta de comanda | propio | Nueva (rosa) · Preparación (mantequilla) · Lista (cielo) · Cobrada (menta) · Anulada |
| Ficha de mesa | propio | Libre · Con comanda · Por cobrar |
| Hoja de detalle | `@shadcn/drawer` | Con/sin foto, con nota |

## 5. Imágenes e ilustración contextual
Cero contenedores vacíos **y cero imágenes inventadas en silencio**: por cada imagen que falte se pregunta a Haytham qué origen usar.
- **Estilo de imagen** de la marca: foto real **cenital (90°)** del plato servido sobre cerámica, luz natural lateral suave, plato recortado o sobre fondo liso del pastel de su categoría, colores naturales. Para estados vacíos y categorías: ilustración **SVG propia** de trazo simple (taza, huevo, tostada) con los tokens de marca.
- **Bloque de estilo para Gemini** (se pega entero en cada prompt, sin retocar; solo si Haytham elige esa vía para un hueco):
  ```
  Overhead 90-degree food photograph of a single plated breakfast dish on a handmade ceramic plate,
  soft natural window light from the left, gentle realistic shadow, appetizing true-to-life colours,
  shallow warm tones, clean solid pastel background (#CFE8F7), centred composition with generous margin,
  no hands, no cutlery clutter, no text, no logos, no watermark, not illustrated, not 3D-rendered.
  ```
- Prohibido en imagen: texto dentro, estética genérica de IA, fotos fotorrealistas de personas ficticias, stock que no sea de la carta real, y lo que diga la anti-referencia.

| Vista / hueco | Qué imagen (tamaño, formato) | Origen decidido por Haytham | Estado |
|---|---|---|---|
| Logo del restaurante (cabecera menú, caja, login) | Vectorial SVG, fondo transparente | **Pendiente de decidir** (pedir a la clienta / SVG propio) | pendiente |
| Foto de cada plato (C1, C2, caja opcional) | Cenital, WebP ≤ 80 kB, 800×800, una por plato | **Pendiente de decidir** (fotos reales de la clienta / prompt Gemini con el bloque de arriba) | pendiente |
| Iconos de categoría (chips C1) | SVG propio, trazo 1,5 px | **Pendiente de decidir** (SVG propio propuesto) | pendiente |
| Estados vacíos y error (C4, C5, K1, A2) | SVG propio con tokens de marca | **Pendiente de decidir** (SVG propio propuesto) | pendiente |
| QR de mesa (A4) | SVG generado con `qrcode`, imprimible A6 | Generado por código | n/a |
| Cabecera/ambiente del local (opcional) | Foto real horizontal | **Pendiente de decidir** (foto real de la clienta o prescindir) | pendiente |

## 6. Responsive y accesibilidad
- **Menú cliente**: móvil primero 375 px; tablet 768 px (3 columnas). **Caja**: tablet y portátil, 768 y 1280 px; en 375 px solo consulta. **Admin**: 1280 px y adaptado a 768.
- Objetivo táctil ≥ 48 px (menú) y ≥ 44 px (caja/admin); contraste WCAG AA medido (ver §2); foco visible de 2 px; el estado nunca solo por color; `prefers-reduced-motion` respetado; tamaño de letra del sistema respetado (rem). Alérgenos visibles en el detalle de plato.
- Caja: botón «Activar sonido» al abrir (los navegadores bloquean audio sin gesto).
- **Reglas de la simulación de clientes** (2026-11-04): texto mínimo 18 px en el menú; texto crítico («Quedan N», «Se acabó», precio, estado del pedido) siempre recto, nunca girado ni sobre foto; «Quedan N» siempre en texto junto a las yemas, que son refuerzo y no el único aviso; plato agotado mientras se mira = gris con «Se acabó», sin saltos de lista; página ligera, texto primero y fotos diferidas; contador de la nota (140) visible desde el primer carácter; C3 con línea fija «Pagas al final, en caja» (por confirmar con la clienta); C5 con teléfono del local; textos del panel en frases sencillas (sin «ticket medio»/«margen» a secas); caja: comandas por antigüedad con punto «sin ver», botones de motivo grandes y «Deshacer» 10 s.

## 7. Movimiento y dinamismo
- **Nivel**: **2 (dinámico) en el menú cliente**, **1 (sutil) en caja y admin**. El menú es la cara que provoca el efecto de escasez; caja y admin deben ser calmados para no cansar.
- **Cómo evita parecer estático sin animar**: bloques pastel de distinto color por categoría, escala dramática del serif en nombres y cifras, pegatinas giradas que rompen la rejilla, un plato destacado a ancho completo cada cuatro.
- **Curva propia del proyecto**: `cubic-bezier(.2, .9, .25, 1.15)` (`--ease-viva`, ligero «rebote» de entrada), duraciones 180–320 ms, reutilizada en todo el proyecto.
- **Elemento vivo firma (máx. uno por pantalla)**: **la hilera de yemas**. En C1/C2, un plato con `N ≤ umbral` muestra N yemas; cuando la disponibilidad baja, una yema se apaga con un pequeño «pop». En K1 el elemento vivo es el **pulso de la comanda nueva** (tarjeta que entra con la curva propia y brilla una vez).
- **Dónde anima, con qué motor**: **Motion** (único motor, el del [[2 - TRD]]): entrada escalonada de tarjetas del menú, hoja inferior de detalle, pop de yemas, entrada de comanda en caja. Solo `transform` y `opacity`. Con `prefers-reduced-motion`: sin rebote, solo fundido; las yemas cambian sin animación.
- Skills previstas: `web-animation-skills:accessible-animation` primero, luego `motion-framer-choreographer`.

## 8. Checklist de marca
- [ ] Prueba del intercambio: cambiando logo y textos no vale para otro negocio
- [ ] Prueba de lejos: sin logo, en 3 segundos se reconoce por forma, color y ritmo
- [ ] No repite combinación de [[Registro de Identidades Visuales]] (y se ha añadido la fila)
- [ ] No parece plantilla genérica
- [x] Contraste verificado (cifras en §2; repetir con el render final)
- [ ] Señales de confianza presentes

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
