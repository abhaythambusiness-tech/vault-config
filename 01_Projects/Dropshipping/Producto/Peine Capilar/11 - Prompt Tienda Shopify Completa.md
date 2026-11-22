---
type: nota
status: por-validar
date: '2026-09-07'
tags:
- dropshipping
- producto
- peine-capilar
- shopify
- cro
- prompt
proyecto: '[[Dropshipping - MOC]]'
origen: mixto
---

Prompt **ejecutable**: se pega a un agente que tiene el **conector de Shopify (MCP)** y construye la tienda del **peine aplicador + aceite capilar** directamente (productos, variantes, plan de suscripción, colecciones, páginas, menús, descuentos, SEO). Destila [[00 - Resumen y Decisiones]], [[02 - Avatar y Posicionamiento]], [[03 - Estrategias y Numeros]], [[07 - Tienda y Conversion]], [[08 - Retencion]], [[01 - Legal y Alegaciones]]. La ficha larga y la galería salen de [[10 - Prompt Ficha de Producto y Galeria]].

## Rellenar antes de ejecutar (`⟨⟩`)
Nombre de marca · precios (peine ⟨62,90⟩ / recambio aceite ⟨24,90⟩ / pack ⟨72⟩ / suscripción ⟨24,90 y 44,90⟩) · ml del frasco · plazo de envío ⟨X–Y días⟩ · dominio.

> **Lo que el conector NO hace** (dejar como tarea manual con instrucciones al final): instalar apps, order bump y upsell post-compra (Vitals/AfterSell), maquetar el tema/home, conectar Klaviyo. El conector SÍ: productos, variantes, `sellingPlanGroup` (suscripción nativa), colecciones, páginas, menús, metacampos, descuentos, ajustes de SEO.

---

## PROMPT (copiar desde aquí)

```markdown
# OBJETIVO
Tienes acceso al conector de Shopify (MCP). Construye la tienda de nicho de un peine
aplicador de aceite para el cuero cabelludo + aceite de recambio. Ejecuta las acciones con
las tools del conector (create-product, update-product, create-collection, create-discount,
graphql_query/graphql_mutation, get-shop-info). Español de España en todo el contenido de
cara al cliente. Antes de crear nada, llama a get-shop-info y comprueba qué ya existe con
search_products / graphql_query; no dupliques.

# REGLA LEGAL (BLOQUEANTE — un fallo puede cerrar la cuenta de ads)
En NINGÚN texto (título, descripción, metacampo, página, FAQ, descuento) se afirma ni se
insinúa que el producto hace crecer el pelo, frena la caída, aumenta la densidad o trata la
alopecia. Prohibidas las palabras "anticaída", "crecimiento", "alopecia", "antes/después".
Se vende: ritual de cuidado, masaje del cuero cabelludo, calma, dosis controlada y aplicar
sin mancharse las manos. Si un texto propuesto incumple esto, reescríbelo antes de enviarlo.

# AVATAR (todo el copy va dirigido a esta persona)
28–45 años, urbano, harto de champús y sérums que empezó y abandonó. Quiere una rutina fácil
de 3–4 min y sentir el pelo con más cuerpo y la cabeza relajada. Objeciones a desactivar:
"¿funciona o es un timo?", "¿cuánto tarda el envío?", "¿el recambio es caro?".
Tono: rutina diaria, calma, cuidado serio. NO gadget, NO oferta agresiva, sin emojis en
títulos, sin claims.

# 1. PRODUCTOS (create-product / update-product)
## Producto A — "⟨Marca⟩ · Peine aplicador de aceite" (el que se anuncia)
- Estado: activo. Tipo: "Cuidado capilar". Etiquetas: peine-aplicador, ritual, ancla.
- Precio: ⟨62,90⟩ €. Sin precio comparativo (no simular rebaja).
- Descripción HTML (habla al cliente, no specs sueltas): 2 párrafos en clave ritual/calma +
  lista de 5 beneficios (beneficio primero): dosis medida en cada pulsación · cabezal de
  púas huecas que masajea y reparte sin arañar · doble depósito de 15 ml · tapón de bomba de
  vacío antigoteo y portátil · recargable, cambias el aceite y no el aplicador.
- Al final de la descripción: "Cómo se usa" en 3 pasos (separa el pelo por zonas → pulsa el
  botón, sale la dosis justa → reparte y masajea con las púas) y "Qué incluye"
  (1 peine aplicador + 1 aceite de recambio de ⟨X⟩ ml).
- SEO: title "Peine aplicador de aceite para el cuero cabelludo | ⟨Marca⟩" (≤60 car.);
  meta description centrada en el ritual de 3 min y aplicar sin mancharse (≤155 car.).
- Metacampos (namespace custom): garantia = "30 días satisfecho o reembolsado, sin
  condiciones raras"; envio = "Envío en ⟨X–Y días⟩ con seguimiento, IVA de importación
  incluido"; faq = JSON con 4 pares P/R (incluye "¿Hace crecer el pelo?" → respuesta
  honesta: es un ritual de cuidado y masaje, no un tratamiento médico; no prometemos
  crecimiento).

## Producto B — "⟨Marca⟩ · Aceite capilar de recambio ⟨X⟩ ml"
- Estado: activo pero fuera de menús (se usa como recambio, order bump y suscripción).
- Precio recambio suelto: ⟨24,90⟩ €. Descripción corta: para qué es, cómo recargar el peine,
  cada cuánto (según ⟨ciclo⟩). Sin claims.
- SEO propio. Etiquetas: aceite, recambio, suscripcion.

## Pack (opcional, solo retargeting / Black Friday)
- Producto "⟨Marca⟩ · Pack peine + aceite" a ⟨72⟩ €, estado borrador hasta que se decida
  usarlo. No enlazar en navegación principal.

# 2. SUSCRIPCIÓN DE RECARGA (graphql_mutation: sellingPlanGroupCreate sobre el Producto B)
Crea un selling plan group "Recarga automática" con 2 planes:
- "1 frasco cada 90 días" — precio ⟨24,90⟩ €.
- "2 frascos cada 90 días" — precio ⟨44,90⟩ € (marcar como recomendado en el nombre).
Política: sin permanencia, se puede pausar o cancelar. (Si la tienda no tiene app de
suscripción nativa activa, deja el grupo creado y anótalo en el bloque de tareas manuales.)

# 3. COLECCIONES (create-collection)
- "El ritual" (manual): solo el Producto A. Será la home/destino de los anuncios.
- "Recargas" (manual): Producto B y planes de suscripción.

# 4. PÁGINAS (graphql_mutation: pageCreate) — texto real, sin relleno
- "Quiénes somos": por qué existe la marca, tono humano, sin claims.
- "Envíos": plazo ⟨X–Y días⟩ con seguimiento, IVA de importación incluido (el cliente no
  recibe carta de aduanas), países a los que se envía.
- "Devoluciones": 30 días satisfecho o reembolsado, pasos, sin condiciones raras.
- "Contacto": email de soporte con respuesta en 24 h.
- "Preguntas frecuentes": 6–8 P/R (envío, recambio, tipo de pelo, uso, garantía, y la de
  "¿hace crecer el pelo?" con respuesta honesta).
- Legales: "Aviso legal", "Política de privacidad", "Política de cookies", "Términos del
  servicio", "Términos de la suscripción" (RGPD; rellenar con los datos fiscales reales).

# 5. NAVEGACIÓN (graphql_mutation: menuCreate/menuUpdate)
- Menú principal: Inicio · El ritual (→ Producto A) · Recargas (→ colección) · Opiniones ·
  Ayuda (→ FAQ).
- Menú de pie: Quiénes somos · Envíos · Devoluciones · Contacto · Aviso legal · Privacidad ·
  Cookies · Términos.

# 6. DESCUENTOS (create-discount) — no mostrarlos en la primera visita
- "BIENVENIDA10" 10 % primera compra (para popup de captación, uso 1/cliente).
- "VUELVE15" 15 % para win-back (email día 30–45).
No crear descuentos automáticos ni banners de urgencia.

# 7. AJUSTES DE TIENDA
- Idioma principal español; moneda EUR; checkout sin cuenta obligatoria (comprobar/anotar).
- get-shop-info y confirmar dominio ⟨dominio⟩; si no está conectado, anótalo en tareas
  manuales.

# 8. TAREAS MANUALES QUE EL CONECTOR NO PUEDE HACER (deja una lista al final)
- Instalar y configurar: app de order bump + upsell post-compra 1 clic (Vitals o AfterSell);
  app de suscripción si no hay nativa; Klaviyo para email/SMS (flujos: carrito abandonado,
  post-compra con petición de reseña, win-back).
- Maquetar la home como landing larga (hero above-the-fold en 7 s: qué es, para quién, por
  qué esta marca; sticky "Añadir al carrito" en móvil; garantía bajo el botón; reseñas
  reales con foto y nombre, nunca placeholders).
- Conectar el dominio propio y subir favicon e imágenes de galería (de la nota 10).
- Meta Pixel + CAPI + GA4.

# ENTREGA
Ejecuta los pasos 1–7 con el conector. Al terminar informa: qué se creó (con IDs/handles),
qué falló, y la lista del punto 8 como checklist accionable. Recorre todos los textos
creados y confirma que ninguno incumple la REGLA LEGAL.
```
