---
type: doc-software
doc: plan-implementacion
proyecto: "Scraper Infoproductores"
status: aprobado
date: 2026-11-01
origen: mixto
---

# 6 · Plan de Implementación

> [!resumen] En cristiano
> Orden para construir, en pasos pequeños que se pueden comprobar. Primero la base de datos con el cobro de créditos (lo más delicado), luego la web, luego los programas que recogen datos. **Antes de empezar el paso 0 hay una puerta**: las entrevistas y la preventa del PRD (Paso 0). Sin esa señal, solo se construye la demo con datos de prueba. El plan cabe en ≤ 1 mes de trabajo de una persona (vía micro SaaS).

> [!riesgo] Puertas antes de código
> 1. **Paso 0 (demanda)**: 5-10 entrevistas y una preventa o pago pequeño. Hasta entonces, solo fase 0-1 y la demo de reunión 1 (PRD §10).
> 2. **Fuentes de v1**: decidir con Haytham si v1 usa solo fuentes oficiales y listados públicos (recomendado) o también Instagram/Hotmart/Digistore.
> 3. **Antes de cobrar**: `Checklist pre-cobro (micro SaaS)` y revisión legal humana (RGPD).

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo desde `starter-saas` lite, `.gitignore`, CI, `.env.example`, `components.json` | build limpio | — |
| 1 Datos | Migración y semilla ([[5 - Backend Schema]]) con pruebas de RLS y créditos | tablas y funciones verificadas en PGlite | US-01, US-03, US-09 |
| 2 Núcleo | Registro, búsqueda, ficha, desbloqueo, lista y CSV ([[4 - AppFlow]]) | ciclo completo OK en local | US-01, US-02, US-03, US-05, US-09 |
| 3 UI | Identidad aplicada y pantallas ([[3 - UI-UX Design]]); wordmark SVG dibujado con `svg-skill` | demo navegable + `DESIGN-IDENTITY.md` en el repo | US-01, US-02, US-03 |
| 4 Cobro | Stripe Checkout, portal y webhook que concede créditos | pago de prueba suma saldo, sin duplicar | US-04 |
| 5 Datos reales | Workers de recogida en Zorin, clasificador por reglas, panel admin y baja | fichas reales con fecha; baja efectiva | US-07, US-08 |
| 6 Pulido | Estados, a11y, rendimiento (≤ 150 kB gzip) | checklist técnico | — |
| 7 Despliegue | Vercel + Supabase en producción y ciclo completo | URL en vivo | — |

Fuera de la v1 y sin tareas: US-06 (alertas de nuevos lanzamientos, prioridad Could).

## 2. Tareas
- [x] T-01 · Scaffold del repo desde `starter-saas` lite (Node 22), `git init` con `.gitignore` antes del primer commit, `.proyecto`, `.env.example`, copiar §2, §5 y §7 de UI-UX a `DESIGN-IDENTITY.md` · `~/Proyectos/scraper-infoproductores/` · `npm run build` y `tsc --noEmit` limpios · depende de: puertas
- [ ] T-02 · (US-09) Migración y semilla generadas con `schema_to_migration.py`; función `conceder_creditos_iniciales` · `supabase/migrations/` · prueba: créditos iniciales una sola vez, solo con correo verificado · depende de: T-01
- [ ] T-03 · (US-01) Funciones `ejecutar_busqueda` y `resultados_busqueda` con pruebas de RLS (`set role`/`reset role` en `finally`) · `supabase/tests/` · prueba: misma clave no recobra, paginar es gratis, sin saldo falla, resultados ajenos invisibles · depende de: T-02
- [ ] T-04 · (US-03) Función `desbloquear_contacto` y `mis_contactos` · `supabase/tests/` · prueba: segundo desbloqueo gratis, contacto ilegible fuera de la función, dos peticiones simultáneas no superan el saldo · depende de: T-02
- [ ] T-05 · (US-09) Registro con Google y enlace mágico (`@supabase/ssr`), llamada a créditos iniciales tras verificar · `src/app/(auth)/`, `src/proxy.ts` · hecho: de visitante a búsqueda con saldo visible · depende de: T-02
- [ ] T-06 · Tokens CSS de UI-UX §2.1, fuentes autoalojadas (Hanken Grotesk, JetBrains Mono) y componentes base shadcn · `src/app/globals.css`, `components.json` · hecho: tokens aplicados, contraste medido con herramienta · depende de: T-01
- [ ] T-07 · (US-01) Pantalla de búsqueda y resultados: filtros, coste visible, tabla con `sparkline`, saldo con «tic» · `src/app/buscar/` · hecho: estados vacío, cargando, sin créditos, error y éxito · depende de: T-03, T-05, T-06
- [ ] T-08 · (US-02) Ficha de infoproductor: redes, `composed-chart` de lanzamientos y anuncios, etiqueta «estimada» con método · `src/app/ficha/[slug]/` · hecho: sin contacto visible · depende de: T-07
- [ ] T-09 · (US-03) Desbloqueo en la ficha: bloque borroso, botón con coste, modal sin créditos · `src/app/ficha/[slug]/` · hecho: tras desbloquear queda marcado y no vuelve a cobrar · depende de: T-04, T-08
- [ ] T-10 · (US-05) «Mis contactos» y exportación `/api/contactos.csv` sin coste · `src/app/contactos/`, `src/app/api/contactos.csv/` · hecho: CSV con solo los contactos del usuario · depende de: T-04, T-06
- [ ] T-11 · (US-09, US-01) Landing con buscador en vivo sobre fichas `demo` (contacto borroso) y wordmark SVG propio validado con `scripts/validate.sh` · `src/app/page.tsx`, `public/` · hecho: la portada funciona sin sesión · depende de: T-06, T-07
- [ ] T-12 · (US-04) Planes y créditos: tarjetas, `stat-card-line-01` con saldo, libro de movimientos; Checkout y portal de Stripe en modo prueba · `src/app/planes/`, `src/app/api/stripe/` · hecho: pago de prueba abre Checkout · depende de: T-05, T-06
- [ ] T-13 · (US-04) Webhook `invoice.paid` con firma sobre cuerpo en bruto que llama a `conceder_creditos_plan` · `src/app/api/stripe/webhook/` · prueba: evento repetido no duplica créditos; impago no concede · depende de: T-12
- [ ] T-14 · (US-08) Formulario público de baja, límite por IP y función `procesar_baja` · `src/app/baja/`, `src/app/api/baja/` · hecho: baja procesada borra la ficha y las listas, y queda en la lista de exclusión · depende de: T-02, T-06
- [ ] T-15 · (US-07) Panel admin: mapa de calor de recogidas por fuente, reintento y cola de bajas · `src/app/admin/` · hecho: solo accesible a `admins` · depende de: T-14
- [ ] T-16 · (US-01) Worker YouTube Data API y Meta Ad Library API (fuentes oficiales) con espera, `robots.txt` y registro en `fuentes_estado` · `worker/` en Zorin · hecho: fichas con `captured_at` real · depende de: T-02, puerta de fuentes
- [ ] T-17 · (US-01) Clasificador por reglas (nicho y nivel) y cálculo de `facturacion_estimada` según Backend Schema §6 · `worker/clasificador.py` · prueba: ejemplo 120 × 497 € = 59.640 €; sin datos queda `null` · depende de: T-16
- [ ] T-18 · (US-07) Timers de systemd en Zorin, consulta de `lista_exclusion` antes de guardar · `worker/` · hecho: una pasada por fuente y día sin recoger perfiles dados de baja · depende de: T-16, T-14
- [ ] T-19 · Estados, accesibilidad (axe a cero), responsive a 375/768/1280 y peso de JS ≤ 150 kB gzip · todo `src/` · hecho: bucle visual con el navegador del panel · depende de: T-07 a T-15
- [ ] T-20 · Revisión de solo lectura con `revisor-codigo` y `differential-review` en pagos, créditos y datos personales · todo el repo · hecho: sin hallazgos críticos abiertos · depende de: T-19
- [ ] T-21 · Despliegue en Vercel + Supabase, variables de entorno y ciclo completo en producción · producción · hecho: registro → buscar → desbloquear → baja → refrescar tras cada paso · depende de: T-20

## 2.1 Starter kits reutilizados
| Kit | Fase | Adaptación |
|---|---|---|
| `starter-saas` lite ([[Starter SaaS]]) | 0, 1, 4 | Login, RLS, suscripciones y webhook ya hechos; añadir créditos, búsqueda y fichas |
| Laya Leads (`[[Laya Leads]]`) | 5 | Reutilizar la lógica educada de recogida (espera, `robots.txt`, RAM baja) y el timer; cambiar fuentes y destino a Supabase |
| Pruebas PGlite del starter (`supabase/tests/harness.ts`) | 1 | Copiar el arnés y añadir `email_confirmed_at` a `auth.users` |

## 3. Estrategia de pruebas
- **Unitarias**: reglas de créditos y estimación (SQL en PGlite y Python del clasificador).
- **RLS**: `set role`/`reset role` en `finally` (sin falsos verdes); contactos ilegibles, ledger no escribible, funciones de plan no ejecutables por usuarios.
- **Concurrencia**: dos desbloqueos simultáneos del mismo usuario no superan el saldo.
- **e2e en producción**: registro → créditos gratis → buscar → refrescar → desbloquear → refrescar → baja → refrescar; y pago de prueba → saldo → webhook repetido → saldo igual.
- **Cliente simulado**: tres agentes (closer en móvil, agencia en escritorio, infoproductor que pide baja) recorren el AppFlow antes de maquetar; resultados en la tabla de [[4 - AppFlow]] §5.

## 4. Despliegue y operación
- **Entornos**: local (PGlite) y producción (Vercel + Supabase); sin staging.
- **Variables**: `NEXT_PUBLIC_SUPABASE_*`, `SUPABASE_SERVICE_ROLE_KEY` (solo servidor y workers), claves de Stripe y del webhook, claves de YouTube y Meta en Zorin. Nunca en el repo; `.env.example` versionado.
- **Dominio**: pendiente de elegir.
- **Backups**: copia diaria de Supabase y antes de cada migración.
- **Monitorización**: panel admin de fuentes; alertas de fallo del webhook; revisión semanal de `fuentes_estado`.

## 5. Riesgos y plan B
> [!riesgo]
> - **Sin demanda**: si no hay preventa, no se construye más allá de la demo; kill a 60-90 días sin 5 clientes de pago.
> - **Fuentes bloqueadas o ilegales**: v1 con APIs oficiales y listados públicos; ampliar solo tras revisión legal.
> - **Fichas insuficientes**: meta de 1.000 fichas; si las fuentes oficiales no llegan, ampliar nicho antes que fuentes.
> - **Doble cobro de créditos**: cubierto por claves de idempotencia y candado; prueba de concurrencia obligatoria.
> - **Bundle de gráficas mayor de lo previsto**: medir cada pieza de Bklit al instalar; si pasa de 150 kB gzip, sustituir por SVG propio.
> - **Zorin caído**: los datos viejos siguen visibles con su fecha de captura.

## 6. Definición de terminado
- [ ] `trace_lint.py` en `RESULTADO: OK` y `schema_to_migration.py` sin avisos de FK
- [ ] Build y type-check limpios
- [ ] Checklist técnico/SEO y de marca
- [ ] Pruebas de intercambio y de lejos superadas; cero imágenes pendientes o inventadas; fila añadida a [[Registro de Identidades Visuales]] (ya añadida el 2026-11-01)
- [ ] `Checklist pre-cobro (micro SaaS)` y revisión legal humana antes de cobrar
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado
- [ ] Retro rellenada al cerrar

---
Anterior: [[5 - Backend Schema]]
