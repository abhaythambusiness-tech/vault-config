---
type: sesion
status: completada
fecha: '2026-10-09'
proyecto: '[[01_Projects/crypto-copy-bot-spec]]'
tags:
- crypto
- trading
- bot
- auditoria
- refactor
- decision
origen: mixto
---

# Sesión — 2026-10-09: auditoría y reconstrucción del crypto-copy-bot

> [!abstract] Resumen
> La auditoría encontró que el bot no estaba conectado a ningún feed: generaba precios con `random` sesgado al alza y escribía el resultado (+5.416 SOL sobre 10 de capital) en el mismo log que leía el dashboard. Se reescribió entero sobre datos reales (alertas de FomoAPI + precios de DexScreener), con contabilidad FIFO persistente y control de riesgo aplicado de verdad, y se relanzó con 100 SOL de capital en papel.

## Contexto

`~/Proyectos/crypto-copy-bot` era el proyecto más reciente de la carpeta (commits del 9-oct). Haytham pidió una auditoría en segundo plano y, tras el veredicto, arreglarlo entero y reiniciarlo con 100 SOL. Es el cuarto intento de bot cripto tras cerrar Memecoin-LSTM, rediseñar AVAX y el NO PASA del Gate 1 de [[04_Archive/goat-trading]].

## Qué se hizo

- **Auditoría en paralelo** con dos subagentes (correctitud Python/contabilidad y seguridad/secretos). Verifiqué a mano los hallazgos de cabecera antes de reportarlos.
- **Comprobación empírica de las dos fuentes de datos** antes de escribir código: el WebSocket de FomoAPI responde y su esquema real no se parece en nada al que el conector esperaba; DexScreener da precio, liquidez, market cap, volumen y edad del par por `tokenAddress`.
- **Reescritura completa** de los 8 módulos, más 3 nuevos (`state_store`, `price_provider`, `risk`, `config`).
- **43 tests** nuevos aislados con `tmp_path` (los anteriores escribían sobre el log de producción y dependían del historial).
- Venv propio, `requirements.txt` fijado, `.gitignore` ampliado, `.env.example`, README y `spec.md` reescrito con lo que **no** está implementado.
- Relanzado: daemon + panel en `127.0.0.1:8050`. Primera compra real a los 20 s (QI, 2 SOL, copiando a DanNicastro888).

## Decisiones tomadas

- **El log viejo no se borra ni se mueve.** Se usan nombres nuevos (`audit_log.jsonl`, `state.json`) y `trade_log.jsonl` queda como histórico. Mover datos existentes es destructivo y además el clasificador de permisos lo bloqueó con razón.
- **El modo live lanza excepción** en vez de devolver `EXECUTED_ONCHAIN` falso. Preferible fallar ruidosamente a mentir.
- **Sin verificador de RugCheck, el filtro se desactiva de forma explícita y ruidosa**, no se "simula" como aprobado. Un flag de seguridad simulado a `True` es peor que apagado.
- **El estado contable se persiste en snapshot atómico propio**; el log pasa a ser solo auditoría. No se deriva el saldo de eventos redondeados.
- **Edad máxima de señal automática**: 1.500 ms con API key, 90.000 ms sin ella. Sin clave el feed llega con 60 s de retraso y el filtro de 1,5 s rechazaría el 100 %.
- Paleta del panel: carbón cálido + ámbar, para no caer en el navy/teal genérico (`CLAUDE.md §4.1.2`).

## Aprendizajes (para futuras sesiones)

> Los cuatro fallos quedaron registrados en `.claude/COMMON_MISTAKES.md` como entradas 30-33.

- **Un múltiplo de tres cifras sobre el capital es, por defecto, una fuente sintética, no una estrategia.** `random.uniform(-0.02, 0.025)` tiene deriva de +0,25 % por tick; compuesto con un sizing del 5 % de la equidad fabrica cualquier curva. Antes de celebrar un resultado, comprobar de dónde sale el precio.
- **Un componente de I/O con test propio puede no estar integrado.** `FeedConnector` tenía lógica de reconexión y su test, y no se instanciaba en ningún camino de producción. El `grep` del nombre fuera de `tests/` es la comprobación que faltaba.
- **El feed de alertas no trae precio.** Todo el diseño original asumía que sí (`market_snapshot.get("price_usd", 1.0)`). Esa suposición no verificada es la raíz del PnL inventado: faltaba una pieza entera de la arquitectura, no un valor por defecto.
- **Las dos fuentes se comprueban antes de diseñar sobre ellas.** 15 minutos de sondas me dieron el esquema real, el retraso de 60 s, los 2.900 eventos de búfer que había que omitir y la confirmación de que DexScreener cubría el hueco del precio. Sin eso habría reescrito el bot contra un esquema imaginario, igual que la versión anterior.
- **"Simulado" en un comentario junto a tres variables fijadas a `False` es un control que nunca puede negar.** Buscar este patrón en cualquier filtro de seguridad heredado.

## Próximos pasos

- Conseguir `FOMOAPI_KEY` gratuita: baja el retraso de 60 s a 15 s. Sin eso, los resultados en papel no son extrapolables a copy trading real.
- Dejarlo corriendo varios días y construir la whitelist con los traders que salgan rentables **de los propios datos**, luego arrancar con `--no-allow-unlisted`.
- Implementar RugCheck real (RPC de Solana: `getAccountInfo` para freeze/mint authority) antes de considerar cualquier modo live.
- Definir el equivalente al Gate de `goat-trading`: qué resultado en papel justificaría dinero real, por escrito y antes de verlo.

## Relacionado

- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[01_Projects/crypto-copy-bot-spec]]
- [[04_Archive/goat-trading]]

