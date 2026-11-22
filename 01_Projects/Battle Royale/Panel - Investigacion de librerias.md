---
type: referencia
status: en-progreso
date: '2026-10-23'
proyecto: '[[01_Projects/Battle Royale]]'
tags:
- panel
- ui
- ux
- investigacion
origen: mixto
---

> [!resumen] En cristiano
> Antes de cambiar el panel miré qué herramientas existen para hacerlo más útil y qué aguanta el servidor. Conclusión: el servidor ya trae el «motor de páginas web» del escritorio (WebKitGTK) y 5,7 GB de RAM libres, así que se puede hacer el panel como una **página web local** mostrada dentro de la ventana nativa. Con esa página podrás trabajar las candidatas (filtrar, marcar, copiar correos) y, además, abrirla desde tu PC por la red de casa. Hace falta muy poco código de terceros: unas 5 librerías pequeñas y gratuitas. Esto es la investigación; el plan está en [[01_Projects/Battle Royale/Panel - Plan de implementacion]].

## 1. Qué admite el servidor (medido el 2026-10-23)

| Dato | Resultado |
|---|---|
| RAM | 7,8 GB en total, **5,7 GB disponibles** con todo encendido |
| Python | 3.12.3 |
| Navegador (Chromium, Firefox, Epiphany) | **ninguno instalado** |
| Node / npm | **no hay** (las librerías web se descargan una vez y se guardan en el proyecto) |
| WebKitGTK 4.1 (motor web del escritorio) | **disponible** por Python (`gi.require_version("WebKit2", "4.1")`) |
| GTK4 + libadwaita | **disponibles** por Python |
| Tipografía Inter | instalada |
| Disco | 140 GB libres |
| Monitor | 1080×1920 vertical, GNOME en Wayland |

**Prueba desechable de RAM** (`scripts/spike_webkit.py`, vista web fuera de pantalla con un canvas animado a 10 fotogramas/s): proceso principal 175 MB + proceso web 150 MB + red 48 MB = **372 MB** y **4,6 % de CPU**. Dos notas: (1) fuera de pantalla WebKit pide desactivar la composición acelerada (`WEBKIT_DISABLE_COMPOSITING_MODE=1`) porque el modo sin ventana no tiene OpenGL; hay que repetir la medida en la ventana real; (2) el panel actual dibujado con Cairo gasta 85-140 MB.

## 2. Tres caminos para el panel

| Camino | Qué es | Ventajas | Inconvenientes |
|---|---|---|---|
| **A. Página web local + ventana WebKitGTK (recomendado)** | Un servidor web pequeño (FastAPI) en el propio equipo y una ventana nativa que lo muestra | Trabajo real: tablas con filtros, formularios, copiar al portapapeles, diálogos; **se puede abrir también desde tu PC o el móvil**; la interfaz se prueba con navegador normal; casi todo es HTML/CSS | +~370 MB de RAM por la vista web; hay que vendorizar unas pocas librerías JS |
| B. Seguir con Cairo | Lo que hay hoy, dibujado a mano | 85-140 MB, ya funciona | Cada botón, filtro o campo de texto hay que programarlo a mano; no se puede abrir desde otro equipo; no sirve como herramienta de trabajo |
| C. GTK4 + libadwaita nativo | Widgets reales (listas, botones, campos) | Aspecto de aplicación del sistema, poca RAM | Gráficas y tablas con filtros siguen siendo trabajo a medida; solo funciona en la pantalla del servidor |

## 3. Librerías comparadas (versiones y licencias verificadas en npm y PyPI el 2026-10-23)

### Lado servidor (Python)
| Librería | Versión · licencia | Para qué | Decisión |
|---|---|---|---|
| FastAPI | 0.161.1 · MIT | servidor web y rutas (ya usada en Laya Trader) | **Adoptar** |
| uvicorn | 0.54.0 · BSD-3 | ejecuta FastAPI | **Adoptar** |
| Jinja2 | 3.1.6 · BSD | plantillas HTML | **Adoptar** |
| sse-starlette | 3.5.0 · BSD-3 | actualizaciones en vivo (servidor → página) | **Adoptar** |
| psutil | 7.2.2 · BSD-3 | RAM, CPU, disco, temperatura (ya en uso) | ya está |
| Apprise | 2.0.1 · BSD-2 | avisos al móvil por Telegram, ntfy y más de 70 servicios | **Opcional** (fase de avisos) |
| segno | 1.6.6 · BSD | códigos QR en SVG sin dependencias | **Opcional** |
| Glances | 4.5.8 · LGPL-3 | monitor del sistema completo | No: psutil ya basta |
| pywebview | 6.2.1 · BSD-3 | ventana con vista web | No: PyGObject directo hace lo mismo con menos capas |
| orjson, humanize, aiosqlite | MPL/Apache, MIT, — | JSON rápido, «hace 5 min», SQLite asíncrono | No de entrada (la stdlib alcanza) |

### Lado página (JavaScript, vendorizado a mano: no hay Node)
| Librería | Versión · licencia · última publicación | Tamaño | Decisión |
|---|---|---|---|
| **htmx** + `htmx-ext-sse` | 2.0.11 · 0BSD · sep-2026 / ext. 2.2.4 | ~50 KB min (14 KB comprimido) | **Adoptar**: filtros, búsqueda y cambios de estado sin escribir JavaScript |
| **Alpine.js** | 3.17.5 · MIT · oct-2026 | ~45 KB | **Adoptar**: pequeños detalles de pantalla (copiar, diálogos, pestañas) |
| **uPlot** | 1.6.32 · MIT · mar-2025 | ~48 KB | **Adoptar** para series de tiempo. En su propia prueba gasta ~10 % CPU y 12 MB frente a Chart.js 40 %/77 MB y ECharts 70 %/85 MB (cifras del autor con versiones antiguas; la documentación es floja, según un usuario) |
| Chart.js | 4.6.1 · MIT · oct-2026 | 254 KB | Reserva si uPlot se queda corto |
| ECharts | 6.1.0 · Apache-2.0 | 1 MB, 60 MB instalado | **Descartada**: pesada para lo que hace falta |
| lightweight-charts | 5.2.1 · Apache-2.0 | ~60 KB | Solo si queremos velas de precio (ya la vendorizamos en Laya Trader) |
| Tabulator | 6.7.1 · MIT · oct-2026 | 30 MB instalado | **No de entrada**: con 261 filas, htmx + HTML basta. Reserva |
| Grid.js | 6.2.0 · MIT · mar-2024 | 1,4 MB | Descartada: sin mantenimiento reciente |
| AG Grid Community | 36.2.0 · MIT | 21,6 MB | Descartada: demasiado pesada; lo avanzado es de pago |
| SortableJS | 1.15.7 · MIT | ~45 KB | **Opcional**: arrastrar tarjetas en el tablero de candidatas |
| Leaflet | 1.9.4 · BSD-2 · may-2023 | ~42 KB | **Opcional**: mapa de zonas. El mosaico de zonas sin mapa es suficiente de inicio. Los mapas de OpenStreetMap exigen atribución, un User-Agent propio y no usar el servidor en exceso |
| MapLibre GL | 6.15.0 · BSD-3 | 29 MB | Descartada |
| ApexCharts | 8.4.1 · «ver licencia» | 29 MB | Descartada: licencia poco clara |
| Frappe Charts | 1.6.2 · MIT · jun-2021 | — | Descartada: abandonada |
| D3 / Observable Plot | 7.9.0 ISC / 0.6.17 ISC | 0,9 / 1,5 MB | Reserva: a bajo nivel solo si hace falta una gráfica a medida |
| Open Props / Pico CSS | 1.7.23 / 2.1.1 · MIT | 1,3 / 19,6 MB | No: unas variables CSS propias bastan |
| Tom Select | 2.6.2 · Apache-2.0 | 3,5 MB | Reserva para listas desplegables con búsqueda |

### Herramientas de vigilancia estudiadas (no se instalan; sirven de modelo)
- **Uptime Kuma** (MIT): pantalla de estado muy pulida y avisos a muchos servicios, pero es una aplicación Node más pesada.
- **Gatus** (Apache-2.0): ligero, se define en un archivo YAML. Lo más cercano a nuestro caso por ligereza.
- **Healthchecks** (BSD-3): sirve para saber si una tarea programada dejó de «dar señales».
- **Idea que adoptamos**: nuestro motor de avisos lee el estado local directamente (no hace falta un servicio aparte).

## 4. Qué enseñan las fuentes sobre el diseño

- **Jerarquía**: los números críticos más grandes y arriba, el resumen primero y el detalle debajo o plegado. Se asume que se mira unos segundos, así que ha de leerse sin pensar.
- **Estados**: el color no basta; hay que acompañarlo de icono o texto (accesible para daltónicos). Rojo y verde solo para malo y bueno, no como decoración.
- **Orden visual**: agrupar con espacio en vez de líneas, leyendas junto a su gráfica, modo oscuro diseñado a propósito (no invertido).
- **Pantallas de pared (Grafana)**: el «modo kiosco» esconde menús y controles, y ajusta los paneles al espacio. No encontré cifras de tamaño de letra según la distancia: **hay que probar a la distancia real del monitor**.
- **Pipeline de contactos (CRM pequeños)**: lista **y** tablero con el mismo dato; cada estado es una columna; los estados terminales («descartada», «cerrada») se ocultan por defecto y se muestran con un interruptor; cambio de estado en bloque con casillas; orden por defecto por fecha del siguiente contacto; vistas guardadas («por llamar hoy»).

## 5. Lo que no pude comprobar (avisos honestos)
- Cifras de RAM de Uptime Kuma, Gatus y Healthchecks: las fuentes no las dan; no se usan en las decisiones.
- Que Apprise soporte ntfy: las fuentes consultadas no lo confirmaban; se comprobará en su documentación al llegar a esa fase.
- Rendimiento de uPlot frente a ECharts: las cifras salen del propio autor de uPlot y de versiones antiguas; se medirá con nuestros datos.
- Cómo se comporta WebKitGTK en la ventana real (no fuera de pantalla): se mide en la fase de la ventana.

## Fuentes
- uPlot, comparativas y opiniones: [cprimozic.net](https://cprimozic.net/notes/posts/my-thoughts-on-the-uplot-charting-library/), [hilo de Node-RED](https://discourse.nodered.org/t/fast-live-time-line-charts-comparison/61342), [TanStack](https://tanstack.com/charts/latest/docs/comparison), [elección de librerías](https://blog.openreplay.com/choosing-javascript-charting-library/).
- WebKitGTK desde Python: [guía de GNOME](https://wiki.gnome.org/Projects/WebKitGtk/ProgrammingGuide/Bindings), [kiosco de ejemplo](https://github.com/sraue/kiosk-browser).
- Diseño de paneles: [AdminLTE 2026](https://adminlte.io/blog/25-best-dashboard-design-examples-for-2026-real-products-principles/), [DesignRush](https://www.designrush.com/agency/ui-ux-design/trends/dashboard-design-principles), [UX Studio](https://www.uxstudioteam.com/ux-blog/dashboard-design).
- Pila FastAPI + htmx + SSE: [ejemplo volfpeter](https://github.com/volfpeter/fastapi-htmx-tailwind-example), [artículo de OneUptime](https://oneuptime.com/blog/post/2026-01-25-build-realtime-dashboards-fastapi/markdown), [FastHX](https://pypi.org/project/fasthx/).
- Tablas: [AG Grid frente a Tabulator](https://www.wmtips.com/technologies/compare/ag-grid-vs-tabulator/), [Grid.js frente a Tabulator](https://www.wmtips.com/technologies/compare/grid.js-vs-tabulator/), [alternativas de Tabulator](https://www.tabulator.info/alternatives/ag-grid/).
- Vigilancia: [alternativas a Uptime Kuma](https://betterstack.com/community/comparisons/uptime-kuma-alternative/), [Gatus frente a Uptime Kuma](https://www.bitdoze.com/md/uptime-kuma-vs-gatus.md).
- Modo kiosco: [Grafana](https://grafana.com/blog/grafana-tutorial-how-to-create-kiosks-to-display-dashboards-on-a-tv/), [grafana-kiosk](https://github.com/grafana/grafana-kiosk).
- Mapas: [política de teselas de OpenStreetMap](https://operations.osmfoundation.org/policies/tiles/).
- Avisos: [Apprise en PyPI](https://pypi.org/project/apprise).
- Contactos y tableros: [Less Annoying CRM](https://lessannoyingcrm.com/blog/new-board-view-for-your-pipelines), [KeyCRM](https://help.keycrm.app/en/working-with-pipelines-applications-leads-deals/how-to-work-with-pipelines).
- Versiones y licencias: registros públicos de npm y PyPI, consultados el 2026-10-23.

