---
title: "Sesión - 2026-10-26 - CRM - correos personalizados y modo prueba"
date: 2026-10-26
type: meta/sesion
proyecto: "[[Neozeler CRM]]"
sesion_id: 7278cd39-e347-4ea2-8fc0-27523aaa06c9
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-10-26: CRM: correos personalizados y modo prueba

> [!resumen] En cristiano
> Se hicieron los correos automáticos del CRM más personales: dicen que ya se hizo trabajo antes de escribir y tocan el dolor del negocio. Se aclaró cómo funciona el modo prueba, para no mandar correos reales sin querer.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `7278cd39`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Nuevos archivos `personalizar.ts`, `webhook.ts`, `n8n/redactar.js` y su test.
- Se explicó el interruptor del nodo «Redactar» en n8n: `const MODO = 'prueba'` envía el correo idéntico al buzón de pruebas; `'enviar'` lo manda al negocio.
- Haytham reportó que salía siempre el mismo correo y errores tras quitar lo de prueba (con capturas).

## Decisiones tomadas
- Para probar un negocio real no cambiar n8n: abrir su ficha en el CRM y pulsar Enviar (llega al buzón de pruebas).

## Archivos y proyectos afectados
- `crm/src/personalizar.ts`
- `crm/src/webhook.ts`
- `crm/n8n/redactar.js`
- `crm/tests/personalizar.test.ts`

## Problemas
- Correo repetido para negocios distintos (síntoma reportado por Haytham); la sesión cerró con la explicación del modo prueba, sin confirmar que se resolviera.
- Peligro: «Enviar los 10 de hoy» con `'enviar'` manda 10 correos reales.

## Mejoras propuestas
- Mostrar en el CRM un aviso visible del modo activo (prueba/enviar).

## Pendientes y próximos pasos
- Confirmar que cada negocio genera un correo distinto.

## Relacionado
- [[2026-10-26 - Reforma del CRM]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
