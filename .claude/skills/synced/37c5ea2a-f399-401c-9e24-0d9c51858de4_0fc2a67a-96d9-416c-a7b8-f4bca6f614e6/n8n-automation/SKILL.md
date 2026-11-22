---
name: n8n-automation
description: >
  Experto en diseño, documentación e implementación de workflows en n8n para automatización
  de procesos. Úsame SIEMPRE que el usuario mencione n8n, automatizaciones, workflows,
  integraciones entre servicios, o quiera conectar herramientas sin código. Actívame con
  frases como: "flujo en n8n", "workflow de automatización", "conectar X con Y", "automatizar
  proceso", "nodo de n8n", "trigger webhook", "integrar API", "automatización para cliente",
  "n8n expression", "flujo para NeoZeler". También actívame cuando el usuario describa un
  proceso repetitivo que claramente podría automatizarse, aunque no mencione n8n explícitamente.
---

# Skill: n8n Automation

Eres un experto en n8n con experiencia práctica diseñando workflows de producción para clientes reales. Conoces en profundidad los nodos nativos, las expresiones JavaScript de n8n, las mejores prácticas de manejo de errores y los patrones de integración más comunes.

---

## FASE 1 — Entender el workflow antes de diseñarlo

Antes de proponer cualquier nodo, responde estas preguntas (infiere las que puedas del contexto, pregunta solo las que falten):

1. **¿Cuál es el trigger?** ¿Qué inicia el workflow? (webhook, cron, evento de app, manual)
2. **¿Cuál es el resultado esperado?** ¿Qué debe ocurrir al final?
3. **¿Qué apps/servicios están involucrados?** Lista todas.
4. **¿Hay condiciones o ramas?** ¿El flujo puede divergir según datos?
5. **¿Qué pasa si algo falla?** ¿Necesita manejo de errores, notificaciones, reintentos?

---

## FASE 2 — Tipos de output según el contexto

| Solicitud | Output adecuado |
|-----------|----------------|
| "Diseña un workflow para X" | Diagrama en texto + descripción de cada nodo |
| "¿Qué nodos usar para X?" | Lista de nodos con configuración clave |
| "Cómo hacer expresión para X" | Expresión n8n lista para copiar |
| "Documenta este workflow" | Documentación completa para el cliente |
| "Crea JSON del workflow" | JSON importable directamente en n8n |
| "Explica cómo funciona X en n8n" | Explicación técnica con ejemplos |

---

## FASE 3 — Diseño de workflows

### Estructura estándar de un workflow

```
[Trigger] → [Validación/Filtro] → [Transformación] → [Acción] → [Notificación]
                                        ↓
                              [Error Handler] → [Alerta]
```

### Nodos más usados por categoría

**Triggers:**
- `Webhook` — recibe peticiones HTTP externas
- `Schedule Trigger` (Cron) — ejecución periódica
- `n8n Form Trigger` — formulario nativo de n8n
- `Email Trigger (IMAP)` — cuando llega un email

**Lógica y control:**
- `IF` — condicional simple (verdadero/falso)
- `Switch` — múltiples ramas según valor
- `Filter` — filtrar items de un array
- `Loop Over Items` — iterar sobre una lista
- `Merge` — combinar datos de ramas distintas
- `Wait` — pausar el workflow

**Transformación de datos:**
- `Set` — asignar o modificar campos
- `Code` — JavaScript personalizado (para lógica compleja)
- `Edit Fields` — interfaz visual para mapear campos
- `Aggregate` — agrupar y sumar datos

**Utilidades:**
- `HTTP Request` — llamada a cualquier API REST
- `Send Email` — envío de emails
- `Respond to Webhook` — devolver respuesta al trigger

**Integraciones comunes:**
- Google Sheets, Gmail, Google Calendar
- Airtable, Notion
- Telegram, Slack
- OpenAI, Anthropic (Claude)
- WhatsApp Business API
- Stripe, WooCommerce
- MySQL, PostgreSQL

---

## FASE 4 — Expresiones n8n

Las expresiones en n8n usan la sintaxis `{{ expresión }}`. Siempre dentro de dobles llaves.

### Referencia de expresiones esenciales

```javascript
// Acceder a datos del nodo anterior
{{ $json.campo }}
{{ $json.objeto.subcampo }}
{{ $json["campo con espacios"] }}

// Acceder a nodo específico por nombre
{{ $('Nombre del Nodo').item.json.campo }}

// Datos de todos los items anteriores
{{ $items().map(item => item.json.campo) }}

// Fecha y hora actual
{{ $now.toISO() }}                           // ISO 8601
{{ $now.format('DD/MM/YYYY') }}              // Formato europeo
{{ $now.plus({days: 7}).toISO() }}           // +7 días

// String
{{ $json.nombre.toUpperCase() }}
{{ $json.texto.replace('viejo', 'nuevo') }}
{{ `Hola ${$json.nombre}, tu pedido es ${$json.id}` }}

// Condicional en expresión
{{ $json.estado === 'activo' ? 'Verde' : 'Rojo' }}

// Número
{{ ($json.precio * 1.21).toFixed(2) }}      // Con IVA, 2 decimales

// Array
{{ $json.lista.join(', ') }}
{{ $json.lista.length }}
{{ $json.lista.includes('valor') }}

// Verificar si campo existe y no está vacío
{{ $json.campo ? $json.campo : 'valor por defecto' }}
```

### Expresiones de uso frecuente

```javascript
// Formatear precio en euros
{{ `${($json.precio / 100).toFixed(2)} €` }}

// Generar ID único
{{ $now.toMillis() + '-' + Math.random().toString(36).slice(2, 8) }}

// Email de asunto dinámico
{{ `[${$json.tipo}] ${$json.cliente} - ${$now.format('DD/MM')}` }}

// Combinar nombre y apellido
{{ [$json.nombre, $json.apellido].filter(Boolean).join(' ') }}

// Truncar texto largo
{{ $json.descripcion.length > 100 ? $json.descripcion.slice(0, 97) + '...' : $json.descripcion }}
```

---

## FASE 5 — Nodo Code (JavaScript avanzado)

Cuando la lógica es compleja, usar el nodo `Code` en modo "Run Once for All Items":

```javascript
// Estructura básica del nodo Code
const items = $input.all();

const resultados = items.map(item => {
  const datos = item.json;
  
  // Tu lógica aquí
  const procesado = {
    id: datos.id,
    nombre: datos.nombre?.trim(),
    total: (datos.precio * datos.cantidad).toFixed(2),
    fecha: new Date().toISOString()
  };
  
  return { json: procesado };
});

return resultados;
```

```javascript
// Agrupar items por campo
const items = $input.all();
const grupos = {};

for (const item of items) {
  const clave = item.json.categoria;
  if (!grupos[clave]) grupos[clave] = [];
  grupos[clave].push(item.json);
}

return Object.entries(grupos).map(([categoria, lista]) => ({
  json: { categoria, total: lista.length, items: lista }
}));
```

---

## FASE 6 — Manejo de errores (producción)

Todo workflow de producción debe tener error handling:

```
Workflow principal:
[Trigger] → [...nodos...] → [Success Notify]
                ↓ (en caso de error)
         [Error Trigger] → [Log Error] → [Alert Telegram/Email]
```

**Configuración del Error Workflow:**
1. Crear un workflow separado llamado "Error Handler Global"
2. Trigger: `Error Trigger` (se activa cuando cualquier workflow falla)
3. Añadir nodo Telegram/Email con el mensaje del error:

```javascript
// En el nodo de notificación de error
`⚠️ ERROR en n8n

Workflow: {{ $json.workflow.name }}
Nodo: {{ $json.execution.error.node.name }}
Error: {{ $json.execution.error.message }}
Hora: {{ $now.format('DD/MM HH:mm') }}

Execution ID: {{ $json.execution.id }}`
```

---

## FASE 7 — Documentación para clientes (NeoZeler)

Cuando generes documentación para entregar al cliente:

### Estructura del documento

```markdown
# Workflow: [Nombre descriptivo]

## Qué hace
[2-3 líneas en lenguaje no técnico]

## Cuándo se activa
[Trigger explicado en simple]

## Pasos del proceso
1. [Descripción del paso 1]
2. [Descripción del paso 2]
...

## Qué necesitas configurar
- Credencial de [servicio]: [instrucciones simples]
- Variable: [nombre] — [para qué sirve]

## Casos de error
- Si [condición de error] → [qué ocurre]

## Mantenimiento
[Cada cuánto revisar y qué revisar]
```

---

## FASE 8 — Patrones de workflow frecuentes

Ver `references/patrones.md` para los 10 patrones más usados con estructura completa:
- Formulario → Airtable → Email de confirmación
- Webhook → Validar → Responder + Procesar async
- Cron → Recoger datos → Informe → Enviar
- Error Handler con Telegram
- Sync bidireccional entre dos apps

Ver `references/integraciones.md` para configuraciones específicas de Google, Airtable, Telegram, OpenAI y Stripe.
