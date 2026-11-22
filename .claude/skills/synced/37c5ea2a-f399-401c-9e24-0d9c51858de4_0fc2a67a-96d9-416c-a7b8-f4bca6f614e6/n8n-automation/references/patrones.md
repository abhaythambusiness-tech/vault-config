# Patrones de Workflow n8n — Referencia

Los 10 patrones más usados en proyectos reales.

---

## 1. Formulario → Base de datos → Confirmación por email

```
[n8n Form Trigger]
    → [Set] (limpiar y estructurar datos)
    → [Airtable: Create Record]
    → [Send Email] (confirmación al usuario)
    → [Telegram] (notificación interna al equipo)
```

**Nodo Set** — mapear campos del formulario a la estructura de Airtable:
- `nombre`: `{{ $json.nombre.trim() }}`
- `email`: `{{ $json.email.toLowerCase() }}`
- `fecha_registro`: `{{ $now.toISO() }}`

---

## 2. Webhook → Validar → Responder + procesar async

```
[Webhook Trigger]
    → [IF] (¿tiene los campos requeridos?)
        → SI: [Respond to Webhook] (200 OK) → [Procesar datos...]
        → NO: [Respond to Webhook] (400 Bad Request)
```

**Clave**: El nodo "Respond to Webhook" debe ir antes del procesamiento pesado para no hacer esperar al cliente que hizo la petición.

---

## 3. Cron → Recoger datos → Informe → Enviar

```
[Schedule Trigger] (cada día a las 8:00)
    → [HTTP Request] (API o Airtable)
    → [Code] (calcular métricas)
    → [Send Email] (informe formateado en HTML)
```

**Nodo Code** para calcular métricas:
```javascript
const items = $input.all();
const datos = items.map(i => i.json);

const total = datos.length;
const completados = datos.filter(d => d.estado === 'completado').length;
const pendientes = total - completados;

return [{
  json: {
    total,
    completados,
    pendientes,
    tasa_completitud: `${((completados/total)*100).toFixed(1)}%`,
    fecha: new Date().toLocaleDateString('es-ES')
  }
}];
```

---

## 4. Error Handler con Telegram

Workflow separado "Error Handler":

```
[Error Trigger]
    → [Set] (formatear mensaje de error)
    → [Telegram: Send Message]
```

**Nodo Set** con el mensaje:
```
⚠️ ERROR en n8n
━━━━━━━━━━━━━━━━
Workflow: {{ $json.workflow.name }}
Nodo: {{ $json.execution.error.node?.name || 'desconocido' }}
Error: {{ $json.execution.error.message }}
━━━━━━━━━━━━━━━━
🕐 {{ $now.format('DD/MM HH:mm:ss') }}
🆔 {{ $json.execution.id }}
```

En cada workflow de producción: Settings → Error Workflow → seleccionar "Error Handler".

---

## 5. Sync entre dos apps (one-way)

```
[Schedule Trigger] (cada hora)
    → [App A: Get Records] (modificados en última hora)
    → [IF] (¿el registro existe en App B?)
        → SÍ: [App B: Update Record]
        → NO: [App B: Create Record]
```

**Filtrar por fecha de modificación**:
```javascript
// En el nodo de App A, filtrar registros modificados en las últimas 2 horas
// (el overlap de 2h evita perder registros en el límite)
const dosHorasAtras = $now.minus({hours: 2}).toISO();
// Usar como filtro en el nodo
```

---

## 6. Clasificación con IA (OpenAI/Claude)

```
[Webhook o Trigger]
    → [HTTP Request] (API de OpenAI/Claude)
    → [Switch] (según clasificación devuelta)
        → "urgente": [Notificar inmediatamente]
        → "normal": [Añadir a cola]
        → "spam": [Ignorar/Archivar]
```

**Prompt de clasificación en el HTTP Request**:
```json
{
  "model": "claude-haiku-4-5-20251001",
  "max_tokens": 50,
  "messages": [{
    "role": "user",
    "content": "Clasifica este mensaje como 'urgente', 'normal' o 'spam'. Responde SOLO con una de esas tres palabras.\n\nMensaje: {{ $json.mensaje }}"
  }]
}
```

---

## 7. Notificaciones multi-canal

```
[Trigger]
    → [Switch] (según preferencia del usuario o tipo de evento)
        → email: [Send Email]
        → telegram: [Telegram: Send Message]
        → whatsapp: [HTTP Request a WhatsApp API]
        → slack: [Slack: Send Message]
```

---

## 8. Rate limiting / Cola de procesamiento

Para APIs con límite de peticiones:

```
[Trigger recibe muchos items]
    → [Loop Over Items]
        → [HTTP Request]
        → [Wait] (1 segundo entre peticiones)
```

**Nodo Wait**: configurar en 1000ms para respetar límites de 1 req/seg.

---

## 9. Webhook con autenticación básica

Validar que el webhook viene de quien debe venir:

```
[Webhook Trigger]
    → [IF] (¿header de autenticación es correcto?)
        → SÍ: [Procesar...]
        → NO: [Respond to Webhook] (401 Unauthorized)
```

**Expresión para verificar token**:
```javascript
// En el nodo IF
{{ $json.headers['x-api-key'] === 'tu-token-secreto' }}
```

---

## 10. Procesamiento de email entrante

```
[Email Trigger (IMAP)]
    → [IF] (¿asunto contiene palabra clave?)
        → SÍ: [Extraer datos del cuerpo] → [Acción]
        → NO: [Ignorar]
```

**Extraer datos del cuerpo del email**:
```javascript
// Nodo Code para parsear el cuerpo del email
const cuerpo = $json.text || '';
const lineas = cuerpo.split('\n');

// Buscar patrón "Campo: valor"
const datos = {};
for (const linea of lineas) {
  const match = linea.match(/^(.+?):\s*(.+)$/);
  if (match) datos[match[1].trim()] = match[2].trim();
}

return [{ json: datos }];
```
