---
title: 'Sesión 2026-10-04: bot real de memecoins y recogida de datos'
date: '2026-10-04'
type: sesion
proyecto: '[[04_Archive/Memecoin-LSTM/00_Roadmap Maestro - Prediccion LSTM Memecoins]]'
tags:
- memecoin
- bot-real
- datos
- jupiter
- discord
- onchain
status: completado
origen: mixto
---

# Sesión — 2026-10-04: bot real de memecoins y recogida de datos

> [!abstract] Resumen
> Se pasó de un bot que solo simulaba a un bot con ejecución real (Jupiter + firma local + Discord) corriendo en **modo ensayo con 5 carteras virtuales**; se entrenaron EXP-16v2, EXP-17 y EXP-16 limpio; se descubrió y arregló una recogida de datos rota con etiquetas falsas; se creó un hub compartido de GeckoTerminal y un vigilante; y se integró el análisis on-chain (Helius). Dinero real: **no** (bloqueado hasta que el ensayo gane tras costes).

## Contexto
Objetivo inicial: poner el bot en real con 10 € esa noche. Proyecto [[04_Archive/Memecoin-LSTM/00_Roadmap Maestro - Prediccion LSTM Memecoins]]. Las notas detalladas de cada parte:
- [[04_Archive/Memecoin-LSTM/09 - Bot real v7 - Funcionamiento y uso|09 · Bot real v7]]
- [[04_Archive/Memecoin-LSTM/10 - Recogida de datos - observador, recolector, hub y vigilante|10 · Recogida de datos]]
- [[04_Archive/Memecoin-LSTM/11 - Modelos EXP-15 a EXP-17 - resultados y comparativas|11 · Modelos]]
- [[04_Archive/Memecoin-LSTM/12 - Analisis on-chain con Helius|12 · On-chain]]
- [[04_Archive/Memecoin-LSTM/13 - Sostenibilidad con 10 euros - investigacion y plan de escalado|13 · Sostenibilidad y escalado]]
- [[04_Archive/Memecoin-LSTM/14 - Pendientes y proximos pasos (2026-10-05)|14 · Pendientes]]

## Qué se hizo (cronología)
1. **Bloque 1**: EXP-16v2 (split temporal, 6.941 filas) vs EXP-15. → modelo nuevo, umbral 0,50.
2. **Bloque 2**: `bot_real_v7.py` con constantes v7 (stop 10 %, trailing 15 %, 60 min, 10 %), mismos filtros y variables que el simulado.
3. **Bloque 3**: `ejecucion_jupiter.py` (Jupiter `/build`, firma local con solders, simulación previa, reintentos de venta, cierre de cuenta), `notificador_discord.py`, estado persistente, límites, CSV; modos `--dry-run`, `--test-token`, real.
4. **Investigación de sostenibilidad** con 10 € (costes, rug rates, Jupiter, Helius, fiscalidad) y backtest honesto de v7.
5. **EXP-17** (momentum del primer minuto) y comparación de modelos.
6. **Ensayo con 3 → 5 carteras virtuales** (EXP-15, EXP-16v2, EXP-16 limpio, EXP-16 limpio + on-chain, EXP-17).
7. **Reparación de la recogida de datos** (rutas, hub, etiquetas fiables, fotos cada 10 s, vigilante, lanzador).
8. **Reentrenamiento limpio** y refit; claves de Jupiter y Helius activadas; módulo on-chain integrado.

## Decisiones tomadas
- Modelo de decisión en real: **EXP-16 limpio** (`modelo_exp16_limpio_final.pkl`), umbral 0,50.
- Slippage compra 8 % (no 15 %), venta 25 %→95 %; filtro de coste ida y vuelta ≤ 8 %; freno a 7 €; −30 %/día; máx. 2 posiciones.
- Dinero real solo tras ensayo ≥ 24 h con ganancia neta (sin los 3 mejores) y prueba de 0,50 €.
- Escalado por tramos 10 → 30 → 100 € con ≥ 100 operaciones reales rentables.
- Se pararon los 3 bots simulados y los observadores/recolectores duplicados (autorizado).
- Secretos en `~/.claude/reference/bot_real.env` (chmod 600), nunca en el repo ni en el chat.

## Aprendizajes (para futuras sesiones)
- **Reorganizar carpetas con procesos de datos vivos los rompe en silencio** (2 h perdidas) → listar procesos antes; vigilante activo.
- **Etiquetas falsas**: hasta el 03-oct 12:45 UTC el recolector guardaba fallos de red como RUG −100 % (36 % de las filas). EXP-16v2 entrenó con 585 de ellas. Reentrenar siempre con `hora_captura ≥ 2026-10-03 13:00 UTC` y etiquetas del observador.
- **No comparar modelos con variables de otra fuente** (volumen de DexScreener vs Gecko): mi primera comparación de EXP-17 fue injusta contra EXP-15/16.
- **El stop medido contra la cotización de venta** (incluye el coste de salir) saltaba a los 6 s; mandar el precio de mercado.
- Gecko gratis: el límite real es **más bajo** que el documentado; el hub adaptativo converge (~11 s entre llamadas).
- Jupiter: clave gratuita obligatoria; `/order` cobra 0,5 % en tokens nuevos, `/build` no.
- Tokens muertos: Jupiter responde "amount threshold" (≈1 lamport) o "No routes found" → pérdida total.
- Fallo propio recurrente: ediciones en paralelo con el control GateGuard: una rechazada dejó el archivo usando nombres sin definir. Aplicar las ediciones dependientes en una sola operación o en orden.
- Backtest: usar **medianas** y "sin los 3 mejores"; las medias se contaminan con saltos de precio erróneos.

## Estado al cierre
Corriendo (con `setsid`, independientes de la sesión): `observador_piscinas.py`, `recolector_multired.py`, `vigilante_datos.py`, `bot_real_v7.py --dry-run`. Primeras 18 operaciones cerradas del ensayo (no concluyente): EXP-15 −0,04 € (2), EXP-16 limpio −0,04 € (4), EXP-16v2 −0,57 € (9), EXP-17 −0,75 € (3); carteras entre 9,48 y 10,00 €. 892 mil fotos de precio en la base, 11.117 tokens Solana capturados, etiquetas con precio 0 ≈ 1 %, sin fallos de bucle.

## Próximos pasos
Ver [[04_Archive/Memecoin-LSTM/14 - Pendientes y proximos pasos (2026-10-05)|pendientes]]: revisar el ensayo a las 24 h, estudiar el CSV on-chain, rotar el webhook de Discord, crear cartera y prueba de 0,50 € solo si hay ganancia neta, detector por WebSocket de Helius.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- Errores propios registrados: `.claude/COMMON_MISTAKES.md` #16–#21

