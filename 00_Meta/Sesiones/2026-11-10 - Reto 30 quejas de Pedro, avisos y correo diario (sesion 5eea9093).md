---
title: "Sesión - 2026-11-10 - Reto 30: quejas de Pedro, aviso al entrar y correo diario"
date: 2026-11-10
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Reto-30/Software/Guia - Skills y reglas por fase]]"
sesion_id: 5eea9093-3ca7-4ca2-bd3f-96266a8f17c6
tags:
  - sesion
  - reto-30
aliases: []
---

# Sesión — 2026-11-10: Reto 30, quejas de Pedro

> [!resumen] En cristiano
> Pedro se quejó de que los muñecos de palitos eran malos, que algunos ejercicios no mostraban nada y que el día repetía ejercicios. Se sustituyeron por fotos de una librería libre, se evitó repetir imágenes en un mismo día, se añadió un aviso al entrar si falta el día, vídeo en el reto extra y un correo diario. Quedó en 5 commits locales sin subir. Para que funcione en producción faltan una migración y 4 variables.

## Contexto
Repo `~/Proyectos/reto-30` (app de Factory Training de Haytham y Pedro; Next 16, Supabase, Playwright, Vitest). Continúa el trabajo de `[[00_Meta/Sesiones/2026-11-09 - Reto 30 descripciones y fotos de ejercicios (sesiones cf1fa63d y 9e8b3cb4)]]`.

## Qué se hizo
- Fotos de `free-exercise-db` (dominio público) para los ejercicios; sustitutos equivalentes sin repetir ejercicio en el mismo día (`src/lib/exercise-guide.ts`); «Sin ilustración» si no queda sustituto libre.
- Aviso al entrar si falta el día de hoy, con acceso directo.
- Vídeo opcional en el reto extra.
- Correo diario con cron de Vercel (06:00 UTC) y Resend.
- Arreglo del test e2e del plan Dúo (`e2e/reglas.spec.ts`): esperaba «Quique» en el primer h2 y sale «Racha conjunta».
- Borradas 22 carpetas `public/exercises/Gen_*` y `scripts/gen-exercise-gifs.py` tras comprobar `git status` (recuperables del último commit).
- Pasaron lint, tipos, 152 tests unitarios, build y 7 tests e2e.

## Commits (sobre `main`, sin push)
`43c7b80` sustitutos y borrado de Gen_* · `883c786` aviso al entrar · `13aacf3` vídeo del extra · `9ade7c3` correo diario · `450378a` arreglo e2e de Dúo.

## Decisiones y porqué
- Librería libre y no GIFs generados: los muñecos de palitos eran la queja principal.
- Variables secretas solo en Vercel; `.env.example` con huecos vacíos.

## Pendientes y próximos pasos
- Aplicar la migración `20261110120000_extra_video.sql` en Supabase.
- Poner en Vercel `CRON_SECRET`, `RESEND_API_KEY`, `MAIL_FROM` y `SITE_URL` (Resend necesita dominio verificado).
- Probar el envío del correo y ver la app en el navegador con una cuenta real.
- 22 ejercicios sin foto abierta (sombra de boxeo, burpee…): decidir si se generan con IA (de pago, Bloom).
- Decidir el push a `origin`.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
