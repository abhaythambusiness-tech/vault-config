---
title: "Sesión - 2026-11-08 - AI Designer Toolkit"
date: 2026-11-08
type: meta/sesion
origen: mixto
proyecto: "Sistema Claude Code"
tags:
  - sesion
  - diseno
  - skills
  - mcp
aliases: []
---

# Sesión — 2026-11-08: AI Designer Toolkit

> [!resumen] En cristiano
> Copiamos a una nota el toolkit de IA para diseñadores de Antonio Díaz Cueto y lo cruzamos con nuestras skills y MCPs. Casi todo ya lo teníamos; cerramos el único hueco real (publicar en Vercel), hicimos que `diseno-central` genere un `DESIGN.md` y dejamos las librerías con enlaces. 21st ya funciona (plan gratuito).

## Contexto
Haytham pasó el [AI Designer Toolkit](https://app.notion.com/p/diazcueto/AI-Designer-Toolkit-26956c795b1380278d21e8278431e837) (Notion) para analizarlo y compararlo con `[[03_Resources/Sistema Claude Code - Configuracion Completa]]`.

## Qué se hizo
- **Réplica del toolkit:** `[[03_Resources/AI Designer Toolkit]]` con las 6 fases, todos los casos de uso con sus herramientas y el diccionario. Los datos se sacaron del DOM de la página (la columna de herramientas no salía en el texto plano).
- **Cruce con nuestro sistema:** `[[03_Resources/Configuracion Ideal - Toolkit x Sistema]]`. ~85 % cubierto; huecos reales: Vercel, `design.md`, y enchufar 21st/Figma.
- **Vercel por CLI:** `npx --yes vercel@latest <comando>`. Ya había sesión iniciada (`abhaythambusiness-2218`); no se instaló nada global ni se guardó token. `--prod` solo con permiso.
- **Exportar `DESIGN.md`:** script nuevo `~/.claude/skills/diseno-central/scripts/export_design_md.py` (de `DESIGN-IDENTITY.md` a `DESIGN.md`). Enlazado en la fase 1 de `SKILL.md` y en `rules/identidad-y-dinamismo.md` §1. Autotest y prueba con ejemplo OK; no probado con un proyecto real.
- **Librerías:** sección «Referencias del AI Designer Toolkit» en `~/.claude/reference/librerias.md`, tabla con enlace y estado. 18 de 20 enlaces dieron 200; Astryx sin localizar, Designmd.co bloquea bots (403).
- **Reglas:** 3 filas nuevas en §2 de `CLAUDE.md` del vault (DESIGN.md, Vercel, librerías); bloque equivalente en `~/.claude/reference/gemini-extra-vault.md`; `sync-gemini.py` regenerado y `--check` al día.
- **21st probado:** MCP conectado por el usuario con `/mcp`. `search` devuelve resultados; plan `free` con 2 descargas de código al día, sin generación con IA. Anotado en `librerias.md`.

## Decisiones tomadas
- No instalar las herramientas externas del toolkit (Relume, Lovable, Bolt, Cursor, Zapier…): duplican a Claude Code, `diseno-central` y n8n, y cada skill extra gasta contexto.
- Vercel por CLI y no por MCP: más simple y sin configuración nueva.
- `DESIGN-IDENTITY.md` sigue siendo la fuente; `DESIGN.md` es derivado y no se edita.

## Aprendizajes (para futuras sesiones)
- `sync-gemini.py` solo copia el §0 del `CLAUDE.md` del vault: lo que se añada al §2 no llega a Gemini salvo que también se ponga en `gemini-extra-vault.md`.
- `astryx.ai` no es el sistema de diseño del toolkit (es una web de trading) y `coss.com` tampoco: coss ui está en `coss.com/ui`.
- La autorización de plugins (`/mcp`) no se puede hacer desde la app de escritorio; hay que usar una terminal con `claude`.
- Pendiente de verificar el script con un proyecto real.

## Próximos pasos
- [ ] Probar `export_design_md.py` con la identidad de un proyecto real (p. ej. Comanda Viva).
- [ ] Decidir si autorizar el plugin de Figma de `product-management` (duplica al Figma MCP ya conectado) y si se paga plan Team de Tactiq.
- [ ] Localizar el enlace de Astryx o descartarlo.
- [ ] Hacer commit de los cambios del vault.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[03_Resources/AI Designer Toolkit]]
- [[03_Resources/Configuracion Ideal - Toolkit x Sistema]]
- [[03_Resources/Sistema Claude Code - Configuracion Completa]]
