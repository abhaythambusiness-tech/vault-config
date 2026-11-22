# Templates de Entregables

Tres formatos según el contexto. **Siempre** termina la skill generando un archivo en `/mnt/user-data/outputs/` y presentándolo con `present_files`. Nada de dejarlo en chat sin archivo.

---

## 1. Informe Markdown / Obsidian (Modo Lupa o Hueco)

**Cuándo usar:** análisis profundo de UN competidor, o documento estratégico personal sobre el mercado. Va al vault del usuario.

**Formato del archivo:** `competitor-[nombre]-[YYYY-MM-DD].md` o `mercado-[nicho]-[YYYY-MM-DD].md`

**Estructura obligatoria:**

```markdown
---
tipo: competitor-research
modo: [lupa|mapa|hueco]
fecha: YYYY-MM-DD
competidor: [nombre o "varios"]
nicho: [...]
tags:
  - competitor-research
  - [nicho específico]
  - [otros tags relevantes]
---

# Competitor Research — [Título]

> [!info] Resumen ejecutivo en 3 líneas
> 1. [hallazgo más importante]
> 2. [segundo hallazgo]
> 3. [tercer hallazgo]

## 🎯 Conclusión accionable

**Lo que harás con esto:**
- [acción 1]
- [acción 2]
- [acción 3]

---

## Análisis detallado

[Aquí va el contenido del framework — secciones 1-7 si es Lupa, comparativa si es Mapa, síntesis estratégica si es Hueco]

---

## Swipe file (lo que merece la pena guardar)

### Hooks que funcionan
- "[hook literal]" — [competidor] — [por qué funciona]

### Garantías interesantes
- [...]

### Formatos de oferta
- [...]

### Lead magnets
- [...]

---

## Próximos pasos

- [ ] [acción concreta con fecha]
- [ ] [...]

---

## Fuentes

- [URL 1] — [qué se sacó de aquí]
- [URL 2] — [...]
```

**Reglas para Obsidian:**
- Usa wikilinks `[[Nombre Competidor]]` cuando menciones a un competidor que merezca su propia nota
- Frontmatter YAML siempre presente
- Callouts (`> [!info]`, `> [!warning]`, `> [!tip]`) para destacar insights
- Tags consistentes: `#competitor-research`, `#[nicho]`, `#posicionamiento`

---

## 2. Documento Word (Modo Mapa, deliverable formal)

**Cuándo usar:** cuando el usuario lo va a presentar a un equipo, socio, o lo va a usar como documento de trabajo formal. También para comparativas de mercado completas.

**Formato del archivo:** `Competitor-Research-[Nicho]-[YYYY-MM-DD].docx`

**Antes de generarlo, leer la skill `docx`** en `/mnt/skills/public/docx/SKILL.md` para usar la herramienta correcta.

**Estructura del documento Word:**

1. **Portada**
   - Título: "Competitor Research — [Nicho/Mercado]"
   - Subtítulo: "Análisis estratégico de [N] competidores"
   - Fecha
   - "Preparado para: [usuario]"

2. **Resumen ejecutivo** (1 página máximo)
   - 3 hallazgos clave
   - Recomendación principal
   - Próximos pasos

3. **Metodología** (media página)
   - Fuentes consultadas
   - Criterios de selección de competidores
   - Limitaciones del estudio

4. **Mapa del mercado** (1-2 páginas)
   - Tabla resumen de los N competidores con: nombre / oferta / precio / posicionamiento
   - Visual: cuadrícula 2x2 sobre 2 ejes relevantes (ej: vertical vs. horizontal × premium vs. value)

5. **Análisis competidor por competidor** (1-2 páginas cada uno)
   - Las 7 dimensiones del framework
   - Síntesis "3 mejores / 3 peores"

6. **Síntesis estratégica** (2-3 páginas)
   - Patrones del mercado
   - Outliers
   - Huecos detectados
   - Recomendación de posicionamiento

7. **Anexo**
   - Fuentes detalladas con URLs
   - Glosario si hay términos técnicos

**Tono del Word:** profesional pero sin pomposidad. Frases cortas. Datos antes que adjetivos.

**Largo máximo:** 25 páginas. Si te pasas, hay grasa.

---

## 3. Tabla comparativa estructurada (Modo Mapa, formato rápido)

**Cuándo usar:** cuando el usuario solo quiere ver "todos los competidores de un vistazo". Es el equivalente a un battle card consolidado.

**Formato del archivo:** `Comparativa-[Nicho]-[YYYY-MM-DD].xlsx` (ver skill `xlsx`) o tabla markdown si es para Obsidian.

**Estructura de columnas (en Excel/markdown):**

| Competidor | Web | Founder | Vertical | Servicios principales | Modelo cobro | Ticket entrada | Hook principal | Lead magnet | Tamaño equipo | Canal contenido principal | Frecuencia | Tienen ads | Casos públicos | Fortaleza clave | Debilidad clave | Implicación |

**Reglas:**
- Una fila por competidor
- Última fila: "PROMEDIO MERCADO" con valores agregados (ticket medio, frecuencia media, etc.)
- Última fila +1: "USUARIO/AGENCIA" donde el usuario rellena cómo se compara él
- Color condicional: rojo si commodity, verde si diferencial, amarillo si ambiguo

**Si va a Excel:** usar la skill `xlsx`. Hoja 1 = comparativa, Hoja 2 = swipe file (hooks, garantías, ofertas guardadas).

**Si va a markdown:** tabla simple, después una sección de "lectura rápida" con los 3 hallazgos principales.

---

## Reglas comunes a los 3 formatos

### Citas y fuentes

Cada dato fuerte (precio, número, claim) lleva URL. Sin URL, no es dato.

Formato sugerido inline:
- "Cobran 2.500€/mes [[fuente](url)]"
- "Tienen +50 clientes según mención en podcast [[1](url)]"

### Marcado de inferencias

Cuando un dato no está confirmado pero lo deduces:
- `[INFERIDO: razón de la inferencia]`
- Ej: "Ticket medio ~3.000€/mes [INFERIDO: caso público mencionando 'inversión similar a una persona junior']"

### Implicación accionable

Cada sección termina con:

> **🎯 Implicación para [usuario]:** [qué hacer con este dato concretamente]

Sin esto, el research es masaje cerebral sin ROI.

### Verificación final antes de entregar

Antes de generar el archivo final, comprueba:

- [ ] ¿Cada competidor tiene mínimo 3 fuentes consultadas?
- [ ] ¿Hay al menos UNA recomendación accionable concreta?
- [ ] ¿El posicionamiento recomendado pasa los 4 filtros (específico/defensible/rentable/honesto)?
- [ ] ¿Las inferencias están marcadas como tales?
- [ ] ¿Hay swipe file con mínimo 5 elementos guardables?

Si alguno falla → vuelve a la fase correspondiente. No entregues research a medio cocer.

---

## Multi-deliverable: cuando el usuario quiere los 3

Si el usuario pide "todo" o el contexto lo justifica, genera los 3 en orden:

1. **Tabla comparativa primero** (xlsx) — para vista rápida
2. **Informe markdown / Obsidian** — para guardar y consultar
3. **Word formal** — solo si va a haber presentación o reunión real (si no, es trabajo desperdiciado)

Pregunta al usuario antes de generar el Word: "¿Vas a presentar esto formalmente o te basta con el markdown + tabla?". El Word lleva tiempo y a menudo no se usa.
