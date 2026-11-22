---
type: guia
status: activo
date: 2026-10-14
origen: humano
---

# Flujo de creación de software (6 documentos)

> [!resumen]
> Todo proyecto de software nuevo empieza creando su carpeta `01_Projects/<Nombre>/` con estos seis documentos **en este orden**. No se pasa al siguiente sin que el anterior esté aprobado por Haytham (`status: aprobado`). El código no se escribe hasta tener el 6.

| # | Documento | Responde a | Plantilla |
|---|---|---|---|
| 1 | PRD | ¿Qué problema, para quién, qué es éxito? | [[1 - PRD]] |
| 2 | TRD | ¿Con qué tecnología y por qué? | [[2 - TRD]] |
| 3 | UI/UX Design | ¿Cómo se ve y se siente? | [[3 - UI-UX Design]] |
| 4 | AppFlow | ¿Cómo navega el usuario y qué pasa en cada paso? | [[4 - AppFlow]] |
| 5 | Backend Schema | ¿Qué datos y qué API lo sostienen? | [[5 - Backend Schema]] |
| 6 | Plan de Implementación | ¿En qué orden se construye y cómo se verifica? | [[6 - Plan de Implementacion]] |

## Paso 0: validar antes de construir (2026-10-28)
**Antes, elegir la vía:** micro SaaS, SaaS o startup, según [[01 - Tipos de producto (Micro SaaS, SaaS, Startup)]]. Cada vía cambia cuánta validación, cuántos documentos y qué seguridad se exigen.

Programar es lo barato; que alguien pague es lo difícil. **Antes del PRD** de un producto propio (micro SaaS, startup, web a medida sin cliente firmado) hace falta al menos una señal de demanda real, anotada en el PRD §1:
- 5-10 entrevistas sobre el problema (qué hacen hoy, cuánto les cuesta); cuenta la conducta, no los elogios.
- Un canal de distribución identificado (SEO, comunidad, cliente de NeoZeler), no «ya lo encontrarán».
- Una prueba de pago: preventa, piloto de pago o depósito. Una lista de espera sola no vale.
Sin esa señal, el proyecto queda en `status: idea` y no se pasa al PRD. Con cliente ya firmado (metodología de 3 reuniones) el paso se da por cumplido. Agente `project-idea-validator` para pasar la idea por el aburrimiento brutal. Fuente: [[Claude Code para micro SaaS y startups]]; antes de cobrar, [[Checklist pre-cobro (micro SaaS)]].

## Cómo arrancar un proyecto nuevo
1. (Solo producto propio) Paso 0 superado. Crear `01_Projects/<Nombre>/` y copiar las 6 plantillas (sin el `00`).
2. Rellenar y cerrar cada documento en orden; cada uno enlaza al anterior y al siguiente.
3. Con el 6 aprobado: `~/Proyectos/<nombre>/` con `git init` + `.gitignore`, `specify` (spec-kit) a partir del PRD y construir fase a fase.
4. Ficha `01_Projects/<Nombre>.md`, README, sesión y `resumen.html` en la raíz del repo (CLAUDE.md §0.8).

## Orquestación y herramientas
- **Skill `/nuevo-proyecto`**: recorre los 6 pasos con aprobación entre cada uno.
- **Búsqueda de librerías**: ficha verificada y presupuesto de dependencias en el TRD (§1.1, §1.2).
- **Componentes y colocación**: [[Catalogo de Componentes]], [[Biblioteca de Layouts]] y tabla de slots en el UI/UX (§4).
- **Reutilización**: [[Starter Kits NeoZeler]] (inventario de candidatos).
- **Control**: [[Dashboard - Proyectos de Software]] (Dataview) y, en `~/Proyectos/flujo-software/tools/`, `trace_lint.py` (historias huérfanas) y `schema_to_migration.py` (migración + auditoría de `ON DELETE`).
- **Calidad temprana**: demo provocadora en el PRD, cliente simulado en el AppFlow, tokens antes que pantallas.
- **Identidad y personalidad (2026-10-26)**: el PRD §11 recoge el carácter de marca; el UI/UX §2, §5 y §7 es la identidad del proyecto (idea visual central, dinamismo, flujo de imágenes: si falta una imagen se pregunta a Haytham). Regla: `~/.claude/rules/identidad-y-dinamismo.md`; plantilla suelta [[Plantilla - Identidad de Proyecto]]; registro [[Registro de Identidades Visuales]].

## Paralelización de agentes (2026-11-03)

> [!resumen] En cristiano
> Lanzar varios agentes a la vez para ir más rápido cuesta unas 7 veces más tokens que uno solo. Compensa solo en tres puntos del flujo donde el trabajo no depende entre sí; en el resto (los 6 documentos) rompe las aprobaciones de Haytham y sale más caro por el retrabajo que por los tokens.

No se construye un agente orquestador nuevo: el `Agent` del harness (con `subagent_type` y `model: haiku`/`sonnet`, o un fork que hereda contexto) ya cubre el patrón de "varios agentes en paralelo con modelo barato". Antes de crear uno, comprobar que no lo cubre ya `investigador`, `archivista`, `revisor-codigo` o `auditor-web` (regla de no duplicar).

**Dónde sí paralelizar:**
- **Paso 0 (validación)**: competencia, tendencia (`last30days`) y señal de demanda en forks con `model: haiku` — o, si basta un solo pase, el agente `investigador` ya lo cubre sin paralelismo.
- **Identidad visual durante los docs 3-6**: buscar referencias (mobbin/hallmark) en paralelo desde que arranca el doc 3 no depende del contenido del TRD; es el hueco de paralelismo más barato del flujo.
- **Fase Build**: tras cada fase del Plan de Implementación, lanzar a la vez `revisor-codigo`, `auditor-web` y revisión de seguridad — son lecturas independientes, no se pisan. Aplica igual a **auditar una web/contenido ya hecho fuera de este flujo** (cualquier proyecto, no solo software nuevo).
- **Cierre**: ya lo hace `archivista` (ficha, retro, MOC, `graphify update`) sin agente nuevo — también **genérico para cerrar cualquier proyecto**, no solo uno de software.

**Dónde no paralelizar:** los documentos 1→6. La aprobación secuencial de Haytham (§0.10 del `CLAUDE.md` del vault) es una barrera dura; procesarlos a la vez genera inconsistencias si un documento anterior cambia tras revisión, y el coste de corregirlas supera el tiempo ahorrado.

**Más rentable que paralelizar**: agrupar peticiones relacionadas en un solo mensaje, consultar `vault-search`/`graphify` antes de lanzar research nuevo, y reservar equipos de agentes para tareas voluminosas y autocontenidas, no por defecto (`~/.claude/rules/tokens.md`).

**Tarea repetible → script (CLAUDE.md §0.12)**: durante el Build, si una tarea manual se repite 3 veces o más (scaffolding, migración, lint de trazabilidad, exportar un informe), convertirla en script en `~/Proyectos/<nombre>/scripts/` en vez de rehacerla a mano o con un agente cada vez; si es transversal a varios proyectos, va a `~/Proyectos/flujo-software/tools/` junto a `trace_lint.py`/`schema_to_migration.py`. Documentar el script en el README.

## Reglas
- **Trazabilidad**: cada pantalla cita su historia (US), cada tabla su flujo, cada tarea su fase.
- **Metodología de 3 reuniones**: el PRD sale de la reunión 1 (demo provocadora); las reglas de negocio exactas de la reunión 2 entran en el PRD y en el Backend Schema §6.
- **Proyectos pequeños** (script o automatización de un día): PRD y Plan bastan; el resto se marca `status: no-aplica` con una línea de motivo.
- Los placeholders `<% %>` son de Templater; si se copian a mano, rellenar `proyecto` y `date`.
