---
title: "Sesión - 2026-10-27 - Los Apuntes de Liyo, flujo de 6 documentos"
date: 2026-10-27
type: meta/sesion
proyecto: "[[01_Projects/Los Apuntes de Liyo]]"
tags:
  - sesion
aliases: []
origen: mixto
---

# Sesión — 2026-10-27: Los Apuntes de Liyo, flujo de 6 documentos

> [!abstract] Resumen
> Se creó el proyecto personal de Haytham "Los Apuntes de Liyo" (RAG tradicional + Groq para alumnos de grado medio de informática) y se completó el flujo de 6 documentos hasta el Plan de Implementación, sin escribir código todavía.

## Contexto
Haytham partió de una conversación previa sobre arquitectura RAG tradicional (tokenización + índice invertido) + API de IA como generador, y quiso convertirla en un proyecto real con `/nuevo-proyecto`. Es un proyecto personal/educativo, no un servicio de NeoZeler.

## Qué se hizo
- PRD, TRD, UI/UX, AppFlow, Backend Schema y Plan de Implementación, los 6 en `[[01_Projects/Los Apuntes de Liyo/1 - PRD|01_Projects/Los Apuntes de Liyo]]`.
- Identidad visual decidida desde cero (sin logo ni cliente previo): "el apunte del compañero que siempre lo tiene todo ordenado", paleta papel+rotulador, registrada en [[Registro de Identidades Visuales]].
- Cliente simulado con dos agentes (`general-purpose`, rol Alumno y rol Admin) sobre el UI/UX y el AppFlow ya escritos: encontraron 2 atascos reales de alumno (sin botón de subida visible con documentos ya existentes; denunciar sin poder explicar el motivo) y varios de admin (sin pantalla de crear módulo, sin autor visible en denuncias, sin previsualización antes de borrar, acceso de admin mezclado con el de alumno). Los 4 documentos se corrigieron con lo encontrado.
- Esquema SQL (SQLite+FTS5) validado de verdad ejecutándolo con `sqlite3` de Python: búsqueda BM25 sin acentos/mayúsculas, `UNIQUE` contra denuncias duplicadas, y borrado en cascada documento→chunks→índice FTS5→denuncias.

## Decisiones tomadas
- Stack: Bun+TypeScript, SQLite FTS5 (sin dependencia npm para la búsqueda), API de Groq (`gpt-oss-20b`) vía `fetch` nativo, despliegue en el servidor Zorin de Haytham.
- Comunidad abierta sin revisión previa al subir apuntes (riesgo avisado: copyright/contenido inapropiado), con denuncia + borrado rápido como mitigación.
- El rol admin **no** es una fila de alumno: entra por `/admin` con un token aparte, nunca con nombre+centro (corregido tras el cliente simulado — antes había riesgo real de que cualquiera entrara como admin escribiendo "Haytham").

## Aprendizajes (para futuras sesiones)
- En este equipo (`alumno2627`) no existe `~/Proyectos/flujo-software/tools/trace_lint.py` ni `~/Proyectos/` — es un entorno distinto al de Haytham en casa; la trazabilidad US↔tareas se hizo a mano en el Plan en vez de con el script.
- `context7`, `obsidian-vault`, `vault-search` y el registro de npm no respondían en esta sesión (sin red/binarios locales) — los datos de Groq se verificaron con `WebFetch` directo a la documentación en vez de context7.
- El cliente simulado sobre documentos de diseño (sin código aún) sí encuentra huecos reales con solo leer las tablas de permisos contra las de pantallas/slots — vale la pena seguir haciéndolo así de pronto en el flujo, no solo al final.

## Próximos pasos
- Crear el repo real `~/Proyectos/los-apuntes-de-liyo/` (en el equipo de Haytham, no en este) con `git init` y arrancar la Fase 0 del Plan.
- Verificar `pdf-parse` en npm cuando haya red (riesgo abierto en el TRD y el Plan).
- Decidir si se abre el acceso fuera de la red de Haytham si de verdad se quiere alumnado "de todos lados" (cambio de alcance, volvería a tocar el PRD).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[01_Projects/Los Apuntes de Liyo/1 - PRD]]
