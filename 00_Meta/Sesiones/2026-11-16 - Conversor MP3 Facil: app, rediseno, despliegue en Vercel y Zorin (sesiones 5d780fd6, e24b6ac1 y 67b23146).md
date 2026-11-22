---
type: sesion
date: '2026-11-16'
proyecto: '[[01_Projects/Conversor MP3 Facil/1 - PRD]]'
origen: maquina
sesion_id:
  - 5d780fd6-47f0-4f78-a64d-ec25665a106e
  - e24b6ac1-b7ec-4c49-9ee3-3648e4d3372a
  - 67b23146-4a11-4250-a778-a00bc9acc567
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Se creó «Mi Música en MP3», una web con letra grande para pasar canciones de YouTube a MP3 en 3 pasos, pensada para personas mayores. La web está en Vercel y el motor de conversión corre en el servidor Zorin, accesible desde fuera de casa con Tailscale Funnel. Tres sesiones encadenadas de la misma conversación (continuaciones por falta de contexto). Estado: desplegada; falta abrirla con la clave en el navegador.

## Qué se hizo
- App nueva en `~/Proyectos/conversor-mp3-facil/`: API en Go (`yt-dlp` + `ffmpeg`) y web Next.js 16 + Tailwind v4 + shadcn/ui + motion. Solo YouTube (Spotify y Amazon Music no son viables). Documentos del flujo en `01_Projects/Conversor MP3 Facil/`.
- Haytham rechazó el primer diseño (formato grande «para mayores» con huecos laterales, «cero premium»): rediseño completo hacia herramienta suave, premium y de uso diario, con `DESIGN-IDENTITY.md` aprobado (crema, tinta, verde; Fraunces + Atkinson Hyperlegible). Reclamó usar el MCP de diseño.
- Ideas de mejora UI/UX aplicadas («añade todo») y despliegue en Vercel aprobado.
- Montaje en Zorin: SSH no respondía hasta que Haytham lo activó; se buscó la IP (172.x eran redes Docker). Se pasó a Tailscale (Funnel) en vez de túnel Cloudflare para uso fuera de casa.
- La clave se pasa por enlace especial `?c=<clave>`; queda guardada en el navegador. La clave real vive en `/etc/conversor-mp3/env` de Zorin (servicio `conversor-mp3`): no se copia aquí.

## Problemas
- `Falta la clave...` al abrir la web sin el enlace especial: se explicó cómo usarlo en cada dispositivo.
- Aviso «hook de headroom no respondió a tiempo»: el hook `headroom init hook ensure` tiene límite de 15 s y el PC iba justo de recursos recién arrancado (carga 5,5, 9,6 de 15,7 GB). Propuesta: subir `timeout` de 15 a 45 en el `hooks.json` del plugin.

## Pendientes
- Autorizar el enlace de Tailscale (si caducó, regenerarlo).
- Probar la web abierta con la clave en el navegador.
- Decidir si se sube el `timeout` del hook de headroom.
- Si la clave se filtra: cambiarla en Zorin y reiniciar el servicio.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
