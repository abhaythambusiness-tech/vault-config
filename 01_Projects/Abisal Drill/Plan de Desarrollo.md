---
date: '2026-10-14'
proyecto: '[[01_Projects/Abisal Drill]]'
status: en-progreso
tags:
- roblox
- gamedev
- plan-maestro
- roadmap
- abisal-drill
title: Plan Maestro de Desarrollo — Abisal Drill
type: proyecto
origen: mixto
---


# Plan Maestro de Desarrollo — Abisal Drill (De Inicio a Fin)

> [!resumen]
> Hoja de ruta técnica y de diseño completa para la producción de **Abisal Drill** en Roblox Studio. Articulada sobre los 5 pilares psicológicos del avatar de Roblox, la regla de los primeros 45 segundos y una arquitectura de red sin física libre optimizada para móvil y PC.

---

## Fase 1: El Bucle Central y Dopamina Inmediata (Pilares 1 y 4)
*Meta: Lograr que los primeros 45 segundos sean adictivos, claros y sin fricción de aprendizaje.*

- [x] **1.1 Arquitectura base de cabina y servidor**:
  - [x] Chasis `DrillRig` con estaciones físicas y atributos en servidor (`Profundidad`, `Presion`, `Combustible`, `SaludCasco`).
  - [x] Reemplazo de graybox por los 4 modelos 3D integrados (`drill_pod`, `pressure_relief_station`, `repair-drone`, `abyssal_crystal_cluster`).
- [x] **1.2 Generador de Descenso y Entorno Procedural (Túnel CFrame)**:
  - [x] Sistema de chunks modulares de túnel rocoso que hacen scroll hacia arriba mediante `CFrame` y `RunService.Heartbeat`, simulando descenso infinito a 60 FPS sin coste de física.
  - [x] Spawner dinámico de vetas de `CristalAbisalPrefab` en las paredes del túnel reciclable con `ProximityPrompt` de extracción.
- [x] **1.3 Sistema de Averías y Presión Progresiva**:
  - [x] Generador de averías físicas: tubería con fuga de vapor a presión (`ParticleEmitter` dinámico al superar 65% de presión).
  - [x] Luz de alarma roja en el techo con destello intermitente sincronizado cuando `Presion >= 80%`.
  - [x] Purgado inmediato con la válvula de emergencia restableciendo los parámetros normales.

---

## Fase 2: Escalabilidad y Dinámica Social Cooperativa (Pilares 4 y 5)
*Meta: Garantizar que una partida sea divertida y viable tanto para 1 jugador solitario como para un grupo de 4 amigos.*

- [x] **2.1 Dron Autónomo Nautilus-Mini (IA de Apoyo)**:
  - [x] Script `DroneAIController` en `ServerScriptService`: el dron detecta partidas de 1-2 jugadores y, ante sobrepresión (>60%), vuela a la válvula con interpolación suave, activa soplete de chispas y purga la presión consumiendo batería.
  - [x] Batería recargable del dron mediante `ProximityPrompt` de mantenimiento en cabina.
- [x] **2.2 Sistema de Extracción y Minería Interactiva**:
  - [x] Baúl de cristales compartido (`BaulCristalesCompartido`) en la cabina para volcar gemas individuales al botín del equipo.
- [x] **2.3 Decisión de Extracción vs Riesgo**:
  - [x] Palanca física de evacuación en la consola central para activar la cápsula de escape, detener el descenso y salvar el 100% de los minerales obtenidos.

---

## Fase 3: Persistencia, Lobby y Urgencia Diaria (Pilares 1 y 3)
*Meta: Transformar sesiones aisladas en un hábito diario recurrente con FOMO positivo.*

- [x] **3.1 Arquitectura de Datos Segura (`ProfileService` / `DataStoreService`)**:
  - [x] `DataPersistenceManager` activo: guarda y recupera `Monedas`, `CristalesTotales`, `ProfundidadMaxima` y `RachaDiaria`, con `BindToClose` y tolerancia a fallos.
- [x] **3.2 Tienda y Refinería de Minerales (Loop de Economía)**:
  - [x] `EstacionRefinado` física con `ProximityPrompt`: funde el botín recolectado por monedas del juego con feedback inmediato en el HUD.
- [x] **3.3 Mecánica de FOMO Diario (Pilar 3)**:
  - [x] Sistema de "Falla del Día" con mutador 2x de valor de gemas activo, reflejado en el badge del HUD superior para incentivar la sesión diaria.

---

## Fase 4: Estatus Social y Monetización de Alto ARPU (Pilar 2)
*Meta: Monetizar por orgullo social, vanidad y rescates in extremis sin introducir ventajas desleales.*

- [x] **4.1 Microtransacciones de Urgencia (Bajo Rechazo)**:
  - [x] Panel interactivo `AbisalShopGui` con botón de "Kit de Reparación de Emergencia" (25 R$) para salvar la nave in extremis restaurando +50 de salud del casco.
- [x] **4.2 Cosméticos de Prestigio en Lobby (Pilar 2)**:
  - [x] Sistema reactivo `SocialStatusManager`: proyecta un `BillboardGui` sobre el avatar con títulos por rango (`Grumete`, `Explorador`, `Buzo Veterano`, `Señor Abisal`) y récord de metros.
  - [x] Aura Bioluminiscente Mítica con partículas turquesa en la espalda al superar 500m o desbloquearla en la tienda.
- [x] **4.3 Gamepasses de Utilidad Grupal (Presión Social Positiva)**:
  - [x] "Radiobaliza de Expedición" (99 R$) configurada en la tienda para otorgar +25% de valor en cristales a toda la tripulación del servidor.

---

## Fase 5: Atmósfera Audiovisual, Pruebas Multiplataforma y Lanzamiento
*Meta: Entregar una experiencia premium con 60 FPS estables en móviles de gama media.*

- [x] **5.1 Diseño de Iluminación y Efectos de Niebla Submarina**:
  - [x] Iluminación `ClockTime = 0` (oscuridad abisal) con `Atmosphere` volumétrica densa (`Density = 0.48`), niebla oscura y focos frontales de penetración en `DrillRig`.
  - [x] Bloom sutil configurado para acentuar el brillo bioluminiscente de cristales y auras.
- [x] **5.2 Paisaje Sonoro Posicional**:
  - [x] `SoundService` con 4 pistas integradas: zumbido de agua profunda ambiental, alarmas de emergencia al superar 80% de presión, crujidos de metal y tintineo de gemas.
- [x] **5.3 Muelle de Superficie y QA de Ciclo Completo**:
  - [x] `LobbyMuelle` con dársena de agua y el submarino completo `drill_pod` en exhibición con foco cenital y `ProximityPrompt` de embarque.
  - [x] Ciclo completo verificado: Spawn en Lobby $\rightarrow$ Embarque $\rightarrow$ Descenso en scroll 60 FPS $\rightarrow$ Averías y soporte de Dron $\rightarrow$ Minería $\rightarrow$ Evacuación y retorno seguro al muelle.

