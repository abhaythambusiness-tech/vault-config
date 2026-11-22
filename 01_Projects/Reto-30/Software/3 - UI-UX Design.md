---
type: doc-software
doc: ui-ux
proyecto: "Reto 30 (app real)"
status: aprobado
date: 2026-10-14
origen: mixto
---
# 3 · UI/UX Design — RETO 30 (app real)

> [!resumen]
> Cómo se ve y se siente la app. La dirección sale del **logo real** de RETO 30 (negro, gris carbón, verde lima, rotulación itálica pesada y una barra de progreso en segmentos), no de un estilo genérico. Cada pantalla traza a una historia del [[1 - PRD]]. Gate de [[Web Interface Guidelines]] y `rules/diseno.md` aplicado: `ui-ux-pro-max` ejecutado (sus resultados, Sketch y Neumorphism, no encajan con una marca atlética y se descartaron), contraste calculado, ningún MCP de componentes ejecutado todavía (se ejecutan al maquetar).

> [!riesgo]
> **Decisión de dirección visual (a aprobar).** La demo actual usa papel cálido con tinta y naranja de seguridad; la nota de marca [[01_Projects/Reto-30/05 - Identidad Visual y Branding|05]] y el logo real usan negro mate con lima. Este documento sigue **el logo y la nota 05**. Si prefieres mantener el estilo de la demo, hay que reescribir §2 antes de aprobar.

> [!resumen]
> **Alcance de la v1 (2026-10-17)**: pantallas y componentes nuevos por [[Cambios de diseno - Ranking, comodines, sorteo y Duo]]: ranking por nivel, comodines visibles, cronómetro de ejercicio, reto extra, pestaña de pareja del plan Dúo y panel admin ampliado. Lo nuevo va marcado. El nivel «Fácil» pasa a llamarse **Básico**. Esta revisión **no cambia** la identidad visual (§2); solo añade piezas con los mismos tokens.

## 1. Principios de experiencia

1. **Dos minutos al día**: abrir la app y ver el reto de hoy a un toque; nada de menús intermedios.
2. **El progreso se ve y se siente**: una sola imagen de marca, la barra de 30 segmentos, que se llena al completar cada día.
3. **Seriedad atlética sin infantilizar**: tono directo y de tú, sin emojis en titulares ni frases de coach ("¡tú puedes!").
4. **Una acción primaria por pantalla**: "Completar el día" en el reto, "Reservar mi plaza" en la portada.
5. **Móvil primero**: se diseña a 375 px y se amplía; los socios lo usan en el teléfono.

## 2. Identidad visual

Solo modo oscuro (`color-scheme: dark`): es la marca. Contrastes calculados con la fórmula WCAG.

| Elemento | Valor |
|---|---|
| Fondo | `#0C0D0E` (matte black) |
| Superficie / tarjetas | `#181A1D` (carbon grey) |
| Separador | `#262A30` (solo divisores decorativos, 1,3:1) |
| Borde de campos y botones secundarios | `#6B7280` (4,0:1, cumple el mínimo de 3:1 para controles) |
| Acento (acción, progreso, racha) | `#CCFF00` (lima eléctrico) |
| Texto de titulares y cifras | `#FFFFFF` (19,5:1 sobre fondo) |
| Texto secundario | `#94A3B8` (7,6:1 sobre fondo, 6,8:1 sobre tarjeta) |
| Texto sobre lima (botones) | `#0C0D0E` (16,6:1) |
| Nivel Básico | `#5EA6FF` (azul acero, 7,0:1 sobre tarjeta) |
| Nivel Medio | `#FFB020` (ámbar, 9,5:1 sobre tarjeta) |
| Nivel Avanzado | `#FF5A5F` (rojo, 5,7:1 sobre tarjeta) |
| Tipografía | **Barlow Condensed** (800, itálica) para titulares y números; **Barlow** (400/600) para cuerpo. Autoalojadas en WOFF2, sin CDN de Google (RGPD). Licencia OFL: **verificar al descargar** |
| Forma | Esquinas cortadas (chaflán 8 px con `clip-path`) en tarjetas y botones, eco del escudo del logo; radio 6 px en campos. **Sin squircle** |
| Movimiento | Curva propia `cubic-bezier(0.16, 1, 0.3, 1)` en todo el proyecto; un solo motor (`motion`) |
| Tono y voz | De tú, frases cortas, verbos de acción; sin "revolucionario", sin "empoderar", sin emojis en títulos |
| Referencias | Logo `99_Assets/reto-30/LogoReto30-sinfondo.jpeg`; Mobbin sin sesión: **no disponible**, sin referencias de ese origen |

**Regla de color**: el lima solo marca *acción, progreso y racha*. Los niveles nunca usan verde (chocaría con el lima): se distinguen por color y por número de rayos (⚡ 1, 2 o 3 como glifo de marca, no emoji).

### 2.1 Tokens primero

Orden obligatorio: marca → variables CSS → componentes → pantallas. Reemplazan los tokens "papel y naranja" de `src/app/globals.css` de la demo.

```css
:root {
  color-scheme: dark;
  --background: #0c0d0e;
  --card: #181a1d;
  --divider: #262a30;
  --control-border: #6b7280;
  --accent: #ccff00;
  --on-accent: #0c0d0e;
  --foreground: #ffffff;
  --muted-foreground: #94a3b8;
  --level-basico: #5ea6ff;
  --level-medio: #ffb020;
  --level-avanzado: #ff5a5f;
  --radius: 6px;
  --chamfer: 8px;
  --ease-brand: cubic-bezier(0.16, 1, 0.3, 1);
  --font-display: "Barlow Condensed", system-ui, sans-serif;
  --font-sans: "Barlow", system-ui, sans-serif;
}
```

Escala de espaciado 4/8 px. Todas las cifras con `tabular-nums`.

### 2.2 Detalle firma: la barra de 30 segmentos

Sale del contador de segmentos del logo. Se usa como indicador de progreso en el panel (30 segmentos grandes) y en el encabezado del reto (versión mini). Cada segmento tiene estado: vacío (borde `--divider`), actual (borde lima parpadeante solo si hay movimiento permitido) y completado (relleno lima). Es el elemento propio de la marca; ningún otro efecto decorativo compite con él.


> [!resumen]
> **Navegación móvil (2026-10-19)**: tras revisar [[Referencia de interfaz - openGym]], la navegación del participante pasa a una **barra inferior** (Inicio · Ranking · «Hoy» central · Insignias o Pareja · Cuenta) y el panel gana cuatro cifras 2×2. La marca y los tokens no cambian. Se oculta la barra en el reto del día.

## 3. Inventario de pantallas

| # | Pantalla (ruta) | Rol | Historia (US) | Layout base (ver [[Biblioteca de Layouts]]) | Estados a diseñar |
|---|---|---|---|---|---|
| 1 | Portada (`/`) | Visitante | US-10 | Landing de captación | cargando · error de red |
| 2 | Acceso (`/entrar`) | Visitante | US-01 | Asistente por pasos (1 paso) | correo inválido · enlace enviado · enlace caducado · error |
| 3 | Empezar (`/empezar`) | Participante | US-01, US-02, US-10, US-17 | Asistente por pasos (nombre y consentimiento → frecuencia y nivel → **plan: individual o Dúo** → código de pareja si es Dúo → estado de la plaza) | plaza pendiente · activa · cancelada · código de pareja inválido o ya usado · error |
| 4 | Panel (`/reto`) | Participante | US-03, US-06, US-11, US-12 | Dashboard adaptado (barra de segmentos + calendario + **comodines**) | día 1 vacío · en curso · completado · sin conexión · racha salvada con comodín |
| 5 | Reto del día (`/reto/[dia]`) | Participante | US-04, US-05, US-14, US-15 | Ficha de entidad (reto + ejercicio + **cronómetro y reto extra**) | bloqueado · actual · ya completado · sin ejercicio cargado · sin vídeo · cronómetro en ejercicio / descanso / terminado |
| 6 | Felicitación (superposición) | Participante | US-05, US-06 | Superposición sobre el reto | día normal · día especial con insignia · día 30 |
| 7 | Insignias (`/reto/insignias`) | Participante | US-06 | Ficha de entidad (rejilla de 4 insignias) | sin insignias · parcial · completo |
| 8 | Diploma (`/diploma`) | Participante | US-07 | Ficha de entidad | bloqueado (faltan días) · listo · error al generar |
| 9 | Cuenta (`/cuenta`) | Participante | US-02, US-13, US-16 | Ficha de entidad | dar o retirar consentimiento · **ocultar mi nombre en el ranking** · **dar de baja el correo diario** · confirmar borrado de cuenta. (Sin cambio de nivel: el nivel se muestra pero no se edita) |
| 10 | Ejercicios admin (`/admin/ejercicios`) | Admin | US-08, US-15, US-18 | Lista + detalle | lista vacía · editando · guardado · error de subida · **sin vídeo** |
| 11 | Gerencia (`/gerencia`) | Gerencia | US-09 | Dashboard | sin inscritos · con datos |
| 12 | Sesión caducada / no encontrada | Todos | US-01 | Mensaje centrado | — |
| 13 | Participantes admin (`/admin/participantes`) | Admin | US-10, US-11, US-17 | Lista + detalle | sin participantes · pendientes primero · plaza activada · plaza cancelada · **Dúo: activar o cancelar a la pareja entera** · error |
| 14 | Ranking (`/reto/ranking`) | Participante | US-13 | Lista | sin datos aún · mi puesto resaltado · yo oculto · sin conexión |
| 15 | Pareja (`/reto/pareja`) | Participante del plan Dúo | US-17 | Ficha de entidad | sin pareja todavía (muestra mi código) · pareja unida · pareja ha abandonado · racha conjunta parada |
| 16 | Reto extra (`/admin/extras`) | Admin | US-14 | Lista + detalle | 10 extras sin cargar · editando · guardado |

Trazabilidad: toda historia del PRD (US-01 a US-18) aparece en al menos una pantalla. US-16 (correo diario) vive en el correo y en `/cuenta`; el diseño del correo está en §4.2.

## 4. Slots por pantalla

Candidatos de [[Catalogo de Componentes]]; a confirmar con `search_items_in_registries` al maquetar. **Cambio respecto al TRD**: sin squircle ni Arc UI (la marca es angular y Arc choca con los tokens), así que los registries previstos quedan en Componentry y Skiper UI (ver nota al final).

**Portada** (US-10)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A cabecera | logo + enlace "Acceder" + botón "Reservar mi plaza" | shadcn Button | marca y acción primaria | — |
| B hero | titular con `kinetic-text-reveal` + lema "30 días. 30 retos. 3 niveles. 1 objetivo: no abandonar." | Componentry | promesa + CTA | texto estático si reduce movimiento |
| C cómo funciona (3 pasos) | tres pasos con cifra grande, **tamaños desiguales** | shadcn Card | entrar · completar · avanzar | — |
| D niveles | tres tarjetas con rayos y color de nivel; cada una dice **cuántos comodines da y cuántos días de racha dan acceso al sorteo**: Básico 4 y 21, Medio 4 y 26, Avanzado 3 y 30 | shadcn Card + Badge | Básico / Medio / Avanzado | — |
| E retos especiales | cuatro hitos (resistencia, fuerza, constancia, final) | shadcn Card | semanas 1–4 | — |
| F precio y CTA final | **Dos tarjetas: Individual 20 € y Dúo 30 € por pareja**, con la línea "Se paga en efectivo en Factory Training"; botón "Reservar mi plaza". El premio del sorteo (US-11) **solo se menciona cuando el sorteo esté activado**, con enlace a las bases | shadcn Button + Card | precio y forma de pago | — |
| G pie | confianza: aviso legal, privacidad, contacto de Factory Training | texto | — | — |

**Panel `/reto`** (US-03, US-06)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A cabecera | "DÍA 07 DE 30" con `split-flap-display` + nombre y nivel | Componentry | día actual | día 01 con mensaje de arranque |
| B racha | cifra animada con rayo | `@number-flow/react` | días seguidos | 0 con texto "empieza hoy" |
| C barra de 30 segmentos | componente propio (§2.2) | propio | progreso | todos vacíos |
| D reto de hoy | tarjeta con título, categoría y botón "Ir al reto de hoy" | shadcn Card + Button | reto actual | "Reto de hoy aún no disponible" |
| E calendario | rejilla 6×5 de días bloqueado/actual/hecho | propio sobre shadcn | estado por día | — |
| F hitos | fila de 4 insignias (ver pantalla 7) | shadcn Card | ganadas/pendientes | insignias en gris con candado |
| G sorteo (US-11) | chip "Sigues en carrera para el sorteo" (con la racha que falta para tu umbral: 21, 26 o 30) o "Ya cumples la racha del sorteo"; si no se alcanza, "Fuera del sorteo: sigues con el reto y el diploma", con enlace a las bases | shadcn Badge | estado en el sorteo | oculto si el sorteo está desactivado |
| H comodines (US-12) | fila de escudos pequeños: ganados, gastados (tachados) y cuántos quedan; al ganar uno, aviso "Has ganado un comodín"; al gastarse, "Se ha gastado un comodín: tu racha sigue" | propio (SVG del escudo con rayo) + shadcn Badge | comodines disponibles y gastados | 0 con "Ganas el primero el día 7" (día 10 en avanzado) |
| I ranking (US-13) | tarjeta «Tu puesto: N en tu nivel» con enlace a `/reto/ranking` | shadcn Card + `@number-flow/react` | puesto en el nivel | «Aún no hay ranking» |

**Reto del día `/reto/[dia]`** (US-04, US-05)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A cabecera | día, categoría, barra mini y nivel | propio | contexto | — |
| B por qué | bloque de texto corto | shadcn Card | `why` | — |
| C ejercicio | nombre, nivel, imagen o animación, pasos | shadcn Card + `Accordion` (Base UI) | ejercicio del nivel (por rotación) | marco tipográfico con el nombre si no hay imagen |
| D cómo y consejo | pasos y consejo | `Accordion` | `how`, `tip` | — |
| E acción | botón fijo abajo "Completar el día" (el día se marca a mano, también después del cronómetro) | shadcn Button | estado del día | deshabilitado con motivo si no toca |
| F cronómetro (US-15) | bloque con cuenta atrás grande: «10 flexiones, tienes 2:00», botón «Empezar» y, al acabar, descanso con su propia cuenta atrás y botón «Saltar descanso». Cifras en Barlow Condensed con `tabular-nums`, aviso con sonido corto, vibración y texto, y `aria-live` | propio (`ExerciseTimer`) sobre shadcn Card + Button | repeticiones, tiempo límite y descanso del ejercicio | sin tiempo programado: se oculta el cronómetro y queda la descripción |
| G vídeo (US-18) | reproductor del ejercicio sobre el cronómetro, sin reproducción automática | `<video>` nativo | vídeo de la librería o propio | imagen o marco tipográfico si no hay vídeo |
| H reto extra (US-14) | tarjeta opcional «Reto extra» solo en los días 3, 6, 9… 30, con botón «Hecho»; no bloquea completar el día | shadcn Card + Button | reto extra del día | oculta si ese día no toca |

**Ejercicios admin `/admin/ejercicios`** (US-08)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A barra | búsqueda + filtro de nivel + "Nuevo ejercicio" | shadcn Input + Select + Button | — | — |
| B lista (40 %) | filas con nombre, nivel y miniatura | shadcn Table | 9 ejercicios de inicio | "Aún no hay ejercicios: crea el primero" |
| C detalle (60 %) | formulario: nombre, nivel, descripción, pasos, imagen, **repeticiones, tiempo límite en segundos, descanso en segundos, origen del vídeo (librería o propio) y enlace o fichero del vídeo** | shadcn Form + Textarea + subida | ejercicio seleccionado | mensaje de selección |

**Ranking `/reto/ranking`** (US-13)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A cabecera | título «Ranking · nivel X» y regla de desempate en una línea: «Más racha; si empatas, menos comodines gastados; después, más retos extra» | texto | nivel de la persona | — |
| B lista | filas con puesto, nombre (nombre de pila + inicial; «Anónimo» si se oculta), racha, comodines gastados y retos extra; la fila propia resaltada con borde lima; sin correos | shadcn Table (en móvil, filas apiladas sin desbordes) | puestos del nivel | «Aún no hay ranking: empieza hoy» |
| C sorteo | línea «Para entrar al sorteo hacen falta N días de racha» (solo si el sorteo está activado) | shadcn Badge | umbral del nivel | oculto si el sorteo está desactivado |

**Pareja `/reto/pareja`** (US-17, solo plan Dúo)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A estado | nombre de la pareja, su racha, comodines que le quedan y si ya ha hecho el reto de hoy | shadcn Card + `@number-flow/react` | datos del otro | «Aún no se ha unido tu pareja» con mi código para compartir y botón de copiar |
| B racha conjunta | cifra grande con la frase «Días seguidos en que los dos habéis cumplido. No cuenta para el sorteo» | `@number-flow/react` | racha conjunta | 0 |
| C aviso | mensaje «Tu pareja aún no ha entrenado hoy» (solo informa, sin botón de reproche) | shadcn Badge | estado de hoy | oculto si ya cumplió |

**Reto extra admin `/admin/extras`** (US-14)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A lista | 10 filas (días 3, 6, … 30) con título y si falta cargarlo | shadcn Table | extras | «Aún no hay retos extra» |
| B detalle | formulario: título y descripción | shadcn Form + Textarea | extra seleccionado | mensaje de selección |

**Gerencia `/gerencia`** (US-09)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A cabecera | título y periodo | texto | cohorte | — |
| B KPI | "N de M participan esta semana (X %)" · terminaron · lo han dejado · en carrera y elegibles para el sorteo (solo cifras, si está activado), con la frase "mide participación en el reto, no la permanencia de socios en el gimnasio" | shadcn Card + `@number-flow/react` | cifras (definiciones en el [[4 - AppFlow]]) | 0 con "aún sin participantes" |
| C progreso | distribución por día alcanzado | barras simples en CSS | participantes por día | — |
| D tabla | participantes con nivel, día y última actividad; nombre completo solo de quien dio su consentimiento, el resto con nombre abreviado | shadcn Table | filas | "Sin participantes" |

**Participantes admin `/admin/participantes`** (US-10)

| Slot | Componente | Registry / librería | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| A barra | búsqueda + filtro por estado (por defecto "Pendientes primero") y filtro "Elegibles al sorteo"; interruptor "Activar sorteo" con fecha límite (desactivado por defecto) | shadcn Input + Select | — | — |
| B KPI | "Pendientes" destacada en lima · activas · canceladas | shadcn Card + `@number-flow/react` | cifras | 0 con "no hay plazas por activar" |
| C lista (40 %) | filas con nombre, nivel, estado de plaza, fecha de alta y, si el sorteo está activado, estado en el sorteo | shadcn Table | participantes | "Aún no se ha apuntado nadie" |
| D detalle (60 %) | datos del participante y acciones "Activar plaza" y "Cancelar plaza" con confirmación. Si es del plan Dúo, muestra a su pareja y ofrece «Activar a la pareja entera» (se cobra una sola vez, 30 €) | shadcn Card + Button + Dialog | participante seleccionado | mensaje de selección |
| E candidatos al sorteo | lista «Candidatos»: los elegibles; si no hay ninguno, los de mayor racha, con una etiqueta «Nadie ha clasificado: se muestran los de mayor racha» | shadcn Table | `admin_lottery_candidates` | «Sorteo desactivado» |

**Casilla de consentimiento** (pantalla 3, primer paso): texto claro "Acepto que la gerencia de Factory Training vea mi nombre y mi progreso en el reto", sin marcar por defecto y con enlace a la política de privacidad.

**Casilla de mayoría de edad** (pantalla 3, primer paso): obligatoria, "Soy mayor de 18 años"; no se guarda la fecha de nacimiento. **Cuenta (pantalla 9)** añade un interruptor para dar o retirar el consentimiento para gerencia, con efecto inmediato, y otros dos: **ocultar mi nombre en el ranking** y **recibir el correo diario**.

**Elección de plan** (pantalla 3): dos tarjetas «Individual · 20 €» y «Dúo · 30 € por pareja». En Dúo se pide elegir entre «Crear mi pareja» (se genera un código de 6 caracteres) y «Tengo un código». Texto sobre el nivel: «El nivel no se puede cambiar una vez empiezas el reto» antes de confirmar.

Pantallas 2, 3, 6, 7, 8, 9 y 12 usan los mismos componentes base (Card, Button, Form, Dialog) y se detallarán al maquetar; sus layouts y estados están en §3.

## 4.1 Componentes clave

| Componente | Librería | Variantes |
|---|---|---|
| Barra de 30 segmentos | propio | grande (panel), mini (reto) |
| Contador de día | `split-flap-display` (Componentry) | con y sin animación |
| Cifra animada | `@number-flow/react` | racha, KPI |
| Botón | shadcn Button (chaflán propio) | primario lima, secundario con borde, deshabilitado |
| Tarjeta | shadcn Card (chaflán propio) | reto, nivel, insignia, KPI |
| Acordeón | shadcn Accordion (Base UI) | simple |
| Insignia | propio (SVG con rayo) | ganada, pendiente |
| Cronómetro `ExerciseTimer` | propio | ejercicio, descanso, terminado, pausado |
| Escudo de comodín | propio (SVG con rayo) | disponible, gastado (tachado) |
| Fila de ranking | shadcn Table | normal, propia resaltada, anónima |

## 4.2 Correo diario

Texto plano con un solo botón. Asunto: «Día N de 30 · tu reto de hoy». Cuerpo (de tú, frases cortas): reto del día en una línea; racha; comodines que quedan; «Vas el N en el nivel X»; si toca, «Hoy hay reto extra»; botón «Ir al reto de hoy»; pie con enlace de baja y dirección de contacto de Factory Training. Sin imágenes pesadas ni emojis en el asunto. Los colores de marca (negro, lima) solo en el botón y la cabecera; contraste comprobado en modo oscuro del cliente de correo.

**Nota para el TRD**: este diseño elimina `@usespaceui/squircle` y los componentes de Space UI y Arc UI (menos dependencias y sin choque de tokens). El TRD aprobado cita esos registries en §1.2; conviene actualizarlo (con tu permiso, porque está aprobado).

## 5. Imágenes e ilustración contextual

Sin fotos de personas ficticias (regla de confianza): siluetas, símbolos e ilustración vectorial en la paleta de marca (negro, carbón, lima), fondo transparente o `#0C0D0E`.

| Vista | Prompt de imagen |
|---|---|
| Portada (hero) | "Dark athletic poster, abstract silhouette of an athlete mid-movement made of angular lime green (#CCFF00) light strokes on matte black (#0C0D0E), a large segmented progress bar of 30 blocks in the background, minimalist premium gym aesthetic, no text, no recognizable face, vector style" |
| Panel día 1 (estado vacío) | "Vector illustration, a single empty shield outline in dark grey with 30 empty segments and one small lime lightning bolt, matte black background, minimalist, no text" |
| Felicitación día normal | "Vector burst: lime green lightning bolt breaking through a dark grey shield, short rays, matte black background, energetic, no text" |
| Insignias (4 semanas) | "Set of four angular metal shield badges, dark grey with lime green edge, each with a different simple symbol: wave, dumbbell, flame, crown, flat vector, matte black background, no text" |
| Diploma | "Premium certificate frame, thin lime green double border with chamfered corners on matte black, space for name, subtle segmented bar of 30 full blocks along the bottom, no text" |
| Admin / gerencia (vacíos) | "Minimal line icon of an empty clipboard with a lime check mark, dark grey on matte black, vector" |
| Comodín | "Small angular dark grey shield with a lime green lightning bolt, flat vector, transparent background, no text" |
| Ranking vacío | "Vector podium with three empty angular steps in dark grey and a thin lime outline on the first step, matte black background, no text, no people" |
| Pareja del Dúo | "Two angular shields side by side sharing one lime green lightning bolt between them, dark grey, matte black background, flat vector, no text, no faces" |

Generación: Bloom (`bloom_generate_image`) con la marca RETO 30 incorporada, o la herramienta de imagen disponible al maquetar. Pendiente: ninguna imagen generada todavía (2026-10-19). Prompts ampliados y listos para generar fuera en [[Prompts de imagenes - App]]; mientras tanto la app usa SVG propios (`src/components/brand/Art.tsx`).

## 6. Responsive y accesibilidad

- Breakpoints: base 375 px; `md` 768 px (admin: lista + detalle); `lg` 1024 px. Comprobar `scrollWidth === clientWidth` en cada ruta.
- Participante en móvil: barra de navegación inferior fija (Panel · Hoy · **Ranking** · Insignias · Cuenta); en el plan Dúo, **Pareja** aparece dentro del Panel como tarjeta, para no pasar de 5 pestañas. Acción primaria fija abajo en el reto.
- **Cronómetro**: la cuenta atrás tiene `aria-live="polite"` y solo anuncia cada 10 segundos y al final; el aviso no depende del sonido (también vibración y texto), botón de pausa siempre visible, objetivo táctil ≥ 44 px y funciona con `prefers-reduced-motion` (sin animación de aro, solo cifras).
- Objetivo táctil ≥ 44 px; foco visible con anillo lima de 2 px; todos los campos con etiqueta; errores con texto además de color.
- Contraste AA calculado en §2; los estados de nivel no dependen solo del color (rayos).
- `prefers-reduced-motion`: sin contador animado, sin barrido de segmentos; el cambio de estado es instantáneo.

## 7. Movimiento

Un solo motor (`motion`) y una sola curva. El cronómetro usa solo `transform` y `opacity` para la transición ejercicio ↔ descanso (≈ 200 ms); las cifras no se animan. Tres momentos con animación: (1) completar el día, un barrido lima que rellena el segmento y un destello del rayo (≈ 600 ms); (2) racha, `NumberFlow` al subir; (3) cambio de día, el contador *split-flap*. Todo lo demás: transiciones CSS de 150–200 ms. Animar solo `transform` y `opacity`.

## 8. Checklist de marca

- [ ] No parece una plantilla genérica de SaaS oscuro (tipografía itálica condensada y barra de segmentos presentes)
- [ ] Contraste verificado en 375 px con el navegador (pendiente: no hay verificación visual disponible hasta tener las pantallas)
- [ ] Señales de confianza en la portada (Factory Training, aviso legal, privacidad); sin logos de terceros ni testimonios inventados
- [ ] Ningún placeholder visible: sin imagen de ejercicio se usa marco tipográfico
- [ ] Cifras con `tabular-nums`; CTAs con nombre de acción ("Reservar mi plaza", "Completar el día")

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]