# Casos de uso de negocio

Cada caso de uso conecta un tipo de análisis (ver `tipos-analisis.md`) con una decisión concreta y una plantilla de salida (ver `assets/`).

## Validación de idea de negocio o producto

**Pregunta que responde**: ¿está creciendo o muriendo la demanda de esto? ¿es buen momento para entrar?

- Análisis a usar: comparación multi-término (idea vs. categoría genérica vs. 1-2 competidores/sustitutos), tendencia de 5 años para ver estructura, últimos 12 meses para momentum reciente, related queries rising para detectar sub-nichos.
- Señales positivas: crecimiento sostenido en 5 años, sin caída post-pico en los últimos 12 meses, related queries en alza sin saturación aparente (poco contenido/competencia visible).
- Señales de alerta: pico aislado no sostenido, categoría genérica plana o a la baja mientras el término específico solo repite un boom pasado, "insufficient data" en la mayoría de mercados objetivo.
- Plantilla: `assets/plantilla-validacion-producto.md`

## Investigación de keywords para SEO/SEM

**Pregunta que responde**: ¿qué términos vale la pena atacar y cuándo?

- Análisis a usar: related queries (top y rising) para expandir el set de keywords, estacionalidad para programar contenido/presupuesto, comparación multi-término para priorizar entre variantes.
- Salida útil: lista de keywords con su categoría de intención, si están en fase "rising" o "top", y el mes/periodo de mayor interés.
- Plantilla: `assets/plantilla-keywords-seo.md`

## Calendario de contenido basado en picos estacionales

**Pregunta que responde**: ¿cuándo debo publicar/promocionar cada tema?

- Análisis a usar: estacionalidad (obligatorio, rango 3-5 años), cruzado con related queries de cada pico para saber qué ángulo de contenido usar en cada momento del año.
- Salida útil: calendario mes a mes con el tema principal, el momento de anticipación recomendado (publicar antes del pico, no en el pico — Google indexa y posiciona con tiempo), y los related terms a incluir.
- Plantilla: `assets/plantilla-estacionalidad.md`

## Detección de nichos emergentes antes de que se saturen

**Pregunta que responde**: ¿qué sub-nicho está creciendo que todavía no está masificado?

- Análisis a usar: breakout/tendencia emergente + related queries rising (prioriza rising-no-top), cruzado con búsqueda web rápida para verificar que no hay ya mucha oferta/contenido cubriendo el nicho.
- Salida útil: lista corta (3-7) de nichos candidatos, cada uno con su nivel de confianza (emergente confirmado / pico puntual / ruido de muestra pequeña, ver `tipos-analisis.md`) y una recomendación de acción inmediata.

## Análisis competitivo (marca propia vs. competidores)

**Pregunta que responde**: ¿cómo estoy respecto a mis competidores en interés de búsqueda, y dónde tengo ventaja u oportunidad?

- Análisis a usar: comparación multi-término (marca propia + hasta 4 competidores en una sola consulta), cruce geográfico para ver fortalezas/debilidades por mercado, related queries de cada marca para ver cómo la asocia el público.
- Salida útil: tabla comparativa por periodo y por región, identificación de mercados donde la marca propia lidera/pierde, y related queries que revelen percepción de marca (ej. "[marca] vs [competidor]", "[marca] opiniones", "[marca] precio").
- Plantilla: `assets/plantilla-benchmark-competitivo.md`

## Timing de lanzamientos de campañas de marketing

**Pregunta que responde**: ¿cuándo lanzar para maximizar el interés orgánico ya existente?

- Análisis a usar: estacionalidad del término/categoría + tiempo real/últimos 7-30 días si hay un evento disparador reciente + vertical relevante (Shopping para e-commerce, YouTube para contenido de lanzamiento).
- Regla práctica: recomienda lanzar con antelación suficiente para que el contenido/campaña esté indexado y posicionado ANTES del pico estacional, no el mismo día del pico — el pico ya es demasiado tarde para SEO orgánico (aunque puede ser correcto momento para paid/social).
