---
title: Sesión - 2026-11-15 - Fusión setter_analisis en setter_clientes
date: '2026-11-15'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/Setter NeoZeler]]'
tags:
- sesion
aliases: []
---

# Sesión — 2026-11-15: Fusión de setter_analisis en setter_clientes

> [!resumen] En cristiano
> Mila guardaba lo que averigua de cada cliente (negocio, interés, problema) en una tabla aparte. Ahora vive en la ficha del propio cliente: una sola tabla, un solo número de teléfono como llave. Los flujos de n8n ya leen y escriben ahí y se probaron sin enviar WhatsApps reales.

## Contexto
Proyecto [[01_Projects/Setter NeoZeler]]. Dos tablas con claves distintas (`chat_id` con `@s.whatsapp.net` en análisis, `telefono` sin prefijo 34 en clientes) obligaban a una búsqueda extra (`BuscarAnalisis`) por mensaje.

## Qué se hizo
- `setter_clientes` ya tenía las columnas de análisis y los datos migrados (teléfono sin prefijo 34, `interes` capitalizado). Sin columna `resumen`.
- Setter (`EngqAtjDTlXIavjR`): eliminado `BuscarAnalisis`; `HistorialChat` conecta directo a `ArmarHistorial`, que lee las etiquetas de `BuscarCliente`.
- Analista (`Qemca8S4XGz7hKlZ`): `ParsearAnalisis` deriva `telefono` del `chat_id` y no genera `resumen`; `GuardarAnalisis` hace `update` en `setter_clientes` por `telefono`.
- Repo `~/Proyectos/setter-neozeler/`: `build.py`, `README.md`, `ids.json` (sin `analisis`), `tablas/analisis.csv` borrado, `resumen.html` con el texto nuevo.
- Pruebas: Analista (ejecución 37946, `update` de la fila 32) y Setter de punta a punta con webhook simulado (ejecución 37947): `ArmarHistorial` leyó bien `tipo_negocio`, `problema_motivo` y `servicio_interes` de la fila.

## Decisiones tomadas
- Clave única `telefono` (9 dígitos) en clientes; `chat_id` completo solo en `setter_mensajes`.
- `update` y no `upsert` en `GuardarAnalisis`: el Setter crea siempre el cliente antes, así no aparecen filas sin nombre.
- Se descarta `resumen`.

## Aprendizajes (para futuras sesiones)
- `ArmarHistorial` lee las etiquetas **antes** de la espera de 20 s; si el Analista no terminó el turno anterior, va una versión atrás. Aceptado, poco probable.
- El `build.py` del repo ya no reproduce el JSON vivo (el original ya no existe); la verdad está en n8n.
- Las pruebas con `test_workflow` ejecutan las tablas de verdad: dejan filas reales.

## Próximos pasos
- Borrar la tabla `setter_analisis` desde la interfaz de n8n (no hay herramienta para ello).
- Borrar las 2 filas `[PRUEBA]` de `setter_mensajes` (chat `34000008001`).
- Probar el Analista con OpenAI real.

## Relacionado
- [[01_Projects/Setter NeoZeler]]
- [[2026-11-15 - Setter clasificador y auditoria]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

