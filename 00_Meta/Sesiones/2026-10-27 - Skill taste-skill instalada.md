---
title: "Sesión - 2026-10-27 - Skill taste-skill instalada"
date: 2026-10-27
type: meta/sesion
proyecto: "[[01_Projects/Los Apuntes de Liyo]]"
tags:
  - sesion
  - skills
  - diseno
aliases: []
origen: mixto
---

# Sesión — 2026-10-27: skill `design-taste-frontend` (taste-skill)

> [!resumen] En cristiano
> Instalé la skill de Leonxlnx para que las webs de marketing y las pantallas de app no salgan con cara de «hecha por IA». Antes revisé su código: no instala nada raro ni manda datos; solo abre un Chrome sin ventana para medir la página y baja imágenes con licencia abierta si se lo pides. Ya está nombrada en las reglas, en los `CLAUDE.md` y en los dos `GEMINI.md`.

## Qué se hizo
- Clonado `Leonxlnx/taste-skill` (v2.1.5, MIT) en carpeta temporal, revisado `install.sh`, los scripts (`lib/cdp.mjs` lanza Chrome headless con perfil temporal; `assets.mjs` consulta APIs públicas sin claves) y el `SKILL.md`. Copiada la carpeta revisada a `~/.claude/skills/design-taste-frontend/`.
- Mencionada en: `~/.claude/CLAUDE.md` §2, `rules/skills-frecuentes.md` (fila + decisión de solapes), `rules/diseno.md`, `rules/identidad-y-dinamismo.md`, `CLAUDE.md` del vault §2, `00_Meta/GEMINI.md` y `~/.gemini/config/GEMINI.md`.

## Aprendizajes
- **Requisitos**: Node 22+ (el `node` por defecto de este PC es 18; hay uno 22 en fnm) y Chrome/Edge/Chromium, que **no están instalados** en este PC: sin él no corren `inspect.mjs` ni `scenes.mjs`.
- **Solape con hallmark**: ambas atacan lo genérico. Regla fijada: la identidad aprobada del proyecto manda y taste solo ejecuta, mide y critica; `draw.mjs` no elige otra dirección si ya hay identidad.
- **Pendiente**: si se quiere usar su inspector, instalar Chromium; y rehacer el paquete del USB (`empaquetar.sh`) para que viaje la skill.
