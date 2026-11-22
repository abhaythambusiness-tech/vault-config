---
type: doc-software
doc: prd
proyecto: "Comanda Viva"
status: aprobado
tipo: web-cliente
date: 2026-11-04
origen: mixto
---

# 1 · PRD — Comanda Viva (marca para la clienta: «Monika Viva»)

> [!resumen] En cristiano
> Una app para el restaurante **Desayunos de Monika** (Alhaurín el Grande, Málaga) con tres partes: **(1)** un menú moderno al que se entra escaneando el QR de cada mesa, **(2)** un inventario donde la dueña apunta lo que tiene en cocina, y **(3)** una caja donde caen solas las comandas de cada mesa, listas para cobrar, más un panel de números del negocio. Cada plato pedido gasta ingredientes del inventario; cuando algo se acaba, los platos que lo llevan desaparecen del menú, y cuando quedan pocos se enseña «quedan 3» para empujar al cliente a decidirse. **Proyecto personal de Haytham** (no de NeoZeler). Producto genérico `Comanda Viva`; esta clienta lo ve como `Monika Viva` (marca personalizada replicable a otros restaurantes).

## 1. Problema
- **Dolor**: la dueña no controla la comida del local. Unos días compra de más (se tira), otros de menos (se acaba y el cliente se va sin lo que quería). Cifras: *pendientes de preguntar* (gasto semanal en compra, merma estimada, platos perdidos por falta de stock).
- **Hoy**: sin control de inventario; comandas y cobro sin sistema (a confirmar: papel / de memoria). Falla porque el stock real y el menú que ve el cliente no están conectados.
- **Fuente**: descripción de Haytham tras hablar con la clienta (2026-11-04). Local: https://maps.app.goo.gl/avg61ysaH4XXtxFt9 (Desayunos de Monika, Av. de Mijas 6, Alhaurín el Grande).
- **Paso 0 (demanda)**: cliente real con el problema; pago/reparto aún por cerrar (ver §8).

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Cliente (comensal) | Persona en una mesa, desde su móvil, sin cuenta | Ver el menú, saber qué hay, pedir y dejar notas por plato | Una vez por visita |
| Dueña | Propietaria del restaurante | Cargar inventario y recetas, ver caja y números | Varias veces al día |
| Caja | Hoy la misma dueña (en el futuro, camarero/a) | Recibir comandas por mesa y cobrarlas | Continuo en servicio |
| Cocina *(futuro)* | Cocineros | Recibir tickets de comanda | Fuera de v1 |

Acceso: cliente sin login (QR con la mesa). Caja y administración con login de la dueña.

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
| Que el menú nunca ofrezca lo que no hay | Platos vendidos sin stock | desconocido | 0 |
| Reducir merma y compras a ciegas | % de ingrediente tirado / semana | desconocido | -30 % en 2 meses (a validar) |
| Empujar la decisión (efecto «quedan pocos») | % de pedidos que incluyen un plato marcado «quedan N» | 0 | medir en piloto |
| Cobro sin papel | % de comandas que llegan a caja por QR | 0 | >80 % en el piloto |
| Visibilidad del negocio | La dueña consulta el panel de ventas | nunca | ≥3 días/semana |

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | Cliente | escanear el QR de mi mesa y ver el menú premium e interactivo | pedir sin esperar al camarero | Must |
| US-02 | Cliente | ver solo los platos disponibles y, si quedan pocos, cuántos | decidir rápido y no pedir lo que no hay | Must |
| US-03 | Cliente | añadir una nota a cada plato (sin cebolla, poco hecho…) | recibirlo como lo quiero | Must |
| US-04 | Cliente | enviar el pedido y ver que ha entrado | saber que se ha registrado | Must |
| US-05 | Cliente | volver a pedir más en la misma mesa sin perder lo anterior | ampliar la comanda durante la visita | Should |
| US-06 | Dueña | registrar ingredientes con unidad, cantidad y coste | tener el inventario real | Must |
| US-07 | Dueña | definir la receta de cada plato (ingredientes y cantidad por ración) | calcular raciones disponibles | Must |
| US-08 | Dueña | que cada pedido descuente automáticamente los ingredientes | no llevar la cuenta a mano | Must |
| US-09 | Dueña | que un plato se oculte solo cuando falte un ingrediente | no vender lo que no hay | Must |
| US-10 | Dueña | ver cuántas raciones quedan de cada plato según el inventario | planificar la compra | Must |
| US-11 | Dueña | ajustar el stock a mano (compra recibida, merma, recuento y corrección) con motivo | cuadrar con la realidad | Must |
| US-12 | Dueña | recibir alerta de ingrediente bajo mínimo | comprar a tiempo | Should |
| US-21 | Dueña | partir de una plantilla de desayunos (ingredientes y recetas típicas editables) | no cargar ~40 ingredientes a mano | Should |
| US-13 | Caja | ver llegar la comanda de cada mesa en tiempo real | no depender de avisos | Must |
| US-14 | Caja | tener la comanda de la mesa guardada hasta cobrarla | cobrar al final del servicio | Must |
| US-15 | Caja | marcar mesa cobrada (efectivo/tarjeta/otro) y cerrarla | cuadrar el día | Must |
| US-16 | Caja | corregir o anular una línea con motivo (stock se repone) | arreglar errores | Should |
| US-17 | Dueña | un panel con ventas por día/semana/mes, ticket medio, platos más vendidos | saber cómo va el negocio | Must |
| US-18 | Dueña | ver coste por plato, margen y consumo real vs. teórico de ingredientes | detectar pérdidas | Should |
| US-19 | Dueña | gestionar el menú (platos, precios, fotos, categorías, activar/desactivar) y las mesas con su QR | mantenerlo sola | Must |
| US-20 | Dueña | iniciar sesión segura; caja y administración solo con su acceso | proteger los datos | Must |

## 5. Requisitos funcionales
- RF-01: Cada mesa tiene un QR único (código no adivinable) que abre el menú ya vinculado a esa mesa.
- RF-02: Disponibilidad de un plato = mínimo, entre sus ingredientes, de `floor(stock / cantidad por ración)`. Si es 0, el plato no se muestra como pedible.
- RF-03: Un ingrediente compartido baja la disponibilidad de todos los platos que lo usan.
- RF-04: «Quedan N» se muestra solo cuando N ≤ umbral configurable (por defecto 5).
- RF-05: Al enviar el pedido, el descuento de stock es atómico (dos mesas pidiendo la última ración a la vez: una la consigue, la otra recibe aviso).
- RF-06: Nota libre por línea de pedido, visible en caja.
- RF-07: Comandas de una mesa se agrupan en una cuenta abierta hasta cobrar; varias tandas se suman.
- RF-08: Caja actualiza en tiempo real sin recargar, con aviso sonoro/visual de comanda nueva.
- RF-09: Anular/corregir línea repone stock (con registro de quién y por qué).
- RF-10: Todo movimiento de stock queda en un histórico (entrada, venta, merma, ajuste).
- RF-11: Panel financiero: ventas, nº de comandas, ticket medio, horas punta, ranking de platos, coste y margen (si hay costes cargados).
- RF-12: Menú gestionable: categorías, fotos, precio, alérgenos, orden, activar/desactivar manual.
- RF-13: Marca personalizable por cliente (nombre, logo, colores) sin tocar código — base para replicar a otros restaurantes.

## 6. Requisitos no funcionales
- **Móvil primero** para el cliente (375 px), caja en tablet/portátil; menú rápido en 4G (mala cobertura en restaurante).
- **Tiempo real** en caja (<2 s desde el envío).
- **Seguridad**: acceso de dueña autenticado; el cliente solo puede crear pedidos de su mesa, nunca leer ni tocar stock ni finanzas.
- **Accesibilidad** WCAG AA; idioma español (inglés opcional más adelante, turismo).
- **Disponibilidad**: si cae internet, caja avisa; plan de contingencia = comanda en papel (a definir en el TRD).
- **Datos**: backup diario; datos del restaurante separados por cliente desde el diseño (replicable).

## 7. Fuera de alcance (v1)
- TPV físico, impresora de tickets, tickets de cocina, pantalla de cocina (futuro previsto, no ahora).
- Pago online desde el móvil del cliente.
- Facturación legal / ticket fiscal (ver riesgo).
- Varios locales, reservas, delivery, fidelización, pedidos por proveedor automáticos.
- Multi-idioma.
- Propina, dividir la cuenta por líneas o por persona, botón «Pedir la cuenta» del cliente, variantes de plato (pan integral, sin huevo), cola de cobro sin conexión (decidido tras la simulación de clientes, 2026-11-04).

## 8. Riesgos y supuestos
> [!riesgo]
> - **Pedidos falsos o de broma**: cualquiera con la foto del QR podría pedir desde fuera. Decisión pendiente: (a) confirmación de caja antes de descontar stock, (b) código de mesa que cambia, (c) límite de líneas por pedido. Propuesta inicial: pedido entra directo, caja puede anular y reponer.
> - **Recetas imprecisas** = disponibilidad falsa. La dueña debe pesar raciones una vez; sin receta, el plato queda «sin control de stock».
> - **Adopción**: si la dueña no actualiza el inventario, el sistema miente. Entrada de compras debe ser rapidísima.
> - **Ley (España)**: software de caja/facturación puede obligar a cumplir la normativa antifraude (VeriFactu). v1 es **control interno, no emite factura ni ticket fiscal**; verificar antes del TPV futuro.
> - **Reparto/cobro sin cerrar**: proyecto personal de Haytham; falta acordar con la clienta si paga, cuánto y qué pasa con el código.
> - **Código parecido a `ComandAi`** (panel interno del vault): nombre distinto, proyecto distinto; no mezclar.
> - **Supuestos a confirmar**: nº de mesas, carta real (nº de platos e ingredientes), si hay camareros, si ya hay datáfono/TPV.

## 9. Criterios de aceptación globales
- [ ] Escanear QR de la mesa 3 → pedido llega a caja marcado «Mesa 3».
- [ ] Pedir la última ración: el plato desaparece del menú de todas las mesas en <3 s.
- [ ] Plato con ingrediente a 0 no es pedible, aunque el cliente tenga el menú ya abierto.
- [ ] Flujo completo verificado: crear → refrescar → anular → refrescar, en producción.
- [ ] Axe sin violaciones; Lighthouse móvil ≥90; probado en 375/768/1280 px.
- [ ] La dueña carga 10 ingredientes y 5 recetas sin ayuda en <15 min.

## 10. Demo provocadora (reunión 1)
- **Pantalla que provoca la reacción**: menú con «Quedan 2 tostadas de aguacate» y un plato oculto al agotarse el aguacate, con datos sintéticos de desayuno (tostadas, café, zumo, huevos, tortilla).
- **Quién la ve**: la dueña, en su móvil; y un cliente de prueba escaneando QR.
- **Reacciones / rechazos**: pendiente.
- **Descartar**: nada de app para cocineros en v1.

## 11. Carácter de marca (insumo de la identidad visual)
*Propuesta de Claude, a validar con Haytham y la clienta tras ver fotos/logo reales del local.*
- 3 adjetivos: **fresco, vivo, cercano** (desayunos, producto del día, el menú «respira»).
- Qué NO debe parecer: carta digital fría de franquicia; app de delivery genérica; plantilla de QR-menu gratuita.
- 2 referencias: *por buscar* (Dribbble/Mobbin: menús de café y brunch premium; se mostrarán 5-8 antes de decidir, fase 0b de `diseno-central`).
- Qué enseñar en vivo: la propia comida (fotos reales de platos), contador de raciones que baja en directo.
- Material propio: *pedir a la clienta* logo vectorial, fotos de cada plato, carta actual con precios y alérgenos. Si falta alguna imagen: parar y preguntar (prompt Gemini / SVG / foto real).

---
Siguiente: [[2 - TRD]]
