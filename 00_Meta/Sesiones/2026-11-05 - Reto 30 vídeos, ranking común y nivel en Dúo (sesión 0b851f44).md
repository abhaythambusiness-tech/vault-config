---
title: "Sesión - 2026-11-05 - Reto 30 vídeos, ranking común y nivel en Dúo"
date: 2026-11-05
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Reto-30/Idea Original - Factory Training 30 dias]]"
sesion_id:
  - 0b851f44-fc72-496e-ac02-20904c01fcc4
tags:
  - sesion
  - reto-30
aliases: []
---

# Sesión — 2026-11-05: quejas de Pedro sobre Reto 30

> [!resumen] En cristiano
> Pedro se quejó de dos cosas en la app de Reto 30: vídeos repetidos que no coinciden con el ejercicio y un ranking donde no veía a nadie. Los vídeos se corrigieron. El ranking no estaba roto: solo enseñaba a gente del mismo nivel y Pedro es el único «avanzado». Se creó un ranking común y se mostró el nivel de la pareja en el modo Dúo. Todo subido a `main` (Vercel despliega solo); falta comprobarlo con el usuario real.

Código en `~/Proyectos/reto-30/`. Proyecto de Haytham y Pedro, no de NeoZeler.

## Qué se hizo
- **Vídeos**: unos 390 ejercicios compartían solo unas 70 imágenes por reglas demasiado amplias en `src/lib/exercise-guide.ts`. Se reordenaron las reglas (cuello, perro boca abajo, etc.). Commit `f501d66`.
- **Ranking**: en producción hay 3 inscripciones activas: Haytham (medio, dúo), Pedro (avanzado, dúo) y Alejandro (medio, individual). El ranking filtra por nivel, por eso Pedro se veía solo. Haytham pidió «un ranking común»: migración `20261105180000_ranking_comun.sql` con la función `common_ranking()`. Haytham la pegó en el SQL Editor de Supabase (no hubo `DATABASE_URL` para aplicarla desde aquí) y se comprobó que existe. Commit `96b7d8f`.
- **Dúo**: la pareja Haytham–Pedro tiene niveles distintos. El nivel no afecta a la racha conjunta (se cuenta por jornadas en común), y ahora vale 0 por otro motivo. Ninguna pantalla asume el mismo nivel. Se añadió `partner_level` a `duo_overview()` (migración `20261105190000_duo_partner_level.sql`) y se muestra «Nivel» del otro en `ParejaView.tsx` y `PartnerStrip.tsx`, con aclaración de que los comodines dependen del nivel. Commit `48b614d`, push a `main`.

## Decisiones tomadas
- Ranking único para todos los niveles, con el mismo orden de siempre.
- Migraciones pegadas por Haytham a mano; Claude no ejecuta SQL en producción sin cadena de conexión.

## Aprendizajes
- Ranking vacío por diseño no es fallo: antes de tocar código, mirar los datos reales.
- La clave de servicio solo sirve para la API REST, no para SQL.
- El repo no tenía identidad git: commits con `abhaythambusiness-tech`, sin guardarla en la configuración. `.gitignore` sigue modificado y fuera de los commits.

## Problemas abiertos
- No se comprobó que el rol `authenticated` pueda ejecutar `common_ranking()` ni que `duo_overview()` devuelva `partner_level`; verlo en `/reto/pareja` (debe poner «Nivel Avanzado» bajo Pedro).
- Los vídeos siguen siendo genéricos para muchos ejercicios (solo ~70 imágenes).

## Próximos pasos
- Comprobar el despliegue en Vercel y ambas pantallas con el usuario real.
- Decidir si se amplía el banco de imágenes de ejercicios.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
