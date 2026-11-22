---
title: "Sesión - 2026-11-03 - ComandAi: panel humano-máquina"
date: 2026-11-03
type: meta/sesion
proyecto: ComandAi
sesion_id:
  - 944f2e29-970c-48e8-86a7-7fa96863b3b4
  - 81eb1633-0096-4538-a2c1-d56b711e052f
tags:
  - sesion
  - cierre-automatico
aliases: []
origen: mixto
---

# Sesión — 2026-11-03: ComandAi, panel humano-máquina

> [!resumen] En cristiano
> A partir de un vídeo sobre montar un «backend con Obsidian», Haytham pidió un panel interno para NeoZeler que se pueda ver desde el móvil. Se creó el proyecto ComandAi: una página única (sin recargas) con tareas, novedades de IA, leads y proyectos, donde Haytham y Claude Code leen y escriben los mismos archivos. Ya arranca solo con el PC en el puerto 8200.

## Contexto
Proyecto nuevo [[01_Projects/ComandAi/1 - PRD|ComandAi]] (también aparece «Panel HQ» como carpeta de PRD). Código en `~/Proyectos/comandai/`; datos en `00_Meta/Panel/` (`humano/` y `maquina/`). La segunda sesión (`81eb1633`) continúa la primera (`944f2e29`) tras agotar el contexto.

## Qué se hizo
- Flujo `/nuevo-proyecto` por la vía micro-saas: PRD, TRD, UI-UX, AppFlow y Backend Schema (los dos últimos «no aplica»), Plan y [[01_Projects/ComandAi/Ficha de Investigacion]]. Fila de ComandAi añadida en [[03_Resources/Registro de Identidades Visuales]].
- Identidad «ventana al paisaje del día»: portadas en SVG propios cuya luz cambia con la hora real.
- Primera versión multipágina; Haytham dijo que «va fatal» y no navegaba fluido como el vídeo. Se volvió a ver el vídeo y se rehízo como página única con View Transitions, carrusel de portadas, dock con indicador deslizante y listas escalonadas. Movimiento subido de nivel 1 a 2 (anotado en UI-UX §7).
- Se pidió: tira de la semana, bloque «Te toca decidir» y tarjetas de cifras en embudo; después, auditoría UI/UX y un sistema bidireccional (Haytham interactúa en el panel y Claude Code lee/escribe lo mismo).
- Archivos compartidos: `humano/tareas.md`, `humano/para-claude.md`, `maquina/util/decisiones.json`, `maquina/logs/ia.jsonl`, `maquina/entrada/*-novedades-ia.json`. Puente para Claude Code: `scripts/panel.py`. Escrituras atómicas y `/estado` para refrescar solo.
- Auditoría con axe: 0 violaciones en 6 rutas. Seguridad: comprobación de Host/Origin, límite de cuerpo 4096, solo 127.0.0.1.
- Arreglo lateral: `context7` no conectaba porque el PATH de `.mcp.json` apuntaba a una ruta de USB inexistente; ahora usa `${HOME}/.local/opt/node/bin`.
- Servicio `comandai.service` (systemd de usuario, `Linger=yes`) instalado tras el «Sí, instalar» de Haytham; responde 200 en `http://localhost:8200`.

## Decisiones tomadas
- Nombre ComandAi; vía micro-saas; uso interno de NeoZeler (dueño: Haytham); SVG propios para las portadas.
- Atarlo a la IP de Tailscale más adelante, nunca a `0.0.0.0`.
- Fuente de interfaz cambiada por Haytham (el UI-UX aprobado fijaba Instrument Sans) y el documento de identidad aún no actualizado.
- Instalar el servicio de arranque solo con permiso explícito: el clasificador automático lo había denegado como persistencia no autorizada y no se rodeó.

## Aprendizajes
- Bun no está en el PATH: `export PATH=$HOME/.local/opt/bun-current:$PATH`.
- Para fluidez tipo vídeo, página única + View Transitions; el multipágina recargaba en cada clic.
- Se pidió auditar con «nuestras mejores skills» y se delegó en subagentes.

## Problemas
- Lighthouse nunca se ejecutó (no hay herramienta). 768 y 1280 px sin revisión visual.
- Faltan las portadas ilustradas (PNG 1600×700 en `public/portadas/`); los prompts están en `docs/prompts-ilustraciones.md`.
- La ficha del vault y el repo no están commiteados; `.mcp.json` sin commitear.

## Pendientes y próximos pasos
- [ ] Generar las portadas y ponerlas en `public/portadas/<seccion>.png`.
- [ ] Actualizar el UI-UX con la fuente nueva y reflejar el cambio en identidad.
- [ ] Atar a la IP de Tailscale y probar desde el móvil.
- [ ] Lighthouse y revisión a 768/1280 px.
- [ ] Commit del repo `~/Proyectos/comandai/`, README, `resumen.html` y ficha del vault (regla §0.8 del vault: documentación completa).
- [ ] Probar el ciclo crear → refrescar → borrar → refrescar en tareas.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
