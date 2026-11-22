---
type: doc-software
doc: plan-implementacion
proyecto: Conversor MP3 Facil
status: aprobado
date: '2026-11-16'
origen: mixto
---

# 6 · Plan de Implementación — Conversor MP3 Fácil

> [!resumen] En cristiano
> Dos piezas: (1) un programa en Go en tu servidor Zorin que busca y convierte con yt-dlp + ffmpeg (ya instalados en este PC; en Zorin hay que comprobarlo); (2) una web Next.js en Vercel con 3 pasos enormes que le habla al programa. Entre las dos, un túnel de Cloudflare y una clave. Nada se construye hasta que apruebes esto.

## TRD corto (decisiones)
| Decisión | Elegido | Descartado y por qué |
|---|---|---|
| Dónde convierte | API Go en Zorin | Vercel serverless: sin binarios, 10-60 s de límite, YouTube bloquea sus IPs |
| Lenguaje API | Go (regla 2026-11-12) | Python: viola la regla |
| Descarga | yt-dlp + ffmpeg (CLI) | Librerías Go de YouTube: se rompen cada semana |
| Conexión | Cloudflare Tunnel (gratis) | Abrir puerto del router: inseguro |
| Web | Next.js + React + Tailwind v4 + shadcn/ui + motion (stack obligatorio) | HTML a mano: prohibido |
| Acceso | Clave compartida (cabecera) + límite 10 conv/h por IP + máx 15 min de vídeo | Cuentas: sobra |
| Librerías de UI (mín. 2) | shadcn/ui (base: Button, Input, Progress, Card) + Magic UI o motion para animar el progreso | — |

## 1. Fases
| Fase | Objetivo | Entregable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo `~/Proyectos/conversor-mp3-facil/` (`api/` Go, `web/` Next), git, `.gitignore` | build limpio | — |
| 1 API | `/buscar`, `/convertir`, `/estado`, `/archivo`, limpieza a 10 min | curl: canción → MP3 | US-01..04, 07 |
| 2 Acceso | Clave + límites + rechazo de Spotify/Amazon | tests Go | US-06, RF-04 |
| 3 Web | Identidad (a aprobar), 3 pasos, errores sencillos | demo en móvil | US-01..05 |
| 4 Pulido | a11y (axe 0), Lighthouse, 375/768/1280 | checklist | — |
| 5 Despliegue | Túnel Cloudflare + Vercel + cron yt-dlp semanal | URL en vivo + prueba con 3 mayores | todas |

## 2. Tareas
- [ ] T-01 (US-01) `api/` Go: `GET /buscar?q=` con `yt-dlp "ytsearch5:"` · hecho: 5 resultados JSON · dep: —
- [ ] T-02 (US-02) Validar enlace YouTube y rechazar otros dominios · hecho: tests tabla · dep: —
- [ ] T-03 (US-03) `POST /convertir` (trabajo en segundo plano) y `GET /estado/{id}` con % · dep: T-01
- [ ] T-04 (US-04) `GET /archivo/{id}` y borrado a 10 min · dep: T-03
- [ ] T-05 (US-06,07) Clave, límite por IP, máx 15 min · dep: T-03
- [ ] T-06 (RF-04) Aviso amable para Spotify/Amazon · dep: T-02
- [ ] T-07 Paleta de componentes + identidad (parar y preguntarte por referencias/logo) · dep: PRD aprobado
- [ ] T-08 (US-01..05) Web 3 pasos con shadcn + motion · dep: T-07, T-04
- [ ] T-09 Despliegue: tú autorizas túnel Cloudflare y `vercel --prod` · dep: T-08
- [ ] T-10 Cron semanal `yt-dlp -U` en Zorin · dep: T-09

## 3. Pruebas
- Go: tests de validación de enlaces, límites y limpieza. Ciclo completo buscar → convertir → descargar → borrado, en producción.
- Prueba real con 3 personas mayores (criterio US de éxito).

## 4. Operación
- `.env` (clave, ruta de temporales) fuera de git. Túnel como servicio systemd en Zorin.

## 5. Riesgos y plan B
> [!riesgo]
> - YouTube bloquea el IP de Zorin: plan B cookies del navegador (solo con tu permiso) o ejecutar en este PC.
> - Zorin sin ffmpeg/yt-dlp: se instalan con tu permiso.

## 6. Definición de terminado
- [ ] Tests Go y build web limpios
- [ ] axe 0 violaciones, Lighthouse, 3 anchos
- [ ] README, ficha en `01_Projects/`, `resumen.html`, sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` revisado

---
Anterior: [[1 - PRD]]

