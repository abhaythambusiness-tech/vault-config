---
type: doc-software
doc: prd
proyecto: ComandAi
status: aprobado
tipo: micro-saas
date: '2026-11-03'
origen: mixto
---

# 1 · PRD — ComandAi

> [!resumen] En cristiano
> Un panel web privado, con portadas grandes por sección, que muestra lo que tu IA ha hecho y encontrado: tareas, noticias de IA, herramientas nuevas, leads y proyectos. Corre en el servidor Zorin y lo abres desde el móvil con Tailscale (una red privada solo tuya). Las carpetas se dividen en `humano/` (lo que dices tú) y `maquina/` (lo que genera la IA y los scripts). Los scripts Python traen datos sin gastar IA; la IA solo los clasifica.
> Referencia: panel del vídeo de Nico CMW (`https://www.youtube.com/watch?v=XwEbK3JX5mc`, min 03:56 y 08:22).

## 1. Problema
- Hoy la información de NeoZeler (tareas, leads, noticias, proyectos) está repartida entre notas, el CRM, Laya Leads y el chat. Para saber "qué hay pendiente" hay que preguntar a la IA cada vez.
- No se distingue lo que dijo Haytham de lo que resumió la IA.
- Fuera del PC (móvil) no hay forma cómoda de ver nada.
- `tipo: micro-saas` (uso interno NeoZeler, propietario: Haytham). Sin cobro, sin multiusuario en v1.

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia |
|---|---|---|---|
| Dueño | Haytham | Ver y editar tareas, leer novedades de IA, revisar leads y proyectos desde PC y móvil | Diaria |

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Meta |
|---|---|---|
| Ver el día sin preguntar a la IA | Abrir el panel y ver tareas del día | < 5 s |
| Acceso móvil | Abrir desde móvil con Tailscale | Funciona con el Zorin encendido |
| Datos frescos sin IA | Scripts programados traen novedades | 1 ejecución/día |

## 4. Historias de usuario
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | Haytham | ver y marcar tareas del día y por proyecto | no preguntar a la IA | Must |
| US-02 | Haytham | una sección «Novedades IA» con noticias, herramientas de moda y metodologías nuevas | estar al día sin buscar | Must |
| US-03 | Haytham | ver leads del CRM / Laya Leads | priorizar ventas | Must |
| US-04 | Haytham | ver proyectos y contenido del vault | saber el estado de todo | Should |
| US-05 | Haytham | abrir el panel desde el móvil por Tailscale | trabajar fuera del PC | Must |
| US-06 | Haytham | que lo mío (`humano/`) y lo de la IA (`maquina/`) estén separados y marcados en la UI | saber qué es mío | Must |

## 5. Requisitos funcionales
- RF-01: estructura `humano/` y `maquina/` por área (empezando por una) y marca visual en el panel.
- RF-02: scripts Python programados (sin IA) que guardan datos crudos en `maquina/entrada/`.
- RF-03: la IA clasifica la entrada y mueve lo útil a `maquina/util/` (patrón del vídeo).
- RF-04: registro automático de lo que hace la IA en `maquina/logs/`.
- RF-05: panel web con portada por sección y barra de iconos inferior.
- RF-06: lectura de Neozeler CRM (puerto 8100) y Laya Leads sin duplicar datos.
- RF-07: servidor arranca solo al encender el Zorin y escucha solo en la IP de Tailscale.

## 6. Requisitos no funcionales
- Poca RAM (el Zorin es un HP ProDesk 400 G5; medir). Web en TypeScript.
- Privado: nunca expuesto a internet; solo Tailscale. Sin secretos en el repo.
- Móvil primero (375 px) y escritorio.

## 7. Fuera de alcance (v1)
- Multiusuario, cobro, app nativa, chat integrado con la IA, edición de notas de Obsidian desde el panel.

## 8. Riesgos y supuestos
> [!riesgo]
> - Datos de fuentes de noticias con licencia/ToS: usar solo RSS/APIs públicas.
> - Si el Zorin se apaga, no hay panel (aceptado).
> - «Misma UI/UX que el vídeo» = misma estructura y sensación, no copia de sus imágenes: las portadas serán propias.

## 9. Criterios de aceptación
- [ ] Panel abre en móvil por la URL de Tailscale.
- [ ] Un script trae novedades de IA y aparecen en la sección sin intervención.
- [ ] Tareas se ven y se marcan.
- [ ] Contenido de `humano/` y `maquina/` se distingue en pantalla.

## 10. Demo provocadora
Pendiente: pantalla «Hoy» con tareas reales y 5 novedades de IA sintéticas.

## 11. Carácter de marca
- Adjetivos: **calmado, cinematográfico, ordenado** (a confirmar).
- Anti-referencias: dashboard SaaS gris genérico.
- Referencias: panel del vídeo (portadas a pantalla ancha + dock de iconos); `Neozeler CRM - Identidad Visual`.
- Qué enseñar en vivo: tareas reales, leads reales, novedades del día.
- Imágenes: **portadas por sección sin definir → se pregunta a Haytham antes de maquetar** (prompt Gemini / SVG / foto real).

---
Siguiente: [[2 - TRD]]
