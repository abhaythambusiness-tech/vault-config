---
title: "Onboarding - {{cliente}}"
date: {{fecha}}
tags:
  - onboarding
  - neozeler
  - cliente
  - agente-ia
type: proyecto
origen: mixto
status: en-progreso
cliente: "{{cliente}}"
sector: "{{sector}}"
referencia: "{{referencia}}"
fase: "Fase 0 - Onboarding"
related:
  - "[[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler]]"
  - "[[Propuesta - {{cliente}}]]"
---

> [!cliente] Status del Cliente
> **Fase actual:** Fase 0 — Onboarding técnico y comercial
> **Responsable NeoZeler:** {{responsable}}
> **Contacto cliente:** {{contacto_cliente}}

## 🗺️ Resumen y flujo del sistema

Breve descripción del sistema a implementar (2-3 líneas): qué hace el agente, por qué canal entra el lead, qué automatiza.

**Flujo del sistema:**
1. Entra el lead → {{origen_leads}}
2. El agente IA cualifica → {{canal_agente}}
3. Se agenda → {{tipo_cita}}
4. Atiende el equipo → {{quien_atiende}}

---

## 1. Accesos técnicos

### 1.1 CRM
- [ ] Invitar como admin a `{{email_neozeler}}`
- [ ] Confirmar landing vinculada al CRM
- [ ] Confirmar número de WhatsApp conectado
- [ ] Confirmar pipeline / etapas montadas

> [!question] Etapas del pipeline
> {{etapas_pipeline}}

### 1.2 Meta Business
- [ ] Meta Business verificado (obligatorio para WhatsApp Business API)
- [ ] Control total sobre el portfolio
- [ ] Acceso concedido a `{{email_neozeler}}`

### 1.3 Número de teléfono (si no hay en el CRM)
- [ ] Crear cuenta en proveedor de telefonía
- [ ] Verificación de identidad
- [ ] Adquirir número
- [ ] Método de pago con auto-recarga
- [ ] Credenciales de acceso: `{{tel_email}}` / `{{tel_pass}}`

### 1.4 OpenAI
- [ ] Crear cuenta
- [ ] Configurar método de pago
- [ ] Activar auto-recarga
- [ ] Credenciales: `{{openai_email}}` / `{{openai_pass}}`

### 1.5 Calendario
- [ ] ¿Usa Google Calendar? {{google_calendar_si_no}}
- [ ] Correo con el que se gestiona: `{{cal_email}}`
- [ ] Nombre del calendario a integrar: `{{cal_nombre}}`
- [ ] Horarios operativos: `{{horarios}}`

> [!example]- Credenciales de API de Google Calendar (colapsable)
> - [ ] Proyecto creado y Google Calendar API activada
> - [ ] Credenciales OAuth creadas
> - ID de cliente: `{{gc_client_id}}`
> - Clave secreta: `{{gc_client_secret}}`

---

## 2. Información del negocio
- **Nombre de la empresa / marca:** {{empresa}}
- **Web y redes sociales:** {{web_redes}}
- **Descripción del servicio:** {{descripcion_servicio}}
- **Catálogo / precios:** {{catalogo_precios}}
- **Idiomas de atención:** {{idiomas}}

---

## 3. Avatar del cliente

> [!tip] Perfil de cliente identificado
> {{avatar_principal}}

- [ ] ¿Avatar adicional? {{avatar_adicional}}

---

## 4. Cualificación del lead

Información que el agente debe recoger:
- {{dato_1}}
- {{dato_2}}
- {{dato_3}}

- **¿Qué hace que un lead sea BUENO?** {{criterio_bueno}}
- **¿Qué lo descarta?** {{criterio_descarte}}
- **¿Presupuesto mínimo?** {{presupuesto_minimo}}

---

## 5. Tono y estilo de comunicación
- **Tuteo o usted:** {{trato}}
- **Tono:** {{tono}}
- **Emojis:** {{emojis}}
- **Presentación del agente:** {{presentacion_agente}}

> [!riesgo] Regla Crítica: El agente NUNCA debe decir
> {{nunca_decir}}

---

## 6. Seguimientos y recordatorios
- **1er follow-up sin respuesta:** {{followup_tiempo}}
- **Máximo de follow-ups:** {{followup_max}}
- **Recordatorio de cita:** {{recordatorio_cita}}
- **Política de reagendamiento:** {{reagendamiento}}

---

## 7. Derivación a humano
- **Contacto de derivación:** {{contacto_derivacion}}
- **Casos de derivación inmediata:** {{casos_derivacion}}
- **Horario de disponibilidad:** {{horario_derivacion}}

---

## 8. Preguntas frecuentes

| Pregunta | Respuesta tipo |
|---|---|
| {{faq_1_p}} | {{faq_1_r}} |
| {{faq_2_p}} | {{faq_2_r}} |
| {{faq_3_p}} | {{faq_3_r}} |

---

## ✅ Checklist de entregables

**Accesos**
- [ ] CRM (admin + configuración confirmada)
- [ ] Meta Business verificado
- [ ] Número de teléfono / WhatsApp
- [ ] OpenAI con pago activo
- [ ] Calendario y credenciales API

**Información**
- [ ] Datos de empresa, catálogo e idiomas
- [ ] Avatar de cliente
- [ ] Criterios de cualificación y descarte
- [ ] Tono y estilo definidos
- [ ] Seguimientos y recordatorios configurados
- [ ] Derivación a humano definida
- [ ] FAQ con respuestas

---

## 📅 Log
### {{fecha}}
Kick-off del proyecto. {{notas_iniciales}}

---
## 🔗 Relacionado
- [[02_Areas/NeoZeler/NeoZeler - MOC|NeoZeler]]
- [[Propuesta - {{cliente}}]]
- [[Fase 1 - {{cliente}}]]
