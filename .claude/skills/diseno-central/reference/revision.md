# Revisión, peor caso y anti-slop (fusión de Jakub Krehel, impeccable, taste, break-ui, tastemaker, designer-skills)

## Cómo revisar (en este orden)
1. **Mirar** (navegador del panel: `preview_start` + `resize_window` + captura) a 375 / 768 / 1280. Sin esto, no hay revisión.
2. **Medir con scripts** (rutas en `herramientas.md`): `anti_slop_scan.py`, `check_contrast.py`, `audit_motion.py`, `impeccable detect`.
3. **Puntuar** (1-5) seis ejes: filosofía/idea, jerarquía, oficio (espacio, tipo, color), función/estados, originalidad, movimiento. **Cualquier eje <3 = rehacer esa parte**, no pulir.
4. **Informe** en una tabla, máx 15 filas, una por causa raíz, orden severidad → alcance:

| Severidad | Dominio | Ubicación `file:line` | Antes | Después | Por qué |
|---|---|---|---|---|---|

Cierre: `Block` (hay HIGH) o `Approve`. "Not verified" para lo que no se comprobó; nunca Approve sin inspeccionar. El arreglo más barato primero: borrar > nativo > reutilizar > corregir valor > añadir.
5. **Bucle**: corregir → volver a capturar → mínimo **2 rondas** antes de dar una pantalla por buena (así se hizo Reto 30).

## Jerarquía visual: patrón de lectura y test del desenfoque
**Patrón F** (webs con mucho texto, listados): la mirada baja por el margen izquierdo y lee en horizontal donde algo engancha. Los dos primeros párrafos son los que más se leen; empezar títulos, subtítulos y viñetas con la palabra clave. La barra lateral sirve para CTAs sin tapar el contenido. El patrón F aburre pasado el primer tercio: romperlo con módulos horizontales.
**Patrón Z** (páginas simples, landings, CTA como única meta): la mirada recorre la franja superior, baja en diagonal y recorre la inferior. Puntos: 1 logo (arriba izq.) · 2 CTA secundario (arriba der.) · centro: imagen o bloque de valor · 3 iconos o pasos (abajo izq.) · 4 CTA principal (abajo der.). Con contenido complejo, usar F; en páginas largas se puede repetir la Z por bloque.
**Contraste de jerarquía**: color (cálido domina a frío, vivo a apagado), tamaño y espacio blanco gestionan atención y relaciones. El tamaño rompe el orden de lectura: un texto grande abajo a la derecha se lee primero. Reducir ruido visual refuerza lo que queda.
**Test del desenfoque** (obligatorio en cada pantalla clave y en cada landing): captura a 375 y 1280 → difuminar 5-10 px (CSS `filter: blur(8px)` en DevTools o editor) → ¿lo que destaca es lo que debe (CTA principal, titular, tarea top)? Si destaca otra cosa, la jerarquía está mal: corregir peso, color o espacio, no añadir más. Anotar en el informe de revisión: `Blur: pasa / no pasa, destaca X`.

## Checklist (H = bloquea, M = arreglar, L = pulir)
1. H Control sin nombre accesible.
2. H Sin foco visible (aro <3:1).
3. H Ruta solo ratón; drag sin alternativa.
4. H Motion ignora reduced-motion.
5. H Recorte a 320 px o 200 % de zoom.
6. H Contraste <4.5:1 (UI/grande <3:1) sobre el fondo real.
7. H Significado solo por color o solo por movimiento.
8. H Destructivo sin confirmar ni deshacer.
9. H Truncado/oculto sin acceso al valor ni pista (asomar 16-32 px).
10. H Error sin recuperación.
11. M `div onClick`, `tabindex>0`, ARIA redundante.
12. M Sin label/autocomplete; input <16 px en móvil.
13. M `transition:all`, `ease-in`, >300 ms en feedback, animar layout.
14. M Animar acciones de teclado; hover sin `(hover:hover)`.
15. M Diana <24 px o solapada.
16. M Medida >75ch, interlineado en px, cifras sin `tabular-nums`.
17. M Colores literales fuera de tokens; >1 acción rellena por vista.
18. M `left/right` en vez de lógicas, `100vh`, altura fija con texto.
19. M Peor caso sin probar.
20. L Radios no concéntricos; sombra/borde incoherente.
21. L `...`/`--` en vez de `…`/`–`; sin `text-wrap`.
22. L Stagger >100 ms por ítem o que bloquea.

## Peor caso (break-ui)
Antes de entregar una vista con datos: mapear cada campo (fuente, tipo, límite) → fixture del peor caso plausible (nombre de 60 caracteres, email largo, 0, 1, 1000 ítems, sin imagen, traducción +30-40 %) → alternar Demo / Peor / Vacío / Uno / 1000. Firmas típicas: avatar aplastado (`flex-shrink:0`), desborde (`min-width:0`), email largo (`overflow-wrap:anywhere`), badge `nowrap`, "1 members" (`Intl.PluralRules`), números (`Intl.NumberFormat`), iniciales (`Intl.Segmenter`), imagen rota (fallback). Truncar: final para metadatos, medio para ficheros/emails, nunca números. Probar 320 px, 200 % zoom, oscuro, RTL. **Informar Broken / Ugly / Fragile antes de arreglar**, y qué aguantó.

## Señales de IA (ninguna por defecto; el scanner las busca)
1 gradiente morado/índigo/cian · 2 texto con gradiente como énfasis · 3 eyebrow sobre cada título · 4 trío de cards icono+título+texto · 5 cards dentro de cards · 6 borde de acento en un solo lado (>1 px) · 7 bento vacío · 8 hero centrado 100vh con 2 CTAs · 9 zigzag ≥3 · 10 fuente-reflejo sin motivo · 11 emojis como iconos o en h1-h6 · 12 glow/glass/grano sin función · 13 stats, logos o testimonios inventados · 14 chips flotantes en el hero · 15 caras/ilustraciones SVG · 16 em dashes y frases plantilla ("Elevate", "Seamless", "revolucionario", "sinergia") · 17 micro-etiquetas y numeración 01/02/03 decorativas · 18 `transition:all`, ease-in, bounce, `hover:scale-105` global · 19 radios y sombras sin regla · 20 solo estado feliz, `href="#"`, sin `alt`/foco · 21 carrusel automático sin pausa, toast de éxito, validar al teclear · 22 sombra offset dura, hero-metric, cards ghost (borde + sombra).
**Test de eliminación**: slop = decisión por reflejo. Quitar el elemento: si nada se pierde, sobraba.

## Anti-"parece barato"
Nunca un placeholder visible (gris, icono roto, Lorem): sin asset real → tratamiento tipográfico intencional (monograma, glifo, textura). Sin fotos fotorrealistas de personas ficticias. Stats con fuente, periodo o "autoinformado". Testimonios con ancla (monograma + rol/empresa o enlace). Ningún logo de tercero para simular integraciones o prensa. CTAs que nombran la acción ("Reservar plaza", no "Entrar"). Tres secciones seguidas de solo texto en grid = relleno.

## Autocrítica de dirección
¿Se reconoce la marca en una captura de 3 s sin logo (forma, color, ritmo)? ¿Intercambiar el logo por otro rompe el diseño? Si no, es genérico: volver a la identidad.
