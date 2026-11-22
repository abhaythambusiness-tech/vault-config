---
title: 'Mini CRM Go: ficha de Laya Leads, construcción y paneles'
date: '2026-11-07'
type: meta/sesion
origen: mixto
proyecto: '[[01_Projects/Mini CRM Go]]'
sesion_id: 093138cb-b64b-4252-931a-155268140691
tags:
- sesion
- cierre-nocturno
---

> [!resumen] En cristiano
> Primero se documentó cómo funciona Laya Leads por dentro. Después se construyó desde cero un mini CRM en Go (programa ligero con base de datos SQLite) para vender 4 servicios de IA a 1.879 negocios de Málaga. Quedó con panel, tabla, kanban, vista «Hoy» y un rastreador de webs que se lanzó en segundo plano. Ojo: el 12-nov Haytham dijo que ningún CRM le convence (ver pendientes).

## Qué se hizo
- Ficha [[01_Projects/Laya Leads - Funcionamiento interno]], sacada del código real del servidor Zorin (sin ejecutar nada allí).
- Proyecto `~/Proyectos/minicrm-go/` en 5 pasos: esquema + importador CSV (1.879 negocios, reimportar no duplica), rastreador de señales por web, reglas de servicio (webs, setter, software, automatizaciones), servidor y plantillas HTMX/Tailwind.
- Se instaló Go 1.22.2 (Haytham ejecutó el `sudo`).
- Identidad visual en borrador `DESIGN-IDENTITY.md` (huella de 4 azulejos por negocio) y registrada en `03_Resources/Registro de Identidades Visuales.md`.
- Clasificación: de 3-7 leads a 1.269 de 1.879 con al menos una señal (traduciendo las señales de Laya del CSV).
- `crm investigate-all` (6 trabajadores, reanudable) lanzado en segundo plano; estimado más de 1 h.
- Vista Panel con KPIs, embudo, feed y chips; cabecera con indicador de scraper activo.
- Auditoría UI/UX y arreglos: móvil (contenido empieza a 436 px en vez de 681), kanban móvil de 12.000 px a 1.150 px, accesibilidad.
- Siguiente paso con fecha por lead, vista «Hoy» y notas autoguardadas.
- Commits `8100096`, `2cf4ca1`, `b2ec996`, `9176ea3`, `b7e453f`, `882e33d`; ficha [[01_Projects/Mini CRM Go]] y README.

## Decisiones tomadas
- Este CRM va aparte y se usa en la práctica en lugar de Neozeler CRM y de la parte CRM de NeoZeler HQ (se guardó en memoria). No se tocaron las fichas antiguas.
- Pasar por `diseno-central` y aprobar identidad antes de maquetar.
- Opción A para clasificar: traducir señales de Laya en vez de esperar al rastreo completo.

## Problemas
- Go no estaba instalado; test fallido por el BOM literal (arreglado con escape).
- Setter y Software quedan cortos de datos hasta terminar `investigate-all`.
- El hook de commits de UI busca capturas en `vault/.capturas/`; se copiaron allí (sin seguimiento en git).
- Git sin identidad: se fijó solo en ese repo.

## Pendientes y próximos pasos
- Comprobar que `investigate-all` terminó y revisar el log `data/investigate-all.log`.
- No se probó 768 px ni Lighthouse.
- Superado el 12-nov: Haytham descartó todos los CRM ([[2026-11-12 - Cierre nocturno]]); decidir si archivar esta ficha.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

