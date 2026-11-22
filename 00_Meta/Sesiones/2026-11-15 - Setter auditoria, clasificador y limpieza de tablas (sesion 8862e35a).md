---
type: sesion
date: '2026-11-15'
proyecto: '[[Setter NeoZeler]]'
origen: maquina
sesion_id: 8862e35a-0e49-4f09-bdb1-f0847cb4072e
tags:
  - sesion
  - cierre-automatico
---

> [!resumen] En cristiano
> Se auditó el setter: se puede pasar de 5 flujos y 6 tablas a 3 flujos y 3 tablas. El flujo Analista ahora solo etiqueta (más barato) y ya está aplicado en n8n y probado. Se borraron dos tablas inútiles; la fusión de tablas quedó a medias porque Haytham interrumpió.

## Qué se hizo
- Auditoría: [[Setter NeoZeler - Auditoria de simplificacion]] (nada tocado en n8n al hacerla).
- Analista convertido en clasificador: devuelve solo etiquetas (negocio, interés, servicio, problema, seguimiento); prompt de ~1,7k a ~0,36k tokens; la recomendación para Mila la calcula el código. Haytham activó «disponible en MCP» (`Qemca8S4XGz7hKlZ`) y se aplicó con `prompt-clasificador.txt` y `ParsearAnalisis`. Un aviso previo, `builtInTools` del nodo OpenAI.
- Probado con el simulador (lote 8, 5 conversaciones); Haytham confirmó: «funciona todo». Nota previa: [[2026-11-15 - Setter clasificador y auditoria]].
- Borradas (con su sí) las tablas `panel_estado` y `Setter clinica`; quedan `setter_mensajes`, `setter_clientes`, `setter_analisis`, `setter_citas`. Flujo temporal archivado.
- Pedida y **interrumpida**: fusionar `setter_analisis` en `setter_clientes` (normalizar `chat_id` y teléfono, quitar `BuscarAnalisis` y la columna `resumen`). Su resultado: [[2026-11-15 - Fusion setter_analisis en setter_clientes]] (no verificado aquí).

## Pendientes (esperan OK de Haytham)
- Borrar filas de prueba restantes (lotes 0-4 y 8, cita «Javier»).
- Unir Errores a Discord con WhatsApp conexión.
- Comprobar que la fusión de tablas quedó completa.

## Relacionado
- [[01_Projects/Setter NeoZeler]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
