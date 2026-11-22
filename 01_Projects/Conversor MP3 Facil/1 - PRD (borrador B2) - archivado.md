---
type: doc-software
doc: prd
proyecto: Conversor MP3 Facil
status: borrador
tipo: micro-saas
date: '2026-11-18'
origen: mixto
version: 2 (decisión B2)
sustituye: 1 - PRD (aprobado 2026-11-16; copia en ~/.claude/_backups/1-PRD-aprobado-20261118.md)
---

# 1 · PRD — Conversor MP3 Fácil (v2, tras decisión B2) — PARA REVISIÓN

> [!resumen] En cristiano
> Una web oscura y tranquila para pasar una canción o vídeo de YouTube a MP3 o MP4 en 3 pasos: buscar o pegar el enlace, convertir, descargar. Ya no es «para mayores»: es para cualquier persona que quiera algo limpio, sin anuncios y sin trampas. **Solo YouTube** (Spotify y Amazon Music llevan audio cifrado y saltarlo es ilegal en España/UE). La web vive en Vercel y la conversión la hace tu servidor Zorin. **Este texto aún no sustituye al PRD aprobado.**

## 0. Qué cambió respecto a la v1 y por qué
- **Dirección B2 (2026-11-18):** diseño «soft premium» (carbón + esmeralda, vidrio fino, calma) en lugar de «cálido, grande, tranquilo para mayores». Sin Magic UI.
- **Usuario:** público general (U2), no personas mayores.
- **Alcance real:** MP4, recorte, ZIP, multiselección, historial y cola persistente ya existen; en la v1 eran «fuera de alcance».
- **Deriva documentada:** el diseño se alejó del PRD en 3 commits (`e0fa96c`, `91620b8`, `b0cd41c`) sin actualizarlo; se corrige aquí.

## 1. Problema
- Quien quiere su música o un vídeo en MP3/MP4 (móvil, coche, USB) acaba en webs de conversión llenas de anuncios, botones falsos y malware.
- Hoy busca «convertidor mp3» en Google y cae en webs engañosas.
- **Promesa:** 3 pasos, sin anuncios, sin trampas.

## 2. Usuarios
| Rol | Quién | Necesita | Frecuencia |
|---|---|---|---|
| Persona cualquiera (U2) | Público general, sin contexto de uso asumido | 3 pasos claros, cero anuncios, que se entienda sin explicación | Ocasional |
| Haytham | Dueño | Que no se abuse ni cueste dinero | — |

Sin nicho declarado. El producto debe funcionar para alguien que no es Haytham, con onboarding mínimo.

## 3. Éxito
| Objetivo | Métrica | Meta |
|---|---|---|
| Rápido (técnica) | Canción de 4 min convertida a MP3 | < 60 s |
| Se usa y funciona (producto) | En las 2 primeras semanas tras publicar: conversiones completadas y tasa de error (errores visibles al usuario / intentos) | ≥ 30 y < 10 % |
| Se entiende solo (cualitativa) | 3 personas fuera del círculo de Haytham completan una descarga sin ayuda | 3 de 3 (**checklist de cierre**, no estado actual) |

## 4. Historias
| ID | Como… | Quiero… | Para… | MoSCoW |
|---|---|---|---|---|
| US-01 | Persona | Escribir el nombre y ver 5 resultados con foto | Elegir el correcto sin enlaces | Must |
| US-02 | Persona | Pegar un enlace de YouTube | Convertir un vídeo concreto | Must |
| US-03 | Persona | Pulsar «Convertir» y ver una barra de progreso con tiempo restante | Saber que funciona | Must |
| US-04 | Persona | Pulsar «Descargar» y que el archivo se guarde | Tenerlo | Must |
| US-05 | Persona | Mensajes de error claros en español sencillo | No perderme | Must |
| US-06 | Haytham | Una clave de acceso compartida | Que no lo use cualquiera | Must |
| US-07 | Haytham | Límites de duración y de peticiones | Proteger el servidor | Must |
| US-08 | Persona | Elegir MP3 o MP4 (480p / 720p) | Audio o vídeo según lo que necesite | Should |
| US-09 | Persona | Recortar un tramo (desde / hasta) | No bajar el vídeo entero | Should |
| US-10 | Persona | Descargar varios archivos en un ZIP | Ahorrar clics | Should |
| US-11 | Persona | Que la cola y el historial sobrevivan a recargar | No perder lo convertido | Should |

## 5. Requisitos funcionales
- RF-01 Buscar en YouTube por texto (5 resultados: foto, título, duración).
- RF-02 Aceptar enlace de YouTube (youtube.com, youtu.be, music.youtube.com).
- RF-03 Convertir a MP3 192 kbps (título como nombre de archivo) o a MP4 480p/720p (h264 + aac).
- RF-04 Si se pega un enlace de Spotify o Amazon: explicar con amabilidad que no se puede y por qué.
- RF-05 Borrar el archivo del servidor a los **10 min** de estar listo (antes 30 en el código; ver §10).
- RF-06 Recorte de tramo (`desde`/`hasta` en segundos); con tramo, el original puede durar hasta 12 h.
- RF-07 ZIP de varios archivos (multiselección).
- RF-08 Aviso de peso y tiempo antes de archivos grandes; aviso con la pestaña en segundo plano; compartir en móvil.
- RF-09 Límites: 10 conversiones/h y 60 búsquedas/h por IP; MP3 hasta 3 h y MP4 (720p) hasta 2 h; 2 conversiones a la vez.
- **Estado de verificación (2026-11-18):** MP3, MP4 480p, recorte y ZIP **probados en local** (API compilada del repo, vídeo de 33 s). **Pendiente verificar en producción** con clave real.

## 6. No funcionales
- Idioma español. Móvil primero.
- **Contraste AA** (4,5:1 texto normal, 3:1 grande). El secundario `#8E968F` sobre `#0B0D0C` (≈ 6:1) pasa. Si se pidiera AAA, hay que subirlo a 7:1 y cambia la paleta.
- **Texto:** cuerpo 16 px, secundario 14 px, **nada por debajo de 14 px** (hoy hay 13 px en títulos de panel: se sube a 14).
- **Botones:** 48 px de alto mínimo.
- **Accesible por teclado y lector de pantalla** (no es de mayores, es de todos); atajos `/` y ⏎ se mantienen.
- `prefers-reduced-motion` respetado; un solo motor de animación (`motion`).

## 7. Fuera de alcance
- Spotify, Amazon Music, Apple Music (DRM). Listas de reproducción. Cuentas de usuario. Pagos.

## 8. Riesgos y supuestos
> [!riesgo]
> - **Deriva del PRD (documentada 2026-11-18):** el diseño y las funciones cambiaron en 3 commits sin actualizar el PRD, y se perdió la tipografía pensada para baja visión. Mitigación: todo cambio de dirección actualiza PRD, Paleta, README y DESIGN* en el mismo commit; el gate `identidad` y la Retro lo comprueban.
> - **Vercel no ejecuta yt-dlp/ffmpeg** de forma fiable. Solución: API en Go en Zorin (IP residencial) y la web en Vercel que le habla.
> - **Exponer Zorin a internet** (hoy por Tailscale): se protege con clave + límites.
> - **Términos de YouTube:** descargar va contra ellos. Aviso visible: usar solo con música propia, libre o con permiso. Con público general el riesgo legal y de abuso sube; la clave y los límites son la barrera.
> - **YouTube cambia a menudo:** yt-dlp debe actualizarse (cron semanal).
> - **Producción sin verificar:** MP4, recorte y ZIP solo probados en local.

## 9. Criterios de aceptación
- [ ] Canción de 4 min: buscar, convertir y descargar en < 60 s desde el móvil.
- [ ] 3 personas fuera del círculo de Haytham completan una descarga sin ayuda (cierre).
- [ ] 2 semanas tras publicar: ≥ 30 conversiones y error < 10 %.
- [ ] Enlace de Spotify muestra el aviso, no un error técnico.
- [ ] Sin clave no se puede convertir.
- [ ] MP4, recorte y ZIP verificados en producción.
- [ ] Contraste AA, texto ≥ 14 px y botones ≥ 48 px comprobados con axe y Lighthouse.

## 10. Alineación código ↔ PRD (pendiente de ejecutar tras aprobar)
Borrado de archivos a **10 min**: `api/main.go:35` (`vidaArchivo`), `web/src/components/conversor.tsx:57` (`VIGENCIA_MS = 9 min`, 1 min de margen) y README, **en el mismo commit**. Si solo cambia uno, la web ofrece «Descargar» sobre un archivo ya borrado (404).

## 11. Carácter de marca
- Adjetivos: tranquilo, preciso, premium (vidrio fino, calma).
- NO debe parecer: web de descargas con anuncios y botones falsos, ni «bling» (haz de borde, brillo que sigue al cursor). Ver [[Paleta de Componentes]] (ancla B2).
- Nombre: **«Conversor MP3 Fácil»** se mantiene: «Fácil» describe la función, no al usuario.
- Referencias: 21st (Signal Bars Loader, Waveform, MP3 Player). Imágenes: solo miniaturas de YouTube; logo por decidir.

---
Siguiente: [[6 - Plan de Implementacion]] (T-07 y las historias nuevas se reconcilian tras aprobar).
