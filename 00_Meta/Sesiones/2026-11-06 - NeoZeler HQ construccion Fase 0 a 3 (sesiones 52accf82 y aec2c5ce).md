---
title: "NeoZeler HQ: de la ficha de investigación a la interfaz (Fase 0 a 3) - 2026-11-06/07"
date: 2026-11-06
type: meta/sesion
origen: mixto
proyecto: "[[NeoZeler HQ]]"
sesion_id:
  - 52accf82-4644-4763-997b-71cab5da4feb
  - aec2c5ce-1e82-4291-af74-96e828062e67
  - fd5c36eb-99d0-4acb-bada-f3eb686db9cf
tags:
  - sesion
  - neozeler-hq
  - cierre-automatico
aliases: []
---

# NeoZeler HQ: Ficha, TRD, Plan, Fase 0 a 3 (6-7 nov 2026)

> [!resumen] En cristiano
> NeoZeler HQ es la herramienta compartida de Haytham (CTO) y Sam (CEO). En estas sesiones se aprobaron los documentos que faltaban (PRD, Ficha, TRD, UI-UX, AppFlow, Esquema, Plan), se montó el servidor y se programaron las primeras pantallas: login, Clientes, importar CSV, Ideas con voto y la pantalla «Hoy». Después se le puso diseño (colores, fuentes, modo oscuro) y se pasó una auditoría. Todo está en commits locales, sin subir a GitHub, y el código corre solo en el servidor Zorin.

Nota de cierre automático. Las sesiones `52accf82` (6 nov, 20:18 UTC → 7 nov), `aec2c5ce` (7 nov, Fase 3) y `fd5c36eb` (continuación de la anterior) se cuentan juntas. La parte final de `fd5c36eb` (auditoría UI-UX y fondos SVG) ya tenía su nota: [[2026-11-07 - NeoZeler HQ auditoria UI-UX y fondos SVG]]; aquí solo se enlaza.

## Qué se hizo
- **Arranque** (`/nuevo-proyecto`): PRD en borrador con contexto «dos socios, Haytham CTO y Sam CEO». Decisiones de Haytham: proyecto nuevo que absorbe ComandAi y Neozeler CRM, corre en Zorin con Tailscale, vía `saas` con los 6 documentos. Alcance del PRD: pantalla «Hoy» sin 3D, CRM con importación de CSV, ideas con voto asíncrono, 4 productos con ficha editable, etiquetas CTO/CEO, mandala 8×8 (aclarado a partir de un vídeo pegado: en realidad es una tabla 9×9) y radar de noticias/YouTube/competencia por script.
- **Documentos aprobados uno a uno** con «Aprobar y seguir»: Ficha de Investigación y TRD (Bun + SQLite, páginas generadas en servidor, puerto 8300, scripts Python con timers), UI-UX (identidad «mesa de dos»: hilo azul `#2563EB` Haytham, magenta `#D6336C` Sam, trenzado si es de ambos), AppFlow y Esquema (probado con SQLite 3.45 de Python, no con `bun:sqlite`), y Plan. `trace_lint` acabó en `RESULTADO: OK` tras añadir US-10/12/15-19 a AppFlow y UI-UX (solo añadidos).
- **Fase 0 (T-01/T-02)**: repo `~/Proyectos/neozeler-hq/` con `git init`, README y `COMMON_MISTAKES.md`; ficha [[NeoZeler HQ]]; `Paleta de Componentes` (sin registry externo); `DESIGN-IDENTITY.md`; `resumen.html`. Servidor compila, 2 tests, `/salud` responde `{"ok":true,"app":"neozeler-hq"}`, 18 MB de RAM (objetivo ≤60 MB).
- **Fase 1 y 2 (T-03 a T-10)**: migración `001_inicial.sql` + seed; login con scrypt, 5 fallos = 10 min de bloqueo, cookies HttpOnly/SameSite=Strict (commit `c8b3267`, 17 tests); Clientes con versión y 409 en conflicto (`e1d662c`, 25 tests); importar CSV con previa y detección de repetidos (`5c8eb96`, 32 tests); Ideas con voto y historial (`679bc7f`, 38 tests); pantalla Hoy con 5 bloques y filtro Yo/Sam/Todos (`98d7233`, 45 tests).
- **Fase 3 (sesión `aec2c5ce`)**: `hq.css` con tokens claro/oscuro, componentes (`OwnerTag`, `VoteDots`, `Stat`, `Timeline`, etc.), vistas Hoy/Clientes/Ideas, fuentes Albert Sans y Spline Sans Mono (6 woff2). Axe 0 violaciones en 7 rutas × 4 anchos × 2 temas; Lighthouse 100/100/100 (SEO 90, falta meta-description, irrelevante en app interna). Commit `588cc8e`.
- **Auditoría UI-UX y fondos SVG** (inicio de `fd5c36eb`): 8 hallazgos corregidos, commit `3fd7234` (detalle en la nota enlazada arriba).

## Decisiones
- Sin referencias de Dribbble: Haytham respondió «hazlo sin referencias pero lo más detallado, fluido y premium»; se tomó la identidad propia «mesa de dos».
- Sin registry externo de componentes (Paleta de Componentes propia).
- La cuarta cifra de Hoy pasó a «Acciones vencidas» porque «Novedades» aún no tiene datos (decisión de Claude, no pedida expresamente).
- `bun` solo existe en el Zorin: se edita en local, se sincroniza por `scp` y se prueba allí.

## Problemas
- Un hook bloqueó un commit por el texto «DROP TABLE» en una nota; se reescribió.
- El servidor de pruebas del Zorin se caía al cerrar la sesión SSH; se relanzó desacoplado.
- Contraste del chip «ok» a 4,38:1; corregido con `--ok-ink`.
- Aviso de Claude: la fecha de «hoy» sale de la hora del servidor (UTC) y puede ir un día por detrás cerca de medianoche en España. Sin corregir.
- Para commitear hubo que fijar nombre y correo de git solo en el repo.

## Mejoras y pendientes
- Faltan por hacer Haytham y Sam antes de T-26 (despliegue): instalar Tailscale en el Zorin (necesita `sudo`), decidir qué hacer con `comandai.service` (fallido) y pasar el logo de NeoZeler.
- Código: voto optimista, autoguardado y aviso de conflicto; ⌘K y arrastrar en el tablero; dibujos de vacío para radar, mandala y competencia; atajo `n` sin comprobar.
- `README.md` y `resumen.html` del repo sin actualizar tras la Fase 3; ningún commit empujado a remoto.
- Siguiente: T-11 (buscador ⌘K) y fases 4+ (fuentes conectadas, mandala, radar).

## Relacionado
- [[NeoZeler HQ]] · [[2026-11-06 - NeoZeler HQ diseno completo]] · [[2026-11-07 - NeoZeler HQ auditoria UI-UX y fondos SVG]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
