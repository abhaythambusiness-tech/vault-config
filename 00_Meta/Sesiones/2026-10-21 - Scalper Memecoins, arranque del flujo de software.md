---
type: sesion
status: completada
fecha: '2026-10-21'
proyecto: '[[01_Projects/Scalper Memecoins]]'
tags:
- crypto
- trading
- bot
- laya
- servidor
- decision
origen: mixto
---


# Sesión — 2026-10-21: Scalper Memecoins, arranque del flujo de software

> [!resumen]
> Se pasó la idea (bot de scalping de memecoins con Laya, panel web en vivo, todo en el servidor Zorin) por el flujo de 6 documentos hasta el Plan aprobado, y se ejecutaron T-01 (repo y entorno) y T-02 (medición de Laya). Laya cabe en RAM y en latencia, pero su primera prueba de discriminación es mala: queda como punto de decisión abierto.

## Contexto
Haytham pidió montar en el servidor un bot de scalping de memecoins "con Laya" (`NandhaKishorM/laya`, un motor de decisiones de texto en un solo pase) con muchos trades pequeños al día y un panel web con ganancias y decisiones en tiempo real. También se limpió antes la RAM del servidor: se pararon Brave y los 12 contenedores del Supabase local de `wallet-fidelidad` (uso de 3,0 a 1,8 GiB; se arrancan con `supabase start`).

## Qué se hizo
- Flujo de 6 documentos en `01_Projects/Scalper Memecoins/`, cada uno aprobado antes del siguiente; `trace_lint` en OK tras añadir US-05 y US-08 donde faltaban.
- **Cliente simulado** (agente independiente): encontró 8 huecos reales (carteras sin definir, "Cerrar todo" sin protección, "Reanudar" que podía anular el corte diario, jerga sin glosario, etc.); se aplicaron al PRD, UI/UX y AppFlow con permiso.
- Esquema SQLite validado con `sqlite3` real (cascadas, restricciones, ejemplo numérico +5,15 %).
- **T-01**: repo en el servidor (`~/Proyectos/scalper-memecoins/`, commit `d107c4a`), `ruff`, `mypy`, `pytest` en verde.
- **T-02**: `laya` 0.4.12 + torch 2.14.1+cpu; medición en `sandbox/medir_laya.py` (commit `e946578`).

## Decisiones tomadas
- **Papel, no dinero real**, y Laya decide estafa/entrada/salida; tres carteras en sombra (Laya, Reglas, Azar) para comparar con una línea base.
- **Gate 1 fijado antes de medir**: ≥ 300 operaciones, ≥ 5 días, IC90 inferior > 0 en las dos mitades y sin las 3 mejores; si no, se cierra.
- Corte diario en **−20 %** (el "stop" que pidió Haytham, entendido como corte diario). Capital 10 SOL por cartera, 3 % por operación, 8 posiciones.
- Todo Python (el servidor no tiene Node); SQLite en vez de Supabase; panel con SSE y `lightweight-charts`.

## Aprendizajes (no obvios)
- **Laya sin entrenar no lee bien un estado numérico**: con 4 casos sintéticos dio la menor puntuación de estafa (0,38) y la mayor de "comprar" (0,67) a la moneda con todas las señales de rug. Confianza interna 0,04. Se trata de un clasificador de lenguaje; hay que medirlo con datos etiquetados reales (T-04) y contra la cartera Azar antes de fiarle nada.
- Medido en CPU del servidor: 2,0 GB de RAM con el checkpoint cargado, p50 595 ms para 3 preguntas, 14 s de carga en frío. Los checkpoints están en `convaiinnovations/laya*` en Hugging Face. `laya.calibrate` existe aunque el README no la documenta.
- El plan del proyecto repite un patrón de cuatro proyectos previos: ventaja bruta menor que el coste. Se asume desde el PRD y no se promete rentabilidad.
- `mcp zorin-ssh`: `read-command` rechaza pipes y paréntesis; `run-command` no admite saltos de línea ni `sleep` largos (60 s agota el tiempo); para scripts se usa `sftp-upload`.
- El hook de seguridad saltó por la palabra "pickle" aunque solo la citaba: reformular en vez de forzar.

## Próximos pasos
- Decidir qué hacer tras T-02 (ver ficha): medir a Laya con datos reales (T-04), afinarla o dejarla solo como filtro antifraude.
- Copiar las bases del observador de Memecoin-LSTM al servidor (pide permiso) y conseguir `FOMOAPI_KEY`.

## Continuación (misma sesión): cambio de mercado y Puerta 0 de forex y oro
- **Verificación de la etiqueta de memecoins**: 0 de 3.000 monedas sin fotos; re-etiquetado por token; veredicto "Laya no aporta" confirmado. Una regla antifraude simple (cuota de compras) sí separa vivas de muertas (AUC 0,85) pero filtrar no da retorno positivo.
- **Cambios de mercado a petición de Haytham**: memecoins → acciones (8-K, confluencia técnica + noticias, PRD pausado) → forex, oro, BTC y ETH. Cada cambio se trató como una prueba offline con **criterio fijado antes de medir**.
- **Forex y oro**: 210 comunicados (Fed 2011-2026, BoE 2017-2026), 442 pares evento-activo. Laya sigue bien el régimen de tono, pero la estrategia no se distingue del azar (p = 0,50 a +1 día) ni del léxico simple. **NO PASA.**
- **Recolector de cripto**: 6 RSS cada 30 min en SQLite, desde 2026-10-21; prueba de cripto no antes de 8 semanas.
- Aprendizajes: (1) Yahoo `range=max` devuelve barras **mensuales**: pedir `period1/period2`; (2) las filas diarias de Yahoo traen el cierre del día anterior: comprobarlo con el movimiento absoluto alrededor de eventos conocidos antes de medir nada; (3) el BCE carga su listado con JavaScript, sin enlaces estáticos; (4) BoE: resúmenes accesibles desde 2017; Fed: páginas históricas por año con enlaces `monetaryAAAAMMDDa.htm`.

## Continuación 2: investigación y bot de tendencia en papel
- **Petición**: investigar a fondo la mejor estrategia y metodología y ponerla a operar en papel hoy, con "bastante" actividad diaria.
- **Investigación** (fuentes en el PRD de Bot de Tendencia): lo mejor respaldado es tendencia diversificada con volatilidad objetivo a frecuencia baja; el Sharpe > 1,5 del preprint de cripto no pude verificarlo; carry de financiación y sentimiento LLM descartados.
- **Resultado**: 12 monedas de Binance, 2020-2026, costes del 0,15 % por lado. **Ninguna de las 3 carteras validó** (T/M/F: Sharpe 2024-26 de 0,42/0,43/−0,13; F pierde un 74 % del capital al año en costes). Operan igualmente como EXPERIMENTALES desde las 16:49 UTC (36 órdenes iniciales, `cron` cada hora).
- **Aprendizajes**: (1) más operaciones empeora el resultado por costes: 7,6 % → 44 % → 74 % del capital al año; (2) la rotación de M y F (296 y 494 veces al año) delata un umbral de rebalanceo demasiado pequeño, no corregido para no añadir pruebas sin deflactar; (3) misma lógica de órdenes (`rebalancear`) en backtest y en vivo para que no diverjan; (4) la ventaja de la tendencia es menor caída máxima, no mayor rentabilidad que Bitcoin.

## Relacionado
[[01_Projects/Bot de Tendencia]] · [[01_Projects/Mercados Laya/1 - PRD|Mercados Laya]] · [[01_Projects/Eventos Bolsa/1 - PRD|Eventos Bolsa (pausado)]] · [[01_Projects/Scalper Memecoins]] · [[00_Meta/Registro de Sesiones|Registro de Sesiones]] · [[04_Archive/Memecoin-LSTM/17 - Resultado Fase 1 y decision|Memecoin-LSTM (cierre)]]

