---
title: Setter, robustez, prompt y analista
date: '2026-11-21'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/Setter NeoZeler]]'
tags:
- sesion
- setter
- n8n
---

> [!resumen] En cristiano
> Mila (el Setter de WhatsApp) quedó más robusta y más obediente: no contesta dos veces, no pierde mensajes si falla la IA, contesta el precio primero y explica «cómo funciona» como asistente de texto, no de voz. Se borraron los chats de prueba y se documentó todo en el README del repo.

## Qué se hizo
- Robustez del Setter vivo (`DedupeMensaje`, timeouts, reapertura de mensajes y aviso de fallo) y publicado (detalle: `~/Proyectos/setter-neozeler/ROBUSTEZ.md`).
- Ráfaga de 27 lotes con `simulador -groq`: el dedupe no bloquea mensajes legítimos. Limpieza de chats de prueba (297 mensajes, 61 clientes; citas vacías).
- Analista: `GuardarAnalisis` apuntaba a una tabla vieja; se publicó el borrador para que escriba en `setter_clientes`. Regla nueva: «pierde llamadas» ≠ «Agente de voz» (versión `db02f405`).
- Prompt de Mila: precio primero y «cómo funciona» = asistente de texto por WhatsApp (versión del Setter `574d2cc7`).
- Pruebas reales con el número de Haytham: entrega por WhatsApp correcta, baja respondida una vez y chat silenciado.
- Documentado en el README: filtros `SinBaja?` y `TemaAjeno?`, nodos de robustez, flags del simulador.

## Aprendizajes
- La copia de n8n manda sobre `workflows/*.json`; el README lo dice.
- `probador-groq` choca con la cuota de Groq (429); `gpt-oss-20b` como alternativa.
- Sin tool para borrar filas de Data Tables: workflow temporal con `deleteRows` y `dryRun` primero.
- La clave de Groq pegada en el chat es efímera: rotarla en console.groq.com.

## Pendiente
`agendar_cita` real, piloto con 5-10 conversaciones, ampliar `TemaAjeno?`, prueba real de «cómo funciona».
