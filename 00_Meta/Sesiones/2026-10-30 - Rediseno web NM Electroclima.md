---
type: sesion
date: '2026-10-30'
proyecto: '[[NM Electroclima]]'
origen: mixto
---

> [!resumen] En cristiano
> Se rediseñó por completo la web de NM Electroclima (landing y panel) con estilo «plano técnico».

## Decisiones
- Dirección visual «plano técnico» y SVG ilustrados (elegidos por Haytham).
- Panel `/admin` restilado conservando su lógica; quitados restos de plantilla Vite.

## Aprendizajes
- Vite 8 exige Node 20+: usar Node 22 de fnm (el del sistema es 18).
- No enviar formularios de prueba: la web escribe en el Supabase real del cliente.

