---
title: Búsqueda de idea Roblox y arreglo del MCP de Studio
date: '2026-10-14'
type: sesion
proyecto: ultimo-en-pie
tags:
- roblox
- mcp
- decision
origen: mixto
---

## Contexto
Haytham dudaba de Abisal Drill. Quería algo más simple, con muchas microtransacciones, para llegar a ~15.000 R$/día y viralizar.

## Decisiones
- Abisal Drill se **pausa sin descartar**: [[01_Projects/Abisal Drill/Idea en pausa - Simulador de mineria]].
- Tras validar minería con mascotas, pesca y otras direcciones, se elige **[[01_Projects/Ultimo en Pie - Sabotaje]]** (arena eliminatoria donde el eliminado compra trampas). Veredicto: go condicionado a un test de 3 semanas.
- Criterios fijados por Haytham: dificultad técnica baja, arte bajo, muchas compras, viralidad media-alta; sin mecánica de "steal".
- Informes y comparativa: [[01_Projects/Ultimo en Pie - Sabotaje/Validacion y comparativa]].

## Aprendizajes
- **MCP `roblox-studio`** fallaba con "protocol version not supported: 2026-07-28". El servidor sí negocia bien; el fallo viene del ruido que Wine escribe por stderr. Solución: script `~/.local/bin/roblox-studio-mcp.sh` que descarta stderr y apunta a la última versión de Studio, y `.mcp.json` apuntando a él. Se borró la entrada duplicada del ámbito de usuario. La conexión es intermitente en `claude mcp list` cuando ya hay otra instancia de Studio MCP abierta; confirmar en sesión nueva.
- Los validadores no pudieron verificar competidores concretos ni la política de acoso de Roblox: comprobarlo a mano antes de construir.
- 15.000 R$/día ≈ 52-57 $/día: meta modesta en dinero y muy dependiente del tráfico, no de la monetización.
- **Construcción:** se creó `~/Proyectos/ultimo-en-pie/` y se verificó la semana 1 en Studio con 1 jugador (ver ficha §9). Tras reconectar el MCP, el código se inyectó desde `execute_luau` y se comprobó con hash que coincide con el repo. Para probar con 1 jugador se bajó temporalmente `Players.Min` a 1, `RoundSeconds` a 30 y se hizo que la ronda no acabase con 1 vivo; todo restaurado y verificado.
- GateGuard exige declarar llamadores, API y la instrucción literal en la primera edición de cada archivo; la primera llamada se deniega siempre y el reintento pasa.

