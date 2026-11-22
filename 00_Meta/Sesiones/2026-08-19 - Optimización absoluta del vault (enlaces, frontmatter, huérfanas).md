---
title: Sesión - 2026-08-19 - Optimización absoluta del vault (enlaces, frontmatter,
  huérfanas)
date: '2026-08-19'
type: meta/sesion
tags:
- sesion
- mantenimiento
aliases: []
origen: mixto
---

> [!abstract] Resumen
> Auditoría completa del vault (159 notas) a petición del usuario ("optimización de datos absoluta"): enlaces rotos, notas huérfanas, duplicados, frontmatter inconsistente y plugins redundantes. Se repararon 7 enlaces con candidato único inequívoco y se enlazaron 3 notas huérfanas recientes; el resto queda documentado como decisión pendiente.

## Qué se hizo
- Extraídos y verificados los ~244 wikilinks del vault contra los 159 archivos reales (script Python ad-hoc, no guardado).
- Reparados 7 enlaces con candidato único:
  - `[[NeoZeler - Modelo de precios]]` → `NeoZeler - Modelo de Precios` (2 notas de Nichos, error de mayúscula).
  - `[[02_Areas/NeoZeler/NeoZeler MOC]]` → `[[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler - MOC]]` (4 notas: 1 investigación + 3 sesiones — el campo `proyecto:` del frontmatter apuntaba a una nota que nunca existió con ese nombre).
  - `[[02_Areas/NeoZeler/Servicios/transcripciones_completas_ecommerce]]` → ruta actual en `04_Archive/` (la nota se archivó después de crear el enlace).
- Corregido `type: resource` (inglés) → `type: nota` en `00_Meta/Plantillas/Plantilla_Nota_Estandar.md` — era el único valor en inglés de todo el vault y se habría propagado a cada nota nueva creada desde la plantilla.
- Enlazadas 3 notas huérfanas creadas en esta sesión/las anteriores (sin ningún backlink entrante):
  - `Public APIs - Lista colaborativa de APIs gratuitas` y `Librerías de iconos y componentes UI frontend` → añadidas a `[[03_Resources/README]]`.
  - `Herramienta - Scraper de leads OSM (neozeler-leads)` → añadida a la tabla de fuentes de `[[02_Areas/NeoZeler/Comercial/NeoZeler - Prospección y captación]]`.
- Verificado que el bug de frontmatter vacío (YAML duplicado como texto dentro de `content` por pasarlo mal a `create_note`, corregido hoy en la nota de iconos) no se repite en ninguna otra nota del vault — 0 casos encontrados.
- Verificado: sin notas completamente vacías, sin duplicados de nombre de archivo real (solo los `README.md` legítimos de cada carpeta), fechas de frontmatter en formato correcto en todo el vault.

## Decisiones tomadas
- No se repararon enlaces con 0 o 2+ candidatos — se listan abajo como pendiente en vez de adivinar.
- No se tocaron los plugins de Obsidian (solo se diagnosticó la redundancia) ni se borró ninguna nota — cualquier acción destructiva queda para que la decida el usuario.

## Aprendizajes (para futuras sesiones)
- El patrón `proyecto: "[[02_Areas/NeoZeler/NeoZeler MOC|NeoZeler]]"` en el frontmatter de sesión llevaba roto desde que existe (aparece en sesiones de 2026-08-09, 2026-08-10 y 2026-08-16) — nunca existió una nota "NeoZeler MOC" a secas, el hub real siempre se llamó "NeoZeler - Master Command Center". Vale la pena revisar el snippet/plantilla que genera ese campo si sigue produciendo el nombre incorrecto.
- Comprobar `.obsidian/plugins/*/manifest.json` es más rápido y fiable que adivinar por el nombre del plugin para detectar solapamiento funcional real (confirmado aquí: `google-drive-sync`, `google-drive-vault-sync` y `remotely-save` los tres declaran explícitamente "sync vault to cloud").

## Pendiente de decisión del usuario
- **Plugins de sincronización redundantes**: `google-drive-sync` + `google-drive-vault-sync` + `remotely-save` instalados a la vez — los tres sincronizan el vault a la nube, con riesgo real de conflictos/escrituras duplicadas si más de uno está activo. Decidir cuál mantener.
- **Enlaces rotos sin candidato** (contenido nunca creado, no reparable por renombrado):
  - `[[diseno-servicios-neozeler]]` — metodología de diseño de servicios referenciada, nunca escrita.
  - `NeoZeler - Competencia` — análisis de competencia de NeoZeler (no confundir con el de Dropshipping, que sí existe).
  - 9 fichas de servicio de los nichos "Instalación" (solar) y "Distribución", presentes en la tabla de precios de `[[02_Areas/NeoZeler/Estrategia/NeoZeler - Modelo de Precios]]` pero sin ficha propia: Centralita IA de Avisos, Comercial Interno IA, Guardián de Preventivos, Normalizador de Catálogo, Parte de Trabajo sin Papel, Pedido Omnicanal al ERP, Presupuesto Express (genérico), RFQ Automática a Proveedores, radar de clientes dormidos demo n8n.
- **12 notas sin frontmatter en absoluto** (mayormente dumps de fuente en `03_Resources/Investigaciones/claude-code-ecosystem-2026/` y las transcripciones originales) — puede ser intencional para contenido "fuente cruda", pero rompe la convención `type:` del resto del vault. No se tocó.
- 1 nota usa `type: servicio` en vez de `type: guia` (que es lo que usan las otras 10 fichas de servicio) — inconsistencia menor, bajo impacto.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

