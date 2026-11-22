---
date: '2026-10-13'
proyecto: '[[GEMINI]]'
tags:
- sesion
- antigravity
- gemini
- tokens
- skills
type: sesion
origen: mixto
---

# Sesión — 2026-10-13: Sincronización y optimización de Antigravity (Gemini)

> [!abstract] Resumen
> Se resolvió el desbordamiento del presupuesto de tokens en Antigravity eliminando el GEMINI.md huérfano duplicado (42 KB), aligerando GEMINI.md global a 7,4 KB y purgando 111 symlinks rotos para dejar únicamente las 29 skills del núcleo frecuente.

## Contexto y Causa Raíz
Antigravity alertaba `Customization token budget exceeded` (>23.600 tokens de personalización frente al límite de 20.000).
1. **Reglas duplicadas (15.441 tokens)**: Se cargaban dos archivos a la vez:
   - `/home/haytham/.gemini/GEMINI.md` (42 KB, 8.008 tokens): copia desactualizada previa al recorte del 11 de octubre.
   - `/home/haytham/.gemini/config/GEMINI.md` (22 KB, 7.433 tokens): contenía ~12 KB de estándares web/dashboards redundantes.
2. **Skills infladas (8.215 tokens)**: `~/.gemini/config/skills/` conservaba 192 enlaces simbólicos (111 rotos y 81 cargando metadatos completos).

## Qué se hizo
- Copia de seguridad en `~/.gemini/backups/2026-10-13-optimizacion/`.
- Eliminado `/home/haytham/.gemini/GEMINI.md` huérfano.
- Aligerado `~/.gemini/config/GEMINI.md` de 22,3 KB a 7,4 KB, alineado con `~/.claude/CLAUDE.md`.
- Purgados los enlaces rotos y configuradas exclusivamente las 29 skills del núcleo frecuente en `~/.gemini/config/skills/`.

