---
type: sesion
date: '2026-10-12'
proyecto: ig-analytics
status: completada
tags:
- sesion
- instagram
- dashboard
origen: mixto
---

## Contexto
Dashboard local para analizar los Reels de cualquier perfil público de Instagram (un perfil cada vez), con más gráficas que el script de `instaloader` de partida y datos sincronizados. Código en `~/Proyectos/ig-analytics/` (rama `feat/ig-analytics`, sin push).

## Decisiones
- "Sincronizado" = datos al día (timer de systemd cada 6 h) **y** gráficas enlazadas (un filtro compartido).
- Solo local por ahora; colector Python → SQLite con histórico → API FastAPI → web Next.js (shadcn + Recharts). Las métricas se calculan en el navegador.
- Sin login de Instagram; si hay bloqueo, el perfil entra en cooldown 1/2/4/6 h.

## Aprendizajes
- `Post` de instaloader 4.15 no expone `product_type`: los Reels se sacan con `Profile.get_reels()` (una petición por Reel). `views` = `video_play_count`, con respaldo en `video_view_count`.
- Instagram permite anclar hasta 3 Reels: la extracción solo para tras 4 antiguos conocidos seguidos.
- `dataviz` prohíbe el doble eje: engagement con selector views/seguidores; curva de un Reel solo con views.
- `create-next-app`: no sobrescribir `next.config.ts` (pierde `cacheComponents` y la regla de Turbopack). `pkill -f` mata la propia shell: usar `fuser -k`.
- Pendiente: prueba con un perfil real e instalación de los servicios (`deploy/README.md`).

## Enlaces
Spec y plan en `~/Proyectos/ig-analytics/docs/superpowers/`.

