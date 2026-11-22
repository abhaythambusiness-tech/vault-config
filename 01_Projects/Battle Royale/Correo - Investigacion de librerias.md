---
type: investigacion
date: '2026-10-23'
proyecto: '[[01_Projects/Battle Royale/Correo a prospectos]]'
status: cerrado
tags:
- correo
- librerias
- panel
origen: mixto
---

> [!resumen] En cristiano
> Para el correo del panel **no hace falta añadir ninguna librería ahora**: ya funciona con HTML hecho a mano y un cliente de Gmail propio sin dependencias. Lo que sí merece la pena, por orden: (1) **configurar bien el dominio de envío** (SPF, DKIM y DMARC), que pesa más que cualquier librería; (2) **comprobar que el correo del destinatario existe** antes de enviar (librería pequeña y gratuita); (3) **leer las respuestas** para apuntar solas las bajas (pide un permiso más a Gmail); y (4) si algún día tienes muchas plantillas, **MJML**. Las plataformas grandes de newsletters (Mautic, listmonk) son demasiado para 40 correos al día.

## Cómo está hoy
HTML de tablas con estilos en línea (lo que entienden Gmail y Outlook), Jinja para las variables, cliente de Gmail propio (OAuth + API, ~200 líneas, probado con servidor falso), conversión a texto plano propia. Cero dependencias nuevas.

## Hacer plantillas bonitas (HTML de correo)
Todos acaban en tablas, porque Outlook no entiende flexbox ni grid.

| Opción | Qué es | Versión y licencia (npm/PyPI, 2026-10-23) | Encaja aquí |
|---|---|---|---|
| **MJML** | Lenguaje de etiquetas que compila a HTML de correo; editor visual y muchos plugins | `mjml` 5.4.1 · MIT · 8,2 M descargas/mes | **Primera candidata si crecen las plantillas.** Necesita Node; hay un port en Python, `mjml-python` 1.4.2 (licencia no declarada en PyPI: **verificar** y comprobar que genera lo mismo) |
| **React Email** | Plantillas como componentes de React | `@react-email/components` 1.0.12 · MIT · 29 M/mes | Cómodo para diseñar en el PC; el servidor no tiene Node, así que se compilaría allí y se pegaría el HTML |
| **Maizzle** | HTML + Tailwind, sale con estilos en línea | `@maizzle/framework` 6.3.0 · MIT · 286 mil/mes | Solo si ya usas Tailwind |
| Foundation for Emails | Veterano | 2.5.1 · MIT · 108 mil/mes (última versión: marzo) | No: menos activo |
| **css-inline** (Python) | Pasa los `<style>` a estilos en línea; núcleo en Rust | 0.23.0 · publicada 2026-10-16 · licencia no declarada en PyPI (**verificar**) | Útil si escribes CSS con clases y quieres inlinearlo en Python |
| premailer (Python) | Lo mismo, clásico | 3.10.0 · **última versión 2021** | No: sin mantenimiento |

## Enviar
| Opción | Veredicto |
|---|---|
| **Cliente de Gmail propio** (el actual) | **Mantener.** Sin dependencias, probado, solo pide permiso de enviar |
| `google-api-python-client` 2.201.0 + `google-auth-oauthlib` 1.5.0 (Apache) | Oficiales y completos; solo compensan si pides más permisos (leer respuestas) |
| `yagmail` 0.16.0 (MIT), `emails` 1.1.3 (Apache) | Envoltorios de SMTP: no aportan sobre lo que hay |
| Amazon SES, Brevo, Resend, Postmark… | Para volumen o correo transaccional; **suelen prohibir el correo en frío** (sin verificar aquí: mira sus políticas antes) |
| **Mautic** (PHP, automatización completa, pesado) · **listmonk** (Go, newsletters, ligero) | Demasiado para 40 al día. Listmonk solo si algún día haces newsletters a suscriptores que lo han pedido |

## Piezas pequeñas que sí valen la pena
- **`email-validator` 2.3.0** (Unlicense) + **`dnspython` 2.9.0** (ISC): comprueban que el dominio del destinatario puede recibir correo (registro MX). Evitan rebotes, que dañan la reputación de tu cuenta. **Recomendado.**
- `nh3` 0.3.7 (MIT): limpia HTML si algún día se pegan plantillas de fuera. De momento no.
- `html2text` 2025.4.15: **GPL-3.0**, mejor no meterla: nuestra conversión a texto ya funciona.
- `Mailpit` (programa aparte): servidor SMTP de pruebas que enseña cada correo, comprueba enlaces e imágenes y puntúa el HTML por compatibilidad; la puntuación de spam necesita SpamAssassin. **No dice si Gmail lo mandará a la bandeja de entrada.** Útil para revisar plantillas sin enviar; hoy el modo simulación ya guarda `.eml`.
- Para ver el correo en Outlook o el móvil de verdad: Litmus o Email on Acid (de pago, sin verificar aquí) o enviarte pruebas a varias cuentas.

## Entregabilidad (lo que más pesa)
- Gmail y Yahoo exigen SPF, DKIM y DMARC a quien envía **5.000 o más correos al día**; tú estás muy por debajo, pero en la práctica **sin SPF y DKIM alineados con tu dominio es mucho más probable acabar en spam**. Quejas por debajo del 0,3 % (ideal 0,1 %).
- Baja con un clic (RFC 8058): exige una dirección **https** pública. Hoy usamos solo `mailto:` en `List-Unsubscribe`. Para el clic haría falta algo público (un túnel o una plataforma). A tu volumen no es obligatorio.
- Límites de envío de Gmail según blogs (no la documentación de Google): **500 destinatarios al día en cuenta personal y 2.000 en Workspace**; el límite de la API es aparte. Tus 40 al día están muy por debajo.
- Abrir y clics: para medirlos hace falta una dirección pública y los píxeles de seguimiento tienen problemas de privacidad y fiabilidad. Aquí **la respuesta es la señal buena**.

## Ley española (no es asesoramiento legal)
- El **artículo 21 de la LSSI** prohíbe la publicidad por correo no solicitada ni autorizada. Resoluciones de la AEPD (2011-2016, sobre la redacción de 2014) la aplican también a empresas y profesionales; debe haber una dirección válida para oponerse; el envío masivo o más de tres a la misma persona en un año se califica de infracción **grave**. Hay una excepción para clientes con relación previa y productos similares. Un ejemplo de sanción propuesta: 2.700 €.
- **Antes de enviar a prospectos, valídalo con un abogado o la AEPD** y comprueba el texto consolidado actual.

## Qué haría, por orden
1. **Dominio propio con SPF, DKIM y DMARC** (si envías desde Google Workspace con `neozeler.com`, se configuran en el DNS y en el panel de Workspace). Sin esto, el resto da igual.
2. **Comprobar MX antes de enviar** (`email-validator` + `dnspython`): pequeño, sin riesgo.
3. **Leer respuestas** (permiso `gmail.readonly`) para apuntar solas las bajas «BAJA» y marcar «respondió» en la candidata. Ahorra errores a mano, pero **amplía el permiso** que se le da a la aplicación: decisión tuya.
4. MJML solo si las plantillas se multiplican.

## Fuentes
- [Comparativa MJML / Maizzle / React Email (2026)](https://www.pkgpulse.com/guides/react-email-vs-mjml-vs-maizzle-email-template-2026) · [Mailtrap: frameworks de correo](https://mailtrap.io/blog/best-email-frameworks/amp/)
- [Límites de envío de Gmail (blog, no oficial)](https://www.usecarly.com/blog/gmail-api-limits/) · [Gmail: límites 2026](https://reply.io/blog/gmail-sending-limits/)
- [Requisitos de Google y Yahoo para remitentes masivos](https://bird.com/explained/deliverability/what-are-the-gmail-and-yahoo-bulk-sender-requirements)
- [Mailpit](https://github.com/axllent/mailpit) · [listmonk vs Mautic](https://use-apify.com/blog/mautic-vs-listmonk-2026)
- [css-inline en PyPI](https://www.pypi.org/project/css-inline/0.10.2/) · [premailer en PyPI](https://pypi.org/project/premailer/2.8.4)
- [AEPD: resoluciones sobre el art. 21 LSSI](https://www.aepd.es/documento/a-00345-2014.pdf)
- Versiones y licencias: registros de npm y PyPI consultados el 2026-10-23.

> [!riesgo] Qué no está verificado
> Las cifras de descargas y los límites de Gmail salen de blogs y agregadores, no de Google. Licencia de `css-inline` y `mjml-python` sin declarar en PyPI: mirar el repositorio. Políticas anti correo en frío de las plataformas de envío: sin verificar.

## Diseño del HTML para correo: qué dice la investigación (2026-10-23, tarde)
> [!resumen] En cristiano
> Un correo «bonito» no siempre es un correo que funcione. Para el **primer contacto en frío**, lo que hay publicado (casi todo de empresas que venden herramientas) sugiere que el texto casi plano llega mejor a la bandeja de entrada que el HTML cargado de imágenes; para correos de marca a gente que ya te conoce, el HTML vale. La salida elegida: **diseño ligero y personalizado con datos reales** (texto en vivo, una sola imagen, poco peso) y **un correo casi texto** para comparar. Lo que de verdad «demuestra que somos buenos» no es el adorno, sino enseñar que hemos mirado **su** web.

**Técnica (consenso de las guías):**
- Maquetar con tablas y estilos en línea; en Outlook para Windows no funcionan flexbox, grid, `float` ni los fondos CSS. Para fondos con imagen hace falta VML; los botones deben ser **texto con relleno** (si fueran una imagen, desaparecen cuando se bloquean las imágenes), con 44 px de alto como mínimo.
- Los efectos al pasar el ratón no existen en Outlook para Windows ni en las apps móviles de Gmail y Outlook.
- Modo oscuro: cada cliente hace lo suyo (invertir, respetar o invertir a medias): logotipos e iconos en **PNG transparente**, sin negro puro sobre blanco y un color de fondo de reserva para cualquier imagen.
- Gmail **recorta** el HTML a partir de ~102 KB (no cuentan las imágenes); margen de seguridad: por debajo de 85 KB. Mantener el HTML ligero y limpio.
- Según la propia documentación de Google, Gmail admite `background-image`, `border-radius` y consultas de pantalla (`@media`); una tabla de terceros decía lo contrario para las consultas: **por eso se deja todo con valores de reserva** y se debe probar en cliente real.
- Cuota de uso (Litmus, julio 2026, citado por un blog): Apple Mail ≈ 62 % de las aperturas, Gmail ≈ 27 %, Outlook de escritorio ≈ 6 %.

**Texto plano frente a HTML en correo en frío (lo publicado, casi todo de proveedores):**
- Hunter (2,2 millones de correos): el HTML rebota un 674 % más que el texto plano. Snov.io (44 millones): respuesta del 1,30 % en texto frente a 1,08 % en HTML (diferencia pequeña). FirstSales: texto plano en los tres primeros contactos.
- A favor del HTML: un solo estudio (Migma, 2024), de una empresa que **vende** HTML.
- **No hay estudio independiente de 2026.** La forma fiable de decidir es **probarlo con tu propia lista**: por eso hay dos plantillas.

**Personalizar con una revisión de su web:** existen herramientas y flujos (n8n, Insites) que envían correos con una auditoría de la web de la empresa, y el playbook de una plataforma da un 4,8 % de respuesta (cifra de proveedor, sin método verificable). No hay datos independientes de que mejore frente al texto plano; el argumento a favor es de sentido común (es específico, demuestra trabajo y no se parece a una plantilla masiva).

**Lo que se aplicó (plantilla «NeoZeler · Revisión de tu web»):**
- Cabecera oscura con el logotipo (única imagen), línea azul de marca, tarjeta de 600 px, bloque de puntuación con barra y una fila ✓/✕ por revisión **calculada con los datos reales del scraper** (https, móvil, tecnología, velocidad, Google, contacto, actualización). El estado no va solo en color.
- Botón a prueba de Outlook (VML), modo oscuro y móvil en la cabecera, texto de previsualización oculto, 0 enlaces externos, < 30 KB. Los puntos fuertes de NeoZeler son un campo de Configuración (solo cosas verdaderas): si se rellenan, aparece el bloque «Por qué NeoZeler».
- «NeoZeler · Texto sencillo»: casi texto plano para el primer contacto.

**Lo que NO se hizo (y por qué):** imágenes de héroe o capturas de pantalla de su web (más peso y más riesgo de filtros; posible mejora aparte), animaciones, contadores o AMP (no funcionan en la mayoría de clientes), seguimiento de aperturas (exige una dirección pública y es poco fiable).

**Fuentes:** [guía de diseño HTML de correo](https://www.warmy.io/blog/email-best-practices/html-email-design-best-practices/) · [modo oscuro](https://wpmailsmtp.com/best-practices-for-designing-emails-for-dark-mode/) · [Hunter: ¿perjudica el HTML la entregabilidad?](https://hunter.io/blog/is-html-harming-your-cold-email-deliverability/) · [FirstSales: texto plano vs HTML](https://firstsales.io/blog/plain-text-vs-html-cold-email/) · [Migma (proveedor de HTML)](https://docs.migma.ai/case-studies/html-vs-plaintext) · [recorte de Gmail](https://docs.bird.com/applications/content/email-templates/concepts/gmail-clipping-of-emails) · [CSS admitido en Gmail (Google)](https://developers.google.com/workspace/gmail/design/css) · [flujo n8n de auditoría + correo](https://n8n.io/workflows/5940-automated-website-audit-and-personalized-outreach-with-lighthouse-and-gpt-4/) · [Overloop: agencias web](https://overloop.com/playbooks/digital-web-agencies)
