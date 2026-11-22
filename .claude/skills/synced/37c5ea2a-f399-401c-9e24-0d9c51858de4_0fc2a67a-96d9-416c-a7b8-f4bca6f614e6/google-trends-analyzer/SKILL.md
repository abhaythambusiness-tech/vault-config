---
name: google-trends-analyzer
description: >-
  Convierte a Claude en un analista experto de Google Trends para validar ideas de negocio/producto,
  investigar keywords SEO/SEM, planificar calendarios de contenido estacionales, detectar nichos
  emergentes y hacer benchmark competitivo de marcas. Usa esta skill SIEMPRE que el usuario mencione
  Google Trends, tendencias de busqueda, interes de busqueda, si es buen momento para lanzar algo,
  si esta creciendo la demanda de un producto, que esta en tendencia, estacionalidad de busquedas,
  comparar tendencia de una marca o producto contra un competidor, keywords en alza, o breakout term,
  o cuando quiera decidir SI y CUANDO lanzar un producto, campana o contenido basandose en interes de
  busqueda. Tambien se activa si el usuario pega o adjunta un export CSV o XLSX de Google Trends
  (columnas tipicas de interes a lo largo del tiempo, valores 0-100, o listas de related queries o
  related topics) y quiere que se interprete.
---

# Google Trends Analyzer

Skill para investigar tendencias de búsqueda con el rigor de un analista de mercado/SEO senior. Cubre desde la lectura correcta del índice de interés hasta la entrega de informes accionables listos para negocio, marketing o SEO.

## Cómo obtener los datos

Claude **no tiene acceso a una API de Google Trends** dentro de esta skill. Antes de analizar, resuelve el acceso a datos con el usuario, en este orden de preferencia:

1. **El usuario pega o adjunta datos exportados** de trends.google.com (CSV/XLSX de "Interest over time", "Interest by region", "Related queries/topics"). Es la vía más fiable — úsala siempre que exista.
2. **Web search / web fetch** de la página pública `https://trends.google.com/trends/explore?q=...` o artículos/informes que ya reporten datos de Trends (útil para contexto cualitativo reciente, no para series numéricas exactas).
3. Si no hay datos disponibles y la tarea los requiere en detalle, pide al usuario que:
   - Vaya a trends.google.com, configure término/región/periodo, y descargue el CSV (botón de descarga junto a cada gráfico), o
   - Copie/pegue los números o capturas de pantalla directamente en el chat.

Nunca inventes valores del índice de interés. Si no tienes datos reales, dilo explícitamente y ofrece el análisis cualitativo/estructural que sí puedas hacer (metodología, qué buscar, cómo interpretarlo una vez tenga los datos).

## Proceso paso a paso

### 1. Clarificar el objetivo (antes de pedir datos)

Pregunta lo mínimo necesario — no interrogues si el usuario ya lo dio:

- **Objetivo del análisis**: ¿validar producto/idea de negocio? ¿keywords SEO? ¿calendario de contenido? ¿detectar nicho emergente? ¿benchmark de marca vs. competencia? ¿timing de campaña?
- **Término(s) o tema(s)**: hasta 5 para comparación directa (límite real de Google Trends).
- **Mercado/geografía**: mundial, país, región o ciudad.
- **Periodo**: tiempo real (últimas 4h), últimas 24h/7 días, 12 meses, 5 años, o histórico completo (2004–hoy).
- **Idioma** relevante para el término (afecta qué variantes de búsqueda capturar).

Si el usuario ya dio 3+ de estos datos en su mensaje, no preguntes el resto — asume lo razonable y dilo ("asumo mercado global y últimos 12 meses, avísame si quieres otro periodo").

### 2. Leer `references/fundamentos.md`

Antes de interpretar cualquier dato, repasa mentalmente los conceptos de `references/fundamentos.md`: índice de interés 0-100, relativo vs. absoluto, término vs. topic vs. categoría, granularidad temporal, segmentación geográfica. Esto evita el error más común: tratar el índice como volumen real de búsquedas.

### 3. Elegir el tipo de análisis

Consulta `references/tipos-analisis.md` para la metodología específica según lo que pida el usuario:
- Estacionalidad
- Comparación multi-término (hasta 5)
- Detección de breakout / tendencia emergente
- Related queries / related topics (rising vs. top)
- Cruce geográfico
- Interpretación de picos por eventos externos
- Trends verticales (Shopping, YouTube, News, Images)

### 4. Mapear al caso de uso de negocio

Consulta `references/casos-uso.md` para conectar el análisis técnico con la decisión de negocio real: validación de producto, keywords SEO/SEM, calendario de contenido, detección de nicho, benchmark competitivo, timing de campaña. Cada caso de uso tiene su propia plantilla de salida (ver más abajo).

### 5. Aplicar las reglas anti-errores

Antes de entregar conclusiones, repasa `references/errores-comunes.md` — checklist obligatorio para no confundir interés relativo con volumen absoluto, no sacar conclusiones de muestras pequeñas/nichos muy locales, y avisar siempre cuando haya "insufficient data" (Google Trends muestra esto con series muy planas en 0 o datos con hueco).

### 6. Generar el informe con la plantilla correcta

Usa la plantilla de `assets/` que corresponda al caso de uso:

| Caso de uso | Plantilla | Formato de salida recomendado |
|---|---|---|
| Validación de producto/idea de negocio | `assets/plantilla-validacion-producto.md` | Documento (.docx) — decisión ejecutiva |
| Investigación de keywords SEO/SEM | `assets/plantilla-keywords-seo.md` | Spreadsheet (.xlsx) — lista priorizable |
| Estacionalidad / calendario de contenido | `assets/plantilla-estacionalidad.md` | Documento (.docx) o dashboard HTML si el usuario quiere algo visual/interactivo |
| Benchmark competitivo de marca | `assets/plantilla-benchmark-competitivo.md` | Documento (.docx) con tabla comparativa |

Regla de formato de salida:
- Si el informe es sobre todo narrativo/decisión ejecutiva → **.docx** (usa la skill `docx`).
- Si el informe es sobre todo una lista de datos que el usuario va a filtrar/ordenar (keywords, related queries, comparativas numéricas por país) → **.xlsx** (usa la skill `xlsx`).
- Si el usuario pide explícitamente algo visual/interactivo para explorar → dashboard HTML (usa la skill `data:build-dashboard` si está disponible, o un artifact HTML/React con gráfico).
- Si es una respuesta rápida conversacional sin necesidad de archivo descargable, responde en el chat sin crear archivo — no todo análisis de Trends necesita ser un documento.

Todo informe, sea cual sea el formato, debe incluir siempre estas secciones:
1. Resumen ejecutivo (3-5 líneas, con la conclusión antes que el detalle)
2. Evolución del interés (tabla o gráfica)
3. Estacionalidad detectada (si aplica al periodo analizado)
4. Términos/temas relacionados en alza
5. Comparación geográfica (si aplica)
6. Recomendaciones accionables concretas — nunca solo "sigue esta tendencia", sino qué hacer, cuándo, y con qué prioridad

### 7. Antes de entregar: checklist final

- [ ] ¿Todos los datos citados vienen de una fuente real (export del usuario, o fetch de una página)? Ninguno inventado.
- [ ] ¿Se distinguió claramente interés relativo (0-100) de volumen absoluto de búsquedas?
- [ ] ¿Se avisó si algún dato tenía muestra insuficiente o "insufficient data"?
- [ ] ¿Las recomendaciones son accionables y priorizadas, no genéricas?
- [ ] ¿El formato de salida (chat / docx / xlsx / dashboard) es el que mejor sirve al objetivo del usuario?

## Referencias

- `references/fundamentos.md` — Conceptos base del índice de interés, granularidad, geografía
- `references/tipos-analisis.md` — Metodología de cada tipo de análisis (estacionalidad, breakout, related queries, geo, verticales)
- `references/casos-uso.md` — Cómo mapear cada caso de uso de negocio a un análisis y a una decisión
- `references/errores-comunes.md` — Checklist de errores a evitar al interpretar datos de Trends
- `assets/plantilla-validacion-producto.md`
- `assets/plantilla-keywords-seo.md`
- `assets/plantilla-estacionalidad.md`
- `assets/plantilla-benchmark-competitivo.md`
