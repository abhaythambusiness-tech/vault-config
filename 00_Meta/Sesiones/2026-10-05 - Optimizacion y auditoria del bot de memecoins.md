---
type: sesion
status: completada
fecha: '2026-10-05'
proyecto: '[[04_Archive/Memecoin-LSTM/00_Roadmap Maestro - Prediccion LSTM Memecoins|Memecoin-LSTM]]'
tags:
- memecoin
- bot
- trading
- auditoria
origen: mixto
---

# Sesión — 2026-10-05: Optimización y auditoría del bot de memecoins

> [!abstract] Resumen
> Se midieron los costes reales, se auditó el proyecto y se aplicaron 12 mejoras con cuatro agentes en paralelo. Conclusión central: la estrategia **no tiene ventaja demostrable**, y el motivo no era que faltara afinarla.

## Contexto
Viene de la noche del 4 al 5 de octubre, en la que las cinco carteras de ensayo de 10 € tocaron el freno de seguridad de 7 € y se pararon solas. Proyecto: `~/Documentos/vault/04_Archive/Memecoin-LSTM/`.

## Qué se hizo

### Hallazgo que invalidaba las pruebas anteriores
Las pruebas antiguas medían el resultado **solo con el precio**. En una estafa típica de estas monedas vacían la liquidez: el precio se queda congelado, así que parecía "sin cambios" cuando en realidad no se podía vender y la pérdida era del 100 %. Entre el 60 % y el 70 % de las monedas que el bot compraría mueren en menos de 30 minutos.

### Costes reales, por fin medidos
Se añadió registro del coste real de ida y vuelta en cada compra (`datos/costes_dryrun.csv`). Con 40 mediciones de Jupiter: **mediana 1,37 %**, percentil 95 del 4,5 %. Se venía suponiendo un 8 %. Las comisiones fijas son el 0,65 % del importe. El escenario válido en los análisis es "1 % + 1 % + 0,65 %".

### Búsqueda exhaustiva de ventaja (todo negativo)
Con el resultado medido correctamente y los costes reales:
- **960 reglas de salida** (stop, trailing, tiempo máximo, venta parcial, salida por liquidez): 0 con intervalo de confianza por encima de cero.
- **36 filtros de entrada** (concentración de tenedores, creador, pump.fun, ratio compras/ventas, operaciones por minuto, franjas horarias, RugCheck): 0 positivos al confirmar con datos no usados para elegirlos.
- **Modelos reentrenados** (9 variables y momentum, con tres objetivos distintos): el que predice "esta moneda no muere" acierta bien (0,83 sobre 1) y baja las muertas del 35 % al 8 %, pero el dinero sigue en negativo. Sobrevivir no es lo mismo que ganar.

### Liquidez bloqueada: reduce muertes, no mejora el dinero
El dato de RugCheck ya se recogía y no se usaba. Con 197 monedas: con 0 % de liquidez bloqueada muere el 84 %, con el 100 % muere el 42 %. La reducción de muertes es real (−19,8 puntos, intervalo −29,6/−9,5). **Pero el dinero no mejora**: +5,1 puntos con intervalo −13,4/+24,9, y al validar hacia delante cae a −0,4. Quita estafas, pero también quita las pocas subidas que pagaban las pérdidas. **No se aplicó como filtro.**

### Universo de prueba desalineado (error metodológico propio)
Las pruebas filtraban las monedas con la liquidez de las fotos del observador, que falta en el 80 % de los casos, mientras que el bot en vivo filtra con la de GeckoTerminal. Solo **178 monedas coincidían** entre los dos universos (de 1.059 y 220). Solo el 17 % de lo que se analizaba era comprable de verdad, y 42 monedas que el bot sí compra nunca se probaron: esas mueren el 95 %. En el universo real todo empeora: mediana −92 % en vez de −49 %.

### Infraestructura y seguridad
- **Secretos**: dos webhooks de Discord estaban en texto claro en cinco scripts. Ahora leen del entorno. Las copias con los valores viejos se movieron a `~/.claude/reference/memecoin-bak-secretos/` (chmod 600).
- **Copias de seguridad**: `scripts/backup_datos.sh`, probada (146 MB, integridad verificada), con timer diario a las 04:30. Sigue siendo el mismo disco: no hay copia externa.
- **Arranque automático**: unidades de systemd de usuario para los cuatro procesos, con seguro anti-duplicado por `pgrep` y `linger` activado. Están `enable` pero **sin arrancar**, para no duplicar los procesos lanzados a mano.
- **Informe diario**: `scripts/informe_diario.py`, con timer a las 08:00.
- **Pruebas**: 40 pruebas nuevas en `scripts/tests/`, todas pasan. Cubren las reglas de salida, el color de los avisos, el margen de gracia de 45 s y la referencia de precio. `pytest` no está instalado: se usa `unittest`.
- **Observador endurecido**: WAL, reintentos con espera creciente y hora en el log. **El proceso sigue con el código viejo hasta que se reinicie.**
- **Dataset unificado**: `scripts/construir_dataset_unificado.py` (3.190 filas, 57 columnas). En adelante los análisis deben partir de aquí.
- **Registro ampliado**: `evaluaciones_bot_real_dryrun_v3.csv` y `espera5_dryrun_v2.csv` guardan de cada moneda vista las redes sociales, RugCheck, concentración de tenedores, datos del creador y el coste real.

## Decisiones tomadas
- Carteras reiniciadas a **15 €** virtuales, freno a 10,5 €.
- **No aplicar** el filtro de liquidez bloqueada: reduce estafas pero no mejora el resultado.
- **No pasar a dinero real.** Ninguna cartera gana en ensayo.
- Mantener la cartera "Espera 5 min" como prueba en vivo, aunque su resultado esperado ha empeorado al corregir el universo.

## Aprendizajes (para futuras sesiones)
- **Medir el resultado con el precio es una trampa en activos sin liquidez.** Si no se puede vender, el precio es ficción. Toda etiqueta debe incorporar la liquidez o la actividad de operaciones.
- **El universo de prueba tiene que filtrarse con los mismos datos que usa el bot en producción.** Filtrar con otra fuente cambia las conclusiones por completo, y hacia peor.
- **Bajar costes no crea ventaja.** Con costes cero, la mejor regla sigue en torno a cero. Primero hay que encontrar ventaja bruta.
- **Reducir el riesgo no es lo mismo que ganar dinero.** El modelo que evita casi todas las estafas sigue perdiendo, porque filtra también las subidas que compensaban.
- **Probar mil combinaciones garantiza encontrar falsos hallazgos.** Lo que hoy parecía prometedor (concentración de tenedores: +5,2 % al elegir) daba −58,3 % al confirmar. Separar siempre los datos de elegir y de confirmar, y contar cuántas combinaciones se probaron.
- La columna `deployer_address` del recolector vale literalmente `"desconocido"` en las 1.077 filas de Solana: la idea de filtrar por historial del creador no se puede ni probar hasta arreglar esa captura.
- Al añadir columnas a un CSV en uso hay que **cambiar el nombre del archivo** (v2, v3), porque la cabecera ya escrita descuadraría las filas nuevas.

## Próximos pasos
- **Rotar a mano los dos webhooks de Discord** (pueden estar en el historial de git del vault).
- Dejar correr la recogida de datos dos o tres días y repetir los análisis con el dataset unificado.
- Reiniciar el observador para activar la versión robusta (abre un hueco de segundos en los datos).
- Arreglar la captura de `deployer_address` en el recolector.
- Decidir si merece la pena seguir: con los datos de hoy, la conclusión honesta es que esta estrategia no tiene ventaja, no que falte ajustarla.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[00_Meta/Sesiones/2026-10-04 - Bot real memecoins y recogida de datos]]

