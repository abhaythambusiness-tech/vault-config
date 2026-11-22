---
type: proyecto
date: '2026-10-23'
proyecto: '[[01_Projects/Battle Royale]]'
status: en-progreso
tags:
- panel
- correo
- laya-leads
origen: mixto
---

> [!resumen] En cristiano
> El panel tiene una pestaña **Correo** para escribir a las candidatas del scraper desde tu Gmail: creas un correo con diseño bonito (con logo e imágenes dentro), eliges a quién se lo mandas entre las candidatas con correo, y el panel los va enviando poco a poco (como mucho 40 al día, de 9 a 18, de lunes a viernes). **Empieza en modo simulación: no envía nada, solo guarda los correos como archivos para que los revises.** Para enviar de verdad tienes que conectar tu cuenta de Gmail (lo haces tú, no se puede automatizar) y pasar a modo real.

## Cómo se usa
1. **Plantillas**: pulsa «Crear ejemplos bonitos» (hay una sin imágenes y otra con logo e imagen destacada), edita el HTML y mira la vista previa. Las imágenes se suben con un nombre (`logo`, `hero`) y se usan como `<img src="cid:logo">`.
2. **Configuración**: pon tu nombre, tu correo y el **pie legal** (quién eres y dónde). Envíate una prueba (en simulación se guarda como archivo en `data/correo_salida/`).
3. **Nueva campaña**: filtra candidatas (nivel, sector, estado), marca a quién escribir y crea la campaña (en borrador).
4. **Activar envío**: el panel pregunta confirmación y empieza. Se puede pausar, cancelar o borrar. Cada envío queda en la tabla (enviado, error, omitido) y la candidata pasa a «contactada».
5. **Bajas**: quien responda «BAJA» se apunta a mano en Configuración y no recibe nada más.

## Conectar Gmail (lo haces tú)
1. En console.cloud.google.com crea un proyecto y activa **Gmail API**.
2. Pantalla de consentimiento OAuth: «Externo» y tu correo como usuario de prueba.
3. Credenciales: «ID de cliente de OAuth» tipo **Aplicación de escritorio**; descarga el JSON.
4. Cópialo al servidor como `~/.config/battle-royale/gmail_client.json` con `chmod 600`. **Nunca a un repositorio.**
5. Abre el panel con el túnel (`ssh -L 8090:127.0.0.1:8090 ssh@192.168.0.100`) en `http://localhost:8090/correo/configuracion` y pulsa **Conectar con Google**. Solo pide permiso de *enviar* (no puede leer ni borrar tu buzón).
6. Mientras la app de Google esté en modo «Prueba», el permiso caduca a los 7 días: hay que volver a conectar (o publicar la app para uso propio).

## Salvaguardas
- Modo simulación por defecto; el modo real exige Gmail conectado, remitente y pie legal.
- Nada se envía hasta activar una campaña a mano.
- Límite diario (40), pausa entre correos (45 s), ventana horaria, bajas respetadas, reintentos de fallos pasajeros (3) y un solo envío por dirección en todas las campañas.
- Pie obligatorio en cada correo (quién escribe, por qué le llega, cómo darse de baja) que la plantilla no puede quitar.
- Escribir en el panel exige estar en el servidor o tener el PIN.

> [!riesgo] Riesgo legal y de cuenta
> En España, la **LSSI (art. 21)** prohíbe enviar publicidad por correo a quien no la ha pedido, **también entre empresas**, y hay multas. El pie y la lista de bajas ayudan, pero **a quién escribes y con qué base es responsabilidad tuya**. Además, Gmail puede limitar o suspender cuentas que envían en frío a muchos desconocidos: no uses tu cuenta principal sin probar con pocos correos y mira si un dominio propio con SPF/DKIM sería mejor.

## No verificado
- **Nunca se envió un correo real**: no tengo tus credenciales de Google. Todo el flujo con Gmail está probado con un servidor falso (OAuth con PKCE, renovación del permiso, 401, 429, 5xx, permisos revocados), no con Google de verdad.
- La vista previa no equivale a ver el correo en Outlook, Gmail o el móvil: prueba enviándote uno antes de una campaña.

## Detalles técnicos
Módulos `correo.py`, `gmail.py` (OAuth + API sin librerías de Google), `cola_correo.py` (tarea del colector), `correo_ejemplos.py`, `web/rutas_correo.py`; tablas `correo_*` (migración v2 de `panel.db`). 423 pruebas pasan (80 nuevas).

## Actualización (2026-10-23, tarde): marca de NeoZeler
- Las dos plantillas de ejemplo son ahora de NeoZeler: cabecera oscura con el **logotipo** (recortado de `99_Assets/logos/logo_completo_sin_fondo.png`, 640 px, 94 KB), línea azul `#2563eb`, cuerpo claro, botón azul y pie. «NeoZeler · Directa» y «NeoZeler · Tres pasos» (qué hemos visto, qué proponemos, siguiente paso). El logotipo viaja con el panel (`src/battle_royale/recursos/`) y «Crear ejemplos» lo carga como imagen `logo`.
- Sin nombre de remitente el texto dice «Hola, os escribimos de NeoZeler» (con nombre: «Hola, soy …, de NeoZeler»).
- El pie legal sale en un bloque centrado de 600 px bajo la tarjeta.
- **La propuesta comercial (los textos) es provisional**: se trabaja aparte, como dijiste.
- Investigación de librerías: [[01_Projects/Battle Royale/Correo - Investigacion de librerias]].

## Actualización (2026-10-23, noche): plantillas más vivas y personalizadas
Las plantillas de ejemplo se rehicieron tras la investigación de diseño (ver [[01_Projects/Battle Royale/Correo - Investigacion de librerias]]):
- **«NeoZeler · Revisión de tu web»**: correo visual con una **mini-revisión de la web de cada candidata** (puntuación con barra, ✓/✕ por punto y el porqué), calculada con los datos reales del scraper (`candidatas.revision_web`). Cada empresa ve la suya. Botón a prueba de Outlook, modo oscuro y móvil, una sola imagen, < 30 KB.
- **«NeoZeler · Texto sencillo»**: casi texto plano para el primer contacto; sirve para **comparar** cuál obtiene más respuestas (no hay estudio independiente sobre cuál es mejor).
- **Puntos fuertes de NeoZeler** (Configuración, hasta 4 líneas): si los rellenas aparece el bloque «Por qué NeoZeler». **Solo cosas verdaderas que puedas demostrar**; no se inventa ninguna cifra ni caso.
- Variables nuevas para tus plantillas: `revision`, `puntos_ok`, `puntos_total`, `pct`, `veredicto`, `prueba_social`.
- 443 pruebas pasan. **Pendiente**: la propuesta comercial (los textos) y una forma de medir qué plantilla funciona mejor (haría falta leer respuestas: permiso `gmail.readonly`).
