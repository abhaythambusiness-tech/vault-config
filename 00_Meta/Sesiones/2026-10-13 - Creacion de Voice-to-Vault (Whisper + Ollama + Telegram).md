---
title: "Sesión - 2026-10-13 - Creación de Voice-to-Vault"
date: 2026-10-13
type: meta/sesion
proyecto: "[[01_Projects/Voice-to-Vault|Voice-to-Vault]]"
tags:
  - sesion
  - automatizacion
  - telegram
  - whisper
  - ollama
aliases: []
origen: mixto
---

# Sesión — 2026-10-13: Creación de Voice-to-Vault

> [!abstract] Resumen
> Arquitectura, desarrollo y validación de Voice-to-Vault: bot de Telegram con transcripción local en CPU (Faster-Whisper int8), estructuración mediante Ollama (Llama 3.2 1B) y volcado automático a Obsidian.

## Contexto
El usuario solicitó un brainstorming de automatizaciones útiles y seleccionó **Voice-to-Vault** y **Radar de Leads Locales**. Se comenzó por Voice-to-Vault para resolver de inmediato la fricción de captura de pensamientos y tareas hacia el vault.

## Qué se hizo
- **Brainstorming y selección**: Propuestas de automatizaciones de alto impacto; selección de Voice-to-Vault y Radar de Leads Locales.
- **Scaffolding fuera del vault**: Código alojado en `~/Proyectos/voice-to-vault/` con virtualenv propio.
- **Transcripción optimizada para CPU**: Configurado `faster-whisper` con `device="cpu"` y `compute_type="int8"` (tarda 3-5s por minuto en el Intel i5-6500 con solo ~250MB de RAM).
- **Procesador y Síntesis con IA Local**: Descargado y probado `llama3.2:1b` en Ollama (~1.3 GB, estructuración en JSON en segundos sin saturar memoria). Soporta conmutación a Groq o fallback seguro.
- **Integración con Obsidian Vault**: Módulo `vault_writer.py` que crea notas con frontmatter YAML compatible con Dataview, callout corporativo `> [!resumen]` y lista de tareas `[ ]` en `00_Inbox/`.
- **Bot de Telegram**: Manejo asíncrono de notas de voz (`.ogg`), audios y textos con verificación de usuario autorizado (`ALLOWED_USER_IDS`).
- **Prueba de ciclo completo**: Ejecutado `test_pipeline.py` generando con éxito la nota `00_Inbox/2026-10-13_1223_preparacion-con-carlos.md`.
- **Documentación exhaustiva**: Ficha completa del proyecto en `01_Projects/Voice-to-Vault.md` con Mermaid, benchmarks de hardware, guías systemd y manual operativo en `README.md`.
- **Fijación de Regla Dura 8**: Incorporada la regla de "Documentación obligatoria de proyectos" en `GEMINI.md`, `CLAUDE.md` y `.agents/rules/documentacion-proyectos.md`.
- **Auditoría de indexación**: Verificada la base de datos del grafo en `graphify-out/graph.json` y sincronizado el AST.

## Decisiones tomadas
- Modelo Whisper: `base` en int8 por defecto para equilibrio óptimo velocidad/precisión en CPU.
- Modelo LLM: `llama3.2:1b` en Ollama local como default; Groq como opción cloud rápida configurable en `.env`.
- Destino de notas: `00_Inbox/` para revisión rápida en Obsidian.
- Regla de proyectos: Ningún proyecto se da por finalizado sin ficha en vault, README en repo, registro de sesión y actualización de MOCs/grafos.

## Aprendizajes (para futuras sesiones)
- En CPUs sin GPU dedicada (Intel i5 Skylake), `faster-whisper` con `int8` y `cpu_threads=4` es órdenes de magnitud más rápido y ligero que el paquete `openai-whisper` estándar.
- `llama3.2:1b` en Ollama mantiene perfectamente la gramática en español y el formato JSON estricto para estructurar resúmenes y checklists.
- La base de datos del grafo de conocimiento en `graphify-out/graph.json` centraliza 1.473 nodos conceptuales del vault accesibles de inmediato mediante AST sin consumo de API.

## Próximos pasos
- Obtener el token de Telegram vía `@BotFather` e introducirlo en `~/Proyectos/voice-to-vault/.env`.
- Activar el servicio en segundo plano con `systemctl --user enable --now voice-to-vault.service`.
- Iniciar el segundo proyecto seleccionado: **Radar Inteligente de Leads Locales & Pitch Automatizado** (`~/Proyectos/lead-radar/`).

## Relacionado
- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[01_Projects/Voice-to-Vault|Voice-to-Vault]]
