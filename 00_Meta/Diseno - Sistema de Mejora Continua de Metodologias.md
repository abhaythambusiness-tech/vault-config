---
type: diseno
status: borrador
date: '2026-10-28'
tags:
- metodologia
- mejora-continua
---

# Diseño: Sistema de mejora continua de metodologías

> [!resumen] En cristiano
> Hoy cada proyecto empieza de cero y Claude entrega "lo mínimo que funciona". Este sistema añade tres cosas: una **ficha de investigación** antes de construir (qué librerías, qué skills y qué webs de referencia usar), una **retro** de 10 líneas al cerrar (cuántos retoques tuviste que hacer tú y qué se aprendió) y una **subida de lecciones** a las plantillas cuando algo se repite. Así el siguiente proyecto arranca mejor que el anterior. Un hook impide dar un proyecto por hecho sin ficha ni retro.

## 1. Intención y por qué

Haytham dirige NeoZeler y hace cuatro tipos de proyecto: **web de cliente, micro-SaaS, SaaS y startup**, cada uno con su vía (`[[01 - Tipos de producto (Micro SaaS, SaaS, Startup)]]`).

Dolor concreto, dicho por él:
- Diseños "cutres", por ejemplo en los apuntes de Liyo antiguos.
- Claude no investiga librerías (ni en los archivos propios ni en internet).
- Entrega "lo mínimo para que funcione" y no exprime las skills ni las usa en todo momento.

**Éxito según Haytham**: el trabajo llega tan bien hecho que apenas retoca nada, con un diseño que parezca de web premium.

## 2. Objetivos, no-objetivos y anti-objetivos

**Objetivos**
- Cada proyecto, de cualquier vía, pasa por investigar antes de construir y por una retro al cerrar.
- Medir la mejora con un número simple: **retoques de Haytham tras la entrega** (debería bajar con el tiempo).
- Lo aprendido en un proyecto llega a las plantillas, no se queda en una nota suelta.

**No-objetivos**
- No reescribir los 6 documentos del flujo ni cambiar sus contenidos aprobados.
- No crear un MCP ni infraestructura nueva.
- No rehacer proyectos ya cerrados (el piloto es `los-apuntes-de-liyo`, ver §6).

**Anti-objetivos (fracaso aunque "funcione")**
- Burocracia: ficha de más de una página o retro de más de 10 líneas.
- Inundar a Haytham de preguntas: en la retro Claude solo le pregunta los retoques.
- Más texto en `CLAUDE.md` en vez de comprobaciones automáticas.

## 3. Lo que ya existe (no duplicar)

Flujo de 6 documentos (`[[00 - Flujo de Software]]`), nota de tres vías, `.claude/COMMON_MISTAKES.md` (451 líneas, errores por dominio), `~/.claude/rules/librerias.md` (154 líneas), `rules/identidad-y-dinamismo.md`, `rules/verificacion-web.md`, hooks en `~/.claude/hooks/` (`guard-web.py`, `format-web.py`, `guard-destructive.py`), skill `/nuevo-proyecto`, agente `archivista`. **Hueco**: nada devuelve lo aprendido a las plantillas ni mide si la entrega salió bien.

## 4. Diseño

### 4.1 Biblioteca de referencias premium
Nota `03_Resources/Biblioteca de Referencias Premium.md`, por tipo de proyecto. Semilla (Haytham vio las 8 y le gustan todas, con la pega de que algunas están saturadas de elementos): Linear, Stripe, Raycast, Vercel, Apple Mac, Framer, Arc, Resend. Regla de gusto fijada: **premium pero limpio; menos elementos, mejor ejecutados**. Cada proyecto elige 2-3 y se mide contra ellas. La biblioteca crece con referencias nuevas que Haytham apruebe.

### 4.2 Ficha de investigación (entrada, antes de construir)
Plantilla `Ficha de Investigacion.md` en `00_Meta/Plantillas/Proyecto Software/`. Máximo una página. Va en `01_Projects/<Nombre>/` y se rellena antes del primer código. Contenido:
1. **Librerías**: 2+ candidatas por necesidad, con motivo. Orden de búsqueda: `librerias.md` → notas del vault (`vault-search`) → `context7` → internet.
2. **Skills y agentes**: cuáles tocan según `rules/skills-frecuentes.md` y cuáles se usarán en qué fase.
3. **Referencias**: 2-3 de la biblioteca (§4.1) y qué se toma de cada una.
4. **Lecciones aplicables**: entradas relevantes de `COMMON_MISTAKES.md` y de retros anteriores de la misma vía.
5. **Extras por vía**: web de cliente (marca, imágenes), micro-SaaS (señal de demanda, checklist pre-cobro), SaaS (multi-equipo, RLS), startup (métricas, inversión).

### 4.3 Retro (salida, al cerrar)
Plantilla `Retro de Proyecto.md` → `01_Projects/<Nombre>/Retro.md`. Máximo 10 líneas. **Claude la rellena solo al cerrar** y pregunta a Haytham una única cosa: cuántos retoques hizo y cuáles. Campos: retoques (número y qué), nivel frente a las referencias (cumple/no cumple), skills previstas vs usadas, librerías nuevas o descartadas, lecciones (Síntoma → Causa → Regla).

### 4.4 Registro central
Nota `03_Resources/Registro de Retros.md` con una tabla Dataview (proyecto, vía, fecha, retoques) para ver la tendencia.

### 4.5 Subida a plantillas
Una lección que aparece en **2 retros** (o 3 veces en `COMMON_MISTAKES`, regla ya existente) se propone como regla de la plantilla del documento que corresponda (PRD, TRD, UI-UX, AppFlow, Schema, Plan). Cada 3 retros nuevas, el agente `archivista` genera la propuesta. **Haytham aprueba** antes de tocar cualquier plantilla (cambiar es destructivo, global §0.3). Las lecciones ya absorbidas se marcan, no se borran.

### 4.6 Cumplimiento automático
Hook nuevo en `~/.claude/hooks/` (estilo de `guard-web.py`): (a) no permite el primer `Edit`/`Write` de código en `~/Proyectos/<x>/` si no existe la ficha en `01_Projects/<Nombre>/`; (b) no permite un commit de cierre o release sin `Retro.md`. La skill `/nuevo-proyecto` crea la ficha y la retro al cerrar. Avisar en una línea cuando el hook bloquee, nunca saltarlo.

## 5. Restricciones
- Lenguaje sencillo y recuadro "En cristiano" en cada nota (global §1, CLAUDE.md del vault §0.11).
- Notas nuevas solo dentro de `00_Meta/` y `03_Resources/` (PARA no se reorganiza).
- Sin secretos en el repo del vault (hace auto-push).
- Todo cambio en `CLAUDE.md` o `rules/` se replica en `~/.gemini/config/GEMINI.md` y `00_Meta/GEMINI.md` en el mismo turno.
- Tras crear notas: `graphify update .` y registro de sesión en `00_Meta/Sesiones/`.

## 6. Piloto y criterio de éxito
- **Piloto**: aplicar ficha y retro a `los-apuntes-de-liyo` (donde Haytham vio los diseños cutres) como primera retro.
- **Éxito**: en los 3 siguientes proyectos cerrados, retoques ≤ 2 y ninguna entrega "mínima" (la ficha muestra librerías y skills elegidas con motivo).

## 7. Decisiones de Haytham
- Cubre desde el principio las 4 vías, cada una con sus extras.
- La retro la rellena Claude solo al cerrar; Haytham solo contesta los retoques.
- Referencias iniciales: las 8 webs vistas; gusto: premium y limpio, sin saturar.

## 8. Llamadas mías (Haytham, revísalas)
- Umbral de subida: 2 retros (a propósito más bajo que las 3 de `COMMON_MISTAKES`, porque las retros son pocas).
- Piloto en `los-apuntes-de-liyo`.
- **Qué es un retoque**: cada petición tuya, tras la entrega, de corregir algo de diseño, funcionalidad o fallo de lo entregado. Claude cuenta primero esas peticiones en la sesión y te da la cifra para que la confirmes o corrijas. Si no contestas, la retro queda `status: pendiente` y el hook no la da por cerrada. El campo `retoques` es numérico para que Dataview lo sume.
- **Cierre**: se marca con el paso «cerrar» de `/nuevo-proyecto` (cambia el `status` de la ficha del proyecto a `cerrado`). El hook solo bloquea ese cambio y los commits de etiqueta `release`/`cierre`, nunca los commits normales.
- **Qué proyectos cubre el hook (opt-in)**: solo los repos con un archivo marcador `.proyecto` en la raíz (con `nombre-vault:` y `tipo:`). Es también el mapeo entre `~/Proyectos/<x>/` y `01_Projects/<Nombre>/`. Bots, scripts y proyectos ya existentes quedan fuera hasta que les pongas marcador.
- **Qué bloquea (a)**: cualquier edición de código fuente (no `.md`, `.gitignore`, configuración ni `spec.md`) en un repo con marcador mientras falte la ficha; sin estado.
- **Orden**: la ficha va después del PRD y antes del TRD (las librerías se deciden en el TRD y las referencias alimentan el UI-UX).
- **Coincidencia de lecciones**: cada lección de la retro lleva dos campos, `dominio` y `documento-destino`, para que la coincidencia sea mecánica; `archivista` la confirma.
- **Cuándo revisa `archivista`**: al escribirse una retro, si el recuento de retros sin revisar (de la tabla Dataview) llega a 3.
- **Web de cliente (la llamada que más conviene que mires)**: usa la misma carpeta y un `tipo: web-cliente` con PRD, UI-UX y Plan (versión corta del flujo de 6) más la ficha y la retro. Si tus webs de cliente ya siguen otro flujo, dímelo y se ajusta.

## 9. Para el constructor
Decide: redacción exacta de las plantillas, contenido concreto de los extras por vía, consulta Dataview, implementación del hook siguiendo `guard-web.py`, y actualización de la skill `/nuevo-proyecto` (crear marcador, ficha y paso «cerrar»).

