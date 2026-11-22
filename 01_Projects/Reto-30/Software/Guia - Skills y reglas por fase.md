---
type: referencia
status: activo
date: '2026-10-16'
proyecto: Reto 30 (app real)
tags:
- reto-30
- skills
- configuracion
origen: mixto
---

# Guía — Skills y reglas por fase (Reto 30)

> [!resumen]
> Cómo se aplican al [[6 - Plan de Implementacion|Plan]] la configuración global y las skills instaladas el 2026-10-16. **No cambia ningún documento aprobado**: solo dice qué herramienta usar en cada fase. Reto 30 es de **Haytham y Pedro**, no de NeoZeler (ver `.claude/COMMON_MISTAKES.md`). Invocar la skill **antes** de escribir código de esa parte.

## 1. Reglas globales que ya cubre el plan
| Regla | Dónde se cumple |
|---|---|
| Cero placeholders, código completo y tipado | T-10 (sin `any`), T-29, §6 Definición de terminado. `ponytail` **no la relaja** |
| Persistir en BD, sin memoria volátil | TRD §5, T-15 |
| Borrado en cascada y ciclo completo (crear → refrescar → borrar → refrescar) | T-07 (avisos de FK), T-35 |
| Imágenes contextuales en vistas clave | T-22 (prompts del UI/UX §5) |
| Sandbox-first, git desde el primer commit | T-01, T-09 |
| Node 22 de fnm, `create-next-app` sin `git init` | T-01 (`librerias.md`, Entorno) |
| Verificación visual: Chrome DevTools bloqueado | T-29 con el navegador integrado; declarar si no hay |

## 2. Skill por fase
| Fase | Skill / herramienta | Uso concreto |
|---|---|---|
| 0 Preparación | `ponytail` (lite) | Vigilar el presupuesto del TRD §1.2 (16 dependencias directas, 1 motor de animación, 1 librería de iconos) |
| 0 · T-03 tokens | `hallmark` (`study` sobre el logo y la marca) | Variar la **estructura** de página sin tocar los tokens fijos: negro `#0C0D0E`, lima `#CCFF00`, Barlow, sin squircle |
| 1 Datos | `supabase` y `supabase-postgres-best-practices` (instaladas 2026-10-16), MCP `supabase` (`list_tables`, `get_advisors`) | Comprobar el esquema real antes de asumir tablas; asesor de seguridad tras T-07 y T-33. Trampas PGlite en `librerias.md` |
| 2 Acceso y reglas | `context7` (si conecta) o documentación oficial | OTP y `@supabase/ssr` (T-11, T-12). `@supabase/auth-helpers-nextjs` está deprecado |
| 3 Pantallas | `hallmark` (pantallas nuevas), `impeccable shape` (plan UX), `web-animation-skills:accessible-animation` | Portada, panel y felicitación sin aspecto genérico; `prefers-reduced-motion` (T-05, T-20) |
| 3 · T-22 imágenes | `Bloom` (imagen sin texto), `Canva` si lleva texto | Hero, estados vacíos, insignias; prompts ya definidos en UI/UX §5 |
| 4 Admin y gerencia | `bklit-ui` (si hay gráficas en `/gerencia`) | Solo si se añade un gráfico; la cifra "N de M" no lo necesita |
| 4 · cada bloque | `ponytail-review` | Revisar el cambio antes de commit |
| 5 Pulido | `impeccable critique`, `audit`, `polish`, `harden` | Contraste, 375 px, foco, estados de error (T-29) |
| 5 · T-28 copy | `humanizer` | Solo en textos de interfaz y explicativos. **No** en las cláusulas legales (T-32, T-40) |
| 5 · T-31 | `vercel-react-best-practices` (instalada 2026-10-16) | Presupuesto de 200 kB |
| 6 Despliegue | `ponytail-audit` | Auditoría del repo antes de abrir la cohorte |
| Documentación | `diagram-design` | Diagramas de la ficha y del README si el Mermaid se queda corto |

## 3. Conflictos y decisiones de solape
- **Diseño**: `hallmark` para pantallas nuevas, `impeccable` para lo ya construido. El gate de `rules/diseno.md` manda y estas skills ejecutan.
- **Marca fija**: si `hallmark` o `impeccable` proponen cambiar paleta o tipografía, gana el [[3 - UI-UX Design]].
- **Legal**: lo redactado por IA sobre aviso legal, privacidad y sorteo sigue pendiente de revisión humana (D5, D7).
- **Skills de Supabase y Vercel React**: instaladas el 2026-10-16 y revisadas (sin `curl | sh` ni comandos destructivos); activas en sesión nueva.

## 4. Antes de cada commit
Build, `tsc --noEmit`, `vitest run` y lint limpios → checklist técnico (`stack-web.md`) → checklist de marca (UI/UX §8). Consulta previa: `grep -i "<dominio>" .claude/COMMON_MISTAKES.md`.

---
Plan: [[6 - Plan de Implementacion]] · Ficha: [[Reto 30 - App real]]
