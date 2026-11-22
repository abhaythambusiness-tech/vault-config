---
type: doc-software
doc: ui-ux
proyecto: "Los Apuntes de Liyo"
status: aprobado
date: 2026-10-27
origen: mixto
---

# 3 · UI/UX Design

> [!resumen]
> Cómo se ve y se siente. Pasa antes por el gate de `rules/diseno.md` (identidad, anti-genérico, contraste, confianza). Cada pantalla traza a una historia del [[1 - PRD]].

## 1. Principios de experiencia
- Rápido en el móvil: nada de esperas largas, el chat responde con streaming y la subida de PDF confirma al instante aunque la indexación siga de fondo.
- La fuente siempre visible: cada respuesta de la IA muestra de qué documento y página sale, nunca una respuesta "flotando" sin origen.
- Cero fricción para subir y para denunciar: dos acciones clave de la comunidad, un toque cada una.

## 2. Identidad visual
> [!resumen] Este apartado es la identidad del proyecto
> **Tercera vuelta 2026-10-27 (opción D, «Luz de lámpara»), elegida por Haytham tras descartar la v1 «papel y rotulador» (demasiado sobria) y la v2 «Cuaderno de verdad».** Comprobado contra [[Registro de Identidades Visuales]]: ya hay proyectos «oscuro + acento fuerte» (`barber-df`: negro puro + lima). Esta se separa de ellos en tres cosas: fondo **azul noche** (no negro), acento **ámbar cálido** (no lima ni neón) y una composición propia, la cita iluminada. Si en el futuro otro proyecto usa azul noche + ámbar, hay que cambiar uno.

- **Idea visual central**: estudiar de madrugada con la lámpara del escritorio. **Todo está en penumbra y solo lo que importa está iluminado**: el trozo exacto de tus apuntes que responde la duda se enciende en ámbar, con su página como marcapáginas. No es un chat oscuro más: es una sala de estudio donde la respuesta te señala el renglón.
- **El producto como diseño**: la propia cita (el trozo de apunte recuperado, con documento y página) es la pieza iluminada de cada respuesta — dato real, no ilustración.
- **Composición firma**: «**la cita iluminada**» = tarjeta azul noche con borde izquierdo ámbar y un resplandor suave, el texto citado con resaltado ámbar translúcido y la página en una pestaña tipo marcapáginas. Se repite en: la respuesta del chat, el hover/foco de las tarjetas de módulo (se «enciende» el borde), la tarjeta de documento al abrirla y el aviso de «sin resultados» (misma tarjeta pero en coral, «luz roja»). Detrás, un «charco de luz» cálido muy tenue arriba a la izquierda, como la lámpara fuera de plano.
- **Anti-referencias**: clon de ChatGPT oscuro (burbujas grises sin identidad), neón gamer o morado/cian de «IA», negro puro + lima (`barber-df`), y cualquier robot o chispa.
- **Referencias reales** (qué se toma, no píxeles):

| Referencia | Qué se toma |
|---|---|
| Linear (modo oscuro) | Jerarquía sobria: bordes finos de 1px en vez de sombras pesadas, mucho aire |
| Readwise Reader (modo oscuro) | El resaltado como objeto real de la interfaz, aquí convertido en la cita |
| Biblioteca universitaria de noche | La sensación de lámpara de mesa: pocos puntos de luz cálida sobre fondo frío |

| Elemento | Valor |
|---|---|
| Paleta | Azul noche + ámbar de lámpara + menta (éxito) + coral (aviso); ver tabla |
| Tipografías y motivo | `Space Grotesk` (títulos, marcapáginas y números: geométrica con carácter, se lee bien en oscuro) + `Work Sans` (cuerpo, legible en pantallas pequeñas). Ambas OFL, autoalojadas |
| Radio / sombras / espaciado | Radio 14px en tarjetas, 10px en controles; bordes de 1px `--line` en vez de sombras; el único resplandor es el ámbar de la cita (`0 0 24px rgba(255,181,71,.22)`); espaciado base 8px |
| Tono y voz | De compañero de clase, frases cortas, sin tecnicismos |

**Paleta con escala:**

| Color | Valores | Papel |
|---|---|---|
| Noche (fondos) | `#0D1120` · `#131A2E` · `#1B2440` · `#27325A` | Página, tarjetas, superficies hundidas, líneas |
| Texto | `#EEF0F7` · `#C3C9DD` · `#97A0BC` · `#6C7594` | Principal, secundario, apagado (≥ 4.5:1 salvo el último, solo decorativo) |
| Ámbar de lámpara (acento primario) | lavado `rgba(255,181,71,.16)` · `#FFD38A` · `#FFB547` · `#E08A12` | Cita iluminada, botón primario (texto `#1A1205`), foco |
| Menta (éxito) | lavado `rgba(94,224,176,.14)` · `#5EE0B0` | Confirmaciones |
| Coral (aviso) | lavado `rgba(255,122,122,.14)` · `#FF7A7A` | Denuncias, errores, «sin contexto» |

### 2.1 Tokens primero
```css
:root {
  --night: #0D1120;       --surface: #131A2E;   --surface-sunk: #1B2440;   --line: #27325A;
  --text: #EEF0F7;        --text-soft: #C3C9DD; --text-muted: #97A0BC;     --text-faint: #6C7594;
  --brand: #FFB547;       --brand-soft: #FFD38A; --brand-deep: #E08A12;    --on-brand: #1A1205;
  --brand-wash: rgba(255, 181, 71, 0.16);
  --accent-success: #5EE0B0; --ok-wash: rgba(94, 224, 176, 0.14);
  --accent-risk: #FF7A7A;    --risk-wash: rgba(255, 122, 122, 0.14);
  --radius: 14px;  --radius-sm: 10px;
  --glow: 0 0 24px rgba(255, 181, 71, 0.22);
  --font-body: "Work Sans", system-ui, sans-serif;
  --font-display: "Space Grotesk", system-ui, sans-serif;
}
```

## 3. Inventario de pantallas
| Pantalla | Rol | Historia (US) | Layout base | Estados a diseñar |
|---|---|---|---|---|
| Entrada (nombre + centro) | Alumno | US-01 a US-06 (acceso) | asistente (un solo paso) | vacío · error (nombre vacío) · éxito |
| Lista de módulos | Alumno | US-03, US-05 | lista-detalle | vacío (sin módulos aún) · cargando · éxito |
| Módulo: documentos + chat | Alumno | US-01, US-02, US-04 | lista-detalle con panel de chat | vacío (sin documentos) · cargando (con esqueleto visible mientras llega la respuesta, no una pantalla en blanco) · error (Groq sin respuesta) · éxito con cita |
| Subir documento | Alumno | US-01 | formulario modal | cargando (indexando) · error (PDF no legible) · éxito |
| Denunciar documento | Alumno | US-06 | formulario modal pequeño | error (sin motivo elegido) · éxito (confirmación) |
| Entrada admin (`/admin`, token) | Admin | — (seguridad) | asistente (un solo paso) | error (token incorrecto) · éxito |
| Panel admin: módulos y denuncias | Admin | US-05, US-06 | dashboard simple | vacío (sin denuncias) · badge con nº pendientes · éxito |
| Crear módulo | Admin | US-05 | formulario modal | error (nombre duplicado) · éxito |
| Previsualizar documento denunciado | Admin | US-06 | visor de documento | error (PDF no se puede previsualizar, igualmente se puede borrar) · éxito |

**Corrección tras cliente simulado (admin, 2026-10-27):** se añaden las 4 pantallas de admin de abajo — no existían documentadas aunque los permisos ya decían que el admin "podía" hacer estas acciones (atascos #1, #4, #5, #7 del informe del agente).

## 4. Slots por pantalla
| Pantalla | Slot (zona) | Componente | Dato que muestra | Estado vacío |
|---|---|---|---|---|
| Entrada | formulario centrado | input nombre + input centro + botón "Entrar" | — | error si falta nombre |
| Lista de módulos | rejilla de tarjetas | tarjeta de módulo (nombre, nº documentos, nº preguntas respondidas) | contador real | ilustración SVG "lámpara apagada" + texto "Pide a Haytham o a un compañero que cree el primer módulo" |
| Módulo | panel izq: cabecera fija | botón "+ Subir apunte" (siempre visible, también con documentos ya subidos) | — | — |
| Módulo | panel izq: lista de documentos | tarjeta de documento (nombre, nº páginas, botón "Denunciar") | — | ilustración SVG "hoja con +" + el mismo botón "+ Subir apunte" de la cabecera (el botón de la cabecera cubre también el primer apunte; no hay un botón distinto solo para el estado vacío) |
| Módulo | panel der: chat | burbuja de pregunta (alumno) + bloque "cita subrayada" (respuesta con fuente) | cita real con documento y página | si no hay contexto: aviso con --accent-risk "No tengo apuntes de este módulo que respondan esto todavía. Puede ser que nadie lo haya subido aún, o que preguntándolo con otras palabras lo encuentre" (texto ampliado tras cliente simulado, atasco "no entendería por qué") |
| Subir documento | modal | input de archivo PDF + barra de progreso | — | error "no se pudo leer el PDF" |
| Denunciar documento | modal pequeño | select con motivos cerrados (contenido erróneo · copiado de un examen/con copyright · spam/no relacionado · otro) + textarea opcional + botón "Enviar denuncia" | — | confirmación visible "Denuncia enviada, gracias" que sustituye al botón "Denunciar" por "Denunciado" en esa tarjeta (para que el alumno sepa que sí se registró) |
| Entrada admin | formulario centrado | input de token + botón "Entrar" | — | error "token incorrecto" |
| Panel admin | cabecera | badge con nº de denuncias pendientes + botón "+ Nuevo módulo" | contador real | — |
| Panel admin | lista de denuncias | fila con documento, módulo, **quién lo subió**, motivo, nº de denuncias acumuladas, botón "ver documento", botón "borrar" | — | "sin denuncias pendientes" |
| Crear módulo | formulario | input nombre (obligatorio) + input centro/ciclo (opcional) + botón "Crear" | — | error "ya existe un módulo con ese nombre" |
| Previsualizar documento | visor | PDF embebido + botón "borrar" + botón "cerrar sin borrar" | documento real | "no se pudo previsualizar, puedes borrar igualmente" |

## 4.1 Componentes clave
| Componente | Librería | Variantes |
|---|---|---|
| Cita iluminada | propio (CSS) | ámbar (respuesta), coral (sin respuesta), con marcapáginas de página |
| Tarjeta de módulo | propio (CSS) | normal, hover/foco con borde ámbar y resplandor, con contador de apuntes |
| Tarjeta de documento | propio (HTML+CSS, sin framework, ver TRD §1) | normal, con botón denunciar, «Denunciado» |
| Panel de chat | propio (CSS) | con charco de luz de fondo |
| Botón primario | propio | normal, cargando, deshabilitado (ámbar con texto oscuro) |

## 5. Imágenes e ilustración contextual
Decidido con Haytham el 2026-10-27: **las imágenes mínimas de la v1 van en SVG propio**, con los colores de la identidad. Sin imágenes generadas ni stock.

- **Estilo de imagen**: trazo fino de una sola línea (`#C3C9DD`, 3px, extremos redondeados) sobre relleno azul noche `#1B2440`, con un único toque de ámbar `#FFB547` como «luz». Sin degradados ni sombras 3D.
- **Bloque de estilo** (reservado por si en el futuro se necesita Gemini; no se usa en v1):
  ```
  Ilustración de línea fina de una sola trazada en #C3C9DD sobre fondo #0D1120, relleno plano #1B2440, un único acento ámbar #FFB547 como punto de luz, sin degradados ni sombras 3D, ambiente de sala de estudio nocturna, sin texto dentro de la imagen, sin manos, sin estética genérica de IA.
  ```
- Prohibido en imagen: texto dentro, estética genérica de IA (robot, chispas), manos, neón.

| Vista / hueco | Qué imagen | Origen decidido | Estado |
|---|---|---|---|
| Lista de módulos vacía | Lámpara de escritorio apagada con un tenue halo, ~96×96px | SVG propio (`vacio-lampara.svg`) | hecho |
| Documentos de un módulo vacío | Hoja con una esquina doblada y un «+» ámbar, ~96×96px | SVG propio (`vacio-documentos.svg`) | hecho |
| Wordmark «Los Apuntes de Liyo» | Logotipo tipográfico en `Space Grotesk` con un trazo de luz ámbar bajo «Liyo» | SVG propio (inline para usar la fuente de la página) | hecho |

## 6. Responsive y accesibilidad
- Mobile-first (es el uso principal); breakpoint único a partir de 768px para pasar de panel único (chat o lista, con pestañas) a los dos paneles lado a lado en el módulo.
- Objetivo táctil ≥ 44px en botones de subir, denunciar y enviar pregunta.
- Contraste (WCAG AA ≥ 4.5:1) comprobado con script sobre los valores reales: `--text`, `--text-soft` y `--text-muted` sobre `--surface` y `--night`; `--on-brand` sobre `--brand`; `--brand`, `--accent-success` y `--accent-risk` sobre `--surface`. Revisar con `auditor-web` al cerrar la fase de pulido.
- Foco visible con anillo ámbar de 3px; `color-scheme: dark`; `prefers-reduced-motion` respetado (ver §7).

## 7. Movimiento y dinamismo
- **Nivel 2 (vivo pero funcional)**: sigue siendo una app de uso en móvil; el movimiento cuenta la metáfora de la lámpara (se enciende lo importante) sin estorbar.
- **Cómo evita parecer estático**: el charco de luz ámbar de fondo, las tarjetas con borde fino que se «encienden» al acercarse, y densidad que cambia entre la rejilla amplia de módulos y el chat vertical y apretado.
- **Curva propia**: `cubic-bezier(0.22, 1, 0.36, 1)` (entrada rápida, asentamiento suave).
- **Elementos vivos** (máx. dos por pantalla):
  1. **Se enciende la lámpara**: al abrir la app, el charco de luz del fondo sube de 0 a su intensidad en ~900 ms.
  2. **Barrido de luz de la cita** (solo en el chat): cuando llega la respuesta, el resaltado ámbar de cada cita se dibuja de izquierda a derecha en ~350 ms y el resplandor se asienta (escalonado ~120 ms entre citas).
- Además, microinteracción de tarjetas: al pasar el ratón o enfocar, el borde pasa a ámbar con resplandor (transición 200 ms).
- Motor: CSS puro (`@keyframes` + `transition`), sin librería (presupuesto TRD §1.2: 0 motores). `prefers-reduced-motion: reduce` deja la lámpara encendida y las citas ya iluminadas, sin barrido ni transición.

## 8. Checklist de marca
- [x] Prueba del intercambio: cambiar el texto no vale para otro negocio — la cita iluminada con página solo tiene sentido para «apuntes de estudio con fuente verificable»
- [x] Prueba de lejos: sin logo, en 3 segundos se reconoce por el azul noche con un único resplandor ámbar sobre la cita y su marcapáginas
- [x] No repite combinación del [[Registro de Identidades Visuales]] (azul noche + ámbar + Space Grotesk; se separa de `barber-df`, negro puro + lima; fila actualizada)
- [x] No parece plantilla genérica (nace de la cita real iluminada, no de un layout de chat de IA)
- [ ] Contraste verificado en código real con `auditor-web` (los valores ya se comprobaron con script en §6)
- [x] Señales de confianza presentes (la fuente/página de cada respuesta es la señal de confianza central)

---
Anterior: [[2 - TRD]] · Siguiente: [[4 - AppFlow]]
