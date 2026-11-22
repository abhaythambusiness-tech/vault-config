---
type: doc-software
doc: ui-ux
proyecto: "Scraper Infoproductores"
status: aprobado
date: 2026-11-01
origen: mixto
---

# 3 · UI/UX Design

> [!resumen]
> Cómo se ve y se siente. Pasa antes por el gate de `rules/diseno.md` (identidad, anti-genérico, contraste, confianza). Cada pantalla traza a una historia del [[1 - PRD]].

## 1. Principios de experiencia
- El coste siempre se ve **antes** de gastar («Búsqueda: 2 créditos») y el saldo está siempre visible.
- Resultados sin contacto; el contacto, borroso hasta desbloquear. Lo ya desbloqueado nunca se vuelve a cobrar y se marca.
- Toda facturación lleva la etiqueta «estimada» y un enlace a cómo se calcula.
- Sin créditos: mensaje claro con el paso siguiente (plan o esperar), nunca un muro mudo.
- Datos con fecha de captura visible.

## 2. Identidad visual
> [!resumen] Este apartado es la identidad del proyecto
> Aquí se rellena lo que pide `~/.claude/rules/identidad-y-dinamismo.md` (plantilla suelta: [[Plantilla - Identidad de Proyecto]]). **Sin esta sección aprobada no se maqueta.** Al crear el repo se copia entera (§2, §5, §7) a `DESIGN-IDENTITY.md` en su raíz. Antes de decidir, mirar [[Registro de Identidades Visuales]] y no repetir combinación.

> [!resumen] Identidad APROBADA por Haytham el 2026-11-01 (§2, §5 y §7). Logo: wordmark SVG propio; avatares: iniciales, sin foto (propuestas aceptadas con la identidad).

- **Idea visual central**: «Esta marca es **un libro mayor que responde al instante**, y lo demuestra con el buscador real en la portada: escribes, las fichas entran en fila y tu saldo de créditos baja con un tic, como un apunte contable». Precisión + rapidez + fiabilidad = contabilidad bien llevada, no cohete.
- **El producto como diseño**: la búsqueda de la portada funciona con fichas reales y públicas (contacto borroso) y el contador de créditos es un elemento visual protagonista.
- **Composición firma**: rejilla de columnas finas con líneas de libro mayor; cifras y etiquetas en monoespaciada alineadas a la derecha; una columna estrecha de «margen» con el saldo de créditos siempre visible; mucho aire.
- **Anti-referencias**: guru chillón (cohetes, dólares, rojo/amarillo), Excel gris de CRM antiguo, plantilla SaaS morada. **Referencias**: Linear (jerarquía clara con pocas cosas alineadas) y Vercel (rejilla y tono técnico); se toma el criterio, no los píxeles.
- **Distinta de las ya registradas**: claro y cálido (las otras son oscuras), sin lima ni azul NeoZeler ni azul noche + ámbar.

| Elemento | Valor |
|---|---|
| Paleta | Papel hueso `#F4F1EA` (fondo), tinta `#15171C` (texto), línea `#D9D4C7`, acento **verde botella** `#0F5B4A` (acciones y saldo), aviso ocre `#B7791F` (créditos bajos), error `#B3261E`. Escala de 8 tonos del verde y de los neutros cálidos a definir en tokens |
| Tipografías | **Hanken Grotesk** (titulares y texto: nítida, neutra, sin parecer Inter) + **JetBrains Mono** (cifras, créditos, etiquetas de dato: el motivo es el aire de libro mayor, columnas alineables). Autoalojadas |
| Radio / sombras / espaciado | Radio 4 px; sin sombras, solo líneas finas de 1 px; espaciado en múltiplos de 4 y 8 |
| Tono y voz | Seco, claro y exacto. «Búsqueda: 2 créditos.» «Quedan 38.» Sin exclamaciones ni promesas de dinero |
| Referencias (Mobbin / Figma / Canva) | Mobbin sin sesión: no disponible. Referencias de [[Biblioteca de Referencias Premium]]: Linear y Vercel |

### 2.1 Tokens primero
Orden obligatorio: marca (Bloom o la existente) → variables CSS (`:root` + oscuro) → componentes → pantallas. No se maqueta ninguna pantalla sin tokens definidos.
Solo tema claro en v1 (el «libro mayor» es papel hueso; un modo oscuro duplicaría la verificación sin aportar a la marca). Contrastes calculados a mano sobre `--surface`; se re-miden con herramienta al maquetar.
```css
:root {
  /* color */
  --surface: #F4F1EA;      /* fondo papel hueso */
  --surface-2: #ECE8DD;    /* filas alternas, zonas hundidas */
  --text: #15171C;         /* tinta, ~16:1 */
  --text-muted: #5B5F68;   /* secundario, ~5.8:1 */
  --line: #D9D4C7;         /* líneas de libro mayor; solo decorativa, nunca texto */
  --brand: #0F5B4A;        /* verde botella: acciones y saldo, ~7:1 */
  --brand-hover: #0B4739;
  --brand-ink: #F4F1EA;    /* texto sobre --brand */
  --warn: #B7791F;         /* créditos bajos: solo icono, borde o texto grande (~3.2:1) */
  --warn-text: #8A5A12;    /* ocre para texto pequeño, ~5.2:1 */
  --danger: #B3261E;       /* error, ~5.8:1 */
  /* tipografía */
  --font-sans: "Hanken Grotesk", system-ui, sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, monospace;
  /* forma */
  --radius: 4px;
  --border: 1px solid var(--line);
  /* espaciado: múltiplos de 4 */
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px; --space-12: 48px; --space-16: 64px;
  /* movimiento */
  --ease: cubic-bezier(0.2, 0.8, 0.2, 1);
  --dur-fast: 160ms; --dur: 240ms; --stagger: 30ms;
}
@media (prefers-reduced-motion: reduce) {
  :root { --dur-fast: 0ms; --dur: 0ms; --stagger: 0ms; }
}
```
Escala de 8 tonos del verde y de los neutros: se genera al instalar shadcn (variables `--primary` y `--muted` apuntan a estos tokens); los tonos intermedios no se inventan a ojo.

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base (ver [[Biblioteca de Layouts]]) | Estados a diseñar |
|---|---|---|---|---|
| Landing con buscador en vivo | Visitante | US-09, US-01 | hero con producto real | vacío · cargando · error · éxito |
| Registro / entrada | Visitante | US-09 | formulario centrado (Google + enlace) | cargando · enlace enviado · error |
| Búsqueda y resultados | Comprador | US-01 | lista con filtros laterales | vacío · cargando · sin créditos · error · éxito |
| Ficha de infoproductor | Comprador | US-02, US-03 | lista-detalle | contacto bloqueado · desbloqueado · sin créditos · error |
| Mis contactos (lista) | Comprador | US-03, US-05 | tabla con exportación | vacío · éxito |
| Planes y créditos | Comprador | US-04 | planes en columnas + historial del libro mayor | gratis · pago · impago |
| Baja de ficha (pública) | Infoproductor | US-08 | formulario simple | enviado · error |
| Admin: fuentes y bajas | Admin | US-07, US-08 | dashboard | cargando · error · éxito |

US-06 (alertas de lanzamientos, Could): fuera de v1, sin pantalla.

## 4. Slots por pantalla
Cada zona de cada pantalla con su componente asignado. Candidatos desde [[Catalogo de Componentes]] y, si falta, `search_items_in_registries` (shadcn-registries). Referencias visuales de Mobbin cuando haya sesión.
| Pantalla | Slot (zona) | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|---|
| Landing | Cabecera | Wordmark SVG + enlaces + «Entrar» + saldo (si hay sesión) | propio | Marca, saldo de créditos | Visitante: «Plan gratis: N créditos» |
| Landing | Buscador en vivo | `command` base con caja de búsqueda y filtros (nicho, ciudad) | @shadcn | Consulta del visitante | Ejemplo precargado con 3 fichas públicas |
| Landing | Resultados de ejemplo | Fila de ficha + `sparkline` | @bklit | Nombre público, red, nicho, curva de lanzamientos (sin contacto) | «Sin resultados: prueba otro nicho» |
| Landing | Cómo se calcula | Texto + enlace (método de «estimada») | propio | `metodo_estimacion` | n/a |
| Registro | Formulario | Botón Google + campo de correo | @shadcn | Estado del enlace | Error con paso siguiente |
| Búsqueda | Filtros laterales | Inputs, selects, rango de facturación | @shadcn | Nicho, ciudad, plataforma, facturación estimada | Filtros vacíos = todo |
| Búsqueda | Coste de la búsqueda | Etiqueta mono junto al botón: «Búsqueda: 2 créditos» | propio | Coste y saldo | Sin créditos: mensaje con plan |
| Búsqueda | Tabla de resultados | `data-table` + `sparkline` en columna «lanzamientos» | @shadcn + @bklit | Nombre, red, nicho, ciudad (o «sin ciudad»), facturación estimada, fecha de captura | «Nada con estos filtros» + sugerir quitar uno |
| Ficha | Cabecera de ficha | Iniciales en círculo + redes + etiqueta de confianza de ubicación | propio | Datos públicos | n/a |
| Ficha | Historial | `composed-chart` (lanzamientos + anuncios) | @bklit | Lanzamientos pasados, anuncios activos | «Sin lanzamientos registrados» |
| Ficha | Contacto | Bloque borroso + botón «Desbloquear: 5 créditos» | propio | Email/teléfono tras desbloqueo | Sin créditos: mensaje con plan |
| Mis contactos | Tabla | Tabla base + botón exportar CSV | @shadcn | Contactos desbloqueados, fecha de desbloqueo | «Aún no has desbloqueado ninguno» |
| Planes y créditos | Planes | Tarjetas de plan | @shadcn | Créditos por mes, precio | Plan gratis marcado |
| Planes y créditos | Saldo en el tiempo | `stat-card-line-01` | @bklit | Saldo y movimientos | «Sin movimientos todavía» |
| Planes y créditos | Libro de movimientos | Tabla mono alineada a la derecha | @shadcn | Apuntes de `credit_ledger` | Solo apunte de créditos iniciales |
| Baja | Formulario | Campos: perfil, motivo, correo de contacto | @shadcn | Estado de la solicitud | Confirmación enviada |
| Admin | Salud de fuentes | `heatmap-chart` + `sparkline` | @bklit | Recogidas por fuente y día, fallos | «Sin recogidas aún» |
| Admin | Bajas pendientes | Tabla base | @shadcn | Cola de bajas | «Ninguna pendiente» |

Las cantidades de créditos del ejemplo («2», «5») son marcadores: se fijan en el Backend Schema tras la preventa.

## 4.1 Componentes clave
| Componente | Librería (shadcn / magicui…) | Variantes |
|---|---|---|
| Botón | @shadcn button | primario (verde), secundario (línea), fantasma, peligro; con coste en mono: «Desbloquear · 5» |
| Indicador de saldo | propio (CSS) | normal · bajo (ocre) · cero; «tic» de 160 ms al bajar |
| Ficha de resultado | propio + `sparkline` | normal · ya desbloqueada (marca verde) · sin ubicación |
| Etiqueta «estimada» | propio | siempre junto a cualquier cifra de facturación, con enlace al método |
| Campo de contacto | propio | bloqueado (borroso, no seleccionable) · desbloqueado · copiado |
| Tabla | @shadcn table / data-table | densa, cifras mono a la derecha |
| Gráficas | @bklit sparkline, composed-chart, stat-card-line-01, heatmap-chart | tamaño pequeño; sin leyendas decorativas |
| Aviso sin créditos | propio | en línea (búsqueda) · modal (desbloqueo) |

## 5. Imágenes e ilustración contextual
Cero contenedores vacíos **y cero imágenes inventadas en silencio**: por cada imagen que falte se pregunta a Haytham qué origen usar (flujo completo en la regla de identidad §3).
- **Estilo de imagen** de la marca: ninguna foto ni ilustración de relleno; el producto (fichas, cifras, líneas de tiempo) hace de imagen.
- **Bloque de estilo para Gemini**: no aplica en v1.
- Prohibido en imagen: texto dentro, estética genérica de IA, cohetes, dólares, gurús.

| Vista / hueco | Qué imagen (tamaño, formato) | Origen decidido por Haytham | Estado |
|---|---|---|---|
| Logo / marca | Wordmark tipográfico con un glifo de línea; SVG | SVG propio (decidido 2026-11-01) | pendiente de dibujar (`svg-skill`) |
| Avatar de infoproductor | Iniciales en círculo de línea fina | Sin foto, por RGPD (decidido 2026-11-01) | n/a |
| Portada | Ninguna: buscador real en vivo | n/a | n/a |

## 6. Responsive y accesibilidad
- **Breakpoints**: 375 px (móvil), 768 px (tableta), 1280 px (escritorio). Móvil primero; la rejilla de libro mayor pasa de 12 columnas a 4.
- **Móvil**: la columna de saldo pasa a barra fija superior (saldo siempre visible); filtros en un panel desplegable; la tabla de resultados se convierte en lista de fichas (nombre, nicho, facturación estimada, curva).
- **Táctil**: objetivos ≥ 44 px; el botón «Desbloquear» nunca pegado a otro botón (evita doble gasto por error).
- **Contraste**: WCAG AA; texto pequeño solo con `--text`, `--text-muted`, `--brand`, `--danger` o `--warn-text`; `--warn` y `--line` nunca como texto.
- **Foco visible**: anillo de 2 px en `--brand` con desfase de 2 px, en todos los controles.
- **Lectores de pantalla**: el saldo anuncia el cambio con `aria-live="polite"`; el contacto borroso lleva `aria-label="Contacto bloqueado"`; las gráficas pequeñas llevan texto alternativo con el dato («Lanzamientos: 4 en 12 meses»).
- **`prefers-reduced-motion`**: sin «tic» ni entrada escalonada; el cambio de saldo es instantáneo.
- **Fuentes**: autoalojadas con `font-display: swap`, solo los pesos usados.

## 7. Movimiento y dinamismo
- **Nivel**: 1 (sutil). Marca de precisión y rapidez: el movimiento es breve y con sentido, nunca decorativo.
- **Cómo evita parecer estático sin animar**: rejilla de libro mayor, contraste entre titular grande y cifras mono pequeñas, columna de saldo asimétrica.
- **Curva propia**: `cubic-bezier(0.2, 0.8, 0.2, 1)`, 160-240 ms. **Elemento vivo firma**: el saldo de créditos baja con un «tic» al gastar y las fichas entran en fila escalonada (30 ms entre una y otra).
- Motor: solo CSS (transiciones y `@starting-style`), sin librería de animación (presupuesto del [[2 - TRD]]: 0 motores). Respeta `prefers-reduced-motion`.

## 8. Checklist de marca
- [ ] Prueba del intercambio: cambiando logo y textos no vale para otro negocio
- [ ] Prueba de lejos: sin logo, en 3 segundos se reconoce por forma, color y ritmo
- [ ] No repite combinación de [[Registro de Identidades Visuales]] (y se ha añadido la fila)
- [ ] No parece plantilla genérica
- [ ] Contraste verificado
- [ ] Señales de confianza presentes

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
