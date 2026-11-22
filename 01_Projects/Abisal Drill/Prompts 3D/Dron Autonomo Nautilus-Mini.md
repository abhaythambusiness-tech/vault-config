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
title: Prompt 3D — Dron Autónomo de Apoyo Nautilus-Mini
type: asset-3d
origen: mixto
---


# Prompt 3D — Dron Autónomo de Apoyo (Nautilus-Mini)

> [!resumen]
> Compañero robótico que acompaña la tripulación en partidas individuales o dúos para asegurar la viabilidad técnica y evitar que el juego se vuelva frustrante.
> - **Archivos generados**: `99_Assets/Abisal Drill/Modelos 3D/repair-drone.glb` y `repair-drone.obj`.

---

## 1. Especificaciones Técnicas
- **Presupuesto de polígonos**: 1.800 – 2.400 triángulos.
- **Mallas separadas**:
  1. `Drone_Body`: Chasis esférico central con hélice superior y ojo cíclope.
  2. `Drone_Arm_Left`: Brazo articulado con soplete de reparación.
  3. `Drone_Arm_Right`: Brazo con llave inglesa hidráulica.
- **Escala**: 2 studs de diámetro (proporción amigable y visible dentro de la cabina).
- **Materiales PBR**: Esmalte naranja de seguridad náutico (`Safety Orange`), aluminio pulido, juntas de goma negra y lente de vidrio emisivo azul turquesa.
- **Animación**: Flotación oscilatoria suave vía `AlignPosition` o `CFrame` con inclinación según la dirección del movimiento.

---

## 2. Prompt Técnico para Generación 3D

```text
Compact spherical helper drone for underwater repairs, lovable robotic companion for Roblox game. 
Single central cyclops glowing glass lens eye with friendly bright cyan emissive pupil, two multi-jointed micro-arms holding miniature repair tools (sparking mini welding torch and hydraulic wrench), twin mini-ducted water propeller thrusters mounted symmetrically on upper sides. 
Top-mounted safety grab handle for player transport. 
Industrial yet charming aesthetic with clean bevels, under 2,400 tris, 2K PBR texture set (Albedo, Normal, Roughness, Metalness, Emissive). 
Vibrant safety orange and white enamel coating with subtle naval maintenance decals and paint chips.
```

---

## 3. Integración en Luau (Roblox Studio)
1. Sistema de seguimiento al jugador líder cuando no hay averías (`PathfindingService` o `BodyPosition`).
2. Cuando `Presion > 60` y hay 1-2 jugadores, el dron se desplaza automáticamente hacia `EstacionPresion` para reducir 15 puntos de presión cada 10 segundos.

