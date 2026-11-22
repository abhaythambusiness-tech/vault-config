---
type: sesion
date: '2026-10-26'
proyecto: '[[01_Projects/Neozeler CRM]]'
tags:
- crm
- n8n
- impeccable
- diseno
origen: mixto
---

> [!resumen] En cristiano
> Se auditó el CRM con las skills de diseño y se **rehízo a medida** del embudo nuevo: tarjetas de negocios con los botones de correo 1, 2 y 3 (que avisan a n8n), pantalla «Hoy» con el embudo y «con quién empezar», ficha con «Ahora toca», demo gratuita agendable y una pantalla «Campaña» con la oferta editable (50 % en el setup + demo gratuita). **Se quitaron el Plan Fundadores y el envío por Gmail.**

## Qué se hizo
- **n8n** instalado en el servidor (Docker, `192.168.0.100:5678`) y webhook en las dos direcciones (CRM → n8n y n8n → CRM con token).
- **Auditoría `impeccable`**: detector sobre las pantallas + capturas de escritorio y móvil + revisión de código. Hallazgos principales: Plan Fundadores en todo el producto, chip de «Simulación» sin sentido, «Hoy» con medidores vacíos, lista sin acciones, bordes laterales de acento, etiquetas en mayúsculas, gris sobre color.
- **Reforma**: migración v4 (se retiran cola, campañas y logo de los correos), módulos nuevos `oferta.ts` y `vistas/campana.ts`, tarjetas con camino de etapa, llamar y WhatsApp, pestañas de etapa, «Ahora toca», `/candidatos/:id/demo`, aviso de correos que n8n no devuelve.
- **Pruebas**: 68 en verde, tipos limpios, ciclo completo en producción y comprobación visual con una copia de la base.
- Documentación: `PRODUCT.md` (contexto del producto para `impeccable`), `README.md`, ficha del proyecto y CLAUDE.md/GEMINI.md.

- **Flujo de n8n** «CRM NeoZeler · correos 1, 2 y 3»: webhook con token → redactar → (simulación | borrador | enviar) → avisar al CRM con el enlace; importado por la línea de comandos de n8n con una credencial cifrada. Probado de punta a punta con el candidato «Prueba Haytham» (correos 1, 2 y 3 en estado listo).

## Aprendizajes
- **Una copia de la base lleva la dirección del n8n real**: pulsar «Enviar» en la copia habría disparado el flujo de verdad. Se apuntó la copia a un «n8n» local de mentira antes de probar.
- La dirección del webhook con `localhost` no llega: n8n escucha solo en la IP de la red; el aviso de error ya lo explica.
- No filtrar la salida de `bun test` con «Received»: vuelca el HTML entero.
- `pkill -f` con el patrón en el comando mata la propia sesión SSH (ya estaba en COMMON_MISTAKES #64): parar por puerto.
- `docker cp` deja los archivos como `root`: para `n8n import:credentials` hay que hacer `chown node` dentro del contenedor y borrar el archivo con el token después.
