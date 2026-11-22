---
title: "Sesión - 2026-10-31 - NeoZeler Web - arranque del proyecto hasta T-11"
date: 2026-10-31
type: meta/sesion
proyecto: "[[NeoZeler Web]]"
sesion_id: 64712084-4014-4e33-84fa-79938c13aace
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-10-31: NeoZeler Web: arranque del proyecto hasta T-11

> [!resumen] En cristiano
> Se arrancó la web de NeoZeler con el flujo de 6 documentos y se construyeron las primeras 11 tareas: formulario «cuéntanos tu caso», agendar llamada y SEO. Aún sin publicar ni empujar a GitHub.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `64712084`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Flujo de 6 documentos aprobados; una sola web con formulario y reserva de llamada con calendario; sin precios ni ofertas por ahora.
- PRD con opción C, identidad aprobada y la Z en SVG plano; despliegue previsto en Vercel.
- Integraciones: Google Calendar y webhook de n8n.
- T-01 a T-11 en `~/Proyectos/neozeler-web`; T-11 (SEO, `robots`, `sitemap`, JSON-LD, Open Graph) en commit `9edcd3b`, sin push.

## Decisiones tomadas
- Vercel como despliegue; el porqué de no usar una librería de componentes se explicó a petición de Haytham.

## Archivos y proyectos afectados
- `~/Proyectos/neozeler-web/`
- `01_Projects/NeoZeler Web/6 - Plan de Implementacion.md`

## Problemas
- La URL base apunta a `http://localhost:3000` hasta fijar `NEXT_PUBLIC_SITE_URL`.
- T-11 sin marcar: su «hecho» pide Lighthouse SEO y eso se mide en T-12.

## Mejoras propuestas
- Imagen social horizontal propia en vez del logo cuadrado.

## Pendientes y próximos pasos
- Fijar dominio y variable.
- T-12 verificación (Lighthouse, axe, 375/768/1280 px).

## Relacionado
- [[NeoZeler Web]]
- [[2026-10-31 - Arranque NeoZeler Web]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
