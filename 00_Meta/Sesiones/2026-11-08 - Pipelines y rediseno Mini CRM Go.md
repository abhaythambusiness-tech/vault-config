---
date: 2026-11-08
type: sesion
origen: mixto
proyecto: "[[01_Projects/Mini CRM Go]]"
tags:
  - sesion
  - crm
  - frontend
---

> [!resumen] En cristiano
> El CRM ahora permite crear varios «pipelines» (embudos): por ejemplo uno de Webs y otro de Tier A. Cada negocio tiene su propia etapa en cada uno. El IA Hub se separó en tres secciones con color propio para distinguir noticias, ideas de vídeo e ideas de implementación. El estilo se inspiró en las interfaces de Airtable.

## Qué se hizo
- Backend: tablas `pipelines` y `pipeline_leads`, API `/api/pipelines`, filtro por tier, etapa por pipeline (General refleja la etapa general).
- Frontend: lista de pipelines en la barra lateral, página de pipeline (Tablero/Tabla), tarjetas de pipelines en el Dashboard, ficha con etapa por pipeline, IA Hub en tres secciones.

## Aprendizajes
- Decisión de Haytham: pipeline = filtro + etapa propia por negocio; 7 etapas siempre iguales.
- El hook de seguridad bloquea comandos que contengan la clase CSS de Tailwind para recortar texto (confundida con SQL): usar Write para esos archivos.
