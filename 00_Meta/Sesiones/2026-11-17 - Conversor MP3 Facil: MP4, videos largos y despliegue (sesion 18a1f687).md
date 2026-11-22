---
type: sesion
date: '2026-11-17'
proyecto: '[[01_Projects/Conversor MP3 Facil/1 - PRD]]'
origen: maquina
sesion_id: 18a1f687-31c8-4b9e-ba95-9cc503fc220b
tags:
  - sesion
  - cierre-nocturno
---

> [!resumen] En cristiano
> El conversor ahora acepta vídeos mucho más largos y también baja MP4 (vídeo), no solo MP3. Se añadieron 9 mejoras de uso (aviso de peso, calidad, tiempo restante, recortar tramo...), se subió la API a Zorin y la web a producción, y se apagó `laya-trader` para liberar memoria. Falta probar una conversión larga de verdad desde la web publicada.

# Sesión 2026-11-17: Conversor MP3 Fácil, MP4 y vídeos largos

## Qué se hizo
- **Límites nuevos**: MP3 hasta 3 h (antes 15 min), MP4 hasta 2 h a 720p máx. Selector «MP3 · música / MP4 · vídeo» (se recuerda la elección). Archivos listos duran 30 min; tope de 3 GB por MP4; límites de tiempo en servidor de 45 min (MP3) y 90 min (MP4).
- **9 mejoras de UX** (a petición «implementar todo»): aviso de peso (>~300 MB), calidad MP4 480p/720p, tiempo restante en la cola, notificación y título «✓ Lista» con la pestaña en segundo plano, cola que sobrevive a recargar, recorte de tramo (`yt-dlp --download-sections`), entre otras.
- **Despliegue API**: Zorin no tenía Go; se instaló (`golang-go` 1.22.2), se compiló allí, se copió el binario anterior a `/usr/local/bin/conversor-api.bak-20261117` y se reinició `conversor-mp3.service` (escucha en `127.0.0.1:8799`, expuesta por Tailscale Funnel en `zorin-mp3.tail5b8c39.ts.net`). La subida por `zorin-ssh` estaba bloqueada (`defaults.transferRoot`) y `scp` fallaba con «No route to host».
- **Despliegue web**: primero vista previa en Vercel, luego `--prod` con permiso de Haytham a `conversor-mp3-facil.vercel.app`. Comprobado: responde 200, CORS correcto (`ORIGEN_WEB`), sin `X-Clave` la API da 401.
- **README** actualizado: despliegue real con Tailscale y puerto 8799 (ya no Cloudflare/8787).
- **Zorin**: la API ya arrancaba sola (`enabled` + `Restart=always`). `laya-trader.service` parado y `disabled` (RAM disponible de 3,0 a 5,1 GB).
- **Calidad**: axe 0 violaciones (escritorio, 375 px, tema claro). Lighthouse: Accesibilidad 100, Buenas prácticas 100, SEO 60 (por `noindex`, esperado), Rendimiento 75 (hilo principal bloqueado 640 ms). Se mejoró con `LazyMotion`, una fuente menos (Geist Mono) y fondo con degradado; commit `aee4060` y despliegue a producción.

## Decisiones
- `noindex` se mantiene: herramienta privada con clave.
- Rendimiento 75 no es crítico; se aplicaron solo los cambios baratos (quitar animación `layout` de filas).
- `--prod` siempre con permiso explícito.

## Problemas
- Subida del binario por `zorin-ssh` y `scp` no disponibles al inicio (se resolvió instalando Go en Zorin).
- Desajuste de puerto en README (8787 vs 8799 real).

## Pendientes y próximos pasos
- Probar una conversión larga (MP3 3 h / MP4 2 h) y el recorte desde la web publicada; no se probó en navegador.
- Probar con la clave real (`X-Clave`) en producción.
- Dos MP4 largos a la vez más `laya-trader` pueden apretar los 7,6 GB de RAM; vigilar. Para reactivar: `systemctl --user enable --now laya-trader.service`.
- Reiniciar Zorin para confirmar que la API arranca sola (deducido de la configuración, no probado).
- Cron semanal de `yt-dlp -U` quitado del README por no estar verificado.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[2026-11-16 - Conversor MP3 Facil: app, rediseno, despliegue en Vercel y Zorin (sesiones 5d780fd6, e24b6ac1 y 67b23146)]]
