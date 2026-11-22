---
type: sesion
status: cerrada
date: '2026-10-28'
proyecto: '[[Starter SaaS]]'
origen: mixto
---

> [!resumen] En cristiano
> Se construyó `~/Proyectos/starter-saas`, la plantilla para arrancar micro SaaS, SaaS y startups, con las dos vías (lite y org) de la nota de tipos de producto. Trae inicio de sesión, datos aislados con pruebas, cobro de prueba con Stripe y la checklist pre-cobro con un script que revisa lo automático. Verificado en local; falta probarlo con Supabase y Stripe reales.

## Qué se hizo
- Repo nuevo con git y `SPEC.md` primero; Next.js 16.4.1, Supabase (`@supabase/ssr`), Stripe 23, vitest y PGlite. Archivos preparados, **sin commit** (a decidir con Haytham).
- Migraciones `0001_base.sql` (lite) y `0002_org.sql` (org) con RLS, funciones `security definer` y escrituras sensibles solo para `service_role`.
- 62 pruebas, `precobro` 13/13, build de las dos vías, humo HTTP. Ficha: [[Starter SaaS]].

## Aprendizajes
- Las pruebas encontraron dos fallos reales de mi SQL (un sondeo de membresía y un `revoke` de más). Y una mutación sobrevivía hasta añadir la prueba de privilegios: COMMON_MISTAKES 70.
- Mi hook `guard-destructive.py` bloqueó dos heredocs por el texto «terraform destroy» que llevaban dentro: COMMON_MISTAKES 69.
- En `stripe` 23, `current_period_end` está en el ítem de la suscripción, no en la suscripción (`librerias.md`).
- Decisión: PGlite en vez de Docker (no hay Docker en el equipo); no sustituye la prueba contra Supabase real.
