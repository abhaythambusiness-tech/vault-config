---
type: ficha-investigacion
proyecto: ComandAi
tipo: micro-saas
status: aprobada
date: '2026-11-03'
origen: mixto
---

> [!resumen] En cristiano
> Piezas que vamos a usar, herramientas de Claude por fase y con qué nos comparamos. Casi no hay librerías: Bun, Python estándar y CSS a mano, para gastar poca RAM.

# Ficha de Investigación

## Librerías
| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
| Servidor web | Bun (`Bun.serve`) | Node + Express | **Bun 1.4.4**: 25 MB en reposo medido en el Zorin, mismo motor que el CRM | `librerias.md` (2026-10-24, neozeler-crm) |
| Estado | `bun:sqlite` | Postgres | **`bun:sqlite`**: sin servicio extra; usar `strict: true` | `librerias.md` |
| Descarga de datos | Python estándar (`urllib`, `xml.etree`) | `feedparser` | **Estándar**: 0 dependencias | Zorin ya trae `python3` |
| Acceso móvil | Tailscale | Cloudflare Tunnel | **Tailscale**: red privada, no se expone a internet | tailscale.com/kb |
| Animación | CSS | GSAP / Motion | **CSS**: nivel 1 de dinamismo, 0 kB de JS de animación | UI-UX §7 |

## Skills y agentes
- Identidad y portadas: `diseno-central`, `svg-skill` (+ `validate.sh`), `hallmark`.
- Código del servidor: `ponytail`, `vercel-react-best-practices` no aplica (sin React).
- Datos de librerías: `context7` (arreglado el `PATH` del vault, vale desde la próxima sesión).
- Calidad: `accesslint-audit`, `impeccable critique`, `pre-ship-gate`.
- Cierre: agente `archivista` (documentación del vault).

## Referencias
- Panel del vídeo de Nico CMW (`https://www.youtube.com/watch?v=XwEbK3JX5mc`): portada ancha por sección + dock de iconos.
- [[Neozeler CRM - Identidad Visual]]: origen de la paleta en el logo NeoZeler.

## Lecciones aplicables
- Panel anterior en el Zorin gastaba ~980 MB y se retiró: medir RAM antes de dar por bueno.
- Web en TypeScript, no Python; UI mirada en el navegador (memoria `feedback-web-poca-ram`).
- Falta imagen = parar y preguntar (ya preguntado: SVG propios).
- `context7` fallaba por Node 18; usar Node 22.

## Extras de la vía
### micro-saas
Uso interno de Haytham: no hay cobro ni señal de demanda externa que medir en v1. Si se decide venderlo, volver a esta sección y revisar [[Checklist pre-cobro (micro SaaS)]].
- Señal de demanda: el propio Haytham lo pide (uso diario).
