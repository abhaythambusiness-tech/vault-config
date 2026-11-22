---
type: sesion
date: '2026-10-25'
proyecto: '[[01_Projects/Neozeler CRM]]'
tags:
- crm
- doory
- canva
- n8n
- plan-fundadores
origen: mixto
---

> [!resumen] En cristiano
> Hoy se liberó memoria del servidor, se auditó el mini CRM y se cambió la oferta: ahora son **10 plazas**, **sin precio fijo** y la **demo solo después de hablar**. Se probó Doory (un «Canva» propio que instalamos en el servidor) y se montó una ficha visual de «Revisión de tu web» para el correo 1. Falta el botón de la ficha del CRM que mande los datos a n8n.

## Qué se hizo
- **Servidor:** se cerraron Brave y gnome-software (de 2.578 a 1.811 MB usados). El CRM gasta ~42 MB, no era el problema.
- **Auditoría CRM:** el circuito no se cierra solo (no lee respuestas, bajas ni rebotes de Gmail; permiso solo de envío), código sin primer commit, PIN inicial por chat sin cambiar.
- **Oferta (decidida por Haytham):** 10 plazas (antes 5), sin precios fijos en los correos, demo solo tras reunión o WhatsApp. Aplicado en `src/campana.ts`, pantalla «Hoy», README y pruebas (67 en verde); copia previa `~/backups/crm/antes-cambio-oferta-2026-10-25.db`.
- **Canva:** plantilla conceptual creada; descartada como motor automático porque Autofill exige Canva Enterprise.
- **Doory** (`~/Proyectos/doory-prueba/doory`, puerto 8080, ~570 MB RAM): instalado con Docker (+`docker-compose-v2`), 253 fuentes, packs de iconos, logos de marca, exportación en servidor y **MCP activado** (token con permisos mínimos registrado en Claude, ámbito usuario).
- **Plantilla «NeoZeler - Lo que ve tu cliente hoy»:** ficha de diagnóstico a 1800 × 3240 px con logo, 4 puntos rojo/verde, 3 mejoras con stickers. Campos: `nombre`, `web`, `puntuacion`, `estado_1..4`, `marca_1..4`, `punto_1..4`, `detalle_1..4`, `mejora_1..3`. Diseño de trabajo editable: `f5e8b41f-554c-4677-8eae-17d136539277`.

## Aprendizajes
- La API normal de Doory solo acepta sesión con contraseña; el **MCP sí usa tokens Bearer**, por eso n8n debe hablar con `/mcp` (`fill_design`).
- Los iconos de línea no se pueden recolorear por MCP (salen morados); los **stickers a color** sí funcionan.
- El botón «Copiar» del token falla en HTTP; se generó el token desde el servidor sin mostrarlo.
- Una sesión ya abierta no recarga los MCP nuevos: hay que abrir una sesión nueva.

## Pendiente
- Botón en la ficha del CRM → webhook n8n → `fill_design` de Doory → correos 1, 2 y 3 (n8n elegido, sin instalar aún).
- Revocar 5 tokens viejos de Doory; borrar la copia «Prueba MCP» si no hace falta.
- Del CRM: conectar Gmail, remitente, pie legal, cambiar el PIN, primer commit; valorar leer respuestas y bajas de Gmail.
- Si se descarta Doory: `sudo docker compose down -v` en su carpeta y quitar el MCP con `claude mcp remove doory`.

