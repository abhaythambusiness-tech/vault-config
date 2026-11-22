---
title: 'Sesión - 2026-11-14 - Panel de Leads: conexión a n8n real, UI/UX y resumen'
date: '2026-11-14'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/Panel de Leads]]'
sesion_id: 05823626-b3a6-4a13-8fdc-9efe353784ed
tags:
- sesion
---

> [!resumen] En cristiano
> Se recuperó el «buffer» del Setter (espera unos segundos para juntar mensajes seguidos) y se publicó. Luego se creó el Panel de Leads desde cero (documentos, identidad, código, login, Docker) y, al final, se conectó al n8n real, se rehízo la interfaz y el Resumen pasó a ser la pantalla principal. Queda sin commit parte del trabajo de UI y hay una clave de n8n pegada en el chat que conviene rotar.

## Qué se hizo
- **Setter:** el buffer estaba escondido en el nodo `Agrupar`; ahora hay un `If` visible (`EsUltimoMensaje?`), espera de 8 s (`EsperaMensajes`) y `PendientesChat` junta los mensajes. Publicado; versión anterior restaurable en el historial de n8n (`810246e9…`). Sin probar con WhatsApp real.
- **Panel de Leads** (vía micro SaaS ligera): PRD, Ficha, TRD, Plan, identidad y Paleta de Componentes aprobados; scaffold Next 16 + shadcn; cliente n8n (`src/lib/n8n.ts`), cruce de leads, pipeline, ficha `/lead/[telefono]`, script `tools/alta` en Go, login (pbkdf2), Docker + Caddy verificados en Zorin, lista y resumen semanal. Cierre y retro en [[00_Meta/Sesiones/2026-11-14 - Panel de Leads construccion y cierre]]; arranque en [[00_Meta/Sesiones/2026-11-13 - Panel de Leads arranque y buffer del Setter]].
- **Tramo final:** instancia de marca NeoZeler (`#2563eb`), conexión a n8n real (5 tablas, vacías al principio), leads y mensajes `[PRUEBA]` insertados (24 filas) y comprobados en la ficha, auditoría UI/UX (columnas que caben, bloque «Requieren atención», botones WhatsApp/Llamar), Resumen con gráficas y como página principal (`/`; pipeline en `/pipeline`), «en proceso» a violeta, barra superior fija y fondo SVG.

## Decisiones
- Se usa la API pública de n8n aunque la clave no se pueda limitar solo a tablas (cada cliente tiene su VPS).
- Quitada la regla de «señal de demanda» solo para Panel de Leads (decisión de Haytham, 2026-11-13); el Paso 0 general no se tocó.
- Librerías de UI mínimo 1-2 obligatorias: entrada 92 en `COMMON_MISTAKES.md`, skill `nuevo-proyecto` y plantilla TRD.

## Problemas
- Dos claves de n8n pegadas en el chat (una de prueba, otra para el panel): **rotarlas**. No se guardaron en disco.
- Quedan 24 filas `[PRUEBA]` en las Data Tables: borrar a mano antes de probar el Setter real. La cita debe tener `estado = agendada`.

## Pendientes
- Commitear el trabajo de UI posterior a `a718e03` (sin commit); no se pasó axe ni Lighthouse.
- Probar login tras el cambio de rutas, botones WhatsApp/Llamar y mover etapa (escribe en `panel_estado`).
- Probar el Setter real y ver que aparece en el panel; ningún `git push` hecho.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

