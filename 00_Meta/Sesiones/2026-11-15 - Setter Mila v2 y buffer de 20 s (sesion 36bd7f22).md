---
type: sesion
date: '2026-11-15'
proyecto: '[[Setter NeoZeler]]'
origen: maquina
sesion_id: 36bd7f22-587a-42f1-b130-7bd57c0f5a24
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Haytham probó a Mila en real y la encontró pesada: hacía unas 12 preguntas y repetía. Se acortó su prompt (v2, máximo 5 preguntas), se alargó la espera de mensajes a 20 s y se instaló la skill de psicología de marketing. Mila repite menos, pero aún repite alguna pregunta.

## Qué se hizo
- Retoma el trabajo de [[2026-11-15 - Setter simulador de 5 conversaciones y costes (sesion f213b7ed)]]: mismo simulador, mismas mediciones.
- Revisión de la conversación real (chat 34640174685, 19:25): ~12 preguntas, varias repetidas; al decir «Sí» a la auditoría, Mila contestó el precio en vez de agendar.
- Cambios aplicados en el n8n real: prompt más corto, buffer `EsperaMensajes` a 20 s, skill `marketing-psychology` instalada y añadida a la configuración.
- Repo sincronizado: `workflows/1 - Setter.json` y `build.py` con el prompt v2 (`prompt-mila-v2.txt`, 5.918 caracteres) y el aviso de preguntas. `build.py` solo comprobado de sintaxis, no ejecutado.
- Filas de prueba 34000005/34000006 siguieron sin borrar hasta el sí de Haytham.
- Última petición, un HTML explicativo con costes y tiempos: se continúa en [[2026-11-15 - Setter resumen html y auditoria (sesion 4c174cc9)]].

## Pendientes
- Ejecutar `build.py` para verificar que genera el mismo JSON.
- Que Mila deje de repetir preguntas del todo.

## Relacionado
- [[2026-11-15 - Mila v2 prompt corto y buffer]]
- [[01_Projects/Setter NeoZeler]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
