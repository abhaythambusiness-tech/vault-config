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
title: Prompt 3D — Consola de Emergencia y Válvula de Presión
type: asset-3d
origen: mixto
---


# Prompt 3D — Consola de Emergencia y Válvula de Presión

> [!resumen]
> Estación interactiva montada en el mamparo interior del taladro. Permite a los jugadores aliviar la presión del casco mediante un `ProximityPrompt`.
> - **Archivos generados**: `99_Assets/Abisal Drill/Modelos 3D/pressure_relief_station.glb` y `pressure_relief_station.obj`.

---

## 1. Especificaciones Técnicas
- **Presupuesto de polígonos**: 1.200 – 1.800 triángulos.
- **Mallas separadas**:
  1. `Valve_Base`: Placa base de montaje, tubos hidráulicos y manómetro.
  2. `Valve_Wheel`: Volante de purga rojo con pivot centrado para animación de giro de 360 grados.
- **Escala**: 3 studs de ancho x 4 studs de alto x 1.5 studs de profundidad.
- **Materiales PBR**: Hierro fundido rugoso, bronce envejecido para diales y esmalte rojo desgastado en el volante.
- **Iluminación**: Bombilla indicadora con textura emisiva (parpadeo en rojo ante sobrepresión).

---

## 2. Prompt Técnico para Generación 3D

```text
Vintage heavy industrial pressure relief station for submarine wall, game-ready prop. 
Cast iron mounting plate with visible bolts and warning stencil labels, large circular brass pressure dial with red danger zone indicator needle behind glass, thick reinforced rubberized hydraulic hoses entering from top and bottom. 
Center feature: Chunky red emergency wheel valve with six spokes and knurled grip texture, distinct separate component with centered origin for rotation animation. 
Small blinking emergency indicator dome bulb mounted on top bracket. 
Stylized realism suitable for Roblox Studio engine, under 1,800 tris, 2K PBR texture maps (Albedo, Normal, Roughness, Metalness, Emissive), clean low-poly topology.
```

---

## 3. Integración en Luau (Roblox Studio)
1. Agrupar `Valve_Base` y `Valve_Wheel` en un `Model`.
2. Insertar `ProximityPrompt` en `Valve_Base`.
3. Al disparar el evento `Triggered`, ejecutar `TweenService` sobre el `CFrame` de `Valve_Wheel` para rotar 180° con sonido de escape de vapor (`SoundId`).

