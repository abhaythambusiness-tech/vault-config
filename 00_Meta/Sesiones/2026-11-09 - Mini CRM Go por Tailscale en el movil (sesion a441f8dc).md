---
title: "Sesión - 2026-11-09 - Mini CRM Go: despliegue descartado y acceso por Tailscale"
date: 2026-11-09
type: meta/sesion
origen: mixto
proyecto: "[[01_Projects/Mini CRM Go]]"
sesion_id: a441f8dc-8b69-422c-851a-0a3d1e93db94
tags:
  - sesion
  - crm
  - despliegue
  - tailscale
aliases: []
---

# Sesión — 2026-11-09: Mini CRM Go, Vercel descartado y acceso por Tailscale

> [!resumen] En cristiano
> Haytham quiso publicar el CRM en Vercel (antes había pedido Netlify). Se le explicó que no se puede: el CRM guarda sus datos en un archivo y Vercel los perdería, y además no tiene contraseña y tiene 1879 negocios con correos y teléfonos. Se eligió dejarlo en su PC y abrirlo desde el móvil por Tailscale (una red privada). Quedó publicado, pero el móvil aún no estaba conectado.

## Contexto
Continuación de las sesiones de `[[01_Projects/Mini CRM Go]]` del 8 de noviembre (migración a React y pipelines: `[[00_Meta/Sesiones/2026-11-08 - Migracion frontend Mini CRM Go]]` y `[[00_Meta/Sesiones/2026-11-08 - Pipelines y rediseno Mini CRM Go]]`). Esta sesión retoma desde el backend de pipelines y el rediseño (commit `fda54b3`, servido en `http://127.0.0.1:8080/app/`).

## Qué se hizo
- Backend de pipelines (esquema y siembra) y rediseño: barra lateral con pipelines General, Webs y Tier A, 7 etapas fijas por pipeline, vistas Tablero (arrastrar) y Tabla, reglas por servicio, tier o tipo de contacto. Tests de Go pasan; axe 0 violaciones; arrastrar con el ratón no se probó.
- Haytham pidió desplegar en Vercel. Claude lo desaconsejó y ofreció tres salidas; la elegida fue «dejarlo local y entrar desde el móvil por Tailscale».
- Instalación de Tailscale en el PC, inicio de sesión, activación de «Serve» en la cuenta y `sudo tailscale serve --bg 8080`. Dirección privada: `https://haytham-b75.tail5b8c39.ts.net/app/` (solo dentro de la red Tailscale). Para quitarlo: `sudo tailscale serve --https=443 off`.
- El servicio responde 200 desde el PC.

## Decisiones tomadas
- Nada de Vercel/Netlify para este CRM: SQLite en archivo no sobrevive a funciones serverless y no hay login con datos de 1879 negocios. Alternativa futura citada: frontend en Vercel + backend en el servidor Zorin con login, accesible por Tailscale o túnel.
- Acceso solo por red privada, sin exponer a internet.

## Problemas y pendientes
- Al cierre, el móvil no aparecía en `tailscale status`: faltaba instalar la app de Tailscale en el móvil con la misma cuenta y activar la conexión (Haytham dijo «no lo puedo abrir en mi móvil»).
- Funciona solo con el PC encendido y el servicio `minicrm` activo.
- Una contraseña de sudo mal escrita causó un reintento; no se guardó ninguna.

## Relacionado
- [[01_Projects/Mini CRM Go]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
