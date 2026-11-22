---
date: '2026-10-02'
negocio: Barber.DF
repo: ~/Proyectos/barber-df
status: congelado
tags:
- barberia
- reservas
- nextjs
- supabase
- mobile-first
- pwa
type: proyecto
origen: mixto
---

# Proyecto Barber.DF — Reserva y Gestión de Barbería Urbana

## Resumen
Web app mobile-first de reservas y gestión completa para **Barber.DF** (barbería privada / un solo barbero). Flujo de reserva en <4 toques desde Instagram, dirección física privada revelada únicamente el día de la cita, área privada del barbero con agenda en tiempo real, gestión de disponibilidad y servicios.

- **Repositorio de código**: `~/Proyectos/barber-df/`
- **Stack**: Next.js 15+ (App Router, Server Actions), TypeScript estricto, Tailwind CSS v4 con `@theme`, shadcn/ui + Radix, Supabase (Postgres, RLS, Storage, Realtime, Edge Functions), TanStack Query, date-fns/tz (Europe/Madrid), Motion, Resend.
- **Identidad**: Estética streetwear / barbería urbana premium, paleta dark-first (`#0A0A0A`), acentos en verde lima (`#BAF225`), tipografía display condensada (`Bebas Neue` / `Anton`) y detalle de marcador urbano (`Permanent Marker`).

## Estado de Implementación
- [x] **Fase 1**: Proyecto base, tokens de marca (`#0A0A0A`, `#BAF225`), layout mobile-first, landing con logo oficial y servicios.
- [x] **Fase 2**: Supabase: esquema SQL, extensión `btree_gist`, RLS policies, auth y middleware de protección de roles.
- [x] **Fase 3**: Motor de disponibilidad en `Europe/Madrid`, anti-solapamiento GiST, flujo de reserva en <4 toques y tests unitarios.
- [x] **Fase 4**: Panel del barbero (`/barbero`): agenda Realtime, gestión de horario semanal y excepciones, catálogo de servicios, directorio de clientes y ajustes con dirección privada.
- [x] **Fase 5**: Sistema de reseñas verificadas (citas completadas), moderación/respuestas del barbero y área de cliente (`/mis-citas`, `/mi-cuenta`) con cancelación online.
- [x] **Fase 6**: Notificaciones transaccionales vía Resend (confirmación al cliente, alerta de nueva cita al barbero, cancelación de cita), recordatorio con revelación de dirección secreta (`/api/cron/send-reminders`), y PWA instalable (manifest, service worker con cache inteligente, iconos 192/512/maskable y prompt de instalación en inicio).
- [x] **Fase 7**: Accesibilidad WCAG AA (`focus-visible`, `prefers-reduced-motion`), SEO local con JSON-LD Schema.org (`HairSalon`), `robots.ts` y `sitemap.ts`.
- [x] **Mejoras Operativas**: Separación e invisibilidad estricta de áreas cliente/barbero, gestión y subida de foto de perfil del barbero (`/barbero/ajustes`) almacenada en Supabase Storage (`barber-assets`) con reflejo inmediato en la landing page.
- [x] **Flujo de Reserva Blindado & Estética 3D**: Autenticación previa obligatoria antes de reservar (redirigiendo a `/login` y preservando el servicio seleccionado), auto-recuperación ante huecos deseleccionados en `BookingFlow`, e integración de tijeras de barbero en 3D estáticas en el fondo de la página pública (`BackgroundScissors.tsx`).
- [x] **Catálogo Oficial de Servicios (4 definitivos)**: Eliminados servicios antiguos. Activos: *Corte menores de 10 años* (4 €, 30 min), *Corte de pelo* (5 €, 30 min), *Corte + Barba + Ceja* (6,50 €, 35 min) y *Corte + (barba) o solo (cejas)* (6 €, 35 min). Sincronizado en base de datos Supabase, constantes y landing page con enlace directo al flujo de reserva.

- [x] **Ofertas y enlace de dos personas (2026-11-03, código escrito, migración pendiente de aplicar)**: página `/ofertas` (cartel: 1 corte 5 €, 2 personas 8 € los dos). Quien pide la oferta de 2 recibe un **código de 6 caracteres** (y enlace de WhatsApp) para su colega; el colega lo canjea en `/reservar?code=XXXXXX` y quedan enlazados (`offer_claims.partner_id`), cada uno con su cita. La oferta de 2 reserva **1 hora** (2 × duración del servicio): quien la pide tiene la primera mitad y, al canjear el código, el colega recibe automáticamente la segunda (no elige hueco). El código caduca al empezar la cita de quien invitó; límite de 1 cita futura por persona y oferta. Precio de oferta (por persona) en emails, agenda del barbero y `/mis-citas`. Migración: `supabase/migrations/20261103000001_offers.sql` (tablas `offers`, `offer_claims`, columna `appointments.offer_claim_id`). Panel del barbero `/barbero/ofertas` (pestaña «Ofertas»): crear, editar, pausar y borrar ofertas (precio = total de la oferta; si ya tiene reservas no se borra, se pausa). Pendiente: aplicar la migración en el SQL editor de Supabase antes de desplegar.

## Cierre de Sesión (2026-10-02)
- Fases 1 a 7 completadas al 100%.
- Bug de colisión horaria y paso 4 de reserva totalmente solventados.
- Notificaciones por email con Resend y PWA instalable operativas.
- Catálogo de precios y servicios oficiales sincronizado.
- Build de producción verificado y código comiteado en `main`.
