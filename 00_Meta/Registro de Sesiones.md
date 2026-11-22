---
title: "Registro de Sesiones y Aprendizajes"
created: 2026-08-08
type: meta/registro
tags:
  - meta
  - sesiones
---

# 🧠 Registro de Sesiones y Aprendizajes

> [!abstract] Qué es esto
> Historial cronológico de sesiones de trabajo con Claude Code en este vault. Cada sesión relevante se registra como nota en `00_Meta/Sesiones/`, con su contexto, decisiones y aprendizajes — para que futuras sesiones no repitan investigación ya hecha ni pierdan el porqué de una decisión.

## Cómo se registra una sesión nueva
1. Usar la plantilla `[[00_Meta/Plantillas/Plantilla - Sesion|Plantilla - Sesion]]`.
2. Guardar en `00_Meta/Sesiones/YYYY-MM-DD - <tema>.md`.
3. Rellenar sobre todo **Aprendizajes**: solo lo no obvio (por qué X y no Y, qué falló, qué convención quedó fijada). No repetir aquí lo que ya vive en el código/las notas del proyecto.

## Todas las sesiones

```dataview
TABLE date as Fecha, proyecto as Proyecto
FROM "00_Meta/Sesiones"
SORT date DESC
```

## Sesiones por proyecto

```dataview
TABLE date as Fecha, file.link as Sesión
FROM "00_Meta/Sesiones"
WHERE proyecto
SORT proyecto ASC, date DESC
```

## Relacionado
- [[00_Meta/Dashboard|Dashboard]]
- [[00_Meta/Plantillas/Plantilla - Sesion|Plantilla de sesión]]
