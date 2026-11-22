---
type: sesion
date: '2026-10-06'
proyecto: '[[CLAUDE]]'
tags:
- sesion
- mcp
- diseno
- shadcn
origen: mixto
---


# Sesión — 2026-10-06: MCP de shadcn y demo RETO 30

> [!abstract] Resumen
> Se comprobó qué librerías de componentes animados tienen MCP, se instaló el MCP oficial de shadcn y se construyó la demo web de RETO 30 (Factory Training) con Componentry, Space UI, Skiper UI y Arc UI.

## Contexto
Haytham pegó cinco librerías de UI y pidió añadirlas al `CLAUDE.md` tras comprobar cuáles tienen MCP. Después pidió una demo web a partir de `RETO 30.pdf` y `RETO 30 Detallado.pdf`. Código en `~/Proyectos/reto-30` (fuera del vault, §6).

## Qué se hizo
- Búsqueda en el registro MCP y en la web: ninguna librería tiene MCP propio; las cuatro se sirven por registries shadcn.
- Instalado el MCP oficial `shadcn-registries` a nivel usuario, con el Node 22 de fnm.
- Documentado en `CLAUDE.md` §4.1.3 (librerías, trampas de integración).
- Demo creada: Next.js 16 + shadcn + spec-kit, 5 rutas, 30 retos en 3 niveles, estado en `localStorage`. Build y lint limpios, probada en escritorio y 375 px.

## Decisiones tomadas
- Dirección visual "ficha de producción" (papel, tinta, naranja de seguridad) en vez del gym oscuro por defecto.
- Un solo motor de animación (Motion). Vídeos de reto como campo opcional, sin huecos visibles.

## Aprendizajes (para futuras sesiones)
- "Arc UI" es el registry `@uiarc`; `@arc` (witharc.co) da 404. "Skecher UI" era Skiper UI. "Planes" sigue sin identificar.
- El Node del sistema es 18 y rompe shadcn (`File is not defined`): usar `~/.local/share/fnm/node-versions/v22.23.3`.
- Los tokens de Arc chocan con los de shadcn: aislar en `.arc-scope`; su `outline: none !important` global se elimina.
- Space UI necesita `@plugin "@usespaceui/squircle"` y un provider; instalar sus ítems de uno en uno.
- El hook `config-protection` bloquea editar `eslint.config.mjs`: usar `eslint-disable` puntual en código vendorizado.
- GateGuard deniega la primera escritura de cada archivo nuevo: declarar y reintentar.
- `npm audit`: 7 vulnerabilidades altas, todas en dependencias del CLI `shadcn` (braces/micromatch), no en código propio.

## Próximos pasos
- Confirmar qué es "Planes".
- Añadir los vídeos reales de cada reto (campo `video`) y decidir la recompensa concreta con Factory Training.
- Si se lleva a producción: dominio, `robots.txt`, `sitemap.xml` y backend para inscripciones y pagos.

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]

