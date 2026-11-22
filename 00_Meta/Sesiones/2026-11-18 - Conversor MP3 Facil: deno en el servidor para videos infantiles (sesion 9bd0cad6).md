---
type: sesion
date: '2026-11-18'
proyecto: Conversor MP3 Facil
origen: maquina
sesion_id: 9bd0cad6-2dac-4512-9ca0-b88ff3161ecd
tags:
- sesion
- conversor-mp3
- zorin
---

> [!resumen] En cristiano
> Un vídeo de YouTube daba «el vídeo no existe» en la app del conversor aunque sí existía. Era porque YouTube exige a la herramienta de descarga un pequeño motor de JavaScript que el servidor no tenía. Se instaló `deno` en el servidor y se reinició el servicio. Falta que Haytham pruebe la descarga desde la web.

## Contexto
Proyecto [[01_Projects/Conversor MP3 Facil|Conversor MP3 Facil]] (servicio `conversor-mp3` en el servidor Zorin). Haytham probó la descarga MP4 con `https://www.youtube.com/watch?v=sTVFochzBTo` y la app respondía que el vídeo no existía.

## Qué se hizo
- Diagnóstico: el vídeo existe (`playabilityStatus: OK`), pero `yt-dlp` falla con «This video is not available». Está marcado como «hecho para niños»; YouTube solo entrega formatos a clientes que resuelven un reto de JavaScript.
- Ese reto lo resuelve un runtime moderno de JS. En el PC de Haytham `node` es la v18.19.1 (`yt-dlp` pide v20 o superior); en el servidor no había `node`, `deno` ni `bun`.
- Con permiso explícito de Haytham, se instaló `deno` 2.9.8 en `/usr/local/bin/deno` del servidor, se reinició `conversor-mp3` (activo) y se comprobó que `yt-dlp` ya lista los formatos de la URL (mp4 de 144p a 480p).

## Decisiones tomadas
- `deno` en `/usr/local/bin` (sin tocar la configuración del servicio: lo encuentra en el `PATH`).
- No se usaron cookies del navegador (no se tocan sin permiso).

## Aprendizajes (para futuras sesiones)
- «El vídeo no existe» en `yt-dlp` puede significar «formato protegido por reto JS», no vídeo borrado; sobre todo en vídeos «hechos para niños».
- El servidor Zorin no tenía ningún runtime de JavaScript: cualquier herramienta que lo necesite fallará igual.

## Próximos pasos
- Haytham: repetir la descarga desde la web de la app (no se probó desde la propia app). El vídeo pesa ~123 MiB en 360p y dura ~48 min, puede tardar.
- Valorar anotar `deno` como dependencia del servidor en la ficha del proyecto y vigilar que `yt-dlp` se mantenga actualizado.

## Relacionado
- [[01_Projects/Conversor MP3 Facil|Conversor MP3 Facil]]
- [[2026-11-18 - Conversor MP3 Facil: rediseno B2, PRD v2 y cierre de Capa 3 (sesion a581fb2d)]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

