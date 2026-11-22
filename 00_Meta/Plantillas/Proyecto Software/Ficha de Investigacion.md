---
type: ficha-investigacion
proyecto: "<% tp.file.folder() %>"
tipo: <web-cliente | micro-saas | saas | startup>
status: borrador
date: <% tp.date.now("YYYY-MM-DD") %>
origen: humano
---

> [!resumen] En cristiano
> Esta ficha es la "tarea previa" de un proyecto: antes de escribir el TRD, apuntamos qué piezas ya hechas (librerías) vamos a usar, qué herramientas de Claude nos ayudan y con qué nos vamos a comparar.
> Así no reinventamos la rueda ni elegimos a ciegas. Se rellena después del PRD y antes del TRD, y debe caber en una página.
> Cuando Haytham la aprueba, `status` pasa de `borrador` a `aprobada`.

# Ficha de Investigación

## Librerías
Una fila por necesidad. Orden de búsqueda: `librerias.md` (`grep -i`) → `vault-search` → context7 → internet. Anota solo la elegida y por qué.

| Necesidad | Candidata A | Candidata B | Elegida y motivo | Fuente |
|---|---|---|---|---|
|  |  |  |  |  |

## Skills y agentes
Qué skills, agentes y MCP se usarán en cada fase de este proyecto (consultar `skills-frecuentes.md` y `agentes-frecuentes.md`; no inventar nombres).

- Fase → herramienta:

## Referencias
Dos o tres proyectos o webs de nivel alto con los que compararemos el resultado al final (enlace y qué los hace buenos). Fuente de ideas: [[Biblioteca de Referencias Premium]].

- 

## Lecciones aplicables
Reglas de retros anteriores o de `.claude/COMMON_MISTAKES.md` que valen para este proyecto (`grep -i` por dominio). Una línea cada una.

- 

## Extras de la vía
Borra los tres subapartados que no apliquen a este proyecto.

### web-cliente
Marca del cliente (logo, colores, tipografía) y estado de las imágenes: ¿hay fotos reales, hace falta prompt de Gemini o SVG? Si falta una, parar y preguntar.

- 

### micro-saas
Señal de demanda antes de construir (entrevistas, canal, prueba de pago) y revisión de [[Checklist pre-cobro (micro SaaS)]] antes de cobrar.

- 

### saas
Multi-equipo (varios clientes en una misma base de datos) y reglas de acceso por fila (RLS) desde el diseño del esquema.

- 

### startup
Métricas que importan (crecimiento, retención, coste de captar un cliente) y plan de inversión o financiación.

- 
