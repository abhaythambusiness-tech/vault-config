---
type: guia
status: activo
date: '2026-10-28'
tags:
- micro-saas
- saas
- startup
- clasificacion
origen: humano
---

> [!resumen] En cristiano
> Son **tres negocios distintos** y cada uno lleva su propia vía de trabajo. Un **micro SaaS** es un negocio pequeño de una persona: una cosa, para un nicho muy concreto, barato, que se construye en semanas y se mantiene con poco. Un **SaaS** (a secas) es un producto de suscripción para empresas con equipos: más funciones, varios roles, soporte y un negocio que crece con calma y gana dinero. Una **startup** es una empresa hecha para crecer muy rápido en un mercado grande, probando hipótesis y quizá buscando inversión; ni siquiera tiene por qué ser software. La diferencia no es la tecnología, es **la ambición y el tamaño**: cuanto más arriba, más pesada la regla. Al empezar, lo primero es decidir cuál es. Las cifras son criterios nuestros orientativos, no datos de mercado.

## 1. Tres ejes que no hay que mezclar
- **Micro** habla del **tamaño** (una persona, un nicho, v1 en semanas).
- **SaaS** habla del **modelo de ingresos** (suscripción mensual por software).
- **Startup** habla de la **ambición** (crecer rápido, mercado grande, posible inversión).

Un micro SaaS y un SaaS son negocios de suscripción que ganan dinero de forma normal. Una startup puede cobrar por suscripción (startup SaaS) o no. En nuestro sistema las tres son **vías de trabajo** y se elige una.

## 2. Cómo decidir la vía (pregunta 0 de `/nuevo-proyecto`)
Se contesta en este orden y se para en el primer «sí»:

1. **¿El plan es crecer muy rápido y/o levantar dinero, en un mercado grande?** → **Startup.**
2. **¿Se cumplen las cuatro?** (a) un solo tipo de usuario y un problema; (b) la v1 cabe en **≤ 1 mes**; (c) la mantiene **una persona** sin horas fijas; (d) no depende de ventas. → **Micro SaaS.**
3. En cualquier otro caso (producto de suscripción con equipos, roles o ventas, pero sin plan de hipercrecimiento) → **SaaS.**

Si dudas entre dos, empieza por la **más ligera** y promociona el proyecto cuando pase el criterio de §5.

## 3. Comparativa

| Aspecto | Micro SaaS | SaaS | Startup |
|---|---|---|---|
| Objetivo | Ingreso recurrente modesto y estable | Ingreso recurrente que crece y es rentable | Crecimiento rápido, mercado grande, posible salida o inversión |
| Cliente | Individuo o negocio pequeño, nicho estrecho | Pymes y empresas con equipos y varios roles | Mercado amplio; empieza en una cuña concreta |
| Precio orientativo | 9-49 €/mes, autoservicio | 29-299 €/mes por plan o puesto | Planes por puesto/uso; ventas si el cliente es grande |
| Canal | SEO, comunidades, directorios; sin ventas | SEO + outbound ligero + partners | Outbound, partners, producto-led + ventas, medido por CAC |
| Validación (Paso 0) | 5-10 entrevistas + preventa o pago pequeño | 10 entrevistas + 2-3 pilotos de pago | 10+ entrevistas + piloto de pago + hipótesis de CAC, retención y tamaño de mercado |
| Documentos del flujo | PRD + TRD corto + Plan (como «proyecto pequeño»); resto `no-aplica` con motivo | Los 6 completos y aprobados en orden | Los 6 + en el PRD: hipótesis a probar y métrica norte |
| Arquitectura | Usuario único o equipos simples; pruebas + producción | Multi-organización, roles, staging | Lo de SaaS + observabilidad, analítica de producto y capacidad de escalar |
| Cobros | Un plan o dos, Stripe Checkout/portal | Planes, asientos, facturas, impagos | Asientos, uso, impuestos, experimentos de precio |
| Seguridad y legal | [[Checklist pre-cobro (micro SaaS)]] completa (nunca se recorta) | Lo anterior + DPA y registro de brechas | Lo anterior + revisión legal y valorar SOC 2 |
| Soporte | Email y FAQ | Horario definido, SLA ligero | SLA, runbooks, guardias |
| CI y revisión | CI verde + revisor de solo lectura + merge humano | Lo anterior + staging obligatorio | Lo anterior + revisión de dos personas en auth y pagos |
| Kill (cuándo parar) | 60-90 días sin 5 clientes de pago | 6 meses sin llegar al MRR objetivo fijado | Hitos trimestrales de retención e ingresos; si fallan dos seguidos, parar o pivotar |
| Starter | `starter-saas` **lite** | `starter-saas` **org** (multi-tenant) | `starter-saas` **org** + analítica |

## 4. Lo que NO cambia (suelo común)
- Spec primero (SPEC.md), verificación pass/fail y evidencia (comando y salida).
- [[Checklist pre-cobro (micro SaaS)]] completa antes del primer cobro, en las tres vías.
- Git desde el primer commit, cero secretos en el repo, hooks de bloqueo (`guard-destructive.py`), MCP de datos solo en desarrollo y de solo lectura.
- Identidad aprobada antes de maquetar (UI-UX §2, §5, §7).

## 5. Cuándo se promociona un proyecto
- **Micro → SaaS**, tras 3 meses con alguna de estas: clientes pidiendo **equipos y roles**, facturación por puestos o uso, un cliente que exige **DPA o auditoría**, o más soporte del que una persona asume. Se abren los documentos que estaban `no-aplica` y se activa el starter *org*; el cambio de arquitectura es un proyecto (PRD de la v2).
- **SaaS → Startup**, solo si se toma la decisión explícita de apostar por crecer rápido o buscar inversión (y hay evidencia de mercado grande). No es un paso automático: muchos SaaS son un buen negocio sin ser startup.
- **Hacia abajo** también vale: una startup que no despega puede cerrarse como SaaS o micro si sigue dando ingresos con poco trabajo.

## 6. Registro por proyecto
En el PRD (§1) se escribe la vía elegida (`tipo: micro-saas | saas | startup`) y la señal de validación obtenida; el [[Dashboard - Proyectos de Software]] puede filtrar por ese campo.

Relacionado: [[00 - Flujo de Software]] · [[Claude Code para micro SaaS y startups]] · [[Starter Kits NeoZeler]].
