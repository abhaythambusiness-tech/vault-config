---
title: Mando de PS4 en Linux, Steam y Wine
date: '2026-11-21'
type: sesion
origen: maquina
proyecto: ''
sesion_id: 8eff4b81-01e6-44d2-829a-5533fb644949
tags:
- sesion
- equipo
- linux
---

> [!resumen] En cristiano
> Haytham quería jugar con un mando de PS4. Linux sí lo veía, pero los juegos no, porque solo `root` podía leerlo. Se arregló con una regla del sistema (udev) que le da acceso a su usuario. Es una sesión de uso personal, sin relación con proyectos de NeoZeler. Dos sesiones comparten el mismo arranque (`7d03db12` es la rama interrumpida).

## Qué se hizo
- Diagnóstico: el mando PS4 sale como `/dev/hidraw4` (permiso `600 root:root`); el driver `hid_playstation` sí estaba cargado.
- Steam (Flatpak) estaba colgado de un cierre anterior: se mataron los procesos y se relanzó; su ventana se quedaba cargando (GPU Intel HD 4000 antigua), con alternativa `-cef-disable-gpu`.
- Se dio a Steam permiso de lectura a las carpetas de los juegos y `--device=all` para los dispositivos de entrada.
- Regla udev aplicada por Haytham (sin sudo para Claude): el mando queda con ACL (`crw-rw----+`) para su usuario.
- Se confirmó que Hollow Knight arranca con Wine directo.

## Decisiones
- No se ayudó a quitar o evitar el parche de copias pirata (Isaac); la vía propuesta fue comprar el juego. Para Hollow Knight (cuenta de GOG) se propuso Heroic Games Launcher con su copia legítima.

## Pendientes
- Probar en el juego que el mando responde (con la copia de GOG vía Heroic).
- Opcional: sin Steam colgado de nuevo, lanzar con `-cef-disable-gpu`.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

