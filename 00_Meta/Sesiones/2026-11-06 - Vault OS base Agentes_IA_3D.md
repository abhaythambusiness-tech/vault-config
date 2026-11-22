---
date: 2026-11-06
proyecto: "[[01_Projects/Vault OS]]"
type: sesion
origen: mixto
---

> [!resumen] En cristiano
> Vault OS pasó a usar la oficina del repo Agentes_IA_3D con la lógica del vault: aparece un personaje por cada sesión de Claude Code que toca el vault. Se añadieron CRM, Prensa y Notas, se rebajó la carga 3D y se rehízo la pantalla: oficina de fondo y ventanas de cristal encima.

## Qué se hizo
- Base: fork de `ederland/Agentes_IA_3D` (JS + scene.js), sin Firebase; minifigs del repo.
- Servidor Node en el puerto 8790: zonas, CRM, estado de sesiones, noticias por reglas, notas (lectura y guardado con control de cambios en disco).
- Rediseño de UI: barra, dock, ventanas arrastrables, paneles Equipo y Hoy, paleta Ctrl+K, tema oscuro «A · Cristal».

## Aprendizajes
- Sin WebGL en el panel del navegador de Claude: la escena 3D solo se valida en un navegador normal.
- Perfil de calidad bajo y gzip/caché resolvieron la lentitud inicial.

## Pendiente
Probar 3D y fluidez en Chrome; aprobar `DESIGN-IDENTITY.md`; Ficha de Investigación; `resumen.html`; probar hooks con sesión real; commit.
