---
type: doc-software
doc: plan-implementacion
proyecto: "Los Apuntes de Liyo"
status: borrador
date: 2026-10-27
origen: mixto
---

# 6 · Plan de Implementación

> [!resumen]
> Orden de construcción en tareas pequeñas y verificables, derivado de los 5 documentos anteriores. Código real en `~/Proyectos/los-apuntes-de-liyo/` (git desde el primer commit).

> [!resumen] Estado 2026-10-27 (equipo de casa)
> Fases 0, 1 y 2 hechas (T-01 a T-11), commits `8d5e045` y el de la Fase 2 (`git log` en el repo) en `ssh@192.168.0.100:~/Proyectos/los-apuntes-de-liyo/` (el código vive en Zorin: allí está Bun 1.4.4 y allí se despliega). `trace_lint.py` ya corrido en casa: **RESULTADO: OK** tras añadir US-04 al Flujo 1 del AppFlow (estaba huérfana). Cambio en el esquema del repo: `documento.subido_por` pasa a admitir nulo (con `not null` + `on delete set null` el borrado de un alumno fallaría).

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo Bun+TS, `.gitignore`, `.env.example` | `bun run` arranca un servidor vacío | — |
| 1 Datos | Migración SQLite + semilla ([[5 - Backend Schema]]) | tablas y FTS5 verificadas (ya probado en el propio documento) | — |
| 2 Núcleo | Tokenización, subida, búsqueda, Groq, denuncia, admin ([[4 - AppFlow]]) | ciclo completo OK (crear módulo → subir → preguntar con cita → denunciar → borrar) | US-01 a US-06 |
| 3 UI | Identidad aplicada y pantallas ([[3 - UI-UX Design]]); 2 SVG propios resueltos | demo navegable + `DESIGN-IDENTITY.md` en el repo | US-01 a US-06 |
| 4 Pulido | Estados vacíos/carga/error, a11y, rendimiento móvil | checklist técnico (`auditor-web`) | — |
| 5 Despliegue | Servicio `systemd` en el servidor Zorin | URL interna en vivo | — |

## 2. Tareas

### Fase 0 — Scaffold
- [x] T-01 · descripción: `bun init` + `git init` + `.gitignore` (`.env`, `node_modules/`, `*.db`) + `.env.example` (`GROQ_API_KEY=`, `ADMIN_TOKEN=`) · archivos: raíz del repo · criterio de hecho: `git log` tiene un primer commit sin secretos, `bun --bun tsc --noEmit` corre sin error en un proyecto vacío · depende de: —

### Fase 1 — Datos
- [x] T-02 · (RF-01 a RF-02, tablas de [[5 - Backend Schema]]) crear `src/db/schema.sql` con el bloque ya validado (modulo, alumno, documento, chunk, chunk_fts, triggers, denuncia, índices) y `src/db/migrate.ts` que lo aplica con `bun:sqlite` al arrancar · archivos: `src/db/schema.sql`, `src/db/migrate.ts` · criterio de hecho: arrancar el servidor crea `data/db.sqlite` con las 5 tablas + la FTS5; repetir el arranque no falla (`if not exists`) · depende de: T-01
- [x] T-03 · (seed) `src/db/seed.ts` con los 3 módulos y el alumno de prueba del bloque `sql seed` · archivos: `src/db/seed.ts` · criterio de hecho: tras `bun run seed`, `select * from modulo` devuelve 3 filas · depende de: T-02

### Fase 2 — Núcleo (AppFlow Flujos 1-4)
- [x] T-04 · (US-01, RF-01) endpoint `POST /entrada` (nombre+centro → cookie de sesión, token aleatorio) · archivos: `src/routes/entrada.ts` · criterio de hecho: cookie `HttpOnly`/`SameSite=Strict` presente tras la respuesta, fila nueva en `alumno` · depende de: T-02
- [x] T-05 · (US-03, RF-06) endpoints `GET /modulos`, `GET /modulos/:id/documentos` · archivos: `src/routes/modulos.ts` · criterio de hecho: lista filtrada por módulo, 401 sin sesión · depende de: T-04
- [x] T-06 · (US-01, RF-01) `POST /modulos/:id/documentos`: extracción con `pdf-parse` (verificar antes `npm view pdf-parse` — TRD §8 riesgo pendiente) + chunking 300-500 palabras con página de origen · archivos: `src/ingest/extract.ts`, `src/ingest/chunk.ts`, `src/routes/documentos.ts` · criterio de hecho: subir un PDF de prueba genera filas en `chunk` con `pagina` correcta · depende de: T-05
- [x] T-07 · (US-01, RF-02) tokenización e indexado: insertar en `chunk` dispara los triggers hacia `chunk_fts` (ya escritos en T-02); función de tokenización reutilizable para limpiar también la pregunta del alumno (RF-03) · archivos: `src/search/tokenize.ts` · criterio de hecho: buscar una palabra con acento distinto al del documento (p. ej. "bateria" vs "batería") encuentra el chunk · depende de: T-06
- [x] T-08 · (US-02, US-03, RF-03 a RF-05) `POST /modulos/:id/preguntas`: `MATCH`+`bm25()` top-5 filtrado por módulo; si no hay score por encima del umbral, responde el aviso fijo sin llamar a Groq · archivos: `src/search/retrieve.ts`, `src/routes/preguntas.ts` · criterio de hecho: pregunta sin relación con ningún documento devuelve el aviso, nunca una llamada a Groq (comprobar en los logs) · depende de: T-07
- [x] T-09 · (US-02, RF-04) integración con la API de Groq (`fetch` nativo, streaming) armando el prompt con los chunks como único contexto y exigiendo citar documento+página · archivos: `src/ai/groq.ts` · criterio de hecho: respuesta en streaming que cita el `nombre_archivo` y `pagina` reales del chunk usado; `GROQ_API_KEY` solo en `.env` · depende de: T-08
- [x] T-10 · (US-06, RF-07) modal y endpoint `POST /documentos/:id/denuncias` con motivo cerrado + texto opcional, `UNIQUE(documento_id, alumno_id)` ya en el esquema · archivos: `src/routes/denuncias.ts`, `public/js/denuncia.js` · criterio de hecho: denunciar dos veces el mismo documento no crea fila duplicada, la UI marca "Denunciado" · depende de: T-05
- [x] T-11 · (US-05, US-06, RF-08) panel admin: `POST /admin/login` (token de `.env`, `crypto.timingSafeEqual`), `GET /admin/denuncias` (con autor, nº acumulado), `GET /documentos/:id/archivo` (previsualización), `DELETE /documentos/:id` (cascada), `POST /admin/modulos` · archivos: `src/routes/admin.ts` · criterio de hecho: entrar a `/admin` con el token de alumno falla (401); borrar un documento denunciado lo quita de respuestas futuras de inmediato · depende de: T-10

### Fase 3 — UI (identidad del UI/UX)
- [x] T-12 · (identidad, §2 y §2.1 del UI/UX) tokens CSS (`:root` con la paleta azul noche + ámbar, opción D «Luz de lámpara») + tipografías `Work Sans`/`Space Grotesk` autoalojadas · archivos: `public/css/tokens.css`, `public/fonts/` · criterio de hecho: ninguna pantalla usa un color fuera de los tokens · depende de: T-01
- [ ] T-13 · (US-01 a US-06) maquetar las 9 pantallas del inventario (§3 del UI/UX): Entrada, Lista de módulos, Módulo (documentos+chat), Subir documento, Denunciar documento, Entrada admin, Panel admin, Crear módulo, Previsualizar documento · archivos: `public/*.html`, `public/js/*.js` · criterio de hecho: las 9 pantallas abren en el navegador con datos reales de la semilla, botón "+ Subir apunte" visible con y sin documentos (corrección cliente simulado) · depende de: T-12, T-06, T-09, T-10, T-11
- [x] T-14 · (imágenes §5 del UI/UX) dibujar los SVG propios (wordmark, lámpara apagada, hoja+esquina doblada) con los tokens de color · archivos: `public/img/wordmark.svg`, `public/img/vacio-lampara.svg`, `public/img/vacio-documentos.svg` · criterio de hecho: ningún estado vacío queda sin ilustración, cero placeholders · depende de: T-12
- [x] T-15 · (dinamismo §7 del UI/UX) barrido de luz de la cita y lámpara que se enciende, en CSS puro con la curva propia, respetando `prefers-reduced-motion` · archivos: `public/css/animacion.css` · criterio de hecho: con "reducir movimiento" activado en el sistema, el subrayado aparece ya hecho, sin barrido · depende de: T-13

### Fase 4 — Pulido
- [ ] T-16 · estados de carga/error de las 9 pantallas (esqueleto en vez de pantalla en blanco, corrección cliente simulado alumno) · archivos: `public/js/*.js` · criterio de hecho: desconectar el servidor a mitad de una pregunta no deja la pantalla en blanco · depende de: T-13
- [ ] T-17 · accesibilidad y contraste (`auditor-web`): verificar en código real los contrastes de la paleta (pendiente marcado en UI-UX §8) · archivos: — (auditoría, no código nuevo salvo fixes) · criterio de hecho: `auditor-web` sin hallazgos críticos · depende de: T-13

### Fase 5 — Despliegue
- [ ] T-18 · servicio `systemd` de usuario en el servidor Zorin (patrón `neozeler-crm`), puerto propio, backup periódico de `data/db.sqlite` (TRD §5) · archivos: `deploy/los-apuntes-de-liyo.service` · criterio de hecho: ciclo completo crear→refrescar→borrar→refrescar probado contra la URL del servidor, no en local · depende de: T-11, T-13

## 2.1 Starter kits reutilizados
| Kit | Fase | Adaptación |
|---|---|---|
| Patrón Bun+SQLite+`PRAGMA foreign_keys` de `neozeler-crm`/`laya-leads` | 0, 1 | Mismo patrón de conexión y backup, sin CRM ni htmx (aquí JS vanilla) |

## 3. Estrategia de pruebas
- Unitarias: tokenización (acentos/mayúsculas), umbral de "sin contexto" (T-08), `UNIQUE` de denuncias (T-10) — ya probadas a mano en [[5 - Backend Schema]], se formalizan en tests al escribir el código.
- E2E: ciclo crear módulo (admin) → refrescar lista (alumno) → subir documento → refrescar → preguntar y recibir cita → denunciar → refrescar panel admin → borrar → refrescar chat (ya no cita ese documento) — en producción (servidor Zorin), no solo en local (T-18).

## 4. Despliegue y operación
- Variables de entorno: `GROQ_API_KEY`, `ADMIN_TOKEN` — en `.env` del servidor, nunca en el repo.
- Dominio: acceso interno vía el servidor Zorin (sin dominio público todavía; decisión pendiente si se abre a alumnos fuera de la red de Haytham).
- Backups: copia periódica de `data/db.sqlite` y de la carpeta de PDFs originales (igual que `laya-trader`, TRD §5).
- Monitorización: vigilar manualmente el panel de uso de Groq (gasto y rate limit) — no hay contador dentro de la app en v1 (riesgo ya anotado en TRD §8 y AppFlow §4).

## 5. Riesgos y plan B
> [!riesgo]
> - Extractor de PDF: se usa **`unpdf` 1.9.1 (MIT)**, probado el 2026-10-27 con un PDF de 3 páginas con acentos: devuelve el texto por página (`extractText(..., {mergePages:false})`), necesario para citar página. `pdf-parse` 2.4.5 (Apache-2.0) queda descartado.
> - Sin probar con la API real de Groq (no hay `GROQ_API_KEY` en el servidor): las pruebas simulan Groq. Falta una prueba real con clave y calibrar `UMBRAL_BM25` con apuntes reales (por defecto basta con que coincida una palabra útil).
> - Rate limit gratis de Groq (1.000 RPM): si se satura en examen, plan B es cola con reintento (ya en TRD §3) o pasar a capa de pago puntualmente.
> - Acceso solo desde la red de Haytham en v1: si se quiere abrir a "alumnos de todos lados" (como pedía la idea original), falta decidir dominio público y ese cambio de alcance no está en este plan — hay que volver al PRD si se confirma.

## 6. Definición de terminado
- [ ] Trazabilidad US ↔ tareas comprobada a mano (tabla abajo; `trace_lint.py` no existe en este equipo — declarado arriba)
- [ ] Build y type-check limpios (`bun --bun tsc --noEmit`)
- [ ] Checklist técnico y de marca (UI-UX §6, §8)
- [ ] Pruebas de intercambio y de lejos superadas (ya hechas en el UI/UX); cero imágenes pendientes o inventadas (T-14); fila ya añadida a [[Registro de Identidades Visuales]]
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada en `00_Meta/Sesiones/`
- [ ] `.claude/COMMON_MISTAKES.md` del repo creado y actualizado tras la primera trampa real

### Trazabilidad US → tareas (comprobación manual, sin `trace_lint.py`)
| Historia | Tareas que la cubren |
|---|---|
| US-01 (subir apunte) | T-06, T-07, T-13, T-14 |
| US-02 (preguntar con fuente) | T-08, T-09, T-13 |
| US-03 (elegir módulo) | T-05, T-08, T-13 |
| US-04 (ver documentos del módulo) | T-05, T-13 |
| US-05 (admin crea/gestiona módulos) | T-11, T-13 |
| US-06 (denunciar y borrar) | T-10, T-11, T-13 |

Ninguna historia queda sin tarea y ninguna tarea cita una historia que no exista en el PRD — comprobado leyendo ambos documentos uno frente al otro (equivalente manual de `RESULTADO: OK`).

---
Anterior: [[5 - Backend Schema]]
