---
type: sesion
date: '2026-10-26'
proyecto: '[[01_Projects/Neozeler CRM]]'
tags:
- diseno
- crm
origen: mixto
---

> [!resumen] En cristiano
> Los diseños salían genéricos, así que se creó una regla nueva: cada proyecto necesita una «identidad» aprobada antes de maquetar, con colores sacados de la marca, un nivel de movimiento y un flujo para las imágenes que faltan (parar y preguntar). Se probó rehaciendo el CRM de NeoZeler, que ya está en producción con la nueva cara.

## Qué se hizo
- Regla `~/.claude/rules/identidad-y-dinamismo.md`, plantilla de identidad y registro de identidades visuales; replicado en los GEMINI.md y el flujo de 6 documentos (sesión aparte).
- CRM: dirección «Escaparates» (elegida entre 3), 288 capturas reales de webs, cabecera nueva, portada de campaña, fichas con ventana de navegador, todas las pantallas.

## Aprendizajes
- Un rediseño cubre el marco y **todas** las pantallas, no una (error #67).
- La paleta sale del logo y la guía de la marca, no de la imaginación (error #68): el primer intento usó amarillo y cobalto, que no son de NeoZeler.
- Al subir al servidor: no hacer `git add` de carpetas con imágenes generadas (se coló en un commit y hubo que reescribirlo); `pkill -f` y `$VAR:` en zsh vuelven a dar guerra (#64).


## Resumen completo de la sesión (cierre)

> [!resumen] En cristiano
> Se creó una regla para que los diseños tengan personalidad (identidad de marca antes de maquetar, movimiento con criterio y, si falta una imagen, parar y preguntar). Se probó rehaciendo el CRM de NeoZeler, que ya está en producción con cara nueva, botón de envío diario y el envío de correos pasado a un n8n en un VPS sin SMTP.

### Hecho
1. **Sistema de diseño**: regla `~/.claude/rules/identidad-y-dinamismo.md`, plantilla `Plantilla - Identidad de Proyecto`, `Registro de Identidades Visuales`, y replicado en CLAUDE.md global, CLAUDE.md del vault y los dos GEMINI.md. Otra sesión (fork) lo integró en el flujo de 6 documentos y en `/nuevo-proyecto`.
2. **CRM, identidad «Escaparates»** (elegida entre 3 maquetas): cabecera clara con navegación en pastillas, portada de campaña (contactados y días de oferta), embudo en tira, fichas con la web real del negocio dentro de una ventana de navegador. Colores corregidos a los de NeoZeler (azul, marino, hielo del logo). Letras Bricolage Grotesque y DM Mono autoalojadas. Aplicado a Hoy, Negocios, Campaña y Ajustes.
3. **288 capturas reales** de webs (script local `~/Proyectos/crm-capturas/capturar.py`), subidas al CRM; 3 faltan.
4. **Correos 1/2/3 compactos** en una fila por ficha; aviso de solo lectura una vez por página.
5. **Botón «Enviar los 10 de hoy»** (`src/cola.ts`): seguimientos primero (correo 3 a ≥4 días, correo 2 a ≥3 días), luego correos 1; uno cada 20 s en segundo plano; sin cola persistente.
6. **n8n en VPS**: flujo simple sin SMTP de 5 nodos (`n8n/flujo-correos-simple.json`, Gmail OAuth2); n8n contesta en la misma petición (el CRM ya no necesita callback); el token viaja en `X-CRM-Token` y en `Authorization`. Correo de prueba idéntico al real (remitente «NeoZeler», firma «El equipo de NeoZeler»).
7. **Datos de prueba**: id 292 «Panadería La Espiga» (southway665) y 293 «Taller Mecánico Ruiz» (aboueladebhaytham), ya sin el nombre de Haytham.
8. Todo con copia de seguridad previa y comprobación antes/después; 78 tests pasan; commits en el repo del servidor.

### Aprendizajes no obvios
- Un rediseño cubre el marco y **todas** las pantallas (error #67) y la paleta sale del logo y la guía (#68).
- La credencial «Header Auth» de n8n lee la cabecera que se le configure (aquí `Authorization`): el CRM manda las dos.
- Un VPS no alcanza `192.168.x.x`: por eso n8n responde en la misma petición.
- `pkill -f`/`kill` dentro de un `ssh` con el patrón en la propia línea mata la shell; usar `fuser -k PUERTO/tcp`. `git add` de carpetas con imágenes generadas las mete al repo (hubo que reescribir el commit).
- Los despliegues a producción necesitan autorización expresa en cada vuelta (el sistema los bloquea si no).

### Pendiente de Haytham
- Pegar el nodo «Redactar» actualizado en n8n y probar **Enviar** en el 292.
- Pasar `MODO` a `'enviar'` cuando dé el visto bueno; precios (setup máx. 700 €, cuota con dominio y alojamiento) y cambiar el PIN.
- Opcional: más identidades en el registro (barber-df, reto-30) al volver a tocarlos.
