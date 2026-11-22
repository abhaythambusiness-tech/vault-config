# Tipos de análisis

## 1. Análisis de estacionalidad

Objetivo: detectar patrones que se repiten cada año/mes/semana.

Método:
1. Usa un rango de al menos 3-5 años (idealmente 5) para promediar el ruido de un solo año atípico.
2. Identifica los meses/semanas con picos recurrentes (mismo mes, año tras año).
3. Calcula (aunque sea de forma aproximada, a ojo sobre los datos dados) cuánto sube el índice en el pico vs. el valle del mismo año, para dimensionar la magnitud de la estacionalidad.
4. Distingue estacionalidad "dura" (se repite todos los años, ej. "regalos Navidad") de picos puntuales no recurrentes (un solo año, causados por un evento externo — ver sección de rupturas).
5. Traduce el patrón a un calendario accionable: "el interés empieza a subir en la semana X y llega al pico en la semana Y" — esto es lo que va directo a la plantilla de calendario de contenido.

## 2. Comparación de hasta 5 términos/temas simultáneos

Objetivo: saber cuál de varios términos/marcas/productos tiene más interés relativo y cómo evoluciona cada uno frente a los demás.

Método:
1. Todos los términos deben compararse en la **misma consulta** (Google Trends limita a 5 términos por comparación) — nunca compares índices sacados de consultas separadas.
2. Identifica quién lidera en cada punto del tiempo — el liderazgo puede cambiar (cruces de líneas son información valiosa: "en enero A superó a B por primera vez en 2 años").
3. Compara también por geografía dentro de la misma consulta: un término puede perder en el agregado global pero liderar en mercados específicos.
4. Si el objetivo es benchmark competitivo, añade siempre al menos un término "categoría genérica" (ej. "zapatillas running") como referencia de tamaño de la conversación total, no solo comparar marcas entre sí.

## 3. Detección de breakout / tendencia emergente

Objetivo: diferenciar ruido de una señal real de crecimiento explosivo.

Método:
1. Google Trends marca como **"Breakout"** un crecimiento >5000% en un related query/topic — trátalo como señal de alta prioridad pero verifica que no sea un artefacto de una base muy pequeña (pasar de 1 a 60 búsquedas también puede marcar breakout).
2. Para confirmar que es una tendencia real y no ruido de una sola semana:
   - Revisa si el crecimiento se sostiene en 2-3 periodos consecutivos, no solo un pico aislado.
   - Cruza con "Related queries" para ver si el crecimiento viene acompañado de más términos relacionados también en alza (señal de que es un tema, no una anomalía puntual).
   - Si es posible, contrasta con una búsqueda web rápida de noticias del periodo para explicar la causa (lanzamiento, viral, evento).
3. Clasifica cada hallazgo como:
   - **Emergente confirmado**: crecimiento sostenido + related terms en alza + explicación identificable.
   - **Pico puntual**: un solo salto, sin sostenerse, probablemente ligado a un evento de un día.
   - **Ruido de muestra pequeña**: base de datos demasiado baja para ser fiable — avisar y no usar como base de decisión.

## 4. Related queries y related topics (rising vs. top)

Objetivo: descubrir oportunidades de contenido, SEO o producto adyacentes al término principal.

Método:
1. **Top** = los términos/temas más buscados junto al principal en términos absolutos dentro de la ventana — útil para entender el contexto general de la demanda.
2. **Rising** = los que más han crecido en el periodo (incluye "Breakout" como caso extremo) — útil para detectar oportunidades antes de que se saturen.
3. Prioriza para contenido/SEO los términos que están en **Rising pero aún no en Top** — son demanda creciente todavía no saturada de contenido/competencia.
4. Agrupa los related terms por intención (informacional, transaccional, comparativa, de marca) para poder priorizarlos según el objetivo (contenido de blog vs. página de producto vs. campaña de conversión).

## 5. Cruce de datos geográficos

Objetivo: encontrar mercados con mayor interés relativo para priorizar expansión, localización de contenido o presupuesto de ads.

Método:
1. Usa "Interest by region/city" dentro de la misma consulta del término/topic.
2. No confundas "mayor índice" con "mayor mercado" — un país pequeño puede tener índice 100 con pocas búsquedas absolutas. Cruza (cuando sea posible) con tamaño de población o de mercado para no sobreestimar oportunidades pequeñas.
3. Para decisiones de expansión, compara al menos 3-5 mercados candidatos en la misma consulta, no uno a uno.
4. Señala explícitamente los mercados con "insufficient data" en vez de omitirlos silenciosamente — es información (el mercado es demasiado pequeño para el término, todavía).

## 6. Interpretación de rupturas de tendencia (picos por eventos)

Objetivo: no confundir un pico causado por una noticia/evento puntual con una tendencia estructural de negocio.

Método:
1. Ante cualquier pico aislado y grande, busca la causa antes de interpretarlo como señal de demanda sostenible: lanzamiento de producto, noticia viral, cambio regulatorio, temporada de premios, etc.
2. Compara la altura y duración del pico con la estacionalidad "normal" del término (ver sección 1) — si el pico es mucho mayor que los picos estacionales habituales, es probable que sea un evento, no estacionalidad.
3. Cuando el pico se debe a un evento puntual, recomienda tratarlo como oportunidad táctica de corto plazo (contenido reactivo, campaña puntual), no como base para decisiones estructurales (lanzar una línea de producto permanente, etc.).

## 7. Trends por vertical: Shopping, YouTube, News, Images

Google Trends permite filtrar por tipo de búsqueda, cada uno con una lectura distinta:

- **Búsqueda web (default)**: intención general, mezcla informacional/transaccional.
- **Google Shopping**: intención de compra más directa — útil para timing de campañas de e-commerce y estacionalidad de producto físico.
- **YouTube Search**: intención de consumo de contenido/entretenimiento/tutorial — útil para estrategia de contenido en video y para detectar tendencias de cultura/entretenimiento antes de que lleguen a búsqueda web.
- **Google News**: intención informativa sobre eventos actuales — útil para relacionar picos con cobertura mediática y anticipar cuándo un tema empieza a "enfriarse" en medios.
- **Google Images**: intención visual/inspiracional — útil en moda, diseño, decoración, recetas.

Método: si el objetivo de negocio tiene un canal claro (ads de Shopping, estrategia de video, PR/comunicación, contenido visual), usa el vertical correspondiente además de (no en vez de) la búsqueda web general — la combinación da una imagen más completa que solo web search.
