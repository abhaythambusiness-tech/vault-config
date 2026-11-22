---
date: '2026-10-13'
proyecto: '[[01_Projects/Abisal Drill]]'
status: completado
tags:
- roblox
- 3d
- prompt
- pbr
- asset
- abisal-drill
title: Prompt 3D — Cristal Abisal Bioluminiscente
type: asset-3d
origen: mixto
---


# Prompt 3D — Cristal Abisal Bioluminiscente

> [!resumen]
> Mineral coleccionable incrustado en las simas rocosas. Es la recompensa económica y la fuente principal de progreso (Pilar 1) para vender en el lobby.
> - **Archivos generados**: `99_Assets/Abisal Drill/Modelos 3D/abyssal_crystal_cluster.glb` (3,9 MB), `abyssal_crystal_cluster.obj` y `.mtl`.

---

## 1. Especificaciones Técnicas
- **Presupuesto de polígonos**: 600 – 900 triángulos.
- **Mallas**: Malla única compacta (`Crystal_Cluster`).
- **Escala**: 2 studs de ancho x 2.5 studs de alto (tamaño ideal para recoger o minar).
- **Materiales PBR**:
  - Roca base: Basalto volcánico rugoso y oscuro (obsidiana mate).
  - Cristales: Prismas geométricos afilados con mapa de color cian/eléctrico y mapa emisivo (`EmissiveMask`) intenso.
- **Efectos de motor**: `PointLight` interno cian (`Brightness = 2`, `Range = 8`) para iluminar el lecho submarino.

---

## 2. Prompt Técnico para Generación 3D

```text
Cluster of raw deep-sea crystalline minerals protruding from volcanic basalt rock, game-ready pickup item. 
Sharp geometric hexagonal crystal formations clustered together, semi-translucent glowing internal core, vibrant electric cyan and radioactive violet bioluminescent highlights. 
Rough porous dark obsidian rock base with natural mineral veins. 
Optimized low-poly asset under 900 tris, clean UV unwrapped topology, 1K PBR texture set (Albedo, Normal, Roughness, Metalness, Emissive mask). 
Designed to look stunning with emissive bloom and point lights inside Roblox Lighting technology.
```

---

## 3. Integración en Luau (Roblox Studio)
1. Instanciar en los módulos de roca durante el descenso.
2. Colocar `ProximityPrompt` ("Extraer Cristal") o detección por herramienta de taladro.
3. Al recoger, emitir partículas (`ParticleEmitter`) luminiscentes y destruir la instancia con sonido de campana de recompensa.

