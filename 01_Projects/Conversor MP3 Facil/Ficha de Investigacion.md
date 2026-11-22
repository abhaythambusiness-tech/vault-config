---
type: ficha-investigacion
proyecto: Conversor MP3 Facil
tipo: micro-saas
status: aprobada
date: '2026-11-16'
origen: mixto
---

> [!resumen] En cristiano
> Piezas ya hechas que usamos para no reinventar: yt-dlp (descarga), ffmpeg (a MP3), shadcn/ui y motion (pantalla). Herramienta personal; sin cobro.

# Ficha de Investigación

## Librerías
| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| Buscar y bajar audio | yt-dlp (CLI) | libs Go de YouTube | yt-dlp: se actualiza a diario; las libs se rompen | ya instalado (`~/.local/bin/yt-dlp`) |
| Pasar a MP3 | ffmpeg | — | estándar | `/usr/bin/ffmpeg` |
| API | stdlib Go (`net/http`) | gin/echo | stdlib: 0 dependencias | Go 1.22+ |
| UI | shadcn/ui | BoardUI | shadcn: base del stack | rules/diseno.md |
| Animación | motion | Magic UI | motion para la barra de progreso | rules/diseno.md |

## Skills y agentes
- API: `superpowers:test-driven-development`. UI: `diseno-central`, `impeccable`, `web-animation-skills:accessible-animation`. Cierre: `auditor-web`, `revisor-codigo`.

## Referencias
- Por decidir con Haytham en UI-UX.

## Lecciones aplicables
- Validar el ciclo crear → refrescar → borrar → refrescar en producción.

## Extras de la vía
### micro-saas
- Sin cobro: herramienta personal. Aviso legal visible de uso.

