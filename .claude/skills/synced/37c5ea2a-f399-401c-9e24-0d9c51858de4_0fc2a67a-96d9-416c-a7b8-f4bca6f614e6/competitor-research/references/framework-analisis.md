# Framework de Análisis — Las 7 Dimensiones

Para cada competidor analizado en Fase 2, cubre estas 7 dimensiones. Cada dimensión tiene preguntas guía y señales de calidad. Si no encuentras la info, márcalo como `[GAP]` — no inventes.

---

## 1. Oferta y Servicios

**Preguntas a responder:**
- ¿Qué venden exactamente? (servicio puro, servicio+software, info-product, hybrid)
- ¿Stack de servicios o servicio único? (setter IA solo vs. paquete completo)
- ¿Productized o custom? (tienen "Plan Starter / Pro / Enterprise" o cada propuesta es a medida)
- ¿Vertical o horizontal? (solo dentistas vs. cualquier negocio)
- ¿Qué herramientas usan? (n8n, Make, Vapi, Synthflow, Retell, GHL, Zapier, custom)

**Señales fuertes:**
- Página de servicios con paquetes nombrados → maduros, productizados
- "Hablemos de tu caso" sin info → custom, transaccional, probablemente ticket alto
- Mismo servicio que tú con otro nombre → competidor directo
- Servicio adyacente (ej: solo agentes de voz cuando tú haces stack completo) → más complementario que rival

**Output esperado:**
```
**Oferta principal:** [una frase]
**Servicios desglosados:** [lista con bullet por servicio]
**Stack técnico detectado:** [herramientas]
**Modelo:** Productized / Custom / Híbrido
**Vertical:** [si aplica]
```

---

## 2. Precios y Modelo de Negocio

**Preguntas a responder:**
- ¿Precio público o "consulta"?
- Modelo: setup único, retainer mensual, % revenue, performance, mixto
- Tickets aproximados (entrada / medio / top)
- ¿Cobran por cita generada / lead cualificado / resultado?
- ¿Tienen tier gratis o trial?

**Cómo encontrar precios cuando no son públicos:**
- Reseñas en Trustpilot, Google, LinkedIn donde clientes mencionan inversión
- Posts de LinkedIn del founder con casos ("conseguimos X para cliente que invirtió Y")
- Podcasts donde entrevistan al founder
- Comparativas en Reddit / foros
- Si todo falla: marca `[INFERIDO: rango estimado]` con justificación

**Output esperado:**
```
**Modelo de cobro:** [setup+retainer / performance / etc.]
**Ticket entrada:** [€X o "no público — inferido en €Y"]
**Ticket medio:** [...]
**Compromiso mínimo:** [3 meses, 6 meses, sin compromiso]
**Garantías ofrecidas:** [si las hay]
```

---

## 3. Posicionamiento y Mensaje

**Preguntas a responder:**
- ¿Cuál es su HOOK principal en home/LinkedIn? (literal, copia la frase)
- ¿Contra quién se posicionan implícitamente? (agencias tradicionales, freelancers, in-house, otras agencias IA)
- ¿Qué dolor atacan? (tiempo, dinero, escala, complejidad)
- ¿Qué prometen? (más leads, menos no-shows, más facturación, menos trabajo manual)
- ¿Tono de comunicación? (técnico / business / aspiracional / agresivo)

**Señales fuertes:**
- Hook claro y específico en home → posicionamiento maduro
- "Soluciones de IA para tu negocio" → posicionamiento débil, blandito
- Contraste explícito vs. alternativas → han pensado en su categoría
- Misma promesa que 5 competidores → commodity, oportunidad de diferenciar

**Output esperado:**
```
**Hook principal (literal):** "[copy textual]"
**Promesa:** [una frase]
**Dolor que atacan:** [...]
**Contra quién se posicionan:** [explícito o implícito]
**Tono:** [...]
```

---

## 4. Embudo de Captación

**Preguntas a responder:**
- ¿Cómo llegan los leads? (orgánico, ads, outbound cold, partnerships, referidos, comunidad)
- ¿Qué lead magnet usan? (audit gratis, playbook PDF, masterclass, llamada estratégica)
- ¿Calendly directo o pasan por VSL/aplicación?
- ¿Tienen proceso de calificación? (formulario con preguntas duras, qualifying call)
- ¿Hacen ads activamente? (Meta Ad Library, Google Ads, LinkedIn)

**Cómo investigar:**
- Meta Ad Library (`facebook.com/ads/library`) → todos los ads activos del competidor
- Análisis de su web: ¿qué CTA tienen? ¿popup? ¿exit intent?
- Su LinkedIn: ¿postean lead magnets? ¿tienen newsletter?

**Output esperado:**
```
**Canales de captación detectados:** [orgánico LinkedIn / ads Meta / outbound LI / etc.]
**Lead magnet principal:** [auditoría gratis / playbook / masterclass]
**Booking flow:** [Calendly directo / VSL → aplicación / formulario qualifying]
**Ads activos:** Sí/No — [si sí, copy del ad principal]
```

---

## 5. Contenido y Autoridad

**Preguntas a responder:**
- ¿Frecuencia de publicación por canal?
- ¿Formato dominante? (carruseles LI, reels IG, videos largos YouTube, threads X)
- ¿Temas recurrentes? (casos de éxito, tutoriales, opinión, build in public)
- ¿Engagement real o vanity? (likes vs. comentarios sustanciales)
- ¿Quién es la cara visible? (founder solo / equipo / nadie)

**Señales fuertes:**
- 4+ posts/semana sostenidos = máquina de contenido
- Pocos posts pero con cientos de comments = autoridad real
- Solo posts "vendiendo" = embudo flojo, no construyen audiencia

**Output esperado:**
```
**Canal principal de contenido:** [LinkedIn / YouTube / IG / X]
**Frecuencia:** [X posts/semana]
**Formato dominante:** [...]
**Top 3 temas recurrentes:** [...]
**Cara visible:** [founder / equipo / faceless]
**Engagement promedio:** [aproximado]
```

---

## 6. Social Proof

**Preguntas a responder:**
- ¿Cuántos casos de éxito públicos tienen?
- ¿Casos con números o solo testimonios cualitativos?
- ¿Logos de clientes visibles? (¿son reales o stock?)
- ¿Reviews en Google / Trustpilot / G2?
- ¿Menciones en prensa o podcasts?

**Red flags a detectar:**
- Mismos 3 testimonios en toda la web → poco volumen real
- Logos sin caso asociado → permission marketing dudoso
- Solo screenshots de WhatsApp con "este cliente facturó X" → bajo nivel de proof
- Casos sin nombre del cliente → puede ser inventado o NDA real, investigar

**Output esperado:**
```
**Casos públicos detectados:** [N casos]
**Calidad del proof:** [Alto / Medio / Bajo + razón]
**Logos destacados:** [si hay clientes reconocibles]
**Reviews externas:** [Google/Trustpilot/G2 — rating + nº]
**Apariciones en medios:** [...]
```

---

## 7. Equipo y Operación

**Preguntas a responder:**
- ¿Solopreneur / equipo pequeño / agencia grande?
- ¿Empleados full-time o red de freelancers?
- ¿Tienen ofertas de trabajo activas? (revela qué están escalando)
- ¿Modelo de delivery? (self-serve / done-with-you / done-for-you)
- ¿Ubicación geográfica del equipo?

**Cómo investigar:**
- LinkedIn de la empresa → tamaño real del equipo
- LinkedIn del founder → conexiones que se identifican como "trabajando en [agencia]"
- Glassdoor / LinkedIn Jobs → ofertas activas
- Página "About" / "Equipo" de la web

**Output esperado:**
```
**Tamaño aproximado del equipo:** [solopreneur / 2-5 / 6-15 / 15+]
**Modelo:** [in-house / freelancers / mixto]
**Ubicación:** [remoto / city-based]
**Modelo de delivery:** [DFY / DWY / self-serve]
**Roles que están contratando:** [si los hay — revela prioridades]
```

---

## Estructura final del análisis individual (Modo Lupa)

Cada competidor analizado debe terminar con esta plantilla cerrada:

```markdown
# [Nombre del competidor]

**Web:** [URL]
**Founder:** [Nombre + LinkedIn]
**Una línea:** [su promesa principal]

## 1. Oferta y Servicios
[...]

## 2. Precios y Modelo
[...]

## 3. Posicionamiento y Mensaje
[...]

## 4. Embudo de Captación
[...]

## 5. Contenido y Autoridad
[...]

## 6. Social Proof
[...]

## 7. Equipo y Operación
[...]

## 🎯 Síntesis estratégica

**3 cosas que hacen MEJOR que el promedio:**
1. [...]
2. [...]
3. [...]

**3 cosas que hacen PEOR o no hacen:**
1. [...]
2. [...]
3. [...]

**Implicación para [usuario/agencia]:**
[Qué hacer con esta info — copiar, evitar, contrarrestar]

**Fuentes consultadas:**
- [URL 1]
- [URL 2]
- [...]
```
