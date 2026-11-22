---
type: sesion
date: '2026-11-15'
proyecto: '[[Setter NeoZeler]]'
origen: maquina
sesion_id: f213b7ed-40be-4a8e-b6a3-2495ca2fa4de
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Se creó un programa que imita los mensajes de WhatsApp para probar a Mila (el setter) con 5 conversaciones falsas. Salieron fallos, se corrigió el prompt y se limpiaron las filas de prueba. Después se midió: Mila tarda ~17 s en contestar y una conversación cuesta 0,03–0,06 $. Esta sesión se interrumpió al pedir el prompt v2 (sigue en la sesión 36bd7f22).

## Qué se hizo
- Simulador en Go: `~/Proyectos/setter-neozeler/scripts/simulador/` (`main.go` y binario). Envía 5 conversaciones (20 mensajes) al webhook de producción con números ficticios `3400000000X`; 20/20 HTTP 200.
- Corrección del prompt de Mila en el workflow Setter de n8n (ya en producción): responde primero la pregunta, no repite preguntas, explica NeoZeler en una frase, rechaza lo ajeno al negocio, no promete resultados al escéptico.
- Borradas (con el sí de Haytham) las filas de prueba `34000…` de `setter_mensajes`, `setter_clientes`, `setter_citas` y `setter_analisis`, mediante workflows temporales de borrado (el MCP de n8n no borra filas); quedan archivados.
- Medición con 3 ejecuciones reales: ~$0,0067 por mensaje del cliente, ~17 s de respuesta (8,1 s solo de espera de buffer), ~6 mensajes del cliente para agendar, GPT-4.1 mini.

## Pendientes
- Eliminar del todo los dos workflows `TMP borrar…` archivados en n8n.
- Cambios del prompt v2 y buffer: ver [[2026-11-15 - Mila v2 prompt corto y buffer]].

## Relacionado
- [[01_Projects/Setter NeoZeler]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
