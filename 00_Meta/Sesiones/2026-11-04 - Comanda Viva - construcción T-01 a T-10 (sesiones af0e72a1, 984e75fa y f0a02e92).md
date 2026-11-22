---
title: "Sesión - 2026-11-04 - Comanda Viva - construcción T-01 a T-10"
date: 2026-11-04
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Comanda Viva]]"
sesion_id:
  - af0e72a1-5bbf-421a-a978-00944a0d2e05
  - 984e75fa-1a35-4466-8d05-f27cf71e0daa
  - f0a02e92-1867-4be4-9a72-c90b0832a55e
tags:
  - sesion
  - comanda-viva
aliases: []
---

# Sesión — 2026-11-04: Comanda Viva, de los documentos al código (T-01 a T-10)

> [!resumen] En cristiano
> Primero se aprobaron los documentos de Comanda Viva y se eligieron referencias de diseño en Dribbble. Después se empezó a programar: el menú por QR, el carrito, «Mi mesa», el login y el tablero de caja con avisos en vivo. La primera cara del menú no gustó («como de niño chico») y se rehízo con un estilo más sobrio. Falta crear el Supabase real, así que lo «en vivo» aún no se ha probado de verdad.

Complementa a [[2026-11-04 - Comanda Viva]], que cubre solo la parte de documentos y diseño de papel. Las tres sesiones son una cadena: cada una continúa a la anterior tras agotar el contexto.

## Qué se hizo
- **Referencias (fase 0b de `diseno-central`)**: 8 shots de Dribbble. Haytham eligió menú del cliente = mezcla de los 2 y 5, caja y administración = mezcla de los 6 y 7. Se aprobaron PRD, Ficha, TRD, identidad, Paleta, UI/UX + AppFlow, Backend Schema y Plan.
- **Código** en `~/Proyectos/comanda-viva/` (commits en orden):
  - T-02 esquema + RLS + 20 pruebas PGlite; T-01 scaffold Next 16 + Tailwind 4; T-03 clientes Supabase, proxy, esquemas Zod y pruebas RPC.
  - T-04 menú `/m/[token]` en tres rondas: tarjetas pastel (revertida), filas con bloque destacado, y por fin la «dirección sobria» aprobada.
  - T-05 hoja de detalle con nota de 140 caracteres; T-06 carrito en `sessionStorage` y envío con clave de idempotencia; T-07 `get_pedidos_mesa` y «Mi mesa»; T-08 menú vivo con sondeo cada 3 s; T-09 login con Supabase Auth y guarda de `/caja` y `/admin`; T-10 tablero de caja con Realtime privado, sondeo de 5 s y sonido (`107e39d`).
- Se escribieron los prompts de Gemini para las 6 fotos de platos: [[Prompts Gemini - Fotos de platos]] en `01_Projects/Comanda Viva/`.
- README y `resumen.html` del repo creados (regla del vault §0.8).

## Decisiones
- Haytham rechazó la primera UI («como el culo», «Rumbo… de niño chico») y pidió ver también caja, administración y finanzas, no solo el menú. Se hizo una maqueta sobria del conjunto y la aprobó.
- Sondeo + Realtime a la vez: si Realtime falla, aparece la banda «Sin conexión en vivo, actualizando cada 5 s».
- Las fotos de platos generadas con IA valen para maquetar; para producción, que Monika mande las suyas.
- Sin crear recursos en la nube sin permiso (Supabase/Vercel).

## Problemas
- T-04 se rehízo tres veces por gusto visual.
- Node 18 por defecto rompe `npx shadcn`; hay que usar Node 22 (`fnm`).
- Al final, sin CLI ni token de Supabase en este PC: no se pudo crear el proyecto.

## Archivos y proyectos afectados
`~/Proyectos/comanda-viva/` (16 commits, sin push), `01_Projects/Comanda Viva/` (documentos 1-6, Paleta, Guía de skills, Prompts Gemini), `DESIGN-IDENTITY.md`.

## Mejoras propuestas
- Pasar las maquetas de las 4 pantallas por captura 375/768/1280 antes de aprobar cada ronda, no después de programar.
- Que el plan marque qué tareas necesitan Supabase real, para no dejar «hecho cuando» sin comprobar.

## Pendientes y próximos pasos
- Decidir cómo crear el proyecto Supabase (CLI + token, o crearlo Haytham) y aplicar la migración `20261104173123_init.sql`.
- Comprobar en real el criterio de T-10 («un pedido de T-06 aparece en caja sin recargar y suena»), la política `caja_recibe` sobre `realtime.messages` y la consulta con `cuentas!inner`.
- Lighthouse pendiente; hacer push cuando Haytham lo pida; seguir con T-11.
- Pasar las fotos reales (o las de Gemini) a `assets-origen/fotos/`.
- Sigue abierto el reparto con la clienta y el hosting.

## Relacionado
- [[01_Projects/Comanda Viva]] · [[2026-11-04 - Comanda Viva]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
