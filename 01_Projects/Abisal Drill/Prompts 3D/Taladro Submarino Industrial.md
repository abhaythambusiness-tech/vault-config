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
title: Prompt 3D — Taladro Submarino Industrial
type: asset-3d
origen: mixto
---


# Prompt 3D — Taladro Submarino Industrial (Drill Rig)

> [!resumen]
> Malla principal y vehículo central de *Abisal Drill*. Actúa como cabina interactiva donde los jugadores caminan y operan estaciones mientras el vehículo desciende.
> - **Archivos generados**: `99_Assets/Abisal Drill/Modelos 3D/drill_pod.glb` y `drill_pod.obj`.

---

## 1. Especificaciones Técnicas
- **Presupuesto de polígonos**: 10.000 – 12.000 triángulos (optimizado para rendimiento en móvil).
- **Mallas separadas**:
  1. `Hull_Exterior`: Casco exterior blindado.
  2. `Drill_Bit`: Broca cónica frontal separada para rotación continua por script.
  3. `Interior_Cabin`: Suelo plano caminable y mamparos sin colisiones complejas.
  4. `Portholes`: Ventanas con material de vidrio/transparencia.
- **Escala**: 20 studs de ancho x 12 studs de alto x 32 studs de profundidad (compatible con avatar R6/R15).
- **Materiales PBR (SurfaceAppearance)**: `ColorMap`, `NormalMap`, `RoughnessMap`, `MetalnessMap` (resolución 2048x2048).
- **Fidelidad de colisión**: `Default` o `PreciseConvexDecomposition` para el interior caminable.

---

## 2. Prompt Técnico para Generación 3D

```text
Industrial steampunk-dieselpunk submersible drill exploration pod, modular interior for Roblox game. 
Exterior: Heavy reinforced steel hull with industrial rivets and welded plates, giant rotating conical drill bit at the front with carbide cutting teeth, dual heavy-duty ballast tanks on flanks with safety decals, four omnidirectional ducted brass thrusters, reinforced glass porthole cockpit with brass framing. 
Interior: Functional walk-around engine room, coal furnace bay with glowing inspection hatch, high-pressure steam pipes along walls, central steering console with analog gauges and warning levers. 
Low-to-mid poly (under 12,000 tris), PBR textures (Albedo, Metalness, Roughness, Normal), clean modular layout with flat walkable floor, 1:1 scale for Roblox character rig, neutral slate grey, dark iron, and safety hazard yellow color palette. Separate drill bit mesh for continuous rotation animation.
```

---

## 3. Guía de Importación a Roblox Studio
1. Exportar en formato `.fbx` u `.obj` con origen centrado en el suelo de la cabina.
2. Importar vía **Asset Manager** o `MeshPart`.
3. Añadir un objeto `SurfaceAppearance` dentro del `MeshPart` y vincular los mapas de textura PBR.
4. Ajustar `CanCollide = true` en el suelo interior y `CollisionFidelity = PreciseConvexDecomposition`.

