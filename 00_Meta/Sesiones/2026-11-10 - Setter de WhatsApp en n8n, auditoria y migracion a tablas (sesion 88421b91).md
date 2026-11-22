---
title: "Sesión - 2026-11-10 - Setter de WhatsApp en n8n: auditoría y migración a tablas"
date: 2026-11-10
type: meta/sesion
origen: maquina
proyecto: ""
sesion_id:
  - 88421b91-8c42-4249-81f7-ff8e10a7bdbc
tags:
  - sesion
  - n8n
  - setter
  - cierre-automatico
aliases: []
---

# Sesión — 2026-11-10: Setter de WhatsApp en n8n, auditoría y migración a tablas

> [!resumen] En cristiano
> Haytham tiene un «setter»: un agente (Mila) que atiende por WhatsApp, agenda citas y resume cada charla. Se auditaron sus tres flujos de n8n, se encontraron fallos serios y se rehicieron sin Airtable ni Google Calendar: ahora todo vive en 4 tablas de n8n, los errores van a Discord y hay un aviso para reconectar el número cuando Evolution API se desconecta. Los flujos están generados en `~/Proyectos/setter-neozeler/` pero Haytham los estaba importando y configurando a mano; falta publicarlos y probarlos con un número real.

## Contexto
Flujos exportados por Haytham: `Setter`, `Analista_Aconsejador` y `Agendar cita`. Cadena: Webhook (Evolution API) → Airtable → Mila → trocear mensaje → Evolution API; en paralelo el Analista guarda el resumen en el CRM. El MCP de n8n de la sesión no permite listar ni leer workflows, así que la auditoría se hizo sobre los JSON.

## Qué se hizo
- Auditoría breve con fallos serios: webhook abierto sin autenticación (y `server_url`/`apikey` de Evolution venían en el cuerpo), clientes en silencio para siempre tras «hablamos el lunes» (el campo `Seguimiento` no se reiniciaba), comparación de textos que daba doble respuesta con dos «ok» iguales, entre otros.
- Generación en `~/Proyectos/setter-neozeler/` (`build.py`, `README.md`, 5 workflows en `workflows/`): setter sin Airtable, espera de 8 s y solo contesta la última ejecución; `Agendar cita` solo usa la tabla `citas` (valida formato, antelación, horario y hueco libre; la cita anterior pasa a `reagendada`).
- Creadas en el n8n de Haytham 4 tablas: `setter_clientes`, `setter_mensajes`, `setter_analisis` y `setter_citas` (la tabla `Setter clinica` no se tocó).
- Errores a un webhook de Discord y workflow «WhatsApp – Conexión»: cada 5 minutos comprueba el estado en Evolution y, si está `close`, manda a Discord un enlace con el QR (antispam de 30 min).
- Guía paso a paso con Haytham: credenciales, marcadores `TU_*`, expresiones de `chat_id` y de `agendar_cita`; el Manager de Evolution no permite cabeceras, así que el secreto pasó a ir dentro de la URL del webhook (sin credencial `Webhook Setter`).
- Diagnóstico del aviso mudo: `Decidir` daba `enviar:false` por el antispam; se explicó cómo forzar la prueba. Haytham confirmó que le llegó el mensaje a Discord con el QR.
- Se creó el perfil `neozeler` de `diagram-design` (el marcador del vault apuntaba a uno inexistente) y `diagrama-setter.html`: visión general y detalle con subworkflows, para explicárselo al CEO o a socios.

## Decisiones tomadas
- Airtable fuera: tablas de n8n. Citas solo en tabla, sin Calendar ni Gmail.
- Secreto del webhook en la URL (no en cabecera) por limitación de Evolution.
- No interactuar con el setter real sin un número de prueba de Haytham.

## Aprendizajes (para futuras sesiones)
- Al reelegir un workflow en un nodo `Execute Workflow` n8n borra los valores de los campos: hay que volver a poner las expresiones.
- Las URL de test de un webhook no sirven en producción; solo la de producción con el workflow activo.
- Un workflow sin pulsar **Publish** no corre los cron automáticos.

## Problemas abiertos
- Sin probar con tráfico real: ni el setter completo ni el cron de conexión de punta a punta.
- Workflows importados a mano: hay que comprobar que `agendar_cita` y `EjecutarAnalista` apuntan a los IDs nuevos.
- Rotar cualquier secreto o API key que se haya pegado en el chat.

## Próximos pasos
- Publicar el workflow de conexión; probar con un número propio; borrar la línea de prueba de `Decidir`.
- Enseñar el diagrama al CEO y decidir si el setter pasa a producto.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
