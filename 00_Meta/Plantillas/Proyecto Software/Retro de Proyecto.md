---
type: retro
proyecto: "<% tp.file.folder() %>"
tipo: <web-cliente | micro-saas | saas | startup>
status: pendiente
retoques:
revisada: false
date: <% tp.date.now("YYYY-MM-DD") %>
origen: humano
---

> [!resumen] En cristiano
> La retro es el "qué aprendimos" al cerrar un proyecto: cuántas veces hubo que corregir lo entregado, cómo quedó frente a las referencias y qué reglas nuevas salen.
> Máximo 10 líneas de contenido. Claude la rellena, pero no la da por completa hasta que Haytham confirma la cifra de retoques.
> Las lecciones repetidas en dos proyectos suben a las plantillas, con permiso de Haytham.

# Retro de Proyecto

## Retoques
Cada petición de Haytham, tras la entrega, de corregir diseño, funcionalidad o un fallo de lo entregado. Claude cuenta las peticiones en la sesión, escribe la cifra en `retoques:` y la confirma con Haytham antes de poner `status: completa`.

- Cifra y qué se corrigió:

## Nivel frente a referencias
Cómo quedó el resultado comparado con las referencias de la ficha (cumple / no cumple en cada una, y en qué).

- 

## Skills previstas vs usadas
Lo que la ficha preveía frente a lo que se usó de verdad, y qué faltó o sobró.

- 

## Librerías
Elegidas en la ficha frente a las que acabaron en el proyecto; trampas encontradas (apuntarlas también en `librerias.md`).

- 

## Medición tras publicar
Cierra el ciclo: medir con usuarios reales y volver al diseño. Rellenar a las 2-4 semanas de publicar; hasta entonces, `pendiente`.
- **Qué se mide** (KPI del PRD §3 + tasa de rebote, tiempo medio en página, conversión por paso del embudo TOFU → MOFU → BOFU):
- **Mapas de calor y sesiones** (clics, scroll, grabaciones; herramienta usada o `no medido`): dónde se clica y dónde se pierden.
- **Prueba A/B** (qué dos versiones, qué métrica, resultado y fuente):
- **Prueba de usuario** (≥5 personas reales, qué falló):
- **Qué hallazgo vuelve al diseño** (pantalla o texto que se rehace y a qué documento destino sube):

## Lecciones
Una fila por lección. `documento-destino` ∈ `PRD | TRD | UI-UX | AppFlow | Schema | Plan`.
`dominio` ∈ `diseno | librerias | skills | datos | seguridad | despliegue | producto | proceso`.

| Síntoma | Causa | Regla | dominio | documento-destino |
|---|---|---|---|---|
|  |  |  |  |  |
