---
title: "Dropshipping - Gestión de Stock con Proveedor Externo"
date: 2026-08-08
tags: [dropshipping, ecommerce, stock, proveedor, operaciones]
type: nota
status: por-validar
related: ["[[../Dropshipping - MOC]]"]
origen: mixto
---

# Gestión de stock cuando no lo controlas tú

**Origen:** propuesta propia. Completa [[Seleccion de Proveedor y Envios]] (cómo elegir proveedor) con el problema operativo del día a día: vender algo que el proveedor ya no tiene.

## El riesgo central
En dropshipping no hay visibilidad directa del almacén — se vende sobre un stock que gestiona un tercero. Si se rompe stock sin que la tienda se entere, se cobra al cliente por algo que no se puede enviar: reembolsos, reseñas negativas y, en agregado, bloqueos de pasarela de pago (ver [[../06_Legal y Finanzas/LLC y Bloqueos de Pago]]).

## Sincronización de stock
- [ ] Si el proveedor lo permite (CJdropshipping, Zendrop, Spocket — ver [[Seleccion de Proveedor y Envios]]), activar sincronización automática de stock vía app/API en vez de revisión manual.
- [ ] Con AliExpress puro (sin agente), revisar stock manualmente cada pocos días — no hay sincronización fiable, es el motivo por el que [[Seleccion de Proveedor y Envios]] recomienda evitarlo para volumen serio.
- [ ] Poner buffer de seguridad: si el proveedor muestra "50 unidades", tratarlo como "40" — los marketplaces suelen sobreestimar disponibilidad real.

## Qué hacer antes de escalar ads
- [ ] Confirmar con el proveedor (o el agente) el volumen que puede sostener antes de subir presupuesto — ver [[../04_Marketing y Ads/Escalado de Ads Ganadores]]. Escalar tráfico más rápido que la capacidad de stock es el error más común al pasar de testing a escalado.
- [ ] Tener un plan B de proveedor/producto sustituto igual o muy similar por si el principal rompe stock a mitad de campaña — no dejar la tienda con el producto ancla fuera de stock sin alternativa.

## Multi-proveedor (cuando hay varios productos o backup)
- [ ] Si se usan varios proveedores para el mismo catálogo, marcar en la ficha de producto interna cuál es el proveedor principal y cuál el backup, con sus tiempos de envío respectivos.
- [ ] Vigilar que el checkout no combine en un mismo pedido productos de proveedores distintos con tiempos de envío muy diferentes — genera confusión y tickets de "¿dónde está mi pedido?" (ver [[../05_Postventa y Retencion/Atencion al Cliente (SLA y Devoluciones)]]).

**Ver también:** [[Seleccion de Proveedor y Envios]], [[../04_Marketing y Ads/Escalado de Ads Ganadores]], [[../05_Postventa y Retencion/Atencion al Cliente (SLA y Devoluciones)]].
