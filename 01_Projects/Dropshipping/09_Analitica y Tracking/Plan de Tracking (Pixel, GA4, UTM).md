---
title: "Dropshipping - Plan de Tracking (Meta Pixel, GA4, UTM)"
date: 2026-08-08
tags: [dropshipping, ecommerce, analitica, tracking, meta-pixel, ga4]
type: nota
status: activo
related: ["[[../Dropshipping - MOC]]"]
source_skill: marketing-skills:analytics-tracking
origen: mixto
---

# Plan de tracking

**Por qué existe esta nota:** el documento fuente da la estrategia de Meta Ads (CBO/ABO, ver [[../04_Marketing y Ads/Estrategia Meta Ads CBO-ABO]]) pero da por hecho que el tracking ya está bien instalado. Sin esto, ninguna de las métricas del documento (CPC, CTR, CPM, ROAS) es fiable. Adaptado de la skill `marketing-skills:analytics-tracking` (pensada para SaaS) al funnel real de una tienda Shopify.

## Eventos mínimos a trackear (funnel ecommerce)

Convención de nombres: `objeto_accion`, snake_case, en minúsculas.

```
page_view              (automático)
view_item              (ficha de producto vista)
add_to_cart            (añadir al carrito)
initiate_checkout      (empieza el checkout)
add_payment_info       (introduce método de pago)
purchase               (compra completada — parámetros: value, currency, transaction_id)
```

Eventos de retención (ligados a [[../05_Postventa y Retencion/Upsell Post-Compra]] y [[../05_Postventa y Retencion/Suscripciones]]):
```
upsell_viewed
upsell_accepted
subscription_started
```

## Meta Pixel + Conversions API (CAPI)

- Instalar el Pixel de Meta en la tienda (vía Shopify o Google Tag Manager).
- **CAPI es casi obligatorio hoy:** el pixel solo por navegador pierde ~30% de conversiones por bloqueadores de anuncios e iOS (App Tracking Transparency). Sin CAPI, las métricas de la campaña CBO/ABO (ver [[../04_Marketing y Ads/Estrategia Meta Ads CBO-ABO]]) están subestimadas y Meta optimiza peor.
- Eventos estándar de Meta a mapear: `PageView`, `ViewContent`, `AddToCart`, `InitiateCheckout`, `Purchase`.

## GA4 (complementario al Pixel, para ver todo el funnel fuera de Meta)

- Activar el paquete de ecommerce mejorado de GA4 (Enhanced Measurement + eventos de ecommerce).
- Marcar `purchase` como key event.
- Vigilar que `page_location` no muestre rutas genéricas — señal de que el tracking de la SPA/tema de Shopify está mal configurado.

## Convención UTM (obligatoria para no perder atribución)

| Parámetro | Convención | Ejemplo |
|---|---|---|
| `utm_source` | plataforma en minúsculas | `meta`, `tiktok`, `instagram` |
| `utm_medium` | tipo de tráfico | `cpc`, `organic`, `email` |
| `utm_campaign` | nombre de campaña (CBO/ABO + fecha) | `cbo-escalado-agosto`, `abo-test-creativos-v3` |
| `utm_content` | variante de creativo | `angulo-dolor-v1`, `angulo-comparativa-v2` |

**Regla:** nunca añadir UTMs al tráfico orgánico o directo — sobreescribe la atribución automática y ensucia los datos.

## Checklist de salud del tracking (revisar antes de escalar presupuesto)
- [ ] El evento `purchase` dispara una sola vez por pedido (no duplicado).
- [ ] El valor (`value`) y la moneda (`currency`) llegan correctamente en `purchase`.
- [ ] CAPI de Meta está activo, no solo el pixel de navegador.
- [ ] Las campañas llevan UTM consistentes con la tabla de arriba.
- [ ] GA4 y Meta Ads Manager muestran números de conversión razonablemente cercanos (si difieren mucho, hay un problema de atribución o duplicación).

**Ver también:** [[../04_Marketing y Ads/Estrategia Meta Ads CBO-ABO]], [[../04_Marketing y Ads/Presupuesto de Arranque]].
