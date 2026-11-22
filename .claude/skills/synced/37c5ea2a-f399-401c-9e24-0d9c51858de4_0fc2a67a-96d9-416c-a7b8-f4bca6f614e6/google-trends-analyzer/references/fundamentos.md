# Fundamentos de Google Trends

## El índice de interés (0-100)

- Google Trends **no** reporta volumen de búsquedas absoluto. Reporta un índice normalizado de 0 a 100 dentro de la ventana temporal y geografía seleccionadas.
- **100** = el punto de máxima popularidad relativa del término en ese periodo/región.
- **50** = la mitad de popularidad relativa respecto al pico.
- **0** = no hay suficientes datos para ese término en ese momento/lugar (no significa "cero búsquedas").
- Los valores se recalculan cada vez que cambias el rango temporal o la geografía — un mismo término puede tener un "100" distinto en cada consulta. **Nunca compares índices de dos búsquedas hechas por separado**: para comparar términos hay que ponerlos juntos en la misma consulta (hasta 5 a la vez).

## Interés relativo vs. absoluto

- Relativo (lo que da Trends): te dice la forma de la curva y la proporción entre términos comparados juntos.
- Absoluto (volumen real de búsquedas): Trends NO lo da. Para eso se necesitan herramientas de keyword planner/SEO (Google Keyword Planner, Ahrefs, Semrush, etc.).
- Regla práctica: Trends sirve para responder "¿está subiendo o bajando?", "¿en qué mes se dispara?", "¿qué término gana más interés que otro?" — no sirve para responder "¿cuántas búsquedas mensuales tiene?".

## Término vs. Topic vs. Categoría

- **Término de búsqueda** (search term): coincidencia literal de texto, incluye variantes ortográficas y errores comunes agrupados por Google.
- **Tema/Topic**: un grupo de términos que Google agrupa semánticamente en torno a un concepto (por ejemplo el topic "Pizza" agrupa "pizza", "pizzeria", "pizza hut", etc., en varios idiomas). Da una señal más limpia y comparable entre idiomas/mercados. Preferible cuando el objetivo es entender demanda de un concepto, no de una palabra exacta.
- **Categoría**: filtro adicional (ej. "Alimentación y bebida", "Negocios e industria") que ayuda a desambiguar términos con doble sentido (ej. "jaguar" coche vs. animal).
- Regla práctica: si el término es ambiguo o el usuario quiere comparar entre países/idiomas, usa Topic + Categoría en vez de término literal.

## Granularidad temporal

| Rango | Uso típico |
|---|---|
| Tiempo real (últimas 4 horas) | Monitorización de eventos en vivo, breaking news, lanzamientos justo ahora |
| Últimas 24 horas / 7 días | Reacción a un evento reciente, picos de corto plazo |
| Últimos 12 meses | Detectar estacionalidad de un año, tendencia reciente de negocio |
| Últimos 5 años | Ver si una categoría crece o decrece estructuralmente, ciclos multianuales |
| 2004–hoy (histórico completo) | Validar si algo es una moda pasajera o una tendencia de largo plazo, comparar con crisis/eventos pasados |

Importante: a mayor rango temporal, más agregados los datos (de datos horarios a datos semanales o mensuales). Si el objetivo es detectar el día exacto de un pico, usa rango corto; si el objetivo es estacionalidad anual, usa 5 años para promediar ruido de un solo año.

## Segmentación geográfica y de idioma

- Niveles disponibles: mundial → país → región/estado → ciudad (la disponibilidad de nivel ciudad depende del volumen de datos del término en esa zona).
- Cuidado con nichos muy locales: a nivel ciudad, el índice puede basarse en muy pocas búsquedas y ser ruidoso o mostrar "insufficient data".
- El idioma de búsqueda no es 1:1 con el país — en mercados multilingües (ej. España con catalán/euskera/gallego, o países con diáspora), conviene comparar variantes del término en cada idioma relevante, no asumir que el término en un idioma captura todo el interés real.
- Para comparar marcas/productos entre países, usa el mismo término (idealmente el Topic, que normaliza variantes de idioma) y compara "interés por región" dentro de una sola consulta, no consultas separadas por país.
