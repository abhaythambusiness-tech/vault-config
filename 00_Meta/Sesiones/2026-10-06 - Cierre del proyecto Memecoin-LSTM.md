---
type: sesion
status: completada
fecha: '2026-10-06'
proyecto: '[[04_Archive/Memecoin-LSTM/00_Roadmap Maestro - Prediccion LSTM Memecoins|Memecoin-LSTM]]'
tags:
- memecoin
- cierre
- decision
origen: mixto
---

# Sesión — 2026-10-06: Cierre del proyecto Memecoin-LSTM

> [!abstract] Resumen
> Tras auditar los datos y medir 6 poblaciones candidatas, **ninguna superó el Gate 1**. Haytham decidió **cerrar** la parte de trading real. Se paró todo sin borrar nada.

## Contexto
Continuación de [[00_Meta/Sesiones/2026-10-05 - Optimizacion y auditoria del bot de memecoins]]. El 5-oct se concluyó que el problema no era el modelo sino la población de monedas, y se escribió un [[04_Archive/Memecoin-LSTM/15 - Plan nuevo: poblacion primero, con gates y escalado|plan nuevo]] con un Gate 1 que cerraba el proyecto si ninguna presa tenía ventaja.

## Qué se hizo
- **Fase 0 completada**: liquidez leída de la blockchain, creador de cada moneda, seguimiento largo y fotos de tenedores. Reinicio del observador y recolector con topes de llamadas **por hora**.
- **Auditoría de datos** ([[04_Archive/Memecoin-LSTM/16 - Auditoria de datos 2026-10-06]]): qué fuentes usar y cuáles no.
- **Fase 1** ([[04_Archive/Memecoin-LSTM/17 - Resultado Fase 1 y decision]]): 6 presas × 4 horizontes × 2 escenarios de coste. **0 de 24 pasan el Gate 1.**
- **Cierre**: copia final (399 MB), parada limpia de 4 procesos, desactivado el arranque automático (4 servicios + 2 temporizadores).

## Decisiones tomadas
- **Cerrar** la parte de trading real (opción 1). No se pasa a la Fase 2.
- No borrar nada: se conservan bases, CSV, modelos, scripts, pruebas y copias.
- Nunca se firmó ni envió una operación real (`SOLANA_PRIVATE_KEY` vacía).

## Aprendizajes (para futuras sesiones)
- **Fijar un criterio de cierre ANTES de medir fue lo que permitió cerrar.** El Gate 1 estaba escrito con una fecha y una condición, así que el resultado negativo no se pudo reinterpretar. Sin él, habría "faltado afinar algo" indefinidamente.
- **Un resultado puntual brillante hay que desmontarlo antes de creerlo**: P5 daba +57 % por una sola moneda que multiplicó x154 (sin las 3 mejores, −8 %); P2 daba +0,7 % que era −0,7 % sin las 3 mejores y −1,1 % en la mitad reciente.
- **Los topes de presupuesto diarios crean sesgo horario**: con un tope diario, un hilo gasta todo en las primeras horas y los datos solo cubren esa franja. Usar topes **por hora**.
- **Estimar mal el volumen cuesta**: se calcularon ~100 candidatas/día y eran 1.100-1.700, y el presupuesto de llamadas se agotó a mitad de día.
- **El resultado medido solo con el precio no ve las estafas** (el precio se congela mientras la liquidez se vacía). Toda etiqueta debe usar si se puede vender.
- **pandas 3 guarda las fechas en microsegundos**: comparar con enteros en nanosegundos da resultados vacíos sin error (n=0).
- **Un análisis grande murió por memoria** (~5 GB libres): limitar a ~3,8 GB.
- **El control de seguridad (GateGuard) bloquea ~1 de cada 3 ediciones** hasta que se declaran los hechos; no discutirlo, declarar y reintentar.
- El valor que queda no es el bot sino el **método**: separar elegir/confirmar, medir con liquidez real, costes reales medidos, y cerrar con un criterio escrito de antemano.

## Próximos pasos
- **Rotar los 2 webhooks de Discord** (pendiente de Haytham; estuvieron en texto claro y pueden estar en el historial de git del vault).
- Decidir cuándo borrar `_archivo_20261005/` y las bases antiguas (1,1 GB). Mientras tanto no estorban.
- Si se reabre: ver los 3 comandos de reapertura en la nota 17.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[04_Archive/Memecoin-LSTM/17 - Resultado Fase 1 y decision]]

