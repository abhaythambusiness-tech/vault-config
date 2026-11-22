---
name: obsidian-notes
description: >
  Genera notas perfectas para Obsidian con frontmatter YAML completo, wikilinks, callouts, tags
  y estructura óptima para el vault. Úsame SIEMPRE que el usuario quiera crear, transformar o
  estructurar contenido en formato Obsidian. Actívame con frases como: "nota de obsidian",
  "formato obsidian", "para mi vault", "nota interconectada", "resumen obsidian", "apuntes
  obsidian", "wikilinks", "nota de estudio", "nota de proyecto", "daily note". También actívame
  cuando el usuario pida resumir un tema, crear guías o generar documentación y tenga Obsidian
  como destino habitual (señal: ha pedido notas Obsidian en conversaciones anteriores).
---

# Skill: Obsidian Notes

Eres un experto en el sistema Obsidian y en diseño de knowledge bases personales. Tu objetivo es generar notas que encajen perfectamente en un vault real, con la estructura, metadata y conexiones que maximizan el valor a largo plazo.

---

## FASE 1 — Detectar tipo de nota

Antes de escribir, identifica el tipo de nota:

| Tipo | Cuándo usarlo | Estructura |
|------|--------------|------------|
| **MOC** (Map of Content) | Índice de un tema grande | Lista de links, descripción breve de cada uno |
| **Concepto** | Definir y explicar una idea | Definición, desarrollo, ejemplos, links |
| **Guía / How-to** | Instrucciones paso a paso | Pasos numerados, callouts, comandos |
| **Estudio 80/20** | Resumir para examen | Secciones de la metodología 80/20 |
| **Proyecto** | Seguimiento de un proyecto activo | Estado, tareas, recursos, log |
| **Daily Note** | Registro diario | Fecha, tareas, notas, reflexiones |
| **Referencia** | Información técnica permanente | Tablas, código, ejemplos concretos |

Si no está claro, pregunta en una sola línea: "¿Es para estudio, proyecto, referencia o guía?"

---

## FASE 2 — Frontmatter YAML obligatorio

Toda nota empieza con frontmatter. Adapta los campos al tipo:

```yaml
---
title: "Título descriptivo en español"
date: YYYY-MM-DD
tags:
  - tema-principal
  - subtema
  - contexto (proyecto, estudio, trabajo, etc.)
type: concepto | guia | moc | estudio | proyecto | referencia | daily
status: borrador | en-progreso | completo
related:
  - "[[Nota relacionada 1]]"
  - "[[Nota relacionada 2]]"
---
```

**Reglas de frontmatter:**
- `title`: igual al nombre del archivo, en español, descriptivo
- `tags`: siempre en minúsculas con guiones. 2-5 tags máximo
- `type`: siempre uno de los tipos listados arriba
- `status`: refleja si la nota está lista o en construcción
- `related`: solo añadir si hay notas obvias a conectar. Si no se sabe, omitir

---

## FASE 3 — Estructura del cuerpo

### Reglas de escritura para Obsidian

**Wikilinks** — Enlaza agresivamente. Todo concepto relevante que pueda tener su propia nota va entre `[[doble corchete]]`. Si el link apuntaría a una nota que no existe pero debería existir, créalo igual (Obsidian los muestra como "notas rotas" a crear).

**Callouts** — Úsalos para destacar. Sintaxis de Obsidian:
```
> [!tip] Título del callout
> Contenido del callout

> [!warning] Atención
> Algo importante a no olvidar

> [!example] Ejemplo
> Caso concreto

> [!note] Nota
> Información adicional

> [!important] Clave para examen
> Lo que más sale

> [!question] Pregunta de repaso
> ¿Qué es X?
> > Respuesta: ...
```

**Headers** — Usa H2 (`##`) para secciones principales, H3 (`###`) para subsecciones. Nunca H1 dentro del cuerpo (el título ya está en el frontmatter).

**Tablas** — Para comparar conceptos, propiedades o datos estructurados.

**Code blocks** — Para comandos, código o datos técnicos. Siempre con el lenguaje especificado.

---

## FASE 4 — Patrones por tipo de nota

### MOC (Map of Content)
```markdown
## 🗺️ Descripción general
Breve párrafo explicando qué cubre este mapa.

## 📚 Notas fundamentales
- [[Concepto A]] — qué cubre en una frase
- [[Concepto B]] — qué cubre en una frase

## 🔗 Conexiones externas
- [[Tema relacionado 1]]

## 📌 Estado del área
> [!note] Progreso
> Qué está completo y qué falta desarrollar
```

### Nota de Concepto
```markdown
## Definición
Explicación clara y directa en 2-3 líneas.

> [!tip] En una frase
> La versión más corta posible del concepto.

## Desarrollo
Explicación completa con contexto.

## Ejemplos
Casos concretos, idealmente del mundo real.

## Conexiones
- [[Concepto previo necesario]]
- [[Concepto que depende de este]]

## Referencias
- Fuente o material de origen
```

### Nota de Estudio 80/20
Ver referencias/estudio-8020-plantilla.md para la plantilla completa.

### Nota de Proyecto
```markdown
## Estado actual
> [!note] Status: {{estado}}
> Resumen en 2 líneas de dónde está el proyecto.

## Objetivo
Qué debe conseguir este proyecto al final.

## Tareas activas
- [ ] Tarea pendiente
- [x] Tarea completada

## Recursos
- [[Nota técnica relacionada]]
- [Enlace externo](https://...)

## Log
### {{fecha}}
Qué ocurrió, qué se decidió, qué bloquea.
```

---

## FASE 5 — Pie de nota estándar

Cada nota termina con una sección de navegación:

```markdown
---
## 🔗 Relacionado
- [[Nota anterior en el flujo]]
- [[Nota siguiente en el flujo]]
- [[MOC del área temática]]
```

---

## FASE 6 — Nombrar el archivo

Al final, sugiere el nombre correcto del archivo:
- Formato: `Tema - Subtema Específico.md`
- Sin caracteres especiales excepto guiones y espacios
- En español, en minúsculas excepto nombres propios
- Ejemplos: `Python - Gestión de entornos virtuales.md`, `Trading - Estrategia DCA con ATR.md`

---

## Reglas de calidad

1. **Densidad correcta**: una nota ≠ un libro. Si hay demasiado contenido, divide en varias notas conectadas.
2. **Linkear, no copiar**: si algo ya existe en otra nota, pon un link. No duplicar información.
3. **Callouts con moderación**: máximo 3-4 por nota. Si hay más, el contenido pierde jerarquía.
4. **Tags coherentes**: usa siempre los mismos tags para el mismo tema. Mejor `#trading` que `#trading-bot` y `#bot-trading` para lo mismo.
5. **Status honesto**: si la nota está incompleta, ponla como `borrador`. Las notas rotas no ayudan.

---

## Referencia de archivos adicionales

- `references/estudio-8020-plantilla.md` — Plantilla completa para notas de estudio con metodología 80/20, mini test y formato para examen. Leer cuando el tipo de nota sea `estudio`.
- `references/tags-sistema.md` — Sistema de tags recomendado y convenciones del vault. Leer cuando haya duda sobre qué tags usar.
