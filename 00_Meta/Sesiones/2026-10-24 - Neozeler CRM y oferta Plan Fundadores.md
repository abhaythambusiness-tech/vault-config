---
type: sesion
date: '2026-10-24'
proyecto: '[[01_Projects/Neozeler CRM]]'
tags:
- crm
- oferta
- mail-marketing
- bun
- typescript
- ram
- panel
origen: mixto
---

# 2026-10-24 — Oferta «Plan Fundadores», CRM en Bun y retirada del Panel

> [!resumen] En cristiano
> Diseñamos una oferta para abrir el embudo (50 % menos en la puesta en marcha para los 5 primeros negocios, con condiciones) y construimos la aplicación que la lleva: candidatos, correos en secuencia, plazas y bajas. Después Haytham pidió hacerla **en tecnología web (TypeScript) y no en Python, gastando la mínima RAM**, y **quitar el Panel del servidor**. Se midió antes de elegir, se rehízo el CRM en Bun (44 MB bajo carga) y se retiró el Panel con copia de seguridad: el servidor ganó unos **980 MB** de RAM libre. Sigue en simulación hasta que se conecte Gmail.

## Decisiones

- **Oferta:** 50 % en el setup solo para 5 plazas, con cuota mínima de 3 meses y fecha de cierre; **sin garantía**; **la demo se ofrece al aceptar**. Las plazas se calculan con quienes de verdad están dentro (no hay urgencia falsa).
- **«Hazlo en web y no en Python, optimizando la RAM al máximo»:** se instalaron Bun 1.4.4 y Node 24.22.1 con suma verificada y se midió el mismo servidor mínimo con SQLite. Bun: 25 MB en reposo / 33 MB tras carga; Node: 63 / 89. **Elegido Bun + TypeScript, sin dependencias de ejecución, un solo proceso (web + cola de envíos).**
- **Dato honesto que se dijo:** el CRM en Python gastaba solo 57 MB; reescribirlo ahorra ~25 MB. Lo que de verdad liberó RAM fue **retirar el Panel (≈ 740 MB + el navegador de la ventana)**.
- **Diseño** (gate de `rules/diseno.md`, `ui-ux-pro-max`, `hallmark`): barra lateral azul marino y zona clara, tema oscuro automático, IBM Plex autoalojada, medidor de plazas y tira de embudo como firma, lista de comprobación antes de activar, tablero que se arrastra, pestañita pequeña de RAM/CPU.
- **El Panel se retiró entero** (web 8090, colector, ventana, correo) con copia `~/backups/panel-2026-10-24.tgz` comprobada antes de borrar. El torneo de Battle Royale no se tocó: `estado` sale idéntico y pasan sus 144 pruebas.
- Flujo `/nuevo-proyecto`: PRD, TRD, UI/UX, AppFlow, esquema y plan en `01_Projects/Neozeler CRM/` (lint de trazabilidad en OK).

## Aprendizajes (lo no obvio)

- **Medir antes de optimizar:** la RAM no era «Python vs JavaScript», eran dos fallos propios: las listas traían un JSON de 2 KB por candidato que no se usaba y «Hoy» cargaba todas las filas para contar. Con un `COUNT` y columnas ligeras, y con `BUN_JSC_useJIT=0` + `--smol`, de 66 MB (pico 90) a 44 MB (pico 49). `tests/carga_rutas.py` enseña cuánta RAM gana cada pantalla.
- **Colisión de nombres en el navegador:** el aviso emergente se llamaba `.aviso` y el chip de modo era `.chip.aviso`; el JavaScript intentó «cerrar» el chip, falló y dejó **todo el JavaScript parado** (sin RAM/CPU en vivo ni tablero). Los avisos emergentes pasaron a `.toast`. Solo se vio mirando la página de verdad, no con las pruebas.
- **`iframe sandbox` + `X-Frame-Options`:** la vista previa del correo salía en blanco; quitar el atributo `sandbox` del `iframe` (la respuesta ya lleva `Content-Security-Policy: sandbox`) lo arregló.
- **Caché del navegador:** con `immutable` y `?v=` fijo al arrancar, los cambios de `crm.js` no llegaban; la versión se calcula ahora con la fecha de los archivos.
- **Prueba intermitente:** una prueba falsificaba una cookie cambiando el último carácter por «0», y 1 de cada 16 veces ya lo era. `scripts/repetir_pruebas.sh` repite la batería N veces para cazar esto.
- **Navegador y PIN:** el navegador integrado no está en el servidor, así que escribir pide PIN y yo no lo tecleo. Se abrió un túnel SSH (`localhost`) para ver la parte de edición, que además es como se conectará Gmail (Google solo devuelve a `localhost`).
- **`zorin-ssh`:** `pkill -f` con el patrón en la propia línea mata la shell (usar `fuser -k PUERTO/tcp`); `sftp-upload` no crea carpetas; `Edit`/`Read` locales no tocan el servidor (parches con un script `assert count == 1`).

## Estado y pendiente

- Hecho: oferta, CRM nuevo en producción (`neozeler-crm.service`, puerto 8100, 291 candidatos), copia diaria a las 04:30, Panel retirado, README y fichas. 67 pruebas del CRM.
- **Pendiente de Haytham:** precios de setup y cuota, fecha de cierre, remitente y pie legal, **conectar Gmail** (túnel `ssh -L 8100:localhost:8100`), enviarse una prueba de cada correo, activar una tanda de 5-10. Cambiar el PIN (el de esta sesión pasó por el chat).
- A los 7 días: borrar `~/Proyectos/neozeler-crm-py` y `~/.local/opt/node-v24.22.1-linux-x64`. Primer commit del código (el repositorio del servidor no tiene ninguno).
- El `battle-royale-vivo.timer` estaba deshabilitado: decidir si el torneo en vivo debe seguir corriendo.

