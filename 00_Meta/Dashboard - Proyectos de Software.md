---
type: dashboard
status: activo
date: 2026-10-14
---

# Dashboard — Proyectos de software

> [!resumen]
> Estado de los 6 documentos de cada proyecto (Dataview). Para comprobar trazabilidad ejecutar:
> `python3 ~/Proyectos/flujo-software/tools/trace_lint.py "01_Projects/<Nombre>"`

## Documentos por proyecto
```dataview
TABLE WITHOUT ID
  proyecto AS "Proyecto",
  doc AS "Documento",
  status AS "Estado",
  date AS "Fecha"
FROM "01_Projects"
WHERE type = "doc-software"
SORT proyecto ASC, file.name ASC
```

## Pendientes de aprobar
```dataview
LIST
FROM "01_Projects"
WHERE type = "doc-software" AND status != "aprobado" AND status != "no-aplica"
SORT proyecto ASC
```

## Recursos del flujo
- [[00 - Flujo de Software]]
- [[Catalogo de Componentes]] · [[Biblioteca de Layouts]] · [[Starter Kits NeoZeler]]
