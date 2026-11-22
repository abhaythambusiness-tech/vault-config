---
title: "Sesión - 2026-10-26 - Configuración portátil de Claude y vault para el instituto"
date: 2026-10-26
type: meta/sesion
proyecto: ""
sesion_id: 135e52c9-1a22-4b53-8acb-f1bcb9f9c97a
tags:
  - sesion
  - cierre-nocturno
aliases: []
origen: mixto
---

# Sesión — 2026-10-26: Configuración portátil de Claude y vault para el instituto

> [!resumen] En cristiano
> Haytham usa el ordenador del instituto en horas libres y allí no tiene su configuración de Claude. Se montó un paquete portátil (`Portable-NeoZeler`) que instala todo sin permisos de administrador, con las claves guardadas en un archivo cifrado aparte.

> Cierre automático (tarea nocturna) a partir del historial de la sesión `135e52c9`; es un resumen fiel pero breve, el detalle está en la conversación original.

## Qué se hizo
- Planteado el problema: equipo ajeno, Linux, sin `sudo`.
- Se creó el flujo de brainstorming y se eligió una solución portátil con archivo cifrado para los secretos.
- Haytham ejecutó `crear-secretos.sh`; se comprobó que el archivo existe y se descifra.
- Se redactó un README: en el instituto basta `bash .../Portable-NeoZeler/usar.sh`; `--secretos` solo si hacen falta las claves (contiene claves de bots y la cartera, en un equipo ajeno casi nunca se necesitan).
- La sesión se archivó con el título «Configuración portátil de Claude y vault».

## Decisiones tomadas
- Sin `sudo`: instalación en el directorio del usuario.
- Secretos solo cifrados y solo bajo petición explícita (`--secretos`).

## Archivos y proyectos afectados
- `Portable-NeoZeler` (USB), `crear-secretos.sh`, `usar.sh`, README del USB

## Problemas
- Riesgo: llevar claves de bots y cartera en un USB; mitigado con cifrado y opción manual.

## Mejoras propuestas
- Mantener actualizado el USB cuando cambie la configuración (se amplió el 2026-11-02).

## Pendientes y próximos pasos
- Rotar claves si alguna vez se descifran en un equipo ajeno.

## Relacionado
- [[2026-11-02 - Raiz ordenada y USB Portable-NeoZeler completo]]
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
