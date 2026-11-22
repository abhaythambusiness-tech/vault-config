---
title: "Decisión - Estructura del Vault (Debate Multi-Agente)"
date: 2026-11-22
tags: [decision, vault, obsidian, para, estructura, debate]
type: nota
status: activo
related: ["[[00_Meta/Dashboard]]"]
---

# Debate multi-agente sobre la estructura del vault (skill agent-debate)

4 agentes con encuadres distintos evaluaron la estructura de carpetas y MOCs del vault de forma independiente.

## Punto de consenso principal

La estructura PARA (Projects, Areas, Resources, Archive) ofrece una organización clara y separa el trabajo activo de las responsabilidades continuas y los recursos reutilizables. El debate se centró en cómo mantener la consistencia mientras el vault crece.

## Inconsistencias identificadas

- **Convención de nombres variables entre proyectos**: algunos usan prefijos de categoría, otros no. Esto afecta la buscabilidad cuando hay múltiples proyectos.
- **MOCs creados ad-hoc**: sin plantilla o regla establecida, lo que genera variabilidad en la estructura de enlaces.
- **Carpetas técnicas fuera de PARA**: `graphify-out/`, `docs/`, `99_Assets/` y carpetas de herramientas residúan en la raíz si no se les asigna un lugar fijo.

## Navegación y usabilidad

- El Dashboard debe enlazar todas las áreas principales: Projects, Areas, Resources, Archive, Assets.
- Las fichas de servicio deben ser distinguibles por título en el buscador rápido.
- Los MOCs por área deben seguir una convención consistente: `Área - MOC`.

## Escalabilidad

- La numeración `00-11` de proyectos se rompe si hay que insertar elementos en medio. Para proyectos secundarios, considerar una estructura paralela o sufijos descriptivos.
- Los MOCs deben tener plantilla definida para evitar inconsistencias al crear nuevos.
- El archivado debe tener reglas claras desde el inicio para evitar que el `04_Archive/` se llene de contenido sin categorizar.

## Arreglos aplicados

1. Dashboard actualizado para incluir filas de Dropshipping, Resources, Archive y Assets.
2. `graphify-out/` y otros directorios técnicos documentados en `CLAUDE.md` §0.2.
3. Convención de frontmatter estandarizada: `type`, `status`, `date`, `origen` (`humano|maquina|mixto`).

## Pendiente de decisión

- Definir plantilla única para MOCs por área.
- Establecer reglas de archivado activas (no solo teóricas).
- Resolver la numeración de carpetas para proyectos secundarios.
- Decidir qué hacer con proyectos huérfanos o en estado de congelado.