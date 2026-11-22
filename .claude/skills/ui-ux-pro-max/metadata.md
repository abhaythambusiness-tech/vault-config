# Skill: UI/UX Pro Max (Design Intelligence)

Esta skill proporciona inteligencia de diseño avanzada mediante una base de datos de estilos, paletas de colores, fuentes, y guías de UX optimizadas para conversión.

## Ubicación
`d:/01 - NeoZeler Core/Agents/_base/skills/ui-ux-pro-max/`

## Uso (CLI)
Para buscar recomendaciones de diseño, ejecuta:
```bash
python "d:/01 - NeoZeler Core/Agents/_base/skills/ui-ux-pro-max/scripts/search.py" "<query>" --domain <domain>
```

**Dominios disponibles:**
- `product`: Recomendaciones por tipo de producto (SaaS, e-commerce, portfolio)
- `style`: Estilos UI (glassmorphism, minimalism, brutalism) + prompts de IA
- `typography`: Combinaciones de fuentes con imports de Google Fonts
- `color`: Paletas de colores optimizadas
- `ux`: Mejores prácticas y anti-patrones de experiencia de usuario
- `landing`: Estructuras de landing pages y estrategias de CTA
- `chart`: Recomendaciones de tipos de gráficas

## Integración en el Workflow
1. **Fase de Planificación**: Consultar estilos y paletas antes de codificar el frontend.
2. **Fase de Implementación**: Usar las clases CSS y palabras clave recomendadas.
3. **Fase de Review**: Validar el diseño contra los anti-patrones de la base de datos `ux`.
