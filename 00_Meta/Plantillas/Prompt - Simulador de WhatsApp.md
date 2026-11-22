---
title: "Prompt - Generador de Simulador de WhatsApp para Demos"
date: 2026-08-04
tags:
  - prompt
  - herramientas
  - ventas
type: plantilla
origen: humano
---

# 🤖 Prompt para generar el Simulador de WhatsApp

Copia y pega este prompt en v0.dev, Claude 3.5 Sonnet, o Cursor para generar tu aplicación.

***

**Actúa como un Desarrollador Frontend Experto en React, Tailwind CSS y UI/UX.**

Quiero que construyas una aplicación web de una sola página (SPA) que replique la interfaz de WhatsApp Web (o móvil). El propósito de esta app es realizar **demostraciones interactivas a clientes** de cómo funcionan nuestros agentes de IA (automatizados con n8n).

### 🛠 Funcionalidades Core:
1. **Gestor de Instancias (Pantalla Inicial):**
   - Al abrir la app, no debe mostrar el chat directamente, sino un panel para seleccionar o crear "Instancias de Demo" (ej. "Demo Presupuesto", "Demo Centralita").
   - Para crear una instancia, el usuario debe introducir:
     - Nombre de la instancia.
     - Nombre del Contacto (ej. "Asistente NeoZeler").
     - **URL del Webhook** (Este es el endpoint de n8n que recibirá los mensajes).
   - Las instancias deben guardarse en el `localStorage` del navegador para no tener que configurarlas en cada reunión.

2. **Interfaz de Chat (Clon de WhatsApp):**
   - Diseño idéntico a WhatsApp: fondo característico (color beige o el doodle de WhatsApp), burbujas verdes para el usuario (derecha) y blancas para el bot (izquierda).
   - Cabecera con el nombre del contacto y un botón para "Volver a instancias".
   - Input de texto en la parte inferior con botón de enviar. Opcionalmente, icono de micrófono y clip (solo visuales por ahora).

3. **Lógica de Conexión (El Motor):**
   - Cuando el usuario escribe y envía un mensaje:
     1. La burbuja del usuario aparece inmediatamente en el chat.
     2. Aparece un indicador de "escribiendo..." simulando que la IA está procesando.
     3. La app hace un `POST fetch` a la **URL del Webhook** configurada en esa instancia.
     4. El payload que envía la app debe ser:
        ```json
        {
          "sessionId": "id_generado_aleatorio_por_instancia",
          "message": "texto del usuario",
          "timestamp": "fecha_y_hora"
        }
        ```
     5. El webhook de n8n procesará esto y terminará con un nodo "Respond to Webhook". La app debe esperar esa respuesta síncrona.
     6. Al recibir el `200 OK` con el JSON de respuesta del webhook, la app oculta el "escribiendo..." y muestra la burbuja de respuesta del bot con el texto devuelto. (El JSON de respuesta de n8n debería tener un formato como `{"reply": "texto de respuesta"}`).

### 🎨 Requisitos Técnicos y de Diseño:
- Usa **React** y **Tailwind CSS**.
- Usa componentes de **Lucide React** para los iconos (flechas, enviar, adjuntar).
- La UI debe ser **responsive**, viéndose bien tanto en móvil (para enseñarlo en un teléfono al cliente) como en vista de escritorio (tipo WhatsApp Web).
- Manejo de errores: Si el webhook falla o da timeout (ej. si n8n está apagado), muestra una pequeña alerta de error sin romper la app.
- Agrega un botón de "Limpiar Chat" en la cabecera para reiniciar la conversación rápidamente en medio de una demo.

Por favor, genera el código completo en un solo archivo (o estructura clara de componentes) listo para probarse.
