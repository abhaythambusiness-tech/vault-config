# Precio, dificultad y prioridad

## Dificultad

| Nivel | Tiempo de montaje | Qué significa |
|-------|------------------|---------------|
| 🟢 Baja | 2-5 días | Un flujo lineal, una fuente de datos, sin integración con el sistema del cliente |
| 🟠 Media | 1-3 semanas | Agente con varias herramientas, datos del cliente que hay que limpiar, o sincronización periódica |
| 🔴 Alta | 4+ semanas | Escritura en el sistema del cliente, varios canales de entrada, o dependencia de un ERP sin API |

Si algo se va por encima de 4 semanas, párate: probablemente son dos servicios encadenados.

## Precio

Regla: **montaje + cuota mensual siempre**. La cuota mensual es entre el 5% y el 10% del montaje.

| Dificultad | Montaje | Mensual |
|-----------|---------|---------|
| 🟢 Baja | 1.500-3.000 € | 150-250 €/mes |
| 🟠 Media | 3.000-6.000 € | 250-450 €/mes |
| 🔴 Alta | 6.000-12.000 € | 450-900 €/mes |

Ajustes:
- **Hacia arriba** si el servicio toca facturación, precios o dinero (el riesgo percibido sube el precio aceptable).
- **Hacia abajo** en el primer cliente de cada servicio: es un caso de éxito, y vale más que el margen.
- **Nunca por horas.** El precio se ancla al ahorro anual que has calculado en la cualificación, no a tu tiempo. Si ahorras 9.000 €/año, cobrar 4.000 € de montaje es evidente.

Qué cubre la cuota mensual (escríbelo en la ficha si no es obvio): hosting y mantenimiento del flujo, consumo de API, ajustes de comportamiento y el informe mensual con la métrica de renovación.

## Prioridad en el portafolio

Se ordena por **facilidad de demo × amplitud del dolor**, no por lo interesante que sea técnicamente.

Sube prioridad si:
- La demo se puede montar con un solo export del cliente.
- El dolor aparece en más de uno de los nichos del [[NeoZeler - MOC de Nichos]].
- El resultado se ve en pantalla en 10 segundos.
- Es puerta de entrada natural a otro servicio del catálogo (venta en escalera).

Baja prioridad si:
- Necesita acceso de escritura a su ERP antes de poder enseñar nada.
- Depende de datos que el cliente tendría que preparar antes.
- El ahorro es real pero difícil de convertir en una cifra en la primera reunión.

## Sanity check antes de dar por cerrado un servicio

- [ ] Puedo decir el ahorro anual estimado en una frase con un número.
- [ ] Puedo montar la demo con lo que el cliente me da en el primer email.
- [ ] Puedo enseñarla funcionando en menos de 10 minutos.
- [ ] Sé qué contador justifica la cuota del mes que viene.
- [ ] El siguiente cliente del mismo nicho reutiliza el 80% de lo montado.
