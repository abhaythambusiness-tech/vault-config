---
title: 'NeoFlow pitch: nueva versión sobre la anterior'
date: '2026-11-14'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/NeoFlow AI]]'
sesion_id:
- 08c69906-9493-4f79-9976-d4efb821836f
tags:
- sesion
- neoflow
- pitch
---

> [!resumen] En cristiano
> Se rehízo el pitch de NeoFlow AI sobre la versión anterior (sin lo de «Premium»). Quedan 9 diapositivas: se quitaron Competencia y Go to market, se fusionaron equipo y cierre, y el modelo de negocio pasó a START / GROW / SCALE. Todo está subido a GitHub (`main`). La web de Vercel puede seguir mostrando una versión vieja.

## Qué se hizo (repo `~/Proyectos/neoflow-pitch/`)
- **Testimonio:** transcripción en recuadro junto al vídeo, sin marcas de tiempo.
- **Problema:** vuelve el título anterior, sin el caso de Javier.
- **Solución:** kicker «La solución · Un sistema», «Se conecta a uno de estos canales», iconos de robot.
- **Demo:** quitadas las tres tarjetas Atiende / Agenda / Archiva.
- **Modelo de negocio:** START 1.500 €, GROW 4.500 € el primer año (1.500 + 250 × 12), SCALE ecosistema ampliado; frase «Un producto que se instala y se paga cada mes» pequeña abajo.
- **Mercado:** TAM España 665,8 M€, SAM Andalucía 108,5 M€, SOM Málaga 28,6 M€; mapa con España azul, Andalucía ámbar y Málaga verde. Implementación por cliente 1.500 €.
- **Roadmap:** línea de tiempo 2026-2029 con ingresos (1,35 M€ en 2027, 2,4 M€ en 2028, 5 M€ en 2029).
- **Equipo + cierre:** una sola diapositiva final con contacto y QR.
- **Quitadas:** Competencia y Go to market.

## Aprendizajes
- Ninguna diapositiva se vio renderizada: el sistema bloqueó el servidor local para mirarla.
- El repo ya estaba en la versión anterior tras el revert; lo que se veía en Vercel era un despliegue viejo (no hay `.vercel/` en el repo).
- No usar frases de posicionamiento («producto, no a medida») sin confirmarlas con Haytham (COMMON_MISTAKES 94).

## Pendiente
- Confirmar la base de las cifras TAM/SAM/SOM y ponerles fuente.
- 1,35 M€ de 2027 lo calculó Claude (300 × 4.500 €); confirmar.
- Republicar en Vercel (`npx vercel --prod`) si se quiere ver esta versión.
- Revisar en pantalla las 9 diapositivas (hueco en Demo, desbordes en Modelo y Equipo).

