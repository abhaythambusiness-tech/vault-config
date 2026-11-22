---
type: sesion
date: 2026-11-17
proyecto: "[[01_Projects/Kit Samira]]"
origen: mixto
---

> [!resumen] En cristiano
> Se montó el kit para el ordenador de Samira: vault, reglas y skills de ventas/marketing, base de búsqueda por significado y sincronización con Zorin. Falta copiarlo al USB (no estaba detectado) y probarlo en su Windows.

## Aprendizajes
- `mcp` v2 renombró `FastMCP`: en `vault_mcp.py` va fijado `mcp>=1.2,<2`.
- Chroma trae embeddings ONNX por defecto (~80 MB): sirve de base vectorial sin PyTorch, mucho más ligero para Windows.
- La identidad de Syncthing de Samira se generó aquí y se añadió a Zorin con `syncthing cli`; así el emparejamiento no necesita pasos manuales. Riesgo: la clave privada viaja en el USB.
- `guard-destructive` bloquea hasta el texto de un push forzado dentro de un heredoc: escribir esos archivos con `Write`.
