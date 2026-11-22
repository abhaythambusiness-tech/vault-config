---
date: 2026-11-05
proyecto: "[[01_Projects/Dashboard Command AI]]"
type: sesion
origen: mixto
---

> [!resumen] En cristiano
> Haytham pidió un panel 3D completo para el servidor con dos usuarios (Jason y Sam), presencia entre ellos, noticias con ideas, clientes del scraper y proyectos de Obsidian. Se construyó en `~/Proyectos/dashboard-command-ai/` y se verificó. Sin commit.

## Qué se hizo
- Proyecto nuevo (Vite + TS + Three.js + servidor Node con WebSocket), README y `resumen.html`.
- Flujo de 6 documentos y fase 0b saltados: petición directa de prototipo, «sin preguntas».
- Datos reales: 1863 leads (242 filtrados).

## Aprendizajes
- `[hidden]` se anula con cualquier `display:` en CSS: hace falta `[hidden]{display:none !important}`.
- Cámara dentro del arco de objetos tapaba la escena: ponerla fuera, a 8.6 de distancia.
- Bloom y materiales brillantes saturan a blanco: bajar bloom, subir rugosidad, bajar `envMapIntensity`.
- `claude -p` con OAuth caducado: las ideas caen a reglas simples; hace falta login.
- zsh no admite `${!var}`; `pkill -f` mata la propia shell: usar `fuser -k PUERTO/tcp`.
- Lighthouse actual exige Node 22; aquí Node 18: usar 11.7.1.
