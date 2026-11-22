---
title: "Sesión - 2026-08-30 - Wallet Fidelidad - spec, F0 y F1"
date: 2026-08-30
type: meta/sesion
proyecto: "wallet-fidelidad"
sesion_id: 2314893c-8cf9-482f-b443-54ab65b1c8bf
tags:
  - sesion
  - cierre-automatico
  - wallet-fidelidad
aliases: []
origen: mixto
---

# Wallet Fidelidad — diseño, base de datos y acceso (fases F0 y F1)

> [!resumen] En cristiano
> Haytham pidió una app interna para crear y gestionar tarjetas de fidelidad en Google Wallet. En esta sesión se diseñó entera (datos, funciones, pantallas, seguridad) y se construyeron las dos primeras fases: base del proyecto, base de datos y entrada con usuario. Al final se arrancó la fase 2.

## Contexto
Proyecto nuevo en `~/Proyectos/wallet-fidelidad/` (Vite + React + TypeScript + Supabase + Edge Functions). Sesión de agosto; se recoge hoy porque su archivo se volvió a tocar el 2026-11-02. El vault actual no tiene ficha de este proyecto. Continúa en [[2026-08-31 - Wallet Fidelidad - F2 wallet-class (sesión a2ace52b)]].

## Qué se hizo
- Documento de diseño en `docs/spec.md`, tras elegir el enfoque A y repasar por secciones: modelo de datos, Edge Functions, frontend y seguridad/secretos/prerrequisitos.
- Plan F0+F1 (`docs/plans/2026-08-30-f0-f1-scaffold-datos-auth.md`) ejecutado con subagentes: guion de Google Cloud, scaffold Vite, Supabase local, migraciones (perfiles, tablas), pruebas pgTAP, cliente Supabase tipado, `useSession` y `RequireAuth`, `LoginPage`, shell con router y tokens de diseño. Cada tarea con su revisión; revisión final de toda la rama y ronda de arreglos.
- Haytham aportó el ID de emisor de Google Wallet, la cuenta de servicio y los datos del proyecto Supabase, y creó el usuario admin.
- Arrancó F2 (plan `2026-08-30-f2-wallet-class-negocios.md`): Task 1 (assets en Storage) cerrada; Task 2 en marcha al acabar.

## Decisiones tomadas
- Opción A del diseño; trabajo por fases con revisión de especificación y calidad en cada tarea.
- Haytham dijo que no le gustaba el diseño actual pero que se avanzara igualmente.

## Aprendizajes (para futuras sesiones)
- Haytham no sabía qué IDs y APIs de Google debía crear: hizo falta guion paso a paso (`docs/google-cloud-setup.md`).
- Los secretos van a `.env` ignorado por git; la clave de la cuenta de servicio, a `~/.claude/reference/` con `chmod 600`.

## Próximos pasos
- Rediseñar la interfaz (el diseño inicial no convenció).
- Crear ficha del proyecto en `01_Projects/` y README, según §0.8 del vault.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[2026-11-02 - Cierre nocturno]]
