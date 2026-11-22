---
type: referencia
status: activo
date: '2026-10-22'
proyecto: Laya Trader
tags:
- laya-trader
- skills
- configuracion
origen: mixto
---

# Guía — Skills y reglas por fase (Laya Trader)

> [!resumen] En cristiano
> Qué herramientas se usaron de verdad en cada fase del [[6 - Plan de Implementacion|Plan]] y cuáles quedan pendientes. **No cambia ningún documento aprobado.** Modelo: la guía de Reto 30. Aquí los seis documentos están en esta misma carpeta (no en `Software/`).

## 1. Reglas globales que ya cubre el plan
| Regla | Dónde se cumple |
|---|---|
| Cero placeholders, código completo y tipado | `mypy --strict` y `ruff` limpios en `src`, `tests` y `scripts` (T-00 a T-19) |
| Persistir en BD, sin memoria volátil | SQLite WAL + `calibration.jsonl` + copias diarias (T-01, T-19) |
| Borrado en cascada y ciclo completo | `tests/test_schema.py` (cascada, `restrict`, `set null`); ciclo equivalente de solo lectura en producción: reinicio y corte de 30 s (T-19) |
| Imágenes contextuales en vistas clave | **Pendiente**: prompts en UI/UX §5 sin generar (el panel usa estados vacíos con icono) |
| Sandbox-first, git desde el primer commit | Repo local en el servidor desde T-00; medición de Laya antes de construir (T-02) |
| Node 22 de fnm | No aplica: el servidor no tiene Node; librerías de interfaz descargadas y verificadas con `scripts/vendorizar.py` |
| Verificación visual: Chrome DevTools bloqueado | Navegador integrado de Claude en 375 y 1200 px, claro y oscuro (T-12 a T-18) |
| Lenguaje sencillo | Glosario único (AppFlow §4.1), ayuda por pantalla y diccionario de etiquetas (UI/UX §4.2) |

## 2. Skill o herramienta por fase (lo realmente usado)
| Fase | Herramienta | Uso concreto |
|---|---|---|
| Arranque | `nuevo-proyecto` | Flujo de 6 documentos, `trace_lint.py` en OK |
| Diseño (UI/UX) | `ui-ux-pro-max` (estilo, tipografía, color), `dataviz` (paleta de series validada con su script, colorblindez y contraste) | Se descartó el «SaaS oscuro navy + verde» que devolvía la búsqueda; IBM Plex y azul/naranja con trazo distinto |
| Librerías | `context7` (lightweight-charts v5, websockets), npm y PyPI | Versiones y licencias verificadas el 2026-10-22; anotado en `~/.claude/rules/librerias.md` |
| Datos | SQLite con pruebas de restricciones | `schema_to_migration.py` no aplica (es para Postgres/Supabase) |
| Núcleo | Agente `general-purpose` como cliente simulado | 14 hallazgos en el AppFlow, aplicados |
| Panel | Navegador integrado (`mcp__Claude_Browser__*`) | Comprobación de desbordes, objetivos táctiles, contraste y clics reales |
| Despliegue | `zorin-ssh` | Servidor tratado como equipo dedicado; sin tocar `sshd` ni red |

## 3. Pendientes recomendados antes del veredicto
| Skill | Para qué | Cuándo |
|---|---|---|
| `ponytail-audit` | Auditoría del repo (código muerto, qué sobra) | Antes del 2026-10-29 |
| `ponytail-review` | Revisión del último cambio | Si se toca código durante la prueba |
| `impeccable audit` / `critique` | Segunda opinión sobre el panel ya construido | Opcional, antes de enseñarlo |
| `humanizer` | Solo textos largos de documentación; **no** el panel (ya escrito en lenguaje llano) | Si se publica la ficha |
| `diagram-design` | Diagramas de la ficha si el Mermaid se queda corto | Opcional |
No se usaron `hallmark`, `impeccable`, `bklit-ui` ni `ponytail*` durante la construcción; los gráficos son de `lightweight-charts` y las curvas de calibración e histogramas son SVG propio.

## 4. Conflictos y decisiones de solape
- **Gráficos**: `bklit-ui` exige React y el servidor no tiene Node; se eligió `lightweight-charts` (TRD §1).
- **Marca**: los tokens del UI/UX §2.1 mandan sobre cualquier skill de diseño.
- **Reglas congeladas**: ninguna skill puede proponer cambiar las reglas del Backend Schema §6 una vez medido; cambiarlas abre un experimento nuevo.

## 5. Antes de cada commit
`pytest -q`, `ruff check src tests scripts`, `mypy src tests scripts` limpios → para cambios de panel, comprobar a 375 px y en claro y oscuro con el navegador integrado → `grep -i "<dominio>" .claude/COMMON_MISTAKES.md`.

---
Plan: [[6 - Plan de Implementacion]] · Ficha: [[01_Projects/Laya Trader]]

