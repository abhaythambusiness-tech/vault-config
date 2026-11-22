---
type: referencia
status: propuesta
date: '2026-10-23'
proyecto: '[[01_Projects/Battle Royale]]'
tags:
- panel
- gtk4
- plan
- servidor-zorin
origen: mixto
---

> [!resumen] En cristiano
> El panel actual está bien para «mirar», pero no para «trabajar»: dibuja todo a mano, no tiene buscador ni filtros, no guarda historia y no avisa solo. La investigación dice que **no hace falta instalar nada pesado**: el servidor ya trae GTK 4 y libadwaita (los componentes nativos de Linux para listas con buscador, avisos y botones). Propongo pasar el panel a GTK 4, mantener los gráficos dibujados a mano (ya los tenemos y quedan bien) y añadir: semáforo con avisos, candidatas como herramienta de trabajo (estados, notas, filtros, copiar correo, QR), historial de 24 horas y gráficas. Son 8 fases; tú revisas cada una antes de pasar a la siguiente. Nada se construye hasta que apruebes este plan.

# Panel v5: investigación y plan de implementación

Basado en el panel actual (`~/Proyectos/battle-royale/`, GTK 3 + Cairo, 128 pruebas) y en tus peticiones: más información, mejor UX y, a futuro, usarlo como herramienta de trabajo.

## 1. Qué hemos comprobado (hechos del servidor, 2026-10-23)

| Dato | Resultado |
|---|---|
| Pantalla | 1080×1920 vertical, escala 1, GPU Intel UHD 630 |
| GTK / libadwaita del sistema | **GTK 4.14.5 y libadwaita 1.5** instalados; PyGObject 3.48.2 en el venv |
| Otras librerías ya presentes | WebKitGTK 2.52 (GTK 3 y 4), librsvg 2.58, libnotify 0.8, Inter, Cairo/Pango, psutil 5.9.8, SQLite 3.45 |
| RAM | 7,8 GB, ~5,6 GB disponibles; la ventana actual gasta ~85-140 MB |
| **Prueba desechable (spike)** | GTK 4 + libadwaita arrancó en 2,2 s en la sesión Wayland: lista de 261 filas con buscador (filtró a 111), aviso tipo «toast» y captura PNG de la ventana. Funciona. |

Componentes de libadwaita 1.5 confirmados en su documentación: `AdwBanner` (desde 1.3), `AdwToastOverlay`, `AdwNavigationSplitView` y `AdwOverlaySplitView` (desde 1.4), `AdwStyleManager` (modo oscuro forzado). **No** disponible en 1.5: `AdwToggleGroup` (llegó en 1.7).

## 2. Opciones evaluadas

| Opción | Licencia / versión | Veredicto | Por qué |
|---|---|---|---|
| **GTK 4 + libadwaita (sistema)** | LGPL · 4.14 / 1.5 | **Elegida** | Ya instalada, sin dependencias nuevas. Da lista filtrable y ordenable (`ColumnView`, `FilterListModel`), buscador, portapapeles, diálogos de confirmación, avisos y accesibilidad. Los gráficos se siguen dibujando con Cairo. |
| Cairo + Pango a mano (actual) | — | Se conserva para gráficos | Control total y ya queda bien. Para formularios, selección, búsqueda y copiar texto es mucho trabajo y frágil. |
| Qt (PySide6 6.12.0, 2026-10-08) | LGPL-3 / GPL | Descartada | Dependencia nueva y grande, otra forma de hacer todo y obligaciones de licencia LGPL. No aporta nada que GTK 4 no dé aquí. |
| Dear PyGui 2.3.1 | MIT | Descartada | Gráficas incluidas, pero estilo propio (no encaja con GNOME), y portapapeles, teclado y accesibilidad son menos maduros (afirmación general mía, no medida aquí). |
| Vista web dentro de la ventana (pywebview 6.2.1 BSD, o WebKitGTK directo) con uPlot/ECharts | BSD / MIT-Apache | Reserva | Permite gráficas muy ricas, pero añade pila web y ~un proceso de WebKit más de RAM (estimación mía). Solo si Cairo se queda corto. |
| uPlot (~50 KB) frente a ECharts (~1 MB) | MIT / Apache-2.0 | Referencia | uPlot es el más ligero: 100.000 puntos en 9 ms en un benchmark de 2026 (de un competidor, hay que tomarlo con cuidado). ECharts consume mucha más CPU en streaming según el autor de uPlot. Con nuestras series pequeñas (1.440 puntos por día) Cairo basta. |
| matplotlib 3.11.2 | licencia PSF | Descartada | Pesada y lenta para refrescar cada 3 s. |
| **segno 1.6.6** (QR) | BSD · sin dependencias · 2025-03-12 | **Elegida (única dependencia nueva)** | Genera la matriz del QR; la dibujamos con Cairo. Alternativa: ningún QR. |
| ntfy (avisos al móvil) | Apache-2.0 / GPLv2 | Opcional, con tu permiso | Los temas funcionan como contraseñas: hay que usar token y/o servidor propio. Solo avisos genéricos, **nunca datos de empresas**. Implica enviar texto a un servicio externo. |
| Iconos SVG (Lucide/Phosphor) + `Rsvg` | ISC / MIT | Elegida | librsvg ya instalada; iconos nítidos a cualquier tamaño. |

Fuentes: [PyPI dearpygui](https://pypi.org/pypi/dearpygui/json), [pywebview](https://pypi.org/pypi/pywebview/json), [segno](https://pypi.org/pypi/segno/json), [PySide6](https://pypi.org/pypi/PySide6/json), [matplotlib](https://pypi.org/pypi/matplotlib/json), [documentación de libadwaita](https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/), [benchmark de gráficas JS](https://apexcharts.com/blog/javascript-chart-library-benchmark/), [comparativa uPlot](https://cprimozic.net/notes/posts/my-thoughts-on-the-uplot-charting-library/), [ntfy y control de acceso](https://ohdear.app/docs/notifications/ntfy).

## 3. Qué debe enseñar el panel y cómo

**Principios**
1. Primero «¿va todo bien?» (2 segundos), luego el detalle al pulsar.
2. Cada dato lleva su edad («hace 40 s») y un color con significado fijo: verde = bien, azul = esperando, ámbar = atención, rojo = problema.
3. Cada aviso dice qué pasa **y qué puedes hacer**.
4. Nada de números sueltos: siempre con su contexto (frente a lo normal, tendencia 24 h).
5. Solo datos reales. Si no hay dato, se dice «sin dato», no se inventa.

**Páginas**

| Página | Contenido | Forma |
|---|---|---|
| **Resumen** | Franja de semáforo con el motivo («Todo bien» / «1 aviso: …»); 4 tarjetas (servidor, scraper, candidatas de hoy, bots); lista «Hoy toca» con 3 acciones | Anillos y minigráficas de 24 h |
| **Candidatas** (herramienta de trabajo) | Buscador, filtros (sector, nivel A/B, con correo), orden por prioridad o fecha; estados *nueva / contactada / respondió / descartada / cliente* con nota; «NUEVA» desde ayer; cola «a llamar hoy»; copiar correo y teléfono; borrador del primer mensaje con la oferta; QR de la web; exportar la lista filtrada | Lista a la izquierda, ficha a la derecha (`NavigationSplitView`) |
| **Scraper** | Webs leídas por hora, cuadrícula de las 33 zonas (hecha / pendiente / en curso), hora estimada de fin, historial de ciclos (duración, nuevas, errores), botón «Ejecutar ciclo ahora» con confirmación | Gráficas y cuadrícula de colores |
| **Servidor** | RAM, CPU, temperatura, disco y red de 24 h y 7 d; servicios y temporizadores (estado y próxima ejecución); registro filtrable; estado de copias | Gráficas de línea y tabla |
| **Torneos** | Curva de capital de los finalistas frente al azar; barra de «días hasta el veredicto»; **cuánto falta para que cada estrategia dispare** en cada moneda; historial de señales de 30 días; pasado y literal | Curvas, barras y tabla |
| **Ajustes** | Umbrales de aviso, notificaciones (opcional), modo noche, tamaño de letra, modo kiosco / modo trabajo | Interruptores |

**Transversal:** modo noche automático (00:00-07:00, menos brillo y casi sin movimiento), indicador de frescura, atajos de teclado, objetivos de clic grandes, y aviso visible («Datos viejos») si el hilo de lectura se cuelga.

**Alertas iniciales (reglas fijas):** disco > 85 %, RAM > 88 % durante 5 min, temperatura > 80 °C, scraper sin ciclo en 3 h, ciclo con error, Overpass fallando, vivo sin actualizar en 90 min, servicio caído, candidatas A nuevas sin revisar.

## 4. Arquitectura (decisiones mías, marcadas)

- **Migración paralela.** El panel GTK 3 actual sigue funcionando. El nuevo es un servicio aparte (`battle-royale-panel2`). Cuando lo revises y des el visto bueno se cambia; marcha atrás = reiniciar el viejo.
- **Capas:** `datos/` (lectores con caché, tipados, ya probados) → `historial.py` y `trabajo.py` (SQLite propio `data/panel.db`) → `alertas.py` (reglas) → `ui/` (GTK 4).
- **Historial:** un servicio de usuario aparte (`battle-royale-muestreo`) guarda una muestra por minuto en `panel.db`, retención 14 días (~20.000 filas). Así la historia no depende de que la ventana esté abierta.
- **El panel solo escribe en su propia base** (`panel.db`). Nunca toca `leads.db` ni los CSV del scraper (lectura).
- **Acciones permitidas (lista blanca):** ejecutar un ciclo del scraper (`systemctl --user start laya-leads.service`), copiar al portapapeles, exportar CSV a `salida/`. Todas con confirmación y registro. El panel **no envía correos ni mensajes**.
- **Gráficos:** Cairo con las primitivas actuales de `lienzo.py` (anillo, minigráfica, barras), movidas a `ui/dibujo.py`, dentro de `Gtk.DrawingArea.set_draw_func`.
- **Capturas de prueba:** técnica probada en el spike (`WidgetPaintable` → `render_texture` → PNG) dentro de la sesión Wayland.

## 5. Plan de implementación

> Para quien ejecute: usar `superpowers:executing-plans` (modo nativo) con revisión tuya al final de cada fase. TDD en las capas de datos; la interfaz se verifica con pruebas de dibujo sin error, de desbordamiento de texto y con capturas.

**Objetivo:** convertir el panel en una herramienta de trabajo con semáforo, avisos, historial, candidatas gestionables y gráficas.
**Stack:** Python 3.12, GTK 4.14 + libadwaita 1.5 (PyGObject del sistema), Cairo, SQLite, psutil; nueva dependencia: `segno` 1.6.6.
**Spec:** este documento (secciones 3 y 4).

### Restricciones globales
- Solo datos reales; si falta un dato, mostrar «sin dato».
- Sin secretos en el repo (token de ntfy en `~/.config/battle-royale/ntfy.env`, `chmod 600`).
- Ningún texto puede salir de su tarjeta ni de la pantalla (1080×1920 y ventana reducida): cortar con puntos suspensivos o ajustar línea.
- Laya Trader y los bots de cron están retirados: no aparecen.
- Toda estrategia nueva o cambio de intervalo se refleja en constantes únicas (no duplicar).
- Todo cambio de plan o convención se documenta en el vault y en `CLAUDE.md`/`GEMINI.md`.

### Puntos de revisión (casos que ninguna tarea probaba de serie)
1. El hilo de lectura se cuelga o `systemctl` tarda → la interfaz sigue viva y muestra «Datos viejos hace X».
2. 261+ candidatas con filtros que no dejan ninguna → estado vacío claro, no una lista en blanco.
3. `panel.db` bloqueada o corrupta → modo solo lectura, la interfaz no se cae.
4. El CSV del scraper cambia mientras se lee → lectura completa o reintento, nunca datos a medias.
5. Clic accidental en «Ejecutar ciclo ahora» → siempre pide confirmación.
6. Reinicio del servidor sin sesión de escritorio → el servicio reintenta hasta que haya pantalla.
7. Textos largos (nombres de empresa, oferta, dirección) → no se desbordan (queja ya vivida).

---

### Fase 1 · Cimientos de datos (sin interfaz nueva)

**T1. Historial de métricas**
- Crear: `src/battle_royale/historial.py`, `tests/test_historial.py`; servicio `battle-royale-muestreo.service` (+ `.timer` por minuto).
- Interfaces: `abrir_panel_db(ruta=None) -> sqlite3.Connection` · `muestrear(con, datos: dict, ahora: float) -> None` · `serie(con, campo: str, desde: float, hasta: float, puntos: int) -> list[tuple[float, float]]` · `purgar(con, ahora: float, dias: int = 14) -> int`.
- Tablas: `muestras(ts INTEGER PRIMARY KEY, ram_pct, cpu_pct, temp, disco_pct, red_rx, red_tx, leidas, con_correo, zonas, candidatas)`.
- Pruebas: `test_muestrear_guarda_una_fila_por_minuto`, `test_serie_reduce_a_n_puntos_conservando_extremos`, `test_purgar_borra_solo_lo_viejo`, `test_base_bloqueada_no_rompe` (punto de revisión 3).
- [ ] Pruebas rojas → implementar → verdes → `systemctl --user enable --now battle-royale-muestreo.timer` → comprobar 3 muestras tras 3 min.

**T2. Estados de candidatas (`trabajo.py`)**
- Crear: `src/battle_royale/trabajo.py`, `tests/test_trabajo.py`.
- Interfaces: `sincronizar(con, candidatas: list[dict], ahora: float) -> int` (registra `primera_vez`, devuelve cuántas son nuevas) · `cambiar_estado(con, dominio: str, estado: str, nota: str | None = None) -> None` · `estado_de(con, dominio: str) -> dict` · `cola_hoy(con, candidatas: list[dict], n: int = 20) -> list[dict]` · `exportar_csv(filas: list[dict], ruta: Path) -> Path`.
- Tabla: `candidatas_estado(dominio PRIMARY KEY, estado, nota, primera_vez, actualizado)`; estados válidos `nueva|contactada|respondio|descartada|cliente`.
- Dominio = host de la web sin `www.`. Pruebas: `test_dominio_normaliza`, `test_nuevas_desde_ayer`, `test_estado_invalido_se_rechaza`, `test_cola_hoy_excluye_descartadas_y_contactadas`, `test_exportar_respeta_filtro`.
- [ ] Rojas → implementar → verdes.

**T3. Alertas (`alertas.py`)**
- Crear: `src/battle_royale/alertas.py`, `tests/test_alertas.py`.
- Interfaces: `Alerta(nivel: Literal["info","aviso","grave"], clave: str, titulo: str, detalle: str, accion: str, desde: float)` · `evaluar(datos: dict, con_historial, ahora: float, umbrales: dict | None = None) -> list[Alerta]` · `resumen(alertas) -> tuple[str, str]` (nivel global y frase).
- Pruebas: una por regla de la sección 3 (`test_disco_alto`, `test_scraper_sin_ciclo_3h`, `test_ram_sostenida_5min_no_salta_por_un_pico`, …) y `test_sin_alertas_dice_todo_bien`.
- [ ] Rojas → implementar → verdes.

**T4. Partir `sistema.py` en `datos/`**
- Mover (sin cambiar comportamiento): `datos/servidor.py`, `datos/scraper.py`, `datos/torneos.py`, `datos/eventos.py`, `datos/candidatas.py`; `sistema.recoger()` queda como fachada con caché por origen y marca de edad (`edad_s`) en cada bloque.
- Prueba: todas las pruebas actuales siguen en verde + `test_cada_bloque_trae_edad` y `test_un_origen_lento_no_bloquea_los_demas` (punto de revisión 1).
- [ ] Mover → ejecutar toda la batería → verde.

### Fase 2 · Estructura nueva en GTK 4

**T5. Esqueleto y tema**
- Crear: `src/battle_royale/ui/app.py`, `ui/tema.css`, `ui/nav.py`; servicio paralelo `battle-royale-panel2.service`.
- Interfaces: `PanelApp(Adw.Application)` · ventana con `Adw.ToastOverlay` > `Adw.ToolbarView` > `Adw.ViewStack` (6 páginas) · `Adw.Banner` de semáforo · `lanzar(captura: str | None, pagina: int, ventana: bool) -> int`.
- Tema oscuro forzado con `Adw.StyleManager` y la paleta actual (variables CSS). Fullscreen por defecto, F11, atajos 1-6 y ← →.
- Pruebas: `test_arranca_y_pinta_sin_error` (se omite sin pantalla), `test_captura_png_genera_imagen_1080x1920`.
- [ ] Implementar → captura → comparar con el diseño actual → tú revisas.

**T6. Widgets de dibujo reutilizables**
- Crear: `ui/dibujo.py` (mover `Pincel` y primitivas de `lienzo.py`), `ui/widgets/{anillo,spark,barras,cuadricula,curva}.py` sobre `Gtk.DrawingArea`.
- Interfaces: `Anillo(valor: float, color: str)` · `Spark(series: list[Serie], rango=(0, 100))` · `Cuadricula(celdas: list[Celda], columnas: int)` · `Curva(series, banda: tuple | None)`.
- Pruebas: `test_widget_pinta_con_datos_vacios`, `test_spark_con_un_solo_punto`, `test_cuadricula_33_celdas`, `test_texto_largo_no_desborda` (punto de revisión 7).
- [ ] Rojas → implementar → verdes → captura.

### Fase 3 · Resumen

**T7. Página Resumen + semáforo**
- Crear: `ui/paginas/resumen.py`.
- Contenido: banner con `resumen(alertas)`, 4 tarjetas con minigráficas de 24 h (usa `historial.serie`), «Hoy toca» (alertas + `cola_hoy` + candidatas nuevas).
- Pruebas: `test_resumen_muestra_motivo_del_aviso`, `test_resumen_sin_historial_dice_sin_dato`.
- [ ] Implementar → captura → **revisión tuya (hito 1)**.

### Fase 4 · Candidatas como herramienta de trabajo

**T8. Lista con búsqueda, filtros y orden**
- Crear: `ui/paginas/candidatas.py`, `ui/modelo_candidatas.py`.
- Interfaces: `Gio.ListStore` de `FilaCandidata(GObject.Object)`; `Gtk.FilterListModel` (buscador + sector + nivel + «con correo» + estado) y `Gtk.SortListModel` (prioridad, fecha, nombre); `Gtk.ColumnView`.
- Pruebas: `test_filtro_por_sector_y_busqueda`, `test_filtros_sin_resultados_muestra_estado_vacio` (punto 2), `test_orden_por_prioridad_descendente`.
- [ ] Rojas → implementar → verdes.

**T9. Ficha lateral, estados, notas y utilidades**
- `Adw.NavigationSplitView` (lista / ficha). En la ficha: selector de estado, nota (guardada al salir del campo), botones **Copiar correo / Copiar teléfono / Copiar borrador / Abrir web**, QR de la web (`segno`), «Exportar lista filtrada».
- Interfaces: `borrador(candidata: dict) -> str` (plantilla con nombre, sector y oferta) en `trabajo.py`; `qr_matriz(url: str) -> list[list[bool]]` en `ui/widgets/qr.py`.
- Pruebas: `test_borrador_incluye_oferta_y_nombre`, `test_qr_matriz_cuadrada`, `test_cambiar_estado_desde_la_ficha_persiste`, `test_exportar_crea_csv_en_salida`.
- Dependencia: `venv/bin/pip install segno==1.6.6`.
- [ ] Rojas → implementar → verdes → captura → **revisión tuya (hito 2)**.

### Fase 5 · Scraper

**T10. Página Scraper**
- Crear: `ui/paginas/scraper.py`; en `datos/scraper.py` añadir `ciclos_recientes(n) -> list[dict]` (duración, zona, empresas nuevas, resultado, desde el journal) y `zonas() -> list[dict]` (estado de las 33).
- Contenido: webs leídas por hora (de `muestras`), cuadrícula de zonas, hora estimada de fin (zonas pendientes × intervalo), tabla de ciclos, botón **Ejecutar ciclo ahora** (`Adw.MessageDialog` de confirmación, `systemctl --user start laya-leads.service`, toast con el resultado).
- Pruebas: `test_hora_estimada_de_fin`, `test_ciclos_recientes_parsea_journal`, `test_ejecutar_ciclo_pide_confirmacion` (punto 5), `test_ejecutar_ciclo_no_se_lanza_si_ya_corre`.
- [ ] Rojas → implementar → verdes → captura.

### Fase 6 · Servidor

**T11. Página Servidor**
- Crear: `ui/paginas/servidor.py`.
- Contenido: RAM, CPU, temperatura, disco y red con selector 24 h / 7 d; servicios y temporizadores con estado y próxima ejecución (`systemctl --user list-timers`); registro filtrable por origen; procesos con más CPU solo cuando la CPU está alta.
- Pruebas: `test_selector_24h_7d_cambia_el_rango`, `test_servicios_marca_caidos_en_rojo`, `test_registro_filtra_por_origen`.
- [ ] Rojas → implementar → verdes → captura → **revisión tuya (hito 3)**.

### Fase 7 · Torneos

**T12. Página Torneos con curva y «cuánto falta»**
- Cambios en estrategias: campo opcional `Estrategia.proximidad: Callable[[pd.DataFrame], float] | None` (0 = lejos, 1 = a punto de disparar) para `donchian` (distancia al máximo de 55 velas) y `squeeze_volumen` (compresión y volumen); devuelve `None` si no aplica.
- Crear: `ui/paginas/torneos.py`; en `datos/torneos.py`: `curva_capital(con, nombre) -> list[tuple[float, float]]` y `senales_30d(con, nombre) -> list[dict]`.
- Contenido: curva de capital de los finalistas, barra de días hasta el veredicto (30 días desde `vivo_inicio`), tabla «cuánto falta» por moneda, historial de señales, pasado y literal.
- Pruebas: `test_proximidad_donchian_entre_0_y_1`, `test_proximidad_no_mira_el_futuro` (recorte de datos), `test_curva_capital_acumula_en_orden`, `test_dias_hasta_veredicto`.
- [ ] Rojas → implementar → verdes → captura.

### Fase 8 · Ajustes, avisos y cierre

**T13. Ajustes, modo noche y notificaciones opcionales**
- Crear: `ui/paginas/ajustes.py`, `src/battle_royale/avisos.py`; configuración en `~/.config/battle-royale/panel.toml` (umbrales, modo noche, tamaño de letra).
- Modo noche automático 00:00-07:00 (menos brillo, sin animaciones). **ntfy es opcional y desactivado por defecto**: requiere tu permiso explícito, un token en `ntfy.env` (`chmod 600`) y manda solo textos genéricos del tipo «Disco al 90 %».
- Interfaces: `cargar_config() -> dict` · `enviar_ntfy(titulo: str, cuerpo: str, config: dict) -> bool` (no hace nada si está desactivado).
- Pruebas: `test_modo_noche_por_hora`, `test_ntfy_desactivado_no_envia`, `test_ntfy_nunca_incluye_datos_de_empresas`, `test_config_invalida_usa_valores_por_defecto`.
- [ ] Rojas → implementar → verdes.

**T14. Corte, documentación y memoria**
- Cambiar el servicio del panel al nuevo tras tu visto bueno; dejar el viejo parado, no borrado. Actualizar README, ficha del vault, sesión, `CLAUDE.md`/`GEMINI.md`, `librerias.md` (GTK 4 + libadwaita 1.5, `segno`, técnica de captura), `graphify update .`.
- [ ] Documentar → `pytest` completo → captura final de cada página → **revisión final tuya**.

---

## 6. Qué no entra (y por qué)
- Enviar correos o mensajes a las empresas desde el panel (el panel prepara el borrador y lo copia; enviarlo es decisión tuya).
- Exponer el panel por red o web.
- Reactivar Laya Trader o los bots de cron.
- Cambiar los datos del scraper (`leads.db`, CSV): solo lectura.

## 7. Cómo lo ejecutaría
Recomiendo **modo nativo** (lo implemento yo en esta misma sesión, fase a fase) con **tu revisión al final de las fases 3, 4, 6 y 8**. Motivo: las tareas se apoyan mucho unas en otras (datos → widgets → páginas) y un revisor independiente por tarea costaría mucho para el riesgo que hay (todo es lectura salvo el estado de candidatas y el botón de ciclo, ambos con confirmación). Si prefieres un revisor independiente por tarea, es el modo «subagentes».

