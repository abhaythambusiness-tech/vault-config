---
type: sesion
origen: mixto
date: 2026-11-06
proyecto: "[[01_Projects/Vault OS]]"
---

> [!resumen] En cristiano
> Las notas ahora se leen como en Obsidian (sin ver el código). El CRM se abre grande, tiene una pestaña Laya donde preguntas «quién puede pagar un agente de 1500 €» y pasa los leads al CRM. Arriba se ve si Haytham (CTO) o Sam (CEO) están conectados y qué hacen.

## Qué se hizo
- Notas: markdown-it seguro, callouts, wikilinks, tareas, tablas; Ctrl+E Ver/Editar.
- CRM: Pipeline, Tabla, Laya; importar CSV a mano, idempotente.
- Presencia: latido cada 15 s, caduca a 45 s.

## Aprendizajes
- La «petición a Laya» usa reglas transparentes sobre el CSV, no el modelo Laya (su test de calidad falló). Cada resultado explica su motivo.
- `data/leads_laya.csv` son datos de terceros: ignorado por git y nunca copiado al vault. Importar un lead crea su nota en el CRM del vault (decisión de Haytham al pedir el CRM conectado).
- La escena 3D no se vio (WebGL apagado en el panel).
