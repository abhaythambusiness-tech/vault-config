---
title: Sesión - 2026-08-26 - Fix de personalización del grafo de Obsidian
date: '2026-08-26'
type: meta/sesion
proyecto: ''
tags:
- sesion
- obsidian
- diseño
aliases: []
origen: mixto
---

# Sesión — 2026-08-26: Fix de personalización del grafo de Obsidian

> [!abstract] Resumen
> Se diagnosticó y corrigió la config de apariencia/grafo de Obsidian (contraste roto, colorGroups huérfanos) y se documentó `awesome-claude-design` como recurso del vault.

## Contexto
El usuario reportó que la personalización de Obsidian tenía fallos: nombres de notas que a veces no se veían, grafo "regular" y colores de algunas notas bugueados. No toca ningún proyecto/área PARA concreta — es configuración técnica del propio vault (`.obsidian/`).

## Qué se hizo
- Diagnóstico de `.obsidian/appearance.json`, `graph.json` y los 5 snippets CSS activos.
- Causa raíz del grafo: `graph.css` forzaba fondo navy + texto claro de forma incondicional, pero nodos/líneas solo se pintaban bajo `.theme-dark` — con el tema real activo (`premium-light-theme`, claro) el resultado era una mezcla inconsistente ("grafo regular").
- Reescrito `graph.css` para usar la misma paleta paper/ink/emerald del resto del vault, sin depender de dark/light mode.
- Revisado el contenido real del vault (`02_Areas/NeoZeler`) contra los `colorGroups` de `graph.json`: 5 de los 8 grupos (Transporte, Instalación, Distribución, Infoproductores, Barberías) eran huérfanos de una estructura de vault anterior (previa a la sustitución de contenido desde USB) — no coincidían con ningún archivo real.
- Eliminados esos 5 grupos huérfanos; quedan solo MOC / Nicho / Cliente, que sí coinciden con la estructura actual.
- Detectado que `custom-vault-style.css` estaba muerto por cascada (todas sus reglas eran sobrescritas por `premium-light-theme.css` vía `!important`) — desactivado en `enabledCssSnippets`.
- Borrado `ai-tech-theme.css` (snippet sin usar, no activado).
- Creada nota `03_Resources/Awesome Claude Design.md` documentando el repo de referencia `~/Proyectos/awesome-claude-design` (9 familias estéticas, cómo aplicarlo con el gate de diseño).
- Actualizado `CLAUDE.md` (catálogo de skills de diseño) para enlazar esa nueva nota.
- Detectado y resuelto un proceso de Obsidian residual en background que sobrescribía `graph.json` en cada edición (mataba el fix); se mató el proceso tras confirmación del usuario.

## Decisiones tomadas
- Los 5 colorGroups huérfanos se eliminan (no se remapean a los nichos actuales) — decisión explícita del usuario ante la pregunta.
- `custom-vault-style.css` queda desactivado, no borrado (reversible si se detecta que sí aportaba algo).

## Aprendizajes (para futuras sesiones)
- Si Obsidian está abierto con la vista de grafo activa, sobrescribe `graph.json` con su estado en memoria al guardar, pisando cualquier edición hecha por fuera. Antes de tocar `.obsidian/graph.json` o `workspace.json`, comprobar que la app esté cerrada (`ps aux | grep obsidian`), no solo que la ventana esté cerrada — el proceso Electron puede seguir vivo en background.
- Los `colorGroups` del grafo son fáciles de dejar huérfanos tras una reorganización de vault (como la sustitución de contenido desde USB del 2026-08-26 anterior) — merece la pena revisarlos contra la estructura real cuando se toque personalización visual.
- No hay herramienta de captura de pantalla instalada en este entorno (sin `grim`/`scrot`/`maim`) — no es posible verificar visualmente cambios de UI de apps de escritorio (Obsidian) sin que el usuario confirme manualmente.

## Próximos pasos
- Usuario debe abrir Obsidian (arranque limpio, proceso ya no residual) y confirmar visualmente que el grafo se ve bien.
- Pendiente de decisión abierta (§9 CLAUDE.md): frontmatter canónico del vault, y destino de `taller-bravo/`.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[03_Resources/Awesome Claude Design]]

