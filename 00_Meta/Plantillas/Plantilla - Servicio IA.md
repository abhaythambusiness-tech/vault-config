---
title: "<% tp.file.title %>"
date: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - ia
  - automatizacion
  - servicio
type: servicio
origen: mixto
status: borrador
nicho: "[[Nicho - <% tp.system.prompt("Nombre del Nicho (ej: Transporte y logística):") %>]]"
related:
---

## 🎯 Descripción General
<% tp.file.cursor() %>

> [!ROI] Cuantificación de Impacto
> - **Tiempo ahorrado estimado**: X horas/semana por operario.
> - **Retorno de inversión (ROI)**: X €/mes en costes operativos.
> - **Riesgo/Complejidad**: Baja / Media / Alta.

> [!AUTOMATION] Flujo n8n & Arquitectura
> ```mermaid
> graph LR
>   A["Entrada: Email / PDF / Webhook"] --> B["Procesamiento: n8n + Gemini AI"]
>   B --> C["Salida: ERP / CRM / WhatsApp Notification"]
> ```

> [!AI] Prompt / Prompt System Base
> ```markdown
> Eres un agente de IA especializado en...
> ```

## 📋 Requisitos de Integración
- [ ] API Key / Credenciales del cliente.
- [ ] Webhook de entrada configurado.
- [ ] Formato de datos de salida validado.

---
## 🔗 Relacionado
- [[NeoZeler - MOC]]
