# Stack NeoZeler

Principio: **la demo se monta con coste de infraestructura cero**. Todo lo que se pueda autoalojar, se autoaloja. Lo que cueste dinero obligatoriamente, o se descarta del catálogo o se traslada al cliente de forma explícita en la ficha.

## Piezas validadas

| Función | Herramienta | Coste | Notas |
|---------|------------|-------|-------|
| Motor de flujos | n8n autoalojado | Gratis | Base de todo el portafolio. Ver [[n8n-automation]] |
| Cerebro conversacional | API de LLM | Céntimos por conversación | Único coste variable aceptable |
| Base de datos + búsqueda semántica | PostgreSQL con pgvector | Gratis | Alternativa: Qdrant autoalojado |
| Canal de mensajería | WhatsApp Cloud API (tramo gratuito) | Gratis | Alternativa: widget web propio |
| Canal interno / escalado a humano | Telegram o email | Gratis | Siempre debe existir una salida a persona |
| Entrada de datos del cliente | Export CSV nocturno del ERP | Gratis | Evita pedir acceso al ERP en la primera fase |
| Formularios y cualificación | Tally | Gratis | Usado en el [[NeoZeler - Diagnóstico IA]] |
| Documentos e imágenes | OCR + extracción con LLM | Céntimos | Base de los servicios de albaranes, partes y facturas |

## Fuera del catálogo

| Pieza | Motivo |
|-------|--------|
| Telefonía / agentes de voz (Twilio, Vapi, Retell) | Coste obligatorio sin tramo gratuito. Se cotiza aparte y se traslada al cliente si lo pide expresamente |
| Cualquier SaaS con mínimo mensual por cliente | Rompe el margen en clientes pequeños y ata la demo a una suscripción |

## Criterios al añadir una pieza nueva

1. ¿Existe versión autoalojada o tramo gratuito real? Si no, busca alternativa antes de aceptarla.
2. ¿El coste escala con el número de clientes o es fijo? El coste por cliente hay que reflejarlo en la cuota mensual.
3. ¿Puedo replicar el montaje para el siguiente cliente sin rehacerlo? Si no, no es stack, es artesanía.
4. Si la pieza es de pago inevitable, la ficha lo dice en la columna de coste y el precio del servicio lo absorbe.

## Patrón de arquitectura recurrente

Casi todos los servicios del portafolio son el mismo esqueleto:

```
Entrada (WhatsApp / email / formulario / archivo)
  → Normalización con LLM (limpiar, estructurar, enriquecer)
  → Almacén consultable (PostgreSQL + pgvector)
  → Agente con herramientas acotadas
  → Propuesta de acción
  → Validación humana
  → Escritura en el sistema del cliente + contador de la métrica
```

Cuando diseñes un servicio nuevo, empieza por encajar el dolor en este esqueleto. Si encaja, es un servicio del catálogo. Si no encaja, justifica por qué antes de seguir.
