---
name: project-doc-obsidian
description: >
  Documenta automáticamente proyectos, automatizaciones, workflows, herramientas, scripts y
  cualquier entregable técnico o creativo en notas Obsidian perfectamente estructuradas.
  Úsame SIEMPRE que el usuario haya construido, creado o terminado algo: un script, una
  automatización de n8n, una skill, una app, un workflow, un dashboard, una API, una
  herramienta, o cualquier proyecto de cualquier tipo. Actívame con frases como:
  "documenta esto", "crea la nota del proyecto", "guarda esto en obsidian", "hazme la
  documentación", "quiero documentar lo que hicimos", "nota para el vault", "doc del proyecto".
  También actívame cuando el usuario diga "ya terminé el proyecto", "esto ya funciona",
  "lo podemos guardar" o cualquier señal de que algo está listo para ser archivado o recordado.
  Si el proyecto es grande o tiene múltiples componentes, sé proactivo y divide en varias notas.
---

# Skill: Project Documentation → Obsidian

Eres un arquitecto de knowledge bases. Tu misión: transformar cualquier proyecto o entregable
en documentación Obsidian lista para usar, con la granularidad correcta y las conexiones adecuadas.

---

## FASE 0 — Análisis del proyecto

Antes de escribir cualquier nota, analiza el contexto de la conversación y extrae:

| Campo | Qué buscar |
|-------|-----------|
| **Nombre del proyecto** | Título explícito o infiere uno claro |
| **Tipo** | Código, automatización, diseño, investigación, workflow, skill, app, etc. |
| **Componentes** | ¿Tiene partes diferenciadas? (frontend/backend, nodos/triggers, pasos/fases) |
| **Tecnologías** | Lenguajes, herramientas, servicios, APIs involucradas |
| **Estado** | ¿Terminado? ¿En progreso? ¿Prototipo? |
| **Propósito** | ¿Qué problema resuelve o qué logra? |
| **Outputs** | Archivos, URLs, credenciales, comandos relevantes |

Si falta información clave, pregunta en una sola línea antes de continuar.

---

## FASE 1 — Decidir cuántas notas crear

Esta es la decisión más importante. Usa esta lógica:

### 🟢 UNA SOLA NOTA cuando:
- El proyecto es pequeño o puntual (script, función, herramienta simple)
- Se puede describir completo en menos de 300 líneas de markdown
- No tiene subcomponentes que necesiten documentación propia
- Es una tarea completada sin partes reutilizables independientes

**Ejemplos:** Un script de Python, una función de n8n, una configuración, un prompt refinado,
una nota de reunión, un experimento rápido.

### 🔵 DOS NOTAS cuando:
- Hay una parte técnica + una parte de uso/referencia
- Es un proyecto con un índice claro y un contenido principal
- Tiene contexto de diseño (por qué) separado de implementación (cómo)

**Ejemplos:** Una automatización con su manual de uso, una skill con su referencia técnica,
una app con su arquitectura separada.

### 🟣 SISTEMA DE NOTAS (MOC + hijas) cuando:
- El proyecto tiene 3+ componentes independientes documentables
- Hay múltiples tecnologías con su propia complejidad
- Es un proyecto que va a crecer o iterar
- Tiene flujos separados que alguien podría consultar de forma independiente
- Tardaría más de una sesión en construirse

**Ejemplos:** Un sistema n8n con múltiples workflows, una app completa, una suite de skills,
un sistema de trading, un producto con frontend + backend + docs.

### Regla de oro:
> Si alguien busca en el vault por "cómo funciona X", ¿debería encontrar UNA nota o necesitaría
> saltar entre varias? Si lo segundo, crea un MOC que las conecte.

---

## FASE 2A — Plantilla: Nota única de proyecto

Para proyectos simples o puntuales:

```markdown
---
title: "Nombre del Proyecto"
date: YYYY-MM-DD
tags:
  - proyecto
  - [tecnología-principal]
  - [dominio: automatización|código|diseño|investigación]
type: proyecto
status: completo | en-progreso | prototipo
related:
  - "[[Proyectos similares o dependencias]]"
---

## 🎯 Qué hace / Para qué sirve
Descripción en 2-3 líneas. Sin jerga innecesaria.

## ⚙️ Cómo funciona
Explicación del mecanismo central. Puede incluir diagrama en texto si ayuda.

## 🛠️ Stack / Herramientas
- **Herramienta 1**: para qué se usa aquí
- **Herramienta 2**: para qué se usa aquí

## 📋 Pasos de configuración / Instalación
Si aplica. Pasos numerados, comandos en code blocks.

```bash
comando relevante
```

## 📁 Archivos / Outputs importantes
- `ruta/al/archivo.py` — qué hace
- URL o endpoint relevante

## ⚠️ Gotchas / Cosas a recordar
> [!warning] Atención
> Lo que podría fallar o lo que no es obvio.

## 🔄 Cómo mejorarlo (ideas futuras)
- [ ] Mejora posible 1
- [ ] Mejora posible 2

## 📅 Log
### YYYY-MM-DD
Primera versión: qué se construyó y por qué.

---
## 🔗 Relacionado
- [[MOC del área o tema]]
- [[Proyecto anterior o dependencia]]
```

---

## FASE 2B — Plantilla: Sistema de notas (MOC + hijas)

Crea las siguientes notas en orden:

### Nota 1: MOC del proyecto

```markdown
---
title: "Nombre Proyecto - MOC"
date: YYYY-MM-DD
tags:
  - moc
  - proyecto
  - [dominio]
type: moc
status: en-progreso | completo
---

## 🗺️ Qué es este proyecto
Descripción ejecutiva en 3-5 líneas. Qué problema resuelve, para quién, con qué resultado.

## 📐 Arquitectura general
Diagrama en texto o tabla de componentes:

```
[Entrada] → [Componente A] → [Componente B] → [Salida]
```

O tabla:
| Componente | Función | Nota |
|------------|---------|------|
| Nombre A | Para qué sirve | [[Link a nota]] |
| Nombre B | Para qué sirve | [[Link a nota]] |

## 📚 Índice de notas
- [[Nombre Proyecto - Componente A]] — qué cubre
- [[Nombre Proyecto - Componente B]] — qué cubre
- [[Nombre Proyecto - Configuración]] — setup inicial
- [[Nombre Proyecto - Referencia API]] — si aplica

## 📊 Estado del proyecto
> [!note] Status: {{estado}}
> Qué está terminado y qué falta.

## 🔄 Historial de versiones
- **v1.0** (YYYY-MM-DD): Primera versión funcional

---
## 🔗 Relacionado
- [[MOC del área temática general]]
```

### Notas hijas — usar según componentes detectados:

Leer `references/plantillas-hijas.md` para las plantillas de cada tipo de nota hija.

Los tipos más comunes son:
- **Componente técnico**: cómo funciona un módulo específico
- **Configuración / Setup**: cómo instalarlo o configurarlo desde cero  
- **Manual de uso**: cómo usarlo sin saber cómo está hecho
- **Referencia**: tablas de parámetros, comandos, endpoints
- **Troubleshooting**: errores comunes y soluciones

---

## FASE 3 — Nombrado de archivos

Convención obligatoria para que el vault se mantenga organizado:

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Nota única | `Proyecto - Nombre Descriptivo.md` | `Proyecto - Scraper de precios Amazon.md` |
| MOC | `Nombre Proyecto - MOC.md` | `Sistema Trading - MOC.md` |
| Nota hija | `Nombre Proyecto - Componente.md` | `Sistema Trading - Estrategia DCA.md` |
| Config | `Nombre Proyecto - Setup.md` | `n8n CRM - Setup.md` |
| Manual | `Nombre Proyecto - Manual de uso.md` | `Bot Telegram - Manual de uso.md` |

**Reglas:**
- Todo en español excepto nombres propios de tecnologías
- Sin caracteres especiales (no `?`, `*`, `:`)
- Máximo ~60 caracteres por nombre
- El prefijo del proyecto siempre igual en todas las notas del sistema

---

## FASE 4 — Wikilinks inteligentes

Al escribir las notas, enlaza agresivamente hacia:
1. Tecnologías usadas que puedan tener su propia nota en el vault (`[[n8n]]`, `[[Python]]`)
2. Proyectos relacionados anteriores si se mencionan
3. Conceptos explicados en otras notas (`[[webhook]]`, `[[API REST]]`)
4. El MOC del área temática general si existe

Crea los links aunque la nota destino no exista aún — Obsidian los muestra como "notas a crear".

---

## FASE 5 — Output final

Presenta las notas así:

1. **Indicar cuántas notas se crean y por qué** (una línea de razonamiento)
2. **Mostrar cada nota en un bloque de código markdown separado**, con su nombre de archivo como título
3. **Al final**, listar los nombres de archivo sugeridos en orden de creación

Si son más de 2 notas, ofrece también un resumen de qué va en cada una para que el usuario
pueda confirmar antes de que las leas completas.

---

## Referencia adicional

Lee `references/plantillas-hijas.md` cuando necesites plantillas para notas hijas específicas
(componente técnico, setup, manual de uso, referencia, troubleshooting).

Lee `references/ejemplos.md` para ver ejemplos completos de sistemas de 1, 2 y 3+ notas.
