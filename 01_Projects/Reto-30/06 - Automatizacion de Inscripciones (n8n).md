---
date: '2026-10-12'
negocio: Factory Training
proyecto: '[[01_Projects/Reto-30/RETO 30 - MOC|RETO 30]]'
status: activo
tags:
- reto-30
- n8n
- airtable
- tally
- automatizacion
type: proyecto
origen: mixto
---

# 06 — Automatización de Inscripciones (n8n)

> Lo único construido hasta ahora además del logo: del formulario de inscripción al CRM y al correo de bienvenida, sin intervención manual.

## Enlaces
- Flujo n8n: https://n8n-n8n.bxecw5.easypanel.host/workflow/sOPUdIStFLNTKnDB
- Base de datos / CRM (Airtable `reto30_inscripciones`): https://airtable.com/appIqXk2gT78KfTQN/pagsFpEtqOfhjXr4R
- Formulario: Tally, formId `VL264E` ("Reto 30"). Webhook n8n en la ruta `/webhook/reto30` (POST).

## Flujo (6 nodos, lineal)
1. **Webhook**: recibe el envío de Tally (`FORM_RESPONSE`).
2. **Code (JS)**: normaliza los datos. Capitaliza nombre y apellido, pasa el correo a minúsculas, quita espacios del teléfono y convierte la lesión de ID de opción a "Sí"/"No". El detalle de lesión solo se guarda si la respuesta es "Sí".
3. **Airtable · Search**: busca el correo en la tabla para evitar duplicados.
4. **If**: solo continúa si el correo **no existe** ya.
5. **Airtable · Create**: crea el registro con Nombre, Primer apellido, Edad, Correo, Telefono, Lesion o molestia y Detalle de la lesion.
6. **HTML → Gmail**: envía el correo "Bienvenido a reto 30" con la marca (fondo `#1C1C1C`, acento lima `#CDFF00`). Dice "hemos recibido tu inscripción… si hay plaza te confirmamos", y añade un párrafo extra si el socio declaró una lesión.

## Campos del formulario
Nombre · Primer apellido · Edad · Correo electrónico · Número de teléfono · ¿Tienes alguna lesión o molestia? (Sí/No) · Detalle de la lesión (condicional).

## Estado y huecos conocidos
- **Funciona**: inscripción → registro en CRM → correo automático. Probado con un envío de prueba (2026-10-02).
- **No existe aún**: la demo web de la app. La del [[00_Meta/Sesiones/2026-10-06 - MCP de shadcn y demo RETO 30|2026-10-06]] solo está en local y no está desplegada. Tampoco hay microvídeos, cobro ni acceso al reto.
- **Duplicados**: si el correo ya existe, el flujo termina en silencio y el socio no recibe nada.
- **Webhook sin verificación de firma**: cualquiera con la URL puede enviar datos. Pendiente de activar la firma de Tally.
- **Filtro de Airtable**: el correo se interpola directo en la fórmula `{Correo} = '...'`. Conviene escapar comillas.
- **Datos de salud (lesiones)**: son datos sensibles bajo RGPD. Falta aviso de privacidad y consentimiento en el formulario.
- **Sin pago**: el correo habla de "plaza", pero no hay cobro ni lista de espera.
- **Credenciales**: están en n8n (Airtable PAT y Gmail OAuth "pagina web"). No se guardan en el vault.

## Pendiente
- [ ] Decidir el precio (15-20 € en [[01_Projects/Reto-30/01 - Propuesta y Modelo de Negocio|01]] frente a 10-15 € en el [[01_Projects/Reto-30/RETO 30 - MOC|MOC]]).
- [ ] Segundo correo de confirmación de plaza, con el acceso.
- [ ] Mensaje de "ya estabas inscrito" para los duplicados.

