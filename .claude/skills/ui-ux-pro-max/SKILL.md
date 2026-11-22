---
name: ui-ux-pro-max
description: "Design intelligence — base de datos consultable (BM25) de paletas de color, tipografías, estilos UI (glassmorphism, minimalism, brutalism...), estructuras de landing pages y anti-patrones UX, con…"

---

# Skill: UI/UX Pro Max (Design Intelligence)

Esta skill proporciona inteligencia de diseño avanzada mediante una base de datos de estilos, paletas de colores, fuentes, y guías de UX optimizadas para conversión.

## Ubicación
`~/.claude/skills/ui-ux-pro-max/`

## Uso (CLI)
Para buscar recomendaciones de diseño, ejecuta:
```bash
python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain <domain>
```

**Dominios disponibles:**
- `product`: Recomendaciones por tipo de producto (SaaS, e-commerce, portfolio)
- `style`: Estilos UI (glassmorphism, minimalism, brutalism) + prompts de IA
- `typography`: Combinaciones de fuentes con imports de Google Fonts
- `color`: Paletas de colores optimizadas
- `ux`: Mejores prácticas y anti-patrones de experiencia de usuario
- `landing`: Estructuras de landing pages y estrategias de CTA
- `chart`: Recomendaciones de tipos de gráficas

También soporta generación de design system persistente:
```bash
python3 ~/.claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Nombre Proyecto" [--page "dashboard"]
```

## Integración en el Workflow
1. **Fase de Planificación**: Consultar estilos y paletas antes de codificar el frontend.
2. **Fase de Implementación**: Usar las clases CSS y palabras clave recomendadas.
3. **Fase de Review**: Validar el diseño contra los anti-patrones de la base de datos `ux`.

## Relación con otras skills
Complementa (no sustituye) a `web-design-guidelines` y `responsive-design`: úsala primero para elegir paleta/tipografía/estructura, y las otras para validar accesibilidad y responsive.
