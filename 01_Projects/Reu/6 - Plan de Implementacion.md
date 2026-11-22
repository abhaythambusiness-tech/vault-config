---
type: doc-software
doc: plan-implementacion
proyecto: Reu
status: aprobado
date: '2026-11-13'
origen: mixto
---

# 6 · Plan de Implementación — Reu

> [!resumen] En cristiano
> Se construye en 5 pasos pequeños, cada uno con algo que se puede probar. Lo más delicado es el paso 2 (leer bien los subtítulos de Meet); el resto es un panel sencillo. Todo en TypeScript, sin servidor y sin coste. Código en `~/Proyectos/reu/`.

## 0. Decisiones técnicas (TRD corto)
| Tema | Elección | Alternativa descartada y por qué |
|---|---|---|
| Tipo | Extensión Chrome Manifest V3 | App web: no puede leer la página de Meet |
| Lenguaje | TypeScript | JS suelto: sin tipos, más fallos al cambiar selectores |
| Empaquetado | Vite (multi-entrada: content script, service worker, panel) | CRXJS: más magia y peor mantenido; Vite plano basta |
| Panel | Preact | React: más peso sin necesidad; HTML a mano: se enreda con lista + detalle + búsqueda |
| Guardado | IndexedDB con la librería `idb` | `chrome.storage.local`: límite de tamaño y sin búsqueda; Dexie: sobra |
| Captura | `MutationObserver` sobre el contenedor de subtítulos de Meet | Grabar audio y transcribir: coste y privacidad, justo lo que no se quiere |
| Pruebas | Vitest para la lógica de unir frases y exportar | Probar todo a mano: se rompe sin avisar cuando Meet cambie |

Antes de instalar: `grep -i <lib> ~/.claude/reference/librerias.md` y docs con context7 (`vite`, `idb`, `preact`, API de extensiones MV3). Nota conocida: `vitest` con npm 10 necesita `--legacy-peer-deps` (ver `librerias.md`).

**Esquema de datos** (IndexedDB, base `reu`):
- `meetings`: `id`, `code`, `title`, `startedAt`, `endedAt`, `participants[]`, `lineCount`.
- `lines`: `id`, `meetingId`, `speaker`, `text`, `at`. Índice por `meetingId`.
- Borrar una reunión borra sus `lines` en la misma transacción (cascada a mano).

## 1. Fases
| Fase | Objetivo | Entregable demostrable | Historias |
|---|---|---|---|
| 0 Scaffold | Repo, `.gitignore`, Vite, manifest, build limpio | La extensión se carga en `chrome://extensions` sin errores | — |
| 1 Datos | Capa IndexedDB (crear, listar, añadir frases, borrar) + pruebas | Pruebas verdes del ciclo crear → leer → borrar | US-03, US-08 |
| 2 Captura | Content script que lee subtítulos, une frases parciales y guarda | Reunión real de prueba (2 pestañas o 2 personas) guardada correcta | US-01, US-02, US-03 |
| 3 Panel | Lista, detalle, búsqueda, borrado | Panel navegable con reuniones reales | US-04, US-05, US-07, US-08 |
| 4 Exportar | `.txt`, `.md`, `.json`, copiar, exportar todo | Un `.md` pegado en el vault se lee bien | US-06, US-10 |
| 5 Pulido | Auto-activar subtítulos, aviso si Meet cambia, reunión de 2 h, README | Checklist de §6 | US-09 |

## 2. Tareas
- [x] T-00 · Scaffold: `npm create vite`, `manifest.json` MV3 (host `meet.google.com`, permiso `storage`, `unlimitedStorage`), `.gitignore`, `git init` · `package.json`, `manifest.json`, `vite.config.ts` · hecho cuando `npm run build` sale limpio y Chrome carga `dist/` · depende de: —
- [x] T-01 · (US-03, US-08) Capa de datos `src/db.ts` con `createMeeting`, `addLine`, `listMeetings`, `getLines`, `deleteMeeting` · hecho cuando Vitest (con `fake-indexeddb`) prueba crear → listar → borrar → listar vacío · depende de: T-00
- [x] T-02 · (US-03) Lógica pura `src/merge.ts` que une las actualizaciones parciales de una frase (Meet reescribe el texto mientras se habla) y descarta duplicados · hecho cuando las pruebas cubren: frase que crece, frase que se corrige, dos hablantes seguidos · depende de: T-00
- [x] T-03 · (US-01) Content script `src/content.ts`: detectar reunión, localizar el contenedor de subtítulos, observarlo, enviar frases al service worker · selectores en un único `src/selectors.ts` · hecho cuando una reunión real queda guardada · depende de: T-01, T-02
- [x] T-04 · (US-02) Indicador en la página de Meet (punto + «Reu captura» + botón pausa), sin tapar controles de Meet · hecho cuando se ve en Meet y la pausa deja de guardar · depende de: T-03
- [ ] T-05 · (US-04, US-05) Panel `src/panel/`: lista de reuniones y detalle · hecho cuando abre desde el icono de la extensión y muestra las reuniones guardadas · depende de: T-01
- [ ] T-06 · (US-07) Búsqueda en todas las frases con resaltado · hecho cuando encuentra una frase de una reunión antigua en menos de 1 s con 50 reuniones · depende de: T-05
- [ ] T-07 · (US-08) Borrar reunión con confirmación · hecho cuando desaparece del panel y de la búsqueda tras recargar · depende de: T-05
- [ ] T-08 · (US-06, US-10) `src/export.ts` con `.txt`, `.md`, `.json`, copiar y exportar todo (un `.json`) · hecho cuando las pruebas comparan la salida con un ejemplo y el `.md` se ve bien en Obsidian · depende de: T-01
- [ ] T-09 · (US-09) Activar subtítulos solos al entrar (pulsar el botón CC) con interruptor en el panel · hecho cuando funciona en 3 reuniones seguidas y se puede apagar · depende de: T-03
- [ ] T-10 · Aviso si pasan 60 s en la reunión sin ver subtítulos («activa los subtítulos o Meet cambió su página») · hecho cuando aparece en el indicador · depende de: T-04
- [ ] T-11 · Prueba de carga: reunión simulada de 2 h (≈ 4 000 frases) sin tirones · depende de: T-03, T-05
- [ ] T-12 · README del repo, ficha `01_Projects/Reu.md`, sesión registrada · depende de: todo

## 2.1 Starter kits reutilizados
Ninguno aplica (no hay backend ni web de producto).

## 3. Estrategia de pruebas
- Vitest: unir frases (T-02), capa de datos (T-01), exportación (T-08).
- A mano, con reunión real: captura de extremo a extremo. Se hace con dos pestañas de Meet (una con otra cuenta o el móvil) y subtítulos activos.
- Ciclo completo crear → refrescar → borrar → refrescar, con recarga de Chrome entre pasos.
- Nota: Meet no se puede probar en automático (pide cuenta de Google). Declarar siempre qué se probó a mano.

## 4. Despliegue y operación
- Instalación: `npm run build` y «Cargar descomprimida» desde `dist/` en `chrome://extensions`. Sin Chrome Web Store.
- Copia de seguridad: botón «exportar todo» (T-08). Los datos viven solo en el navegador: si se borran los datos del sitio, se pierden.
- Si Meet cambia y deja de capturar: editar solo `src/selectors.ts`.

## 5. Riesgos y plan B
> [!riesgo]
> - Meet cambia el HTML de los subtítulos → selectores aislados y aviso (T-10).
> - Frases duplicadas o cortadas por la reescritura parcial → T-02 con pruebas antes de tocar Meet.
> - Este equipo no tiene Google Chrome instalado (constará en la sesión del 15-08) → comprobar `which google-chrome chromium` antes de T-00; si no hay, instalar Chromium o probar la extensión en otro equipo.
> - Plan B si leer el HTML se vuelve inviable: Meet permite descargar transcripción en cuentas de pago; no aplica a cuentas gratuitas, así que el plan B real es mantener los selectores.

## 6. Definición de terminado
- [ ] Reunión real capturada y exportada a `.md` correctamente
- [ ] `npm run build` y `tsc --noEmit` limpios; Vitest en verde
- [ ] Cerrar/abrir Chrome conserva los datos
- [ ] Reunión simulada de 2 h sin tirones
- [ ] README en el repo
- [ ] Ficha en `01_Projects/` y sesión registrada
- [ ] `.claude/COMMON_MISTAKES.md` actualizado si hubo fallos

---
Anterior: [[1 - PRD]]
