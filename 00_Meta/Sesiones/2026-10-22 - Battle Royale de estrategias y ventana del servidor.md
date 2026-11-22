---
type: sesion
date: '2026-10-22'
proyecto: '[[01_Projects/Battle Royale]]'
tags:
- trading
- servidor-zorin
origen: mixto
---

> [!resumen] En cristiano
> Se montó un torneo entre 14 estrategias de trading sin IA, con una ventana en la pantalla del servidor que muestra memoria, procesos, scraper y marcador. El pasado ya está jugado: ninguna estrategia le gana al azar de forma convincente. Sigue corriendo en vivo con dinero ficticio para confirmarlo en 30 días.

## Qué se hizo
- Diseño aprobado en chat (pasado + vivo, ventana en el servidor) y PRD en `[[01_Projects/Battle Royale/1 - PRD]]`.
- Código en `~/Proyectos/battle-royale/` (motor, 14 estrategias, árbitro del azar, torneo, vivo, ventana GTK3, 61 pruebas).
- Servicios de usuario: ventana (`panel-ventana.service`) y vivo (`battle-royale-vivo.timer`, minuto 02).
- Torneo del pasado jugado una sola vez con parámetros fijados antes.

## Aprendizajes
- El criterio que importa es el azar, no «ganar dinero»: sin árbitro, `ruptura_vwap_ma@4h` y `donchian` parecían buenas; con comisión doble y azar, ninguna aguanta.
- Con 27 luchadores hay que exigir p ≤ 0,05 / nº de luchadores; un t de 2 aparece por suerte.
- El MCP `zorin-ssh` corrompe PNG al bajarlos y oculta base64 largo; no se puede traer una captura. Medir el diseño con tamaños (`scripts/medir_panel.py`) y confiar en la pantalla del servidor.
- `sh -c 'mkdir -p a/{b,c}'` no expande llaves (sh, no bash): crea una carpeta literal `{b`.
- Montar un servidor HTTP temporal para sacar un fichero lo bloquea el clasificador de permisos («exponer servicios locales»).
- Pendiente de Haytham: confirmar que la ventana se ve bien en el monitor del servidor.


## Continuación (2026-10-23): panel, torneo literal y repos
- Panel renovado: título «Panel del servidor», dos páginas que rotan (servidor/scraper/combate y torneos), procesos y servicios solo de nuestros proyectos, disco, temperatura, red y próximo ciclo.
- Torneo literal con 5 min y 2 años: ninguna estrategia supera al azar; en 5 min la señal sin comisión ronda 0 % y la comisión la hunde (ver ficha).
- Repos revisados (trading-estrategias, CME-TRADING, pypro_bot): casi nada reutilizable; solo el Stat-Arb de CME-TRADING, añadido como `pairs_z` (versión larga contra BTC).
- Aprendizaje: `scp` con la clave dedicada sí trae PNG del servidor (el MCP los corrompe); el descargador en marcha no recoge cambios de código hechos después de lanzarlo (faltaron los enlaces de 1 h).

## Panel v5: investigación y plan (2026-10-23)
- Investigado qué usar para mejorar el panel: el servidor ya trae GTK 4.14 + libadwaita 1.5 (más WebKitGTK, librsvg, libnotify); una prueba desechable confirmó lista filtrable, toast y captura PNG. Decisión propuesta: migrar a GTK 4 + libadwaita manteniendo Cairo para gráficos; única dependencia nueva `segno` (QR). Descartadas Qt/PySide6, Dear PyGui y matplotlib; vista web como reserva.
- Plan de 14 tareas en 8 fases (semáforo y avisos, candidatas con estados, historial 24 h, scraper, servidor, torneos, ajustes). Documento: `[[01_Projects/Battle Royale/Panel - Investigacion y plan]]`. Pendiente de aprobación; nada construido.
- Aprendizaje: en un mismo proceso no se puede cargar GTK 3 y luego GTK 4 (`require_version` falla); probar versiones en procesos separados.

## Panel v5: construcción de las fases 0-8 (2026-10-23)
> [!resumen] En cristiano
> El panel del servidor pasó de una ventana dibujada a mano a una **página web** (FastAPI + htmx + uPlot) que el monitor muestra en una ventana WebKit y que se abre desde el PC en `http://192.168.0.100:8090`. Tiene semáforo con avisos, historial con gráficas, candidatas del scraper con seguimiento, torneos con la curva de capital frente al azar, PIN para editar desde la red y ajustes. Registro por fase en [[01_Projects/Battle Royale/Panel - Plan de implementacion]].

- **Aprendizajes no obvios:** (1) con comisiones, el azar pierde casi siempre, así que con 0 operaciones el capital «parece» ganarle: hay que decir «sin operaciones» y no «por encima del azar»; (2) la repetición de 30 días mostró que las tres estrategias **sí operan y pierden** (−2,2 %, −0,4 %, −1,5 %); (3) FastAPI + SQLite exige conexión compartida entre hilos; (4) FastAPI no admite un tipo de retorno `A | B` de respuestas; (5) WebKit a pantalla completa cuesta ~311 MB frente a 44 MB de Cairo.
- **Estado:** 323 pruebas; servicios `panel-web` (`--lan`), `panel-colector`, `panel-ventana`. Pendiente del usuario: fijar PIN, revisar el monitor, decidir retirar Cairo y la Fase 7.
