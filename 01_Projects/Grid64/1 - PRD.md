---
type: doc-software
doc: prd
proyecto: "Grid64"
status: aprobado
tipo: micro-saas
date: 2026-11-08
origen: mixto
---

# 1 · PRD — Grid64

> [!resumen] En cristiano
> Grid64 es una app de móvil para organizar una meta grande en un cuadro de 9×9 casillas (método Harada): 1 meta central, 8 pilares y 64 acciones pequeñas. Todo se guarda **en el propio móvil**, sin cuenta ni internet. Cada día te enseña hasta 5 acciones para hacer hoy y tiene una bandeja para apuntar ideas sueltas y convertirlas luego en meta, pilar o acción.
> **Decisión que te toca:** aprobar este PRD (y las 4 puertas abiertas del §8) para pasar al TRD.

## 1. Problema
- **Vía**: micro-saas, proyecto **personal de Haytham** (no de NeoZeler). Sin cobro previsto en v1; si se vende luego, aplica [[Checklist pre-cobro (micro SaaS)]].
- **Paso 0 (demanda)**: no cumplido ni exigido en v1 por ser herramienta de uso propio. Antes de cobrar o publicar en tienda hace falta señal de demanda (entrevistas + canal + prueba de pago).
- Dolor: las metas grandes se quedan en una nota; la matriz Harada funciona pero en papel/Excel es incómoda en móvil y no te empuja a actuar cada día.
- Hoy: hojas de cálculo o plantillas en papel; apps de tareas que no entienden la jerarquía meta → pilar → acción.
- Ya existe un mandala 9×9 dentro de [[NeoZeler HQ]] (uso de equipo, en web). Grid64 es personal, móvil y offline; no lo sustituye.

## 2. Usuarios y roles
| Rol | Quién es | Qué necesita | Frecuencia de uso |
|---|---|---|---|
| Usuario único | Haytham (luego, quien instale el APK) | Ver su meta, hacer lo de hoy, apuntar ideas con una mano | Diaria, sesiones de 1-3 min |

Sin roles ni cuentas.

## 3. Objetivos y métricas de éxito
| Objetivo | Métrica | Valor actual | Meta |
|---|---|---|---|
| Crear un mandala completo rápido | Tiempo de meta vacía a 8 pilares | n/a | < 5 min |
| Uso diario | Días con ≥1 acción marcada en 30 días | 0 | ≥ 20 |
| Captura sin fricción | Toques para guardar una idea | n/a | ≤ 3 |
| Rendimiento | Arranque en frío en el móvil de Haytham | n/a | < 2 s |
| Privacidad | Peticiones de red salientes | n/a | 0 |

## 4. Historias de usuario
| ID | Como… | Quiero… | Para… | Prioridad |
|---|---|---|---|---|
| US-01 | Usuario | crear un mandala con meta central y 8 pilares | estructurar una meta grande | Must |
| US-02 | Usuario | rellenar las 8 acciones de cada pilar | bajar el pilar a tareas concretas | Must |
| US-03 | Usuario | ver un pilar a pantalla completa (3×3) y pasar de uno a otro con swipe | trabajar de uno en uno con el pulgar | Must |
| US-04 | Usuario | ver el panorama 9×9 con color y nivel de llenado por pilar | saber dónde voy de un vistazo | Must |
| US-05 | Usuario | marcar acciones como hechas y ver el % de pilar y de mandala | medir el avance | Must |
| US-06 | Usuario | elegir hasta 5 acciones como prioridad de hoy | tener un foco diario | Must |
| US-07 | Usuario | ver en Inicio las acciones de hoy con checkbox háptico | actuar sin abrir el mandala | Must |
| US-08 | Usuario | capturar una idea al vuelo desde un botón flotante | no perder pensamientos | Must |
| US-09 | Usuario | convertir una idea en meta central, pilar o acción | estructurarla sin reescribir | Must |
| US-10 | Usuario | mantener pulsada una acción y editar notas Markdown, fecha tope e idea vinculada en una hoja inferior | detallar sin salir de la matriz | Should |
| US-11 | Usuario | ver racha de días activos y progreso global | motivarme | Should |
| US-12 | Usuario | alternar entre varios mandalas | llevar varias metas | Should |
| US-13 | Usuario | exportar un mandala a PNG/PDF | compartirlo o imprimirlo | Could |
| US-14 | Usuario | copia de seguridad y restauración de mi base | no perder datos al cambiar de móvil | Should |

## 5. Requisitos funcionales
- RF-01: CRUD de Mandala (Project + CoreGoal), 8 Pilares y 64 Acciones por mandala, con índices 1-8 fijos.
- RF-02: Progreso de pilar = acciones hechas / 8; de mandala = media de pilares. Se recalcula al marcar.
- RF-03: Pestañas inferiores fijas: Inicio, Mis Mandalas, Ideas.
- RF-04: Inicio: saludo, racha, progreso global, tarjeta de objetivo activo (% y días restantes), lista «Acciones de hoy» (máx. 5) y botón `+`.
- RF-05: Mis Mandalas: selector horizontal, vista panorama 9×9, vista enfoque 3×3, swipe entre 8 pilares, hoja inferior por pulsación larga.
- RF-06: Ideas: lista/grid con etiquetas, estados inbox/linked/archived, conversión en un toque a meta / pilar / acción.
- RF-07: Conversión idea→destino marca la idea `linked` y conserva el vínculo.
- RF-08: Persistencia local atómica; sin red.
- RF-09: Copia de seguridad: exportar/importar el archivo de base de datos.

## 6. Requisitos no funcionales
- Android (APK), vertical, uso a una mano; objetivos táctiles ≥ 48 dp. Modo oscuro por defecto.
- Local-first: sin cuentas, sin servidores, sin analítica, sin permiso INTERNET en el manifiesto de la app final (salvo el bucle local del WebView).
- Rendimiento: arranque < 2 s, interacción < 100 ms, 60 fps en swipe.
- Accesibilidad: contraste AA, etiquetas en controles, `prefers-reduced-motion` respetado.
- Idioma: español.

## 7. Fuera de alcance (v1)
- Sincronización entre dispositivos, cuentas, compartir en equipo, iOS, notificaciones push, IA, widgets, tienda Play (solo APK de instalación directa).

## 8. Riesgos y supuestos
> [!riesgo]
> - **Toolchain Android ausente** en este PC (sin SDK/NDK; solo Go 1.22). Instalarlo es trabajo previo y pesa varios GB.
> - **Wails no soporta Android** (la petición lo nombra): se usa Go + WebView nativa fina (ver TRD).
> - **SQLite sin CGO en Android sin comprobar**: `modernc.org/sqlite` en gomobile hay que validarlo con un spike antes de comprometerse.
> - **Cobertura del spec**: faltan campos para lo pedido (fecha tope, etiquetas, fecha de completado para la racha). El TRD los añade.

**Puertas abiertas para Haytham:**
1. ¿«Acciones de hoy» se eligen a mano cada día o se arrastran las no hechas al día siguiente?
2. ¿Racha = días con ≥1 acción marcada hecha, o también cuenta capturar ideas?
3. ¿Fecha de «días restantes» sale de `target_date` del mandala (único)? Asumido que sí.
4. ¿Idioma y marca definitivos: nombre «Grid64» confirmado?

> [!resumen] Aprobado 2026-11-08
> Haytham aprobó el PRD sin responder las 4 puertas. Defaults asumidos hasta que diga otra cosa: (1) las acciones de hoy se eligen a mano cada día; (2) la racha cuenta solo días con ≥1 acción hecha; (3) los días restantes salen de `target_date`; (4) nombre «Grid64» y español.

## 9. Criterios de aceptación globales
- [ ] Mandala completo (1+8+64) creado, editado y borrado en cascada sin huérfanos.
- [ ] Datos persisten tras matar la app y reiniciar el móvil.
- [ ] Cero tráfico de red verificado.
- [ ] Idea convertida a cada uno de los 3 destinos, y estado `linked`.
- [ ] Ciclo crear → refrescar → borrar → refrescar OK en el dispositivo real.

## 10. Demo provocadora
Uso propio: se sustituye por un mandala de ejemplo sintético («Lanzar NeoZeler HQ») precargado en el primer arranque. Sin rechazo de operarios de campo (usuario único).

## 11. Carácter de marca
- 3 adjetivos: **calmado, preciso, motivador**.
- Anti-referencias: app de productividad infantil/gamificada; dashboard corporativo gris.
- 2 referencias: pendiente de elegir con Haytham (fase de referencias de `diseno-central`, 5-8 en Dribbble).
- Qué enseñar en vivo: el propio cuadro 9×9 relleno (el producto es el diseño).
- Material propio: ninguno aún; sin imágenes de stock. Si falta alguna imagen, se pregunta a Haytham.

---
Siguiente: [[2 - TRD]]
