---
type: sesion
date: '2026-11-15'
proyecto: '[[Setter NeoZeler]]'
origen: mixto
---

> [!resumen] En cristiano
> El flujo Analista del setter ahora solo clasifica (negocio, interés, servicio, problema, seguimiento) y ya no escribe resúmenes: más barato y más rápido. Está aplicado en n8n y Haytham confirmó que funciona. Además hay una propuesta de simplificar (menos flujos y tablas) pendiente de su OK.

## Hecho
- Auditoría de flujos y tablas del setter: [[Setter NeoZeler - Auditoria de simplificacion]] (5→4 flujos, 6→3 tablas, propuesta).
- Analista convertido en clasificador: `prompt-clasificador.txt` (~0,36k tokens, antes ~1,7k) y `ParsearAnalisis` con recomendación por reglas. Aplicado en `Qemca8S4XGz7hKlZ` (versión «Analista pasa a clasificador»).
- Costes: clasificador ≈ $0,002 por conversación; total setter ≈ $0,013 (precios OpenAI de memoria, sin verificar). `resumen.html` actualizado.
- Prueba con el simulador (lote 8): Haytham confirma «funciona todo».

## Decisiones
- El Analista sigue como flujo aparte (no se mete en el Setter).

## Pendiente (esperan OK de Haytham)
- Borrar tablas `panel_estado` y `Setter clinica`; fusionar `setter_analisis` en `setter_clientes`; unir Errores a Discord con WhatsApp conexión.
- Borrar filas de prueba (lotes 0-4 y 8, cita «Javier»).
- Mila: a veces reformula la pregunta del sector y busca hueco antes de aceptar la auditoría.

