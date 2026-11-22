---
date: '2026-10-13'
proyecto: '[[01_Projects/Abisal Drill]]'
status: completado
tags:
- sesion
- roblox
- gamedev
- abisal-drill
- brainstorming
title: 'Sesión — 2026-10-13: Estudio de mercado y diseño de Abisal Drill en Roblox'
type: sesion
origen: mixto
---


# Sesión — 2026-10-13: Estudio de mercado y diseño de Abisal Drill en Roblox

> [!abstract] Resumen
> Estudio del mercado de Roblox basado en la psicología del avatar (dopamina y 5 pilares), evaluación comparativa de 3 conceptos y formalización del GDD y arquitectura técnica de *Abisal Drill*.

## Contexto
- Proyecto / Área: [[01_Projects/Abisal Drill|Abisal Drill]] y [[03_Resources/Roblox - Avatar y Psicologia del Jugador/Roblox - Psicologia del Jugador y Retencion - MOC|Roblox - Psicología del Jugador y Retención - MOC]].
- Reglas operativas: Incorporación de la regla general de prompts 3D en [[GEMINI.md]] y [[CLAUDE.md]].

## Qué se hizo
- Análisis de saturación del mercado de Roblox (descarte de simulators pasivos y MMORPGs inabarcables; identificación de océanos azules en Co-op Tycoon y Session Roguelite).
- Brainstorming de 3 conceptos con puntuación multidimensional (Retención, Viralidad, Monetización, Viabilidad).
- Elección por parte de Haytham del concepto **Abisal Drill** (taladro/submarino cooperativo de 1 a 4 jugadores).
- Creación de la ficha técnica y GDD en [[01_Projects/Abisal Drill]].
- Fijación de la **Regla 9** en directrices generales del vault: generación proactiva de prompts técnicos para modelos 3D si no existen en internet.
- Modularización de fichas técnicas en `01_Projects/Abisal Drill/Prompts 3D/` para los 4 assets clave.
- Importación e integración de los 4 modelos 3D en Roblox Studio: sustitución de graybox por mallas reales (taladro exterior, consola de purgado, dron Nautilus-Mini y mineral bioluminiscente con prefab en ReplicatedStorage).
- Implementación de la **Fase 1**: generador procedural de túnel en scroll continuo por CFrame (60 FPS sin física), spawner de cristales interactivo, fuga de vapor por partículas y baliza de alarma roja.
- Implementación de la **Fase 2**: IA autónoma del Dron Nautilus-Mini (`DroneAIController`) con reparación automática bajo sobrepresión en solo/dúo, baúl compartido de cristales y palanca de evacuación segura.
- Implementación de la **Fase 3**: sistema de persistencia de perfiles (`DataPersistenceManager`), fundición de minerales en monedas en `EstacionRefinado` y badge de evento FOMO diario 24h (2x valor de gemas).
- Implementación de la **Fase 4**: estatus social sobre el avatar (`SocialStatusManager`) con títulos dinámicos, aura bioluminiscente de partículas en la espalda y panel de tienda `AbisalShopGui` (kit de revives a 25 R$, boosters y auras).
- Implementación de la **Fase 5**: muelle de superficie en Lobby (`LobbyMuelle`) con exhibición de la nave completa `drill_pod` en dársena, atmósfera submarina volumétrica (`Atmosphere`), focos frontales abisales y paisaje sonoro (`SoundService`).
- **Etapa de Pulido Visual & UI Premium**:
  - Corrección de elevación del taladro: ya no está enterrado en el suelo; ahora reposa en una cuna industrial de astillero sobre el agua en el muelle y suspendido en el foso abisal.
  - Corrección funcional del botón de embarque: implementado `LobbyManager` en `ServerScriptService` con teletransporte persistente desde el muelle a la cabina del taladro (`0, 3.5, 5`).
  - Reconstrucción completa del HUD a estándar comercial AAA (estilo *Pressure* / *Deepwoken*):
    - Cero emojis de texto o pegatinas informales.
    - Barras de instrumentación analógicas funcionales animadas por `TweenService` para Presión del Casco (cambio verde-ámbar-rojo) y Combustible.
    - Indicador digital de profundidad central y tarjetas de economía compactas con iconos vectoriales en la esquina superior derecha.
  - Renovación de la tienda `AbisalShopGui` con diseño naval de alto impacto.
  - Eliminación de sobreexposición blanca en la malla del taladro: acabado en acero naval azulado mate.
- Validación de ciclo completo en playtest de Studio: flujo cerrado de punta a punta (Spawn en Lobby $\rightarrow$ Embarque $\rightarrow$ Descenso $\rightarrow$ Minería $\rightarrow$ Averías y auxilio de dron $\rightarrow$ Evacuación al muelle y venta de botín).

## Decisiones tomadas
- **Arquitectura de red sin física libre**: Mover el taladro por interpolación CFrame o animación en bucle de entorno para erradicar desincronizaciones de red en Roblox Physics.
- **Escalabilidad y juego en solitario**: Implementación del dron auxiliar "Nautilus-Mini" para garantizar partidas fluidas con 1 o 2 jugadores sin quebrar la experiencia cooperativa.
- **Monetización ética y de estatus**: Revives accesibles a 25 R$, boosters cooperativos para todo el servidor y cosméticos/auras luminiscentes en el lobby (Pilar 2).

## Aprendizajes (para futuras sesiones)
- La viralidad en TikTok/YouTube de Roblox se apoya en momentos de pánico cooperativo ("¡tapa esa fuga!") con micro-roles claramente diferenciados.
- Para evitar el bloqueo por falta de assets 3D específicos en la toolbox, definir de inmediato el prompt técnico detallado (geometría, estilo, tris, PBR y paleta) acelera la fase de arte sin detener la programación.

## Próximos pasos
- [ ] Iniciar prototipo funcional en Roblox Studio (`workspace` modular de cabina y taladro).
- [ ] Implementar el sistema de atributos de presión/combustible con `RunService` y `ProximityPrompt`.
- [ ] Generar los assets 3D prioritarios (cabina del taladro y válvula de presión) con los prompts definidos.

## Relacionado
- [[01_Projects/Abisal Drill|Abisal Drill]]
- [[03_Resources/Roblox - Avatar y Psicologia del Jugador/Roblox - Psicologia del Jugador y Retencion - MOC|Roblox - Psicología del Jugador y Retención - MOC]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

