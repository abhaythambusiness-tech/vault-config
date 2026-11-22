---
title: "Sesión - 2026-10-31 - Barber DF - propuestas UI-UX, maquetas y arreglo de subida de fotos"
date: 2026-10-31
type: meta/sesion
proyecto: "[[Barber-DF]]"
sesion_id: f4d211cc-2c42-4a4b-8c26-546a57577e14
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-10-31: Barber DF: propuestas UI/UX, maquetas y arreglo de subida de fotos

> [!resumen] En cristiano
> Se revisó la app de la barbería con propuestas de mejora como las de Reto 30, se hicieron dos maquetas y se aplicaron en una rama. Después se arregló la subida de fotos, que fallaba probablemente por el peso de las fotos de móvil.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `f4d211cc`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Nota `01_Projects/Barber-DF - Propuestas de mejora.md` y dos maquetas HTML.
- Segunda maqueta: barra de reserva fija, galería y reseñas arriba en la landing; agenda de hoy primero y acciones rápidas por cita en el panel.
- Aplicado en rama y subido.
- Arreglo de subida: las fotos se reducen en el navegador (máx. 1600 px, JPEG) y el límite de Next sube a 4 MB; igual para la foto de perfil. Commit `71eea30` en `main`; `tsc` y build limpios.

## Decisiones tomadas
- Trabajar en rama y luego subir.

## Archivos y proyectos afectados
- `01_Projects/Barber-DF - Propuestas de mejora.md`
- `next.config.ts`

## Problemas
- Causa del fallo de subida probable pero no confirmada (sin acceso a logs de Vercel); no se probó una subida real.

## Mejoras propuestas
- Ninguna registrada.

## Pendientes y próximos pasos
- Si sigue fallando: comprobar `SUPABASE_SERVICE_ROLE_KEY` en Vercel, bucket `barber-assets` público y rol `barber` del usuario.

## Relacionado
- [[Barber-DF]]
- [[Barber-DF - Propuestas de mejora]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
