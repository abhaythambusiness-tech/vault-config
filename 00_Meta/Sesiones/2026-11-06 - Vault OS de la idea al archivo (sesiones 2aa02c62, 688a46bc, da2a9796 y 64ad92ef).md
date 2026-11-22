---
title: "Vault OS, de la idea al archivo - 2026-11-06"
date: 2026-11-06
type: meta/sesion
origen: mixto
proyecto: "[[04_Archive/Vault OS]]"
sesion_id:
  - 2aa02c62-f7a9-4a51-a031-6e1eae63178a
  - 688a46bc-fec4-4a19-94aa-dc570eca2ecb
  - da2a9796-6b8a-40db-943d-1c2c7fb42ed7
  - 64ad92ef-5cd6-4a7b-ab2c-d82ff2671ffd
tags:
  - sesion
  - vault-os
aliases: []
---

# Vault OS: de la idea al archivo (6 nov 2026)

> [!resumen] En cristiano
> Durante el 6 de noviembre Haytham diseñó, construyó, rehízo y al final cerró Vault OS, una app web con una oficina 3D de fondo para sustituir a Obsidian. Tres sesiones fueron construcción; la cuarta añadió notas legibles, CRM con leads de Laya y presencia, y terminó con «no me gusta»: se cerró y se archivó. Las notas por tema ya existían; esta solo une las cuatro sesiones y añade lo que faltaba.

## Línea de tiempo
1. **`2aa02c62` (mediodía-tarde): diseño.** Haytham pega el contexto de «3D Vault OS» (reemplazar Obsidian; ventanas de cristal sobre una oficina 3D). Se archiva `Dashboard Command AI` (lo sustituye), se mueven los 15 archivos `.glb/.obj/.mtl` de la raíz a `99_Assets/3d/`, se aprueban PRD y Plan y se elige el estilo «A · Cristal», sin referencias. Reparto de modelos 3D: `tech-core` = Haytham (CTO), `command-totem` = Sam (CEO), `layth-ai-node` = una IA que entra y cambia o crea archivos, `data-receiver-drone` = el script de prensa, `data-vault-diorama` = la oficina. Se aprueba la identidad visual («Adelante»). Al final los avatares «no pegan con la oficina»: Claude entrega prompts de objetos simbólicos animados y un prompt de oficina adaptada a los modelos.
2. **`688a46bc` (tarde): cambio de base.** Se compara con el repo `ederland/Agentes_IA_3D` y se decide usarlo como base con la lógica del vault: aparece el personaje de Claude Code cuando toca algo del vault y deja de teclear cuando espera respuesta. Se añaden prensa (noticias solo con reglas simples, sin IA) e ideas. Solo se muestran carpetas de NeoZeler y se integra un CRM. Despliegue en `http://192.168.0.102:8790` sin PIN; Haytham lo ve lento → auditoría de UI/UX, se «rebaja» la carga y se reordenan componentes. Cierra pidiendo que lo pruebe en Chrome o Firefox.
3. **`da2a9796` (tarde-noche): prensa y commit.** Haytham confirma que va fluido en Chrome, se marca `DESIGN-IDENTITY.md` como aprobado y se hace commit en `~/Proyectos/vault-os` (`ba5e904`, solo `Prensa.jsx` e `index.mjs`). La API `/api/noticias` y el botón «Actualizar noticias» ya existían y funcionan. No hay remoto, sin push.
4. **`64ad92ef` (noche): notas, CRM, presencia y cierre.** Notas como mini-Obsidian (markdown ya renderizado), CRM grande conectado a leads/Laya y presencia de Haytham (CTO) y Sam (CEO). Después Haytham dice «cierra el proyecto no me gusta»: ficha a `cerrado`, se archiva en `04_Archive/`, el repo se copia a `~/Proyectos/archive/vault-os-20261106.tar.gz` (228 archivos, 1,2 MB) y se borra de `~/Proyectos`.

## Decisiones
- `Dashboard Command AI` queda sustituido y archivado (copia en `~/Proyectos/archive/dashboard-command-ai-20261106.tar.gz`).
- Noticias por reglas simples, sin IA.
- Cierre de Vault OS por decisión de Haytham (no le gustó). No se escribió la retro completa porque Haytham no dio el motivo.

## Archivos y proyectos afectados
- Ficha: [[04_Archive/Vault OS]]; docs del proyecto movidos a `04_Archive/`.
- Modelos 3D: `99_Assets/3d/`.
- Notas de tema ya existentes: [[2026-11-06 - Vault OS arranque]], [[2026-11-06 - Vault OS base Agentes_IA_3D]], [[2026-11-06 - Vault OS notas CRM Laya presencia]].

## Problemas
- El panel del navegador de Claude no tiene WebGL: la oficina 3D nunca se pudo ver ahí, solo en Chrome o Firefox.
- Lentitud inicial por la escena 3D; se arregló con calidad baja y gzip/caché.
- Los avatares del repo no encajaban con la oficina que Haytham tenía.
- Varias continuaciones por contexto lleno (la sesión `2aa02c62` y `688a46bc` se resumieron 3 veces).

## Mejoras propuestas
- Antes de construir una app «para sustituir X», hacer una maqueta de una pantalla y probarla un día: Vault OS se cerró tras un día de trabajo.
- Si se cierra un proyecto sin retro, preguntar el motivo en una línea y guardarlo (aquí falta el porqué del «no me gusta»).

## Pendientes
- Borrar el tar del dashboard solo cuando se confirme que no hace falta (la nota de arranque lo condicionaba a portar la escena; ya no se porta).
- Registrar el motivo del cierre en la ficha archivada si Haytham quiere aprender de él.
- Los modelos 3D reaparecieron en la raíz durante el ordenado del vault (ver [[2026-11-06 - Estructura del Vault y limpieza de la raiz]]); hoy están en `99_Assets/3d/`, la raíz no tiene `.glb/.obj/.mtl`.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
