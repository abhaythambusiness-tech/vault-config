---
title: 'Sesión - 2026-11-14 - NeoFlow pitch: transcripción del testimonio y competencia'
date: '2026-11-14'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/NeoFlow AI]]'
sesion_id: 08c69906-9493-4f79-9976-d4efb821836f
tags:
- sesion
---

> [!resumen] En cristiano
> Se ajustó la landing de NeoFlow (`~/Proyectos/neoflow-pitch/`): la transcripción del vídeo de testimonio va ahora en un recuadro junto al vídeo, y la diapositiva de competencia se simplificó con números totales y definiciones cortas. Todo subido a `main`, pero nada se vio renderizado y Vercel puede no estar actualizado.

## Qué se hizo
- Recuadro de transcripción (sin marcas de tiempo) al lado del vídeo de Javier López; commits `3171370` y `49f4fba`.
- Se comprobó que el repo ya equivale a la versión anterior (`a40b202`) con solo la transcripción encima; la versión «Premium» (`88a77b4`) no está en el código.
- Diapositiva del problema devuelta a su texto anterior (`889774c`).
- Competencia: 61 guardadas = 49 agencias/freelancers de IA en España (7 en Málaga) + 6 consultoras grandes + 6 de software; sin lista de call centers ni nombres de competidores; «a medida» corregido (`58c74db`, `8e21ac4`, `fb3a52a`).

## Decisiones
- Sin nombres de competidores, solo definiciones breves.

## Problemas y pendientes
- Vercel muestra una versión vieja: el repo no tiene `.vercel/`, probablemente se subió con la CLI; falta decidir si se republica con `npx vercel --prod` (pide permiso de Haytham).
- Nada se vio renderizado; comprobar que las tarjetas de competencia no se desbordan.
- La lista de cambios que Haytham iba a dictar al inicio no llegó en esta sesión.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

