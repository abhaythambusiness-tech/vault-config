---
title: "Sesión - 2026-11-02 - Reto 30 - producción, ejercicios y acceso por aprobación"
date: 2026-11-02
type: meta/sesion
proyecto: "[[01_Projects/Reto-30/Reto 30 - App real]]"
sesion_id: 8b485c03-5f5d-4da0-9245-4a0e67ff7096
tags:
  - sesion
  - cierre-automatico
aliases: []
origen: mixto
---

# Reto 30 — puesta en producción: ejercicios, acceso y admin de prueba

> [!resumen] En cristiano
> Se revisó la app de Reto 30 para publicarla de verdad. Se corrigió el reparto de ejercicios (30 por nivel más 10 extras), se cambió el alta para que cada persona quede «pendiente» hasta que un admin la acepte, y se creó un admin de prueba. Falta que Haytham ejecute una migración en Supabase y confirme que el flujo sin correo funciona.

## Contexto
Continuación del trabajo de [[01_Projects/Reto-30/Reto 30 - App real|Reto 30 - App real]] (repo `~/Proyectos/reto-30`, Next.js + Supabase + Vercel). La sesión se retomó una vez tras agotar contexto. Complementa la nota 2026-11-02 - Reto 30 - auditoría de UI-UX, arreglos y PR #3.

## Qué se hizo
- Auditoría de la app «para producción» y arranque de arreglos.
- Ejercicios: `Ejercicios.txt` se convirtió en un `seed.sql` nuevo con 90 ejercicios (30 por nivel) y 10 retos extra (días 3, 6… 30). Scripts nuevos `supabase/reset-public.sql` (destructivo, se avisó) y `supabase/reemplazar-ejercicios.sql`; Haytham los aplicó.
- Error `type "app_role" already exists` al reejecutar el SQL: se dio un SQL que no choca.
- Alta con aprobación: nueva migración `20261102140000_alta_pendiente.sql` (estado por defecto `pendiente`), pantalla de espera «Estamos revisando tu acceso» en `/empezar`, tarjeta «Pendientes» y botón «Activar acceso» en el panel de admin.
- Despliegue: Vercel despliega solo desde `main`; se subieron los cambios (último push `ea388eb..29800ec`). Se descubrió que Vercel bloquea commits con un correo no vinculado a GitHub y se usó el correo noreply.
- Admin ficticio: `admin@reto30.test` creado con `npm run staff:create` (necesita Node 20+; se usó el Node 24 de Playwright). Nuevo script `scripts/staff-link.mjs` para generar un enlace de acceso de un solo uso.
- Arreglo de un fallo en Pareja/«Hoy» con plan Dúo sin pareja (nombre `null`): arreglado en `ParejaView.tsx` y `PartnerStrip.tsx`, commit `29800ec`.

## Decisiones tomadas
- Sin correo propio ni dominio: se usa la misma base de Supabase que en desarrollo.
- Sin alta libre: el admin acepta desde el panel y mientras tanto la persona ve una pantalla de espera.
- Quitar la confirmación de correo («prefiero quitar eso, mejor sin confirmación»): el correo de Supabase solo envía ~2 al día y solo a miembros de la organización.

## Aprendizajes (para futuras sesiones)
- El correo integrado de Supabase no sirve para producción real (límite bajo, plantilla por defecto sin código).
- El Node del sistema es 18: para `--env-file` hay que usar el Node 24 de Playwright (`~/.cache/ms-playwright-go/1.57.0`).
- El comando de ejemplo lleva `TU_CLAVE` como marcador; se avisó de que si se usó tal cual, es una contraseña débil. No se copia ninguna contraseña aquí.

## Próximos pasos
- Ejecutar en el editor SQL de Supabase la migración `20261102140000_alta_pendiente.sql` (no confirmado).
- Desactivar «Confirm email» en Supabase (Authentication → Sign In / Providers → Email) y probar el flujo completo: crear → refrescar → borrar → refrescar.
- Cambiar la contraseña del admin ficticio antes de abrir al público.
- `scripts/staff-link.mjs` y su script de `package.json` estaban sin commitear; las pruebas e2e no se ejecutaron.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[2026-11-02 - Cierre nocturno]]
