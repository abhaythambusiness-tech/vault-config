# Errores comunes a evitar (checklist obligatorio)

Repasa esta lista antes de entregar cualquier informe basado en Google Trends.

## 1. Confundir interés relativo con volumen real de búsquedas

- ❌ "Este término tiene un índice de 80, así que tiene 80.000 búsquedas al mes."
- ✅ "Este término tiene un índice de interés relativo de 80 sobre su propio pico en el periodo analizado — para volumen absoluto real se necesita una herramienta de keyword planning (Keyword Planner, Ahrefs, Semrush)."
- Nunca traduzcas el índice 0-100 a una cifra de búsquedas inventada.

## 2. Comparar índices de consultas separadas

- ❌ Consultar el término A solo, anotar su pico de 100, luego consultar el término B solo, anotar su pico de 100, y concluir que "A y B tienen el mismo interés".
- ✅ Comparar A y B siempre dentro de la misma consulta (Trends normaliza ambos sobre la misma escala 0-100 cuando se comparan juntos).

## 3. Sacar conclusiones de muestras pequeñas o nichos muy locales

- Si el dato es a nivel ciudad o de un nicho muy específico, la muestra puede ser tan pequeña que el índice sea ruido estadístico.
- Señal de alerta: series con muchos saltos bruscos entre 0 y 100 sin patrón claro, o "insufficient data" frecuente.
- Regla: cuando la muestra sea pequeña, dilo explícitamente en el informe y baja el nivel de confianza de la recomendación asociada — no la elimines silenciosamente ni la trates con la misma seguridad que un dato robusto.

## 4. Ignorar o esconder "insufficient data"

- Google Trends muestra "insufficient data" cuando no hay suficiente volumen para calcular el índice de forma fiable en esa combinación de término/geografía/periodo.
- ❌ Omitir esos mercados/periodos del informe sin explicar por qué.
- ✅ Listarlos explícitamente como "sin datos suficientes" — es información útil (puede significar mercado pequeño, término demasiado nicho, o necesidad de un término más amplio/topic en vez de término literal).

## 5. Tratar un pico puntual como tendencia estructural

- Ver `tipos-analisis.md` sección 6. Antes de recomendar una decisión estructural (lanzar una línea de producto permanente, invertir en SEO de largo plazo), confirma que el patrón se sostiene en varios periodos y no es un evento aislado.

## 6. Inventar datos cuando no se tienen

- Si el usuario no ha compartido datos reales (CSV, capturas, cifras) y Claude no ha podido obtenerlos por búsqueda web, **no generar valores de índice inventados** para rellenar una tabla o gráfica.
- En su lugar: pedir los datos, o entregar el análisis metodológico/cualitativo que sí es posible sin cifras exactas (qué buscar, cómo interpretarlo, qué decisión tomar según cada escenario posible).

## 7. Confundir correlación temporal con causalidad

- Un pico de interés que coincide con un evento no prueba que el evento lo causó — corrobora la hipótesis pero no la confirma sin evidencia adicional (cobertura de noticias del periodo, anuncios oficiales, etc.).
- Redacta las explicaciones de causa con el matiz adecuado ("coincide con...", "es probable que esté relacionado con...") en vez de afirmaciones categóricas sin evidencia directa.

## 8. Olvidar el desfase entre búsqueda e indexación/posicionamiento SEO

- Un pico de búsqueda hoy no significa que el contenido publicado hoy vaya a posicionar a tiempo para capturarlo.
- Para recomendaciones de timing de contenido/campaña, siempre añade el margen de antelación necesario (ver `casos-uso.md`, sección de timing de campañas).
