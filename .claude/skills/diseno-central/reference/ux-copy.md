# UX copy (Fase 4)

Texto de interfaz con valores concretos. Origen: `design:ux-copy` (se puede invocar para variantes). Voz de marca: `DESIGN-IDENTITY.md` / `PRD §11`; sin voz definida, preguntar una vez.

## Principios (orden de prioridad)

1. **Claro**: lo que pasa y qué hacer. Sin jerga ni siglas sin traducir.
2. **Corto**: las menos palabras que dicen todo. Botón 1-3 palabras; título de error ≤ 6.
3. **Consistente**: un término por cosa en toda la app (no «Proyecto» y «Espacio» para lo mismo). Anotar el glosario en la identidad.
4. **Útil**: cada palabra ayuda a avanzar. Fuera adornos y disculpas vacías.
5. **Humano**: persona útil, no robot. Segunda persona, voz activa, sin culpar al usuario.

## Patrones

| Elemento | Fórmula | Bien | Mal |
|---|---|---|---|
| **CTA / botón** | Verbo + objeto real | «Crear cuenta», «Guardar cambios» | «Enviar», «OK», «Click aquí» |
| **Error** | Qué pasó + por qué + cómo arreglarlo | «Pago rechazado. Tu banco lo bloqueó. Prueba otra tarjeta.» | «Error 402» |
| **Estado vacío** | Qué es + por qué está vacío + primer paso | «Aún no hay proyectos. Crea el primero para invitar a tu equipo.» | «No hay datos» |
| **Confirmación** | Acción concreta + consecuencia; botones = verbos | «¿Borrar 3 archivos? No se puede deshacer.» [Borrar] [Conservar] | «¿Seguro?» [OK] [Cancelar] |
| **Carga** | Qué se hace + espera si > 2 s | «Calculando tu informe…» | «Cargando» |
| **Éxito** | Confirmar el resultado, sin fiesta | «Cambios guardados» | «¡¡Genial!! 🎉» |
| **Tooltip** | Solo lo no obvio | «Oculta el precio al cliente» | «Botón de precio» |
| **Onboarding** | Un concepto por paso | «Paso 1 de 3: conecta tu calendario» | Muro de texto |
| **Formulario** | Etiqueta visible + ayuda bajo el campo + error junto al campo | «Teléfono (para avisarte del pedido)» | Solo placeholder |

## Tono por contexto

Éxito: sobrio y positivo · Error: empático y accionable · Aviso: claro, con la acción · Neutro: informativo · Destructivo: serio, sin humor.

## Reglas duras

- Nunca Lorem ni «Texto aquí» (Fase 2).
- Sin mayúsculas gritadas ni más de un signo de exclamación por pantalla.
- Sin culpar: «No pudimos guardar» y no «Introdujiste mal el dato».
- Longitud: previsto +30 % al traducir; botones sin romper a 375 px.
- Todo lo que no es texto visible también cuenta: `aria-label`, `alt`, títulos de pestaña, meta descripción.
- Textos de oferta/precio/promesa de la landing: vienen de `oferta-central` (no inventarlos aquí).

## Revisión rápida (antes de Fase 6)

☐ Cada botón dice la acción · ☐ cada error trae solución · ☐ cada vacío trae primer paso · ☐ un término por concepto · ☐ ningún «Error», «OK», «Enviar» desnudos · ☐ `humanizer` pasado si hay párrafos largos (no en legal).
