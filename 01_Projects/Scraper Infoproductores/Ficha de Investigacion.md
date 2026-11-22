---
type: ficha-investigacion
proyecto: "Scraper Infoproductores"
tipo: micro-saas
status: aprobada
date: 2026-11-01
origen: mixto
---

> [!resumen] En cristiano
> Antes del TRD apuntamos qué piezas ya hechas usaremos, qué herramientas nos ayudan y con qué nos compararemos. Propuesta: partir de `starter-saas` (login, base de datos y cobro con Stripe ya listos) y de lo aprendido en Laya Leads (recoger datos sin saturar a nadie). **Ojo**: Laya Leads concluye que la IA Laya "se probó y no sirvió" y clasifica con reglas de código; hay que decidir si aquí Laya clasifica o se hace igual con reglas. Pendiente de tu aprobación.

# Ficha de Investigación

## Librerías
Fuentes revisadas: `librerias.md` y notas del vault. context7 y npm se contrastan en el TRD, antes de fijar versión.

| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| Base web + login + datos por usuario | `starter-saas` lite (Next 16, Supabase `@supabase/ssr`, RLS) | Bun + SQLite como el CRM | **A**: ya probado, login y RLS hechos | `librerias.md`, [[Starter SaaS]] |
| Cobro mensual | Stripe Checkout + portal + webhook (`stripe` 23) | Lemon Squeezy | **A**: ya en el starter, modo prueba | `librerias.md` |
| Créditos | Tabla de movimientos en Postgres (saldo = suma, nunca un contador suelto) | Contador en Stripe | **A**: auditable y a prueba de reintentos | Por diseñar en el TRD |
| Recogida de páginas con anti-bot | Scrapling (venv en Zorin) | Playwright | **Por decidir**: Scrapling si hay Cloudflare; Playwright ya tiene trampas anotadas | `skills-frecuentes.md`, `librerias.md` |
| Anuncios de Meta | API oficial Ad Library | Scraping de la web | **A**: oficial, menos riesgo legal (verificar alcance en España con context7/docs) | Por verificar |
| YouTube | YouTube Data API v3 | Scraping | **A**: oficial y con cuota | Por verificar |
| Instagram y Hotmart/Digistore | Solo datos públicos, sin login | Servicios de terceros de pago | **Por decidir en el TRD**: es el punto de mayor riesgo legal y técnico | [[Laya Leads]] |
| Clasificación | Reglas en código (como Laya Leads) | Laya (IA) | **A (decidido por Haytham, 2026-11-01)**: Laya Leads descartó la IA por no servir; Laya se puede probar en una v2 | [[Laya Leads]] |
| Ejecución de recogidas | Servidor Zorin con timers de systemd | Cron en nube | **A**: ya existe `laya-leads.timer`, sin coste | CLAUDE.md global |

## Skills y agentes
- Validar: `project-idea-validator` antes del TRD; `investigador` para competencia (ad-spy, listas de leads).
- Datos: `supabase`, `supabase-postgres-best-practices`; MCP `supabase` (`list_tables`) si hay BD remota.
- Recogida: `scrapling-official` y agente `scraper`; `robots.txt`, 1 s de espera, como en Laya Leads.
- UI: identidad primero (`rules/identidad-y-dinamismo.md`), luego `hallmark` o `design-taste-frontend`, `bklit-ui` para gráficas de lanzamientos, `vercel-react-best-practices`.
- Textos: `marketing-skills:copywriting` y `humanizer` en la web de venta (nunca en textos legales).
- Cierre: `revisor-codigo`, `auditor-web`, `differential-review` en pagos y datos personales, `pre-ship-gate`.

## Referencias
Comparar al final contra [[Biblioteca de Referencias Premium]]:
- **Linear**: SaaS sobrio, jerarquía clara con pocas cosas bien alineadas (para la tabla de resultados).
- **Vercel**: minimalismo técnico y rejilla (para el buscador y el panel).
- Pendiente: 1 ad-spy o lista de leads real del nicho como referencia de producto (lo busca `investigador`).

## Lecciones aplicables
- Borrado en cascada y ciclo completo crear → refrescar → borrar → refrescar en producción (`COMMON_MISTAKES.md`; clave para la baja RGPD de una ficha).
- Comprobar el esquema real antes de asumir tablas; nada de memoria volátil en lambdas.
- Stripe 23: `current_period_end` está en el `SubscriptionItem`; verificar la firma del webhook con el cuerpo en bruto.
- Pruebas de RLS con `set role` y `reset role` en `finally` para no dar falsos verdes.
- Laya Leads: respetar `robots.txt`, esperar entre peticiones y no guardar en el vault datos de terceros.

## Extras de la vía

### micro-saas
- **Señal de demanda**: débil (conversación en tu formación de lanzamientos). Falta: 5-10 entrevistas y una preventa o pago pequeño antes del TRD. Kill: 60-90 días sin 5 clientes de pago.
- **Antes de cobrar**: [[Checklist pre-cobro (micro SaaS)]] completa. Añadir RGPD: base legal (interés legítimo), aviso a la persona afectada, canal de baja y registro de tratamientos. Revisión legal humana.
- **Riesgo clave**: términos de Instagram, YouTube y Meta frente al scraping, y estimación de facturación presentada como dato.
