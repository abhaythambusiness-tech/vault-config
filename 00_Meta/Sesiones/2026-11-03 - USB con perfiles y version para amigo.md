---
type: sesion
date: 2026-11-03
proyecto: Portable-NeoZeler
status: completada
origen: mixto
---

> [!resumen] En cristiano
> El USB ahora pregunta qué instalar (todo, solo Claude, solo Antigravity, solo el vault…) y mira solo cómo es el ordenador. Además puede generar una versión para un amigo sin ningún dato tuyo: mismas herramientas para ahorrar tokens, vault con plantillas vacías.

## Qué se hizo
- `.mcp.json` portable con `${HOME}`; `usar.sh` verifica plugins y repara los "fantasma".
- Menú de perfiles y autodetección en `usar.sh`; `construir-amigo.sh` crea `Portable-Amigo/` con plantillas en `plantillas-amigo/`.
- Escáner de fugas obligatorio antes de publicar el paquete de amigo.

## Aprendizajes
- Un salto de línea vacío en una variable cuenta como "hay fugas": comparar tras quitar espacios.
- Los plugins públicos traen datos de prueba con pinta de claves e IPs privadas: el escáner de claves solo se aplica a lo que escribe uno mismo; el de identidad (usuario, empresa) a todo.
- Los reflog de git de los marketplaces guardan usuario y correo: se borran al empaquetar.
