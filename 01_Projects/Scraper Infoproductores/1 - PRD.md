---
type: doc-software
doc: prd
proyecto: "Scraper Infoproductores"
status: aprobado
tipo: micro-saas
date: 2026-11-01
origen: mixto
---

# 1 · PRD — Product Requirements Document

> [!resumen] En cristiano
> Una web de suscripción donde agencias de lanzamientos, closers, editores de vídeo y otros infoproductores encuentran **infoproductores** (gente que vende cursos y mentorías online) ya reunidos en una lista: sus redes, cuánto facturan más o menos, qué lanzamientos hicieron, cómo contactarles y qué anuncios tienen activos. Te registras (Google o enlace por correo) y entras con un **plan gratis de pocos créditos** para que pruebes y quieras pagar. Cada **búsqueda** (con filtros de ciudad, nicho y palabras clave) y cada **contacto desbloqueado** gasta créditos; el contacto queda guardado en tu lista y no se cobra dos veces. Los planes de pago dan más créditos al mes. Los datos salen de Instagram, YouTube, Hotmart/Digistore y la biblioteca de anuncios de Meta, y **Laya** los ordena por nicho y nivel. Decisión pendiente tuya: validar con 5-10 entrevistas antes de construir (ver Paso 0).

## 0. Vía y Paso 0 (demanda)
- **Vía**: micro SaaS con intención de monetizar (un tipo de usuario principal, v1 ≤ 1 mes, la mantiene una persona, sin ventas). Kill: 60-90 días sin 5 clientes de pago.
- **Señal de demanda actual**: Haytham está en una formación de lanzamientos y "todos buscan infoproductores". Es una señal **débil** (opinión, no pago).
- **Falta (antes del TRD)**: 5-10 entrevistas a gente de esa formación + una preventa o pago pequeño. Hipótesis a confirmar: pagarían X €/mes por una lista actualizada.

## 1. Problema
- Dolor concreto: quien vive de servir a infoproductores (agencias de lanzamientos, closers, editores) pasa horas buscando a mano quién vende, cuánto factura y cómo contactarle. Cifras: **sin medir** (pendiente de entrevistas).
- Cómo lo resuelven hoy y por qué falla: buscan a mano en Instagram/YouTube, miran la biblioteca de anuncios, preguntan en comunidades. Es lento, desordenado y sin datos de facturación ni de lanzamientos.

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Comprador principal | Agencia de lanzamientos o closer | Lista filtrable de infoproductores con facturación estimada y contacto | Semanal |
| Comprador secundario | Editor de vídeo, otro infoproductor | Encontrar clientes o competencia/referentes | Quincenal |
| Admin | Haytham | Ver fuentes, errores del scraper, créditos y cobros | Diaria al principio |

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
| Validar demanda | Entrevistas hechas / preventas | 0 | 5-10 / 3 de pago |
| Base útil | Infoproductores con ficha completa | 0 | 1.000 en el lanzamiento |
| Ingresos | Clientes de pago | 0 | 5 a los 60-90 días |
| Frescura | Fichas actualizadas en <30 días | n/a | ≥ 80 % |
| Conversión | Usuarios del plan gratis que pasan a pago | 0 | por fijar tras la preventa |

## 4. Historias de usuario (priorizadas)
| ID | Como… | Quiero… | Para… | Prioridad (MoSCoW) |
|---|---|---|---|---|
| US-01 | Comprador | Buscar infoproductores con palabras clave y filtros (ciudad, nicho, facturación estimada, plataforma); cada búsqueda gasta créditos | Encontrar prospectos adecuados | Must |
| US-09 | Visitante | Registrarme con Google o enlace por correo y recibir un plan gratis con pocos créditos | Probar el servicio y animarme a pagar | Must |
| US-02 | Comprador | Ver la ficha: redes, lanzamientos pasados y anuncios activos | Valorar si merece contactarle | Must |
| US-03 | Comprador | Desbloquear el contacto de un infoproductor gastando créditos y que quede guardado en mi lista (sin volver a cobrar) | Contactarle y tener mi propia base | Must |
| US-04 | Comprador | Pasar a un plan de pago mensual con más créditos | Buscar y desbloquear más | Must |
| US-05 | Comprador | Guardar listas y exportar a CSV | Trabajar en mi CRM | Should |
| US-06 | Comprador | Alertas de nuevos lanzamientos de un infoproductor | Llegar el primero | Could |
| US-07 | Admin | Ver estado de cada fuente y reintentar fallos | Mantener datos frescos | Must |
| US-08 | Infoproductor | Pedir que borren o corrijan mi ficha | Cumplir el RGPD | Must |

## 5. Requisitos funcionales
- RF-01: Recogida de datos de Instagram, YouTube, Hotmart/Digistore y biblioteca de anuncios de Meta (solo datos públicos).
- RF-02: Clasificación con **Laya** por nicho, tipo de oferta y nivel estimado (supuesto: Laya = el clasificador ya usado en Laya Leads; confirmar alcance en el TRD).
- RF-03: Facturación **estimada** siempre marcada como estimación, con método explicado.
- RF-04: Sistema de créditos: cada **búsqueda** y cada **contacto desbloqueado** gasta créditos (cantidades por fijar en el Backend Schema; el CSV no cobra aparte). Plan gratis con créditos iniciales bajos; planes de pago con más créditos al mes. Sin créditos no se busca ni se desbloquea. Un contacto ya desbloqueado se ve de nuevo sin coste.
- RF-07: Registro con Google y enlace por correo.
- RF-08: Lista personal de contactos desbloqueados, con exportación a CSV.
- RF-05: Cobro recurrente con portal de gestión y baja.
- RF-06: Canal para que un infoproductor pida baja/corrección de su ficha.

## 6. Requisitos no funcionales
Datos de contacto solo desbloqueables con login; español; móvil y escritorio; datos con fecha de captura; panel admin con salud de fuentes; coste de RAM bajo (ver feedback web).

## 7. Fuera de alcance (v1)
- App móvil, API pública, equipos con roles, envío de emails desde la plataforma, otros idiomas, mensajería privada o datos tras login de una red.

## 8. Riesgos y supuestos
> [!riesgo]
> - **RGPD**: emails y perfiles de personas son datos personales aunque sean públicos; hace falta base legal (interés legítimo), aviso, baja y registro. Revisión legal humana antes de cobrar.
> - **Términos de las plataformas**: Instagram, YouTube y Meta prohíben o limitan el scraping; riesgo de bloqueos o reclamaciones. Preferir APIs oficiales (Meta Ad Library tiene API) y solo datos públicos.
> - **Facturación estimada** puede ser falsa y dañar la confianza: etiquetarla y justificarla.
> - **Demanda sin validar**: una formación entusiasta no es un pago.
> - **Filtro por ciudad (ej. Málaga)**: pocas fuentes dan la ubicación del infoproductor; saldrá de la bio o el perfil y habrá fichas sin ciudad. Decir en la UI cuántas fichas tienen ubicación.
> - **Plan gratis**: abuso con cuentas falsas para sacar créditos gratis (limitar por correo verificado y revisar patrones).
> - **Competencia**: listas de leads y herramientas de ad-spy existentes; hay que concretar la cuña (infoproductores hispanos, con lanzamientos).

## 9. Criterios de aceptación globales
- [ ] Ciclo completo en producción: crear cuenta → comprar → gastar créditos → refrescar → borrar ficha → refrescar
- [ ] Ninguna ficha muestra contacto sin créditos
- [ ] Toda cifra de facturación lleva etiqueta "estimada"
- [ ] Baja de un infoproductor efectiva y comprobable
- [ ] `Checklist pre-cobro (micro SaaS)` completa

## 10. Demo provocadora (reunión 1)
- Pantalla que provoca la reacción: buscador con 30-50 infoproductores **reales y públicos** (nombre artístico, red, nicho) con facturación estimada y último lanzamiento; sin contactos.
- Quién la ve: 5-10 personas de la formación de lanzamientos (agencias, closers, editores).
- Reacciones / rechazos → ajustes: pendiente.
- Descartar móvil de campo: n/a (usuarios de oficina).

## 11. Carácter de marca (insumo de la identidad visual)
Respondido por Haytham el 2026-11-01.
- 3 adjetivos que debe transmitir: **preciso, rápido, fiable**.
- Qué NO debe parecer (anti-referencias): **guru chillón** (nada de cohetes, dólares ni rojo/amarillo de curso milagro).
- 2 referencias que le gustan y por qué: Linear (jerarquía clara, pocas cosas bien alineadas) y Vercel (minimalismo técnico y rejilla), de [[Biblioteca de Referencias Premium]].
- Qué del negocio se puede enseñar en vivo: **un buscador real con resultados** (búsqueda de ejemplo que funciona, fichas con contacto borroso).
- Material propio disponible: ninguno aún (sin logo ni fotos); la identidad se construye con tipografía, datos y rejilla.

---
Siguiente: [[2 - TRD]]
