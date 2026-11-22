---
title: 'Obsidian: plugin Rho Network y tema oscuro'
date: '2026-11-13'
type: meta/sesion
origen: mixto
proyecto: ''
sesion_id:
- 8f81f004-d30a-48d4-b78f-43f38a3a0094
tags:
- sesion
- obsidian
---

> [!resumen] En cristiano
> Haytham instaló un plugin de Obsidian (Rho Network) que promete una vista de galaxia con las notas. No funcionaba como decía: salía 0 órbitas y iba a trompicones. Se pasó el vault a tema oscuro y se ajustó el plugin; quedó sin confirmar si ya dibuja la galaxia.

## Qué se hizo
- Tema cambiado a `obsidian` (oscuro) en `.obsidian/appearance.json`; se quitó el snippet `premium-light-theme` de los activos porque pisaba el oscuro. Para volver: `moonstone` + reactivar el snippet.
- Diagnóstico: el plugin no mostraba galaxia (captura: 653 notas, 0 órbitas). Se creó `data.json` con agrupación por carpetas, calidad baja, menos estrellas/brillo, sin cometas.

## Decisiones y problemas
- `data.json` ya existía (lo creó el plugin) y se sobrescribió sin leerlo antes; probablemente solo tenía valores por defecto.
- Causa de las 0 órbitas con agrupación automática: no encontrada.

## Pendientes
- Recargar Obsidian y comprobar si sale una órbita por carpeta; si no, tecla `G` para cambiar agrupación o poner `Stars` a 0.
- Decidir si el plugin merece quedarse (rendimiento flojo con 653 notas y 1.651 enlaces).
- Cambios sin commit en `.obsidian/`.

## Relacionado
[[00_Meta/Registro de Sesiones|Registro de Sesiones]]

