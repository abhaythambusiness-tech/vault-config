---
title: "Dropshipping - Debate Multi-Agente y Puntos Ciegos"
date: 2026-08-11
tags: [dropshipping, ecommerce, plan-accion, riesgo, debate, puntos-ciegos]
type: nota
status: activo
related: ["[[00 - Plan Maestro y Cronograma]]", "[[01 - Presupuesto 500 Euros Desglosado]]", "[[02 - Reparto de Roles y Tareas]]", "[[06 - Legal Fiscal Espana-USA-UE]]", "[[../02_Producto/Estudio de Mercado Dropshipping (Agosto 2026)]]"]
origen: mixto
---

# Debate multi-agente sobre el plan (skill agent-debate, Pattern B)

4 agentes con encuadres distintos (Financiero escéptico, Operador realista, Mercado contrarian, Auditor legal/pagos) leyeron todo el vault de forma independiente (Ronda 1), luego se confrontaron entre sí (Ronda 2). Objetivo: encontrar puntos ciegos y supuestos poco realistas antes de lanzar.

## 🔴 Punto más crítico — consenso 4/4 (confianza alta)

**Nadie tiene asignada la vigilancia diaria de la cuenta de pago (Stripe/Shopify Payments), y el presupuesto de 500€ no tiene colchón para un bloqueo/rolling reserve — probabilidad estimada 60-80% dado el perfil de la operación (cuenta nueva, volumen ascendente, sin historial).**

Si ocurre, el negocio no muere por falta de ventas ni por mal producto: muere por caja. El único mecanismo de detección hoy es el check-in semanal (voluntario, sin mecanismo forzoso) — insuficiente, porque Stripe puede retener el 100% del importe cobrado y el colchón de 335-385€ de testing no lo cubre.

**Acción recomendada:** definir HOY quién revisa la cuenta cada día (no semanal) y reservar explícitamente un % del presupuesto como colchón de retención, aunque baje aún más el gasto de testing.

## Segunda cadena de riesgo (también convergente)

Nicho no decidido (el banco de 30 ideas del 10-ago no se filtró contra [[../02_Producto/Estudio de Mercado Dropshipping (Agosto 2026)|el estudio de mercado]] del 11-ago, que marca varias de esas categorías como saturadas) + canal elegido (Shopify+Meta Ads clásico) desalineado con lo que el propio estudio dice que mejor convierte (TikTok Shop/UGC) + presupuesto 6-10x menor que el que el propio vault recomienda (2.000-3.000€ vs 500€).

## Hallazgos por agente (Ronda 1, resumen)

**Financiero escéptico:**
- Presupuesto real necesario según el propio vault: 3.000-5.000€ vs 500€ disponibles.
- Cash-flow negativo estructural (retención Stripe/Shopify 7-21 días) sin colchón.
- Margen no calculado con cifra concreta en ningún archivo del proyecto.
- Devoluciones/chargebacks sin partida presupuestada.
- 100% del presupuesto de ads se da por perdido de antemano (objetivo es señal, no ROAS).

**Operador realista:**
- Dedicación horaria de cada socio no definida en ningún lugar.
- Nadie cubre atención al cliente fuera de horario (desfase EE.UU. 6-9h).
- Check-in semanal es la única salvaguarda contra fuga de presupuesto y es voluntario.
- Reparto de responsabilidad legal/capital entre socios: "pendiente, no lo resuelve el vault".
- Amigo colaborador sostiene el frente de mayor carga (vídeo+SEO) sin compensación ni compromiso.
- Decisión de escalar/pivotar/parar en semana 6 sin mecanismo de desempate si no hay consenso.

**Mercado contrarian:**
- Decisión de nicho aún no tomada; banco de ideas no cruzado con el estudio de mercado posterior.
- Canal de adquisición desalineado con el avatar/estudio.
- Timing de validación (semana 3-6) más lento que los ciclos de viralidad ("semanas").
- Ángulo "diferenciador" de las 30 ideas es en realidad lógica de consumible, no diferenciación de marca.
- Avatar único no decidido pese a la regla propia del vault ("un avatar hasta 100K€/mes").
- Modelo ancla+consumible sigue "por validar", no viene de las fuentes originales.

**Auditor legal/pagos:**
- Bloqueo de pasarela de pago: probabilidad 60-80% en 3-6 meses si escala rápido.
- Rolling reserve no modelado en cash flow — puede retener el 100% del importe cobrado.
- Chargebacks con plazo de resolución 45-120 días vs. envío ya pagado, sin ratio máximo de disputas definido.
- Botón de desistimiento UE mal encuadrado: el mercado principal es EE.UU., donde esa directiva no aplica.
- Alta autónomo con 0-50€ de margen para gestoría — riesgo de recargos por alta tardía.
- IVA en exportaciones a EE.UU. no resuelto, sin fecha ni presupuesto para consulta.

## Incertidumbre principal
No está definida la dedicación horaria real de cada persona. Es la variable que, si se resolviera, probablemente arrastraría solución a la mitad de los demás puntos (nicho, timing, monitorización de cuenta).

## Puntos ciegos de fricción interna (menor severidad, igualmente reales)
- Reparto de responsabilidad legal/capital entre socios sigue "pendiente" en el vault.
- Single point of failure en proveedor sin plan de contingencia si hay rotura de stock a mitad de campaña.
- Riesgo arancelario EE.UU. reconocido pero sin plan B si el checkpoint de semana 1 sale negativo.
