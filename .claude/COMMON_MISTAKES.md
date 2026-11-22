# Common Mistakes

**⚠️ CRITICAL - Read at session start**

Registro vivo de errores que Claude **ya ha cometido en este vault/proyectos**. Formato de cada entrada: **Symptom → Check/Causa → Fix/Regla**. Gobernado por `CLAUDE.md §7.1`: consultar antes de actuar en el dominio correspondiente; añadir/reforzar entrada en la misma sesión tras un error corregido por Haytham; a la 3.ª reincidencia, promover la regla a §0–§6 de `CLAUDE.md`.

Índice de dominios: Vault/frontmatter (1–5, 14) · Diseño/UI (6–10, 93, 98, 99, 101, 103) · GateGuard/ejecución (11) · MCP (12, 102) · Scaffolding web (13) · Hooks y pruebas de seguridad (69–70, 100) · Verificación visual, 3D y entorno (75–91) · Datos/bots de trading (16–21, 23–29).

---

## Top 5 Critical Mistakes — Vault

### 1. Romper el frontmatter YAML

**Symptom**: las queries Dataview de `00_Meta/Dashboard.md` dejan de mostrar la nota o fallan.
**Check**: todo `type:` debe usar uno de los valores existentes (`moc`, `proyecto`, `pmbok-fase`, `servicio`, `referencia`, `estrategia`, `guia`, `plantilla`, `resource`, `meta/dashboard`); `status:` debe ser coherente (`activo`, `borrador`, `completado`/`completo`, `demo-funcional`, `en-progreso`).
**Fix**: copiar el bloque frontmatter de una nota hermana del mismo tipo en vez de inventar campos nuevos.

### 2. No mantener los backlinks (`related:`) al mover o crear notas

**Symptom**: una nota queda huérfana, no aparece enlazada desde ningún MOC.
**Check**: toda nota nueva debe añadirse a `related:` de su MOC/hub padre y viceversa (wikilinks `[[...]]`).
**Fix**: al crear `Cliente - X`, `Servicio - X` o `Nicho - X`, actualizar también el MOC correspondiente (`NeoZeler - MOC de Clientes.md`, `... de Nichos.md`, `... de Servicios.md`).

### 3. Ignorar el estilo de respuesta de `00_Meta/GEMINI.md`

**Symptom**: respuestas largas, con preámbulo, emojis o resúmenes finales — el usuario ya pidió lo contrario.
**Check**: español, máximo 8 líneas, empezar por la conclusión, sin "Claro"/"Por supuesto".
**Fix**: aplicar las mismas reglas en Claude Code, no solo en Gemini (ver sección dedicada en `CLAUDE.md`).

### 4. Colocar contenido en la carpeta PARA incorrecta

**Symptom**: proyectos con fecha de fin acaban en `02_Areas`, o responsabilidades continuas acaban en `01_Projects`.
**Check**: `01_Projects` = con entregable/fin definido (ej. Cauce); `02_Areas` = responsabilidad continua sin fin (ej. NeoZeler); `03_Resources` = referencia sin acción; `04_Archive` = inactivo.
**Fix**: mover la nota a la carpeta correcta y actualizar sus enlaces.

### 5. Romper la sintaxis Templater al copiar plantillas a mano

**Symptom**: aparece literalmente `<% tp.file.creation_date("YYYY-MM-DD") %>` en vez de la fecha, porque el archivo se creó fuera de Obsidian/Templater.
**Check**: si la nota se crea por script o edición directa (no desde Obsidian), sustituir manualmente los placeholders `<% tp... %>` por valores reales.
**Fix**: rellenar `created`/`updated`/`title` a mano cuando no se use el comando "New note from template" de Obsidian.

### 14. Reescribir/sobrescribir una nota ya entregada cuando Haytham pedía estructura nueva

**Symptom**: Haytham pide "aplica el conocimiento X a este producto" y Claude sobrescribe (varias veces) una nota ya creada en la sesión, en vez de crear la carpeta con notas por tema que él tenía en mente. Percibido como trabajo que hay que deshacer.
**Causa**: interpretar "aplicar conocimiento a un producto" como "editar la nota existente" sin preguntar formato/ubicación, cuando el entregable era ambiguo (nota única vs carpeta de notas cortas por tema).
**Fix**: ante un entregable de documentación no trivial y ambiguo en forma o sitio, hacer **una** pregunta antes de escribir (`CLAUDE.md §5`): ¿nota única o carpeta con varias? ¿dónde? Preferir siempre aditivo (carpeta/notas nuevas) sobre sobrescribir algo ya entregado; no reescribir una nota más de una vez sin confirmación.

### 15. Checkboxes de checklist invisibles al desmarcar en temas personalizados

**Symptom**: las casillas desmarcadas (`- [ ]`) no se ven en el editor ni lectura; al marcarlas (`- [x]`) sí aparecen porque tienen fondo sólido.
**Causa**: usar `appearance: none` en `.task-list-item-checkbox` sin forzar `border: 1.5px solid #64748b !important` sobre todos los selectores (`input[type="checkbox"]`, `.task-list-item-checkbox`, Live Preview). El tema nativo resetea el borde y el fondo blanco sobre papel blanco vuelve invisible la casilla.
**Fix**: en snippets CSS de Obsidian, definir siempre las variables nativas `--checkbox-*` en `:root` y aplicar `border: 1.5px solid #64748b !important; background-color: #ffffff !important;` cubriendo `input[type="checkbox"]` y `.task-list-item-checkbox`.

---

---

## Diseño / UI (proyectos de código con capa visual — `CLAUDE.md §4.1`)

Todas estas entradas vienen de feedback real de Haytham + debate multiagente sobre landings reales (`aura-sisters`, `neozeler-landing`, `infoproductor-demo`). No son hipótesis.

### 6. Placeholder vacío visible en una sección de prueba social

**Symptom**: `<div>` gris sin imagen, icono roto o "Lorem ipsum" donde debería ir foto de instructor/equipo, logo de cliente o captura de producto. Señal #1 de desconfianza.
**Causa**: no había asset real y se dejó el contenedor vacío "para rellenar luego".
**Fix**: nunca dejar el contenedor vacío. Resolver con tratamiento tipográfico/gráfico intencional (monograma, glifo de marca, patrón halftone, marcas de esquina tipo visor). Ejemplo ya implementado: `infoproductor-demo/app/components/Instructor.tsx`.

### 7. Fabricar foto fotorrealista de una persona ficticia

**Symptom**: rostro sintético de un "instructor"/"fundador" inventado, con bio y credenciales falsas, presentado como real — aunque sea demo.
**Causa**: tratar "es solo una demo" como permiso para contenido engañoso sobre identidad.
**Fix**: prohibido. Tratamiento tipográfico/abstracto (iniciales en serif, glifo). El footer debe declarar "producto e infoproductor ficticios" si aplica.

### 8. Cifras destacadas sin fuente ni metodología

**Symptom**: stats tipo "€2.1M facturados", "94% completa el curso" sin nota de contexto → se leen como infladas/marketing vacío.
**Causa**: se copió el patrón visual de stat-row sin la línea de respaldo.
**Fix**: cada stat grande lleva debajo, en texto pequeño, periodo + muestra + "autoinformado" si aplica. Ejemplo: `infoproductor-demo/app/components/Hero.tsx` ("Autoinformado por alumnos, cohortes 1–10 · 2023–2025").

### 9. Output de diseño "genérico de IA" por saltarse el gate

**Symptom**: fondo navy/negro + acento teal, hero centrado con botón pill, 3 columnas de cards icon+title+text repetidas sección tras sección, easing por defecto de la librería, todos los tamaños de tipo iguales entre secciones.
**Causa**: maquetar antes de correr `ui-ux-pro-max` y sin aplicar `03_Resources/web-interface-guidelines.md`.
**Fix**: seguir el gate de `CLAUDE.md §4.1` en orden: estilo (`ui-ux-pro-max`) → maquetación → validación (`web-design-guidelines`, `responsive-design`). Curva de easing propia reutilizada en todo el proyecto. Romper la simetría del grid en ≥1 punto por sección. Declarar en la respuesta qué skill/MCP se ejecutó.

### 10. Contraste insuficiente en tema oscuro

**Symptom**: texto por debajo de ~55% de opacidad en <14px sobre fondo oscuro → falla WCAG AA.
**Causa**: no verificar en viewport móvil (375px) antes de dar por terminado.
**Fix**: subir opacidad/uso de color-fg real; verificar visualmente a 375px. Si no hay navegador en el entorno, decirlo explícitamente en vez de asumir.

### 15. Clonar la dirección de arte de un proyecto hermano

**Symptom**: `bodega-cero` (1er intento) salió "casi idéntica a `infoproductor-demo`": mismo acento naranja-rojo (`#ff3d00` ≈ `#E4501E`), `border-radius:0` en todo, misma fórmula "display condensada + labels monoespaciadas + reveal GSAP", mismos iconos (Lucide). Respuesta textual: *"todo muy cuadrado muy calculado no hay nada creativo ... tipo pagina web de 10000 euros"*.
**Causa**: consultar `ui-ux-pro-max` pero no mirar los proyectos previos del mismo dominio (infoproductos/landing) para diferenciarse; el default editorial-brutalista de `ui-ux-pro-max` coincide con lo ya hecho.
**Fix**: antes de maquetar en un dominio donde ya hay un proyecto en `~/Proyectos/`, abrir su `globals.css`/tokens y prohibirse explícitamente su acento, su radius, su pareja tipográfica y su librería de iconos. Ofrecer a Haytham 2-3 direcciones distintas con preview cuando pida "premium/impactante" — no adivinar. Icono no-Lucide (Phosphor) como salida rápida del look "IA".

### 96. Defaults, aceptaciones marcadas y formularios largos (UX, 2026-11-16)

**Symptom**: casilla de términos o newsletter ya marcada; ajustes por defecto poco pensados que nadie cambia; formulario largo de una sola vez que se abandona.
**Causa**: los usuarios casi nunca cambian los valores por defecto, y lo que exige decisión no se puede decidir por ellos.
**Fix**: acertar el default solo si el backend puede adivinar la preferencia o beneficia al usuario; **nunca preseleccionar** aceptar términos o suscribirse. Facilitar cambiar el default. Partir formularios largos en pasos cortos (la gente prefiere 10 tareas pequeñas a 1 grande) con progreso visible y feedback por acción (deshacer).

### 97. Innovar el patrón sin referencia conocida (regla MAYA, 2026-11-16)

**Symptom**: navegación o control «nuevo» que el usuario no entiende o ignora.
**Causa**: el público resiste el cambio brusco (MAYA: lo más avanzado que aún se acepta).
**Fix**: metáfora visual familiar, **alternativa tradicional de respaldo** (p. ej. búsqueda clásica junto a la nueva), alcance sensato y lanzar por dosis. Si un control o palabra no se entiende, se ignora: hover/tooltip para iconos ambiguos y mismo término en etiqueta y texto de ayuda.

---

## GateGuard / ejecución (`CLAUDE.md §2`)

### 11. Repetir `Edit`/`Write`/`Bash` sin volver a declarar los hechos

**Symptom**: el hook Fact-Forcing bloquea la llamada aunque los hechos se declararan segundos antes para otro archivo.
**Causa**: GateGuard exige declaración **por cada archivo o comando nuevo** de la sesión, inmediatamente antes de la primera llamada sobre él.
**Fix**: antes del primer `Edit`/`Write` de cada archivo nuevo, declarar en texto: importadores, API afectada, esquema de datos y verbatim del usuario. No pelear el bloqueo ni usar `ECC_GATEGUARD=off`: responder el gate y reintentar la misma operación.

---

## MCP (`CLAUDE.md §0.7`, `§3`)

### 12. Forzar un MCP fuera de sus precondiciones en vez de declararlo no disponible

**Symptom**: intentar `bloom_onboard_brand` para un proyecto local sin deploy ni URL pública / Instagram real que crawlear.
**Causa**: asumir que el MCP de diseño aplica siempre que la tarea sea "de diseño".
**Fix**: si faltan las precondiciones del MCP, declararlo no disponible en la respuesta y usar el fallback correcto (para imágenes: SVG/código propio con los design tokens del proyecto, sin dependencia nueva ni imagen falsa). Nunca fallar en silencio ni sustituir de tapadillo.

---

## Scaffolding web (`CLAUDE.md §6.1`)

### 13. Entregar una web como un único `.html` / Artifact cuando se pide "una página web"

**Symptom**: (1ª vez) demo entregada como HTML suelto → reescrita como scaffold Next.js (`infoproductor-demo`). (2ª vez, `bodega-cero`) Haytham pidió "una página web", se entregó un Artifact de un archivo; respuesta textual: *"no me vuelvas a generar un artefacto cuando te pido una pagina web"*.
**Causa**: tratar el Artifact/HTML único como default. "Es para una demo" ≠ "quiero un archivo suelto": una demo también es un proyecto real en `~/Proyectos/`.
**Fix**: si la petición dice "página web / web / landing / sitio", default = scaffold real en `~/Proyectos/<nombre>/` (`§6.1`: Next.js si necesita SEO; Vite+React si no) con git desde el primer commit. Artifact/archivo único **solo** si Haytham escribe explícitamente "un archivo suelto" o "enséñamelo en el chat". 2 ocurrencias — a la 3ª, promover a `§0`.

---

## Datos y bots de trading (proyecto `04_Archive/Memecoin-LSTM`)

### 16. Fiarse de las etiquetas de un dataset sin auditarlas

**Symptom**: modelos "malos" (EXP-16v2 con nota de azar) y backtests con cifras raras. `tokens_capturados` tenía el 36 % de filas Solana con `precio_m30 = 0`, concentradas antes del 3-oct ~12:45 UTC (88–100 % por franja).
**Causa**: el recolector antiguo guardaba como "RUG −100 %" cualquier fallo de consulta (429, timeout). Se entrenó EXP-16v2 con 585 de esas filas (8,4 %).
**Regla**: antes de entrenar o evaluar, medir el % de `precio_m30 <= 0` por hora y descartar los tramos sospechosos; preferir etiquetas derivadas de las fotos del observador; un fallo de red nunca es una etiqueta (ver `recolector_multired.py` v3).

### 17. Reorganizar carpetas con procesos de recogida en marcha

**Symptom**: ~2 h (20:39–22:46 del 04-oct) sin guardar fotos ni tokens; el log decía "Snapshot tomado" y el recolector "no such table" en bucle; aparecieron bases de 0 bytes en la raíz.
**Causa**: los procesos viejos mantenían rutas antiguas y los `except: return []` / `pass` tragaban los errores (también el 429 de Gecko, ~70 peticiones/min contra un límite de 30).
**Regla**: antes de mover archivos, listar procesos (`ps`) y sus ficheros abiertos (`/proc/<pid>/fd`); reiniciarlos tras mover; no tragar errores sin contarlos; mantener `vigilante_datos.py` activo.

### 18. Comprobar mal el resultado de un comando

**Symptom**: dije "parado" tras un `kill` que había fallado (en zsh `$VAR` no se separa en palabras); y un recuento de filas comparó fechas ISO como texto (`T` vs espacio).
**Regla**: pasar los PID explícitos y verificar con `kill -0 <pid>`; parsear fechas como fechas (UTC) antes de comparar; leer el mensaje de error del comando antes de afirmar que funcionó.

### 19. Medir el stop contra el precio de VENTA en vez del precio de mercado

**Symptom**: una posición abierta saltó el stop del −10 % a los 6 s (−10,3 %).
**Causa**: el valor de la posición era el mínimo entre el precio de mercado y la cotización de venta de Jupiter, que ya incluye el coste de salir (hasta ~8 % permitido en el filtro de entrada): el stop quedaba con ~2 % de margen. El backtest que eligió v7 usaba el precio medio.
**Regla**: los stops/trailing NO se evalúan contra lo gastado: el coste de entrar y salir se lleva casi todo el margen del stop.

**CORREGIDA el 2026-10-05 (ver #22)**: la primera solución fue "usar el precio de mercado de DexScreener" y NO funcionó — 15 de 20 stops seguían saltando en menos de 60 s (mediana 12 s). Regla vigente: medir la cotización de venta de AHORA contra la cotización de venta JUSTO TRAS COMPRAR (`valor_base` en `bot_real_v7.py`), más un margen de gracia de 45 s; DexScreener queda solo como dato informativo. **Caveat abierto**: esa definición de precio ya no es la del backtest que eligió v7 (precio medio), así que sus resultados no se trasladan 1:1.

### 22. Comparar dos precios que no están en la misma escala

**Symptom**: ventas tituladas "STOP LOSS (−87,3 %)" cuya pérdida real fue del 2,8 %; otra "(−14,4 %)" que en realidad ganó +0,30 %; otra "(−17,3 %)" que ganó +56 %. 15 de 20 stops en menos de un minuto. Y 4 de 19 stop-loss salían en VERDE en Discord.
**Causa**: el disparo del stop usaba el precio de DexScreener de un pool de 1–2 min (dato a menudo viejo) dividido por el precio EFECTIVO pagado (que ya incluye el impacto de la compra), mientras el color y el PnL usaban la cotización real de Jupiter. Dos varas distintas: una decía −87 % y la otra ~0 %. El bot compraba y soltaba en segundos pagando el coste de ida y vuelta cada vez; las 5 carteras del ensayo acabaron en pérdidas por esto, no por elegir mal.
**Regla**: cualquier umbral (stop, trailing, límites) se compara contra una referencia tomada con la MISMA fuente, unidad y momento que el valor vigilado. Antes de dar un corte por bueno, mirar en los datos cuánto duran las posiciones: si la mediana son segundos, el precio está mal, no el mercado. Y el color o emoji de una venta se decide por el MOTIVO (un stop loss nunca en verde), no solo por el signo del PnL.

### 20. Comparar modelos con variables de otra fuente de datos

**Symptom**: EXP-16v2 salió "como el azar" (AUC 0,49) en la comparación con EXP-17, pero 0,71 en su propio universo.
**Causa**: la comparación usaba el volumen/liquidez de DexScreener (el que guarda el observador) mientras EXP-15/16 se entrenaron y se usan con los de GeckoTerminal; además la entrada era 40 s más tarde. Yo atribuí el fallo a las etiquetas falsas sin comprobarlo.
**Regla**: evaluar cada modelo con las variables EXACTAS (fuente y momento) con las que operará; comprobar la hipótesis (reentrenar y medir) antes de afirmarla como causa.

### 21. Ediciones dependientes lanzadas en paralelo con un control que puede rechazar una

**Symptom**: el control (GateGuard) rechazó la edición de las constantes mientras otras dos, que las usaban, sí se aplicaron → el archivo quedó con nombres sin definir (`NameError` latente). Ocurrió dos veces en la misma sesión (gecko_hub.py y COMMON_MISTAKES.md).
**Regla**: las ediciones que dependen unas de otras se aplican en secuencia (o en una sola), y tras un lote con algún rechazo se revisa qué se aplicó antes de seguir; compilar siempre después (`py_compile`).

---

### 23. Dar por bueno un informe sin comprobar que midió lo que dice

**Symptom**: el primer informe del Gate 1 de `goat-trading` daba "0 de 6 trimestres en positivo" con cuatro trimestres a 0,00 €, indistinguible de un mercado plano.
**Causa**: la cuenta había caído a 24 € y el tamaño de posición objetivo (un tercio de la cartera) quedaba por debajo del mínimo de orden de 25 €: el bot no podía comprar. Estaba **muerta**, no plana. Había 31-58 monedas elegibles en esas fechas.
**Regla**: un 0 en un informe puede significar "no pasó nada" o "no se pudo actuar", y son cosas opuestas. Antes de reportar cualquier resultado (también uno negativo), comprobar que el sistema estaba en condiciones de producir un resultado distinto: contar candidatos, operaciones posibles y capital disponible en el tramo en cuestión.

### 24. Añadir un filtro y no revisar si los tests quedan en vacío

**Symptom**: al añadir `MIN_REALIZED_VOL` en `goat-trading`, dos tests siguieron en verde porque el ranking salía vacío y aserciones del tipo `"X" not in ranked` se cumplían trivialmente. Uno de ellos comparaba dos listas vacías y nunca había probado nada.
**Causa**: aserciones negativas sin aserción de no-vacuidad.
**Regla**: toda aserción del tipo "X no está en la lista" lleva al lado un `assert lista` o un `assert lista == [esperado]`. Tras añadir cualquier filtro, revisar los tests que podrían quedar satisfechos por una colección vacía.

### 25. Fixtures sin ruido para métricas ajustadas a volatilidad

**Symptom**: el test "la serie fuerte gana a la floja" fallaba con rectas perfectas: la que menos subía puntuaba 8 veces más (15.160 contra 1.854).
**Causa**: sobre una recta, la volatilidad realizada mide la curvatura de la rampa (mismo incremento sobre base creciente), no el nervio del precio.
**Regla**: ningún fixture de una métrica que divida por volatilidad puede ser una recta lisa. Ruido realista y la misma semilla en las dos series que se comparan, para que la volatilidad no sea la variable oculta del test.

### 26. Agrupar por el periodo de los eventos en vez de por el calendario

**Symptom**: `evaluate_gate1` daba PASA a un bot que había dejado de operar dos años antes, con "4 de 4 trimestres en positivo".
**Causa**: `groupby(trimestre del cierre de la operación)` solo contiene los trimestres **con** operaciones, así que `tail(6)` cogía los últimos 6 presentes y no los últimos 6 reales.
**Regla**: cuando una condición habla de "los últimos N periodos", el eje se construye del calendario (o del rango de la serie) y se rellenan con 0 los periodos sin eventos. Nunca de los periodos que aparecen en los datos.

### 27. Construir un universo con datos de hoy y aplicarlo al pasado

**Symptom**: el backtest de `goat-trading` corría sobre las 136 monedas con más de 2 M€/día **hoy**, durante 900 días hacia atrás.
**Causa**: `fetch_tickers()` da el volumen de las últimas 24 h del momento de la llamada.
**Regla**: la pertenencia a un universo se evalúa con el dato **de cada momento** (volumen reconstruible de las propias velas: `close*volume` en ventana de 24 h). La parte que no se puede recuperar —los activos que ya no existen en la fuente— se declara por escrito en el informe como sesgo al alza, no se omite.

### 28. Fixtures todos de la misma longitud

**Symptom**: el Bot M de `goat-trading` abortó en su primera ejecución real con `IndexError: Boolean index has wrong length: 5399 instead of 2218`, con 14 tests en verde.
**Causa**: `pd.DataFrame(dict de Series)` alinea al índice **unión**, así que la etiqueta de una moneda con histórico corto salía con la longitud del panel entero. Las 136 monedas reales van de 1.166 a 5.399 velas; todos los fixtures tenían la misma longitud.
**Regla**: por cada estructura de datos que venga del mundo real, al menos un fixture **irregular**: longitudes distintas, huecos, series que empiezan y acaban en fechas distintas. Un panel uniforme no es un panel.

### 29. Mirar el titular de un backtest antes que su fragilidad

**Symptom**: la variante diaria de `goat-trading` dio 100 € → 136,87 € (+37 %). Parecía la ganadora.
**Causa**: sin las tres mejores operaciones el resultado era **−201,39 €**. Todo el beneficio eran tres aciertos, con una caída máxima del 74,9 %.
**Regla**: el primer número que se mira de cualquier backtest no es el capital final, es **el resultado sin las 3 mejores operaciones**. Si eso es negativo, no hay estrategia: hay una cola derecha gorda. (Mismo patrón que cerró Memecoin-LSTM con un +57 % que era una moneda haciendo x154.)

### 30. Rellenar con `random` lo que debía venir del feed, y escribirlo en el log de producción

**Symptom**: `crypto-copy-bot` mostraba +5.416 SOL sobre 10 de capital, con una posición de 271 SOL. Parecía una estrategia que funcionaba.
**Causa**: `service.py` no usaba el feed. Generaba el tick de precio con `random.uniform(-0.02, 0.025)` —media **+0,25 % por tick**— y las señales al azar, todo al mismo `trade_log.jsonl` que leía el dashboard. Era una caminata aleatoria sesgada, compuesta por un sizing del 5 % de la equidad. Las métricas de win-rate e "hipótesis validada" derivadas de ese log no medían nada.
**Regla**: los datos simulados nunca comparten archivo, ni esquema, ni nombre de evento con los reales; van a su propia ruta y con un campo `source: "sim"`. Y un simulador de precios no lleva deriva: `uniform(-x, +x)` simétrico, o la deriva se declara como supuesto. Si en un informe aparece un múltiplo de 3 cifras sobre el capital, la primera hipótesis es que la fuente es sintética, no que la estrategia funciona.

### 31. Escribir un conector y no cablearlo nunca

**Symptom**: `FeedConnector` existía, tenía su test y su lógica de reconexión. El bot llevaba días "en marcha" sin haber escuchado una sola alerta real.
**Causa**: la clase solo se instanciaba en `tests/test_feed.py`. Ningún camino de producción la importaba, y nada lo señalaba porque el daemon tenía su propia fuente (la aleatoria del punto 30).
**Regla**: al dar por terminado un componente de entrada/salida, `grep` de su nombre fuera de `tests/`. Si solo aparece en su definición y en su test, no está integrado: está en el repo. Un test que lo instancia no demuestra que el sistema lo use.

### 32. Controles de riesgo declarados, simulados o inaplicados

**Symptom**: el bot tenía `max_position_sol=0.5`, `require_rugcheck_pass=True`, `max_slippage_bps`, whitelist y hard stop. Ninguno protegía de nada.
**Causa**: cuatro patrones distintos a la vez. (a) El tope vivía en el executor y el orquestador recalculaba el tamaño por su cuenta → hasta el 16 % de la equidad por orden. (b) El rugcheck fijaba `has_freeze_authority=False, has_mint_authority=False, is_honeypot=False` "simulado", así que el filtro **nunca** rechazaba. (c) `if self.whitelist and wallet not in self.whitelist` → una lista vacía aceptaba a cualquiera. (d) El hard stop hacía `break` del bucle sin persistir nada, y un reinicio lo anulaba.
**Regla**: un control que no puede rechazar no es un control, es un comentario. Por cada límite: un test que lo haga **disparar** (no solo pasar), el cálculo del tamaño en un único sitio por el que pase toda orden, y la ausencia de verificador se traduce en rechazar, no en aprobar. Un flag de seguridad sin implementación detrás se desactiva de forma explícita y ruidosa; "simulado a True" es peor que apagado porque da falsa confianza.

### 33. Reconstruir el saldo sumando el log en vez de persistir el estado

**Symptom**: reiniciar el bot subía la equidad y borraba las pérdidas latentes. El freno del −15 % se esquivaba con un reinicio (y `systemd Restart=always` lo haría solo).
**Causa**: `_reconcile_from_history` sumaba el PnL realizado del log pero nunca reconstruía `self.positions`, así que `open_capital` valía 0 y el coste de lo abierto volvía a caja. Además sumaba valores **redondeados** a 4 decimales, perdiendo precisión en cada trade.
**Regla**: el estado contable se persiste como snapshot propio, escrito de forma atómica (`tmp` + `fsync` + `os.replace`), y el log queda solo como auditoría. Nunca derivar el saldo de un log de eventos redondeados. Prueba obligatoria: abrir posición → marcarla a pérdida → reinstanciar desde disco → la equidad debe coincidir al céntimo.

### 34. Reescribir un componente y perder funciones del original sin inventariarlas

**Symptom**: en `crypto-copy-bot` el bot reescrito no tenía trailing stop: QI llevaba un -25 % desde su máximo y nada lo cerraba. Haytham lo notó por otra vía (el límite de posiciones).
**Causa**: el original ponía `trailing_stop_pct: 0.15` en cada lote, pero en la reescritura no hice una lista de lo que el código viejo hacía; solo arreglé lo que la auditoría marcó como roto. Además cambié sin avisar parámetros de negocio (tamaño base 5 % → 2 %, límite de 5 lotes → 6).
**Regla**: antes de reescribir, inventario de comportamientos del original (cada constante, límite y regla de salida) y cada uno acaba en "conservado", "cambiado (con motivo, avisado)" o "eliminado (con motivo)". Los números de negocio que el usuario fijó (5 %, 5 lotes) no se tocan por defecto y, si se cambian, se dice en la primera respuesta, no cuando el usuario lo descubre.

### 35. Mover trabajo a hilos sin proteger la comprobación-y-acción

**Symptom**: con límite de 5 posiciones, 8 señales simultáneas abrían 8 (reproducido en test).
**Causa**: pasé `handle_signal` a `asyncio.to_thread` para no bloquear el event loop con HTTP, pero la secuencia "comprobar límite → abrir posición" no era atómica y la cartera no tenía lock. La auditoría previa había dicho "no hay carrera, todo es síncrono": dejó de ser cierto con mi cambio.
**Regla**: al introducir hilos, revisar cada secuencia leer-decidir-escribir y ponerla bajo un lock; lo lento (HTTP) va fuera del lock y la decisión dentro. Y el test de una carrera se verifica **desactivando el lock** para comprobar que el test falla sin él; si no falla, no prueba nada.

### 36. Diagnosticar "no se actualiza" en la capa equivocada

**Symptom**: Haytham veía el PnL del dashboard "parado". Había subido el refresco de la UI (3 s → 2 s) y el del bot (20 s → 5 s) sin mirar si servía.
**Causa**: ni la UI ni el bot: la **fuente** (DexScreener) solo cambia el precio de estos tokens ~1 vez cada 40 s. Además, la tarjeta principal ("PnL realizado") por definición solo cambia al cerrar posiciones, y los lotes de otras cadenas (BSC, Robinhood) no los cubre Jupiter.
**Regla**: ante "no se actualiza", medir cada capa por separado antes de tocar nada (fuente → bot → API → DOM) comparando valores en el mismo instante; y medir la cadencia real de la fuente en vez de suponerla. Una métrica que solo puede cambiar con eventos raros no debe ser la cifra principal de un panel "en vivo". Un indicador de frescura debe medir cuándo CAMBIÓ el dato, no cuándo lo consulté.

---

### 37. Patrón ganador: Generación proactiva de prompts de imagen contextuales para la UI

**Síntoma**: aplicaciones o dashboards funcionales pero visualmente fríos o desangelados, con cajas vacías o iconos genéricos donde deberían lucir imágenes representativas del negocio.
**Causa**: esperar a que el usuario diseñe o busque las imágenes, o dejar placeholders grises.
**Regla**: redactar proactivamente prompts fotorrealistas/3D hipercontextualizados (ej. maquetas de obra, planos técnicos, personal con EPIs, certificados visuales) para que el usuario o el generador cree los assets clave de un vistazo, integrándolos con tratamiento visual cuidado (badges, sombras suaves, overlays de legibilidad).

### 38. Asumir persistencia o existencia de tablas remotas sin validar ciclo completo en producción

**Síntoma**: datos eliminados o creados que reaparecen al refrescar tras desplegar en Vercel; acciones que fallan silenciosamente al intentar borrar registros con claves foráneas.
**Causa**: asumir que una migración SQL local existe en la base remota de Supabase, recurriendo a un fallback de memoria volátil en Server Actions que se reinicia con cada lambda serverless; y no prever borrado en cascada para registros con dependencias relacionales (como clientes con facturas).
**Regla**: antes de dar por buena una funcionalidad de base de datos o estado:
1. Verificar si la tabla remota existe realmente en Supabase. Si no hay DDL directo, persistir en Supabase Storage JSON inmediatamente, nunca en memoria del proceso.
2. Todo borrado relacional debe contemplar borrado en cascada transaccional o advertir claramente los vínculos dependientes.
3. Test obligatorio de ciclo completo: crear → recargar → borrar → recargar en producción.

---

### 39. Fallback arbitrario (|| 1) y omisión de campos en inserts de BD

**Síntoma**: al crear una obra o recurso con un importe válido (ej. presupuesto de 150.000 €), en la pantalla de detalle aparece con 1 €.
**Causa**: dos fallos combinados:
1. La Server Action (`createProjectAction`) validaba el dato en Zod pero omitió `presupuesto_total` en el objeto `.insert()` de Supabase, guardándolo como `null`.
2. En la lectura de la ficha (`getAdminObraDetallesAction`), para evitar división por cero en el porcentaje de desviación, se usó `Number(project.presupuesto_total) || 1` como valor del presupuesto en lugar de condicionar únicamente el cálculo del divisor.
**Regla**:
1. Todo campo de formulario validado debe mapearse explícitamente en el `.insert()` / `.update()` hacia la base de datos.
2. Nunca usar fallbacks numéricos ficticios (`|| 1`) en campos monetarios o de negocio; proteger solo las operaciones aritméticas que lo requieran (`presupuesto > 0 ? gasto / presupuesto : 0`).
3. Añadir siempre capacidad de edición directa en la vista de detalle para corregir datos sin obligar a recrear el recurso.

**Last Updated**: 2026-10-12

### 40. Resiembra automática de datos demo al vaciar una colección (re-seeding on empty list)

**Síntoma**: el usuario borra todos los registros de prueba (ej. partes de trabajo) y al recargar la página vuelven a aparecer exactamente los mismos registros iniciales.
**Causa**: la función lectora (`getStoredPartes`) comprobaba `if (validados.length > 0) return validados;` y, al llegar a 0 elementos tras ser borrados, asumía que "no existía aún", resembrando automáticamente los datos demo de prueba (`INITIAL_DEMO_PARTES`) en Supabase Storage.
**Regla**: una colección vacía (`[]`) es un estado de datos completamente válido. Comprobar si el contenedor existe (`Array.isArray(parsed)`) y devolver los elementos validados (aunque sean 0). Nunca resembrar datos ficticios automáticamente ante una lista vacía intencionada.

### 41. Caché persistente de Next.js Data Cache sobre llamadas internas de Storage

**Síntoma**: tras eliminar o modificar un archivo JSON en Supabase Storage, al recargar la página en Next.js App Router vuelven a aparecer los registros antiguos como si no se hubieran borrado.
**Causa**: `@supabase/storage-js` ejecuta `fetch()` internamente sin `cache: 'no-store'` ni clave de timestamp. En Next.js 14/15, el servidor almacena la respuesta en su Data Cache persistente y la sirve en cada recarga sin volver a consultar Supabase.
**Regla**: para persistencia en Storage JSON en Next.js, usar `fetch()` directo con cabecera `cache: 'no-store'`, headers de API key explícitos y parámetro timestamp (`?t=${Date.now()}`) para garantizar bypass absoluto de la caché; y sincronizar el estado reactivo del componente cliente cuando cambien las props tras revalidar.

### 42. Atribuir un proyecto a NeoZeler por defecto
**Symptom**: el PRD de Reto 30 ponía a NeoZeler como admin y como receptor del 85 % de los ingresos; Haytham corrigió que es un proyecto suyo y de su amigo Pedro.
**Causa**: asumir que todo lo del vault es de la agencia por contexto (plantillas, enlaces `[[NeoZeler]]` en notas antiguas).
**Regla**: antes de nombrar propietario, reparto de ingresos o enlace a NeoZeler, comprobar de quién es el proyecto; si no está claro, preguntar. Ver memoria `feedback-no-todo-es-neozeler`.

### 43. Proponer un modelo para predecir algo que el sistema ya define por fórmula
**Síntoma**: la idea "predecir el coste real con una regresión" (T2 del plan ML) no tenía sentido: el coste del papel-trading lo calcula el propio bot (suelo 1 % + 20 × tamaño/liquidez, red fija) y casi no varía (62 de 77 compras con 1,0 %).
**Causa**: diseñar la idea desde la nota de memoria sin abrir `paper_wallet.py` ni medir la variación de los datos antes de proponerla.
**Regla**: antes de proponer un modelo sobre una variable, comprobar de dónde sale (medida real o fórmula del propio sistema) y cuánto varía. Si es fórmula o casi constante, no es un problema de ML. Medir antes de proponer.

### 44. Dar por cierta una fecha y una "v2" que eran provisionales
**Síntoma**: tras la sesión del 2026-10-17 se resumió Reto 30 con "revisión v2" e "inicio el 1 de noviembre"; Haytham aclaró que no hay v2 (todo es la v1) y que la fecha era un ejemplo.
**Causa**: escribir una fecha de ejemplo del chat como dato del proyecto y etiquetar con "v2" cada cambio en vez de integrarlo en el documento.
**Regla**: una fecha dicha como ejemplo no se guarda como dato; ante la duda, preguntar. Los cambios de alcance de un proyecto aún sin código se integran en los documentos sin sufijos de versión. Al informar del pendiente, partir de la nota del proyecto y confirmar fechas con Haytham.

### 45. Patrón con condiciones que se contradicen: 0 señales y ningún aviso
**Síntoma**: las banderas daban 0 operaciones en 2 años de datos (en TradingView el panel salía "Activo" sin errores y nadie lo notó).
**Causa**: la pendiente de la consolidación se medía incluyendo la vela de ruptura; esa vela cierra fuera del rango y vuelve la pendiente positiva, así que "pendiente <= 0" y "rompe el máximo" nunca coincidían.
**Regla**: al escribir un patrón con varias condiciones, contar en el backtest cuántas velas cumplen cada subcondición y en acumulado; un patrón con 0 operaciones es un fallo hasta demostrar lo contrario. Los atributos del setup se miden con velas previas a la vela de gatillo. Y valorar siempre contra una línea base aleatoria con los mismos stop, RR y comisión (en 5m la ventaja bruta era +0,04 R frente a un coste de 0,28 R).

### 46. Identificador de día calculado con la unidad de tiempo supuesta
**Síntoma**: las pruebas de `alts.py` fallaron: los límites de "3 operaciones al día" y "-3 % diario" no se reiniciaban nunca y solo operaba el primer día del periodo.
**Causa**: `index.floor("D").asi8 // 86_400_000_000_000` asume nanosegundos; con pandas 3.0 `date_range` y los parquet usan microsegundos, así que todos los días daban el mismo número.
**Regla**: no usar `asi8` con divisores fijos. Calcular días con `(index.floor("D") - pd.Timestamp("1970-01-01", tz="UTC")) // pd.Timedelta(days=1)`. Y escribir las pruebas de límites antes de correr datos reales: este fallo habría aplicado los límites diarios a dos años enteros como si fueran un solo día.

## Laya Trader: servidor, motor y panel (proyecto `01_Projects/Laya Trader`, 2026-10-22)

### 47. `pkill -f` / `pgrep -f` se encuentran a sí mismos (reaparición 2)
**Síntoma**: la orden `pkill -f "laya-trader panel"` mató la propia sesión SSH y el resto de la orden no se ejecutó; `pgrep -f medir_laya` decía «sigue» con el proceso ya terminado.
**Causa**: el patrón también aparece en la línea de órdenes de la shell que lo ejecuta.
**Regla**: liberar un puerto con `fuser -k PUERTO/tcp` y comprobar un proceso con el archivo que genera (o `pgrep -af "[p]atron"`). Ya está en `librerias.md`; una tercera vez sube a norma dura.

### 48. `zorin-ssh`: órdenes con saltos de línea y esperas largas
**Síntoma**: `Command cannot contain a line break` con heredocs y scripts de varias líneas; `timed out after 60000ms` en bucles de espera.
**Causa**: `run-command` solo acepta una línea y corta a los 60 s.
**Regla**: scripts por `sftp-upload` y ejecutarlos por ruta; procesos largos con `(nohup … &)` y consultar su log o su base en otra llamada; ninguna espera encadenada pasa de ~55 s.

### 49. Conexión SQLite abierta en un hilo y usada en otro: 500 solo en el servidor real
**Síntoma**: el panel daba 500 en producción con `SQLite objects created in a thread can only be used in that same thread`; las 19 pruebas de la API pasaban.
**Causa**: FastAPI abre la dependencia en un hilo del grupo y ejecuta el endpoint síncrono en otro; el `TestClient` reutiliza siempre el mismo hilo y no lo reproduce.
**Regla**: conexión por petición con `check_same_thread=False` (uso exclusivo) y una prueba de regresión que cree la conexión en un hilo y la use en otro. Mirar siempre el panel en el servidor real antes de dar por buena una API.

### 50. FastAPI con `from __future__ import annotations`: alias `Annotated` dentro de una función
**Síntoma**: todas las rutas pedían `conn` como parámetro de consulta (`Field required`).
**Causa**: FastAPI resuelve las anotaciones como texto y no ve alias definidos dentro de `create_app`.
**Regla**: los alias `Annotated[..., Depends(...)]` y las dependencias van a nivel de módulo (leen el estado de `request.app.state`).

### 51. Pruebas que pasan con datos de prueba inválidos
**Síntoma**: el feed sintético dejaba el libro cruzado (compra mayor que venta, spread −228 puntos) y las 205 pruebas pasaban; se vio en el navegador.
**Causa**: las eliminaciones de niveles se enviaban al lado equivocado y ninguna prueba comprobaba la validez del generador.
**Regla**: todo generador de datos sintéticos lleva una prueba de sus invariantes (aquí `mejor compra < mejor venta` en cada paso). Mirar una vez los datos de demostración con los ojos.

### 52. Cambios de JavaScript que no se ven: caché del navegador y módulos
**Síntoma**: tras editar `ui.js` el navegador seguía con el viejo («hace 8798,8 h» en vez de «367 días»).
**Causa**: los módulos importados se guardaban con caducidad heurística aunque `index.html` cambiara de URL.
**Regla**: servir los estáticos con `Cache-Control: no-cache` (ETag) y, al probar, forzar `fetch(archivo, {cache: "reload"})` de cada módulo tocado antes de recargar.

### 53. Parches por texto exacto tras `ruff format`, y parches a medias
**Síntoma**: `AssertionError` al parchear una función que el formateador había reescrito en varias líneas; el primer archivo ya estaba escrito y el segundo no.
**Causa**: se escribía cada archivo según se validaba, y el texto esperado era el anterior al formateo.
**Regla**: `grep` del texto real antes de parchear y comprobar **todos** los reemplazos en memoria antes de escribir ningún archivo; no formatear entre el diseño del parche y su ejecución.

### 54. Fórmula de tamaño pensada para dos clases usada con tres
**Síntoma**: `kelly_hat = 2·confianza − 1` daba tamaño 0 para cualquier confianza < 0,5; Laya (0,35-0,44 en `direction`, tres respuestas) nunca habría operado y el experimento habría acabado en «no sirve» por la fórmula.
**Causa**: se congelaron las reglas sin probarlas con la distribución real de las entradas.
**Regla**: antes de aprobar reglas numéricas, pasarles 30 casos reales del modelo y mirar qué decisiones salen. Un cambio así se hace antes de medir, con fecha, igual en las dos carteras y anotado.

### 55. `systemd`: el servidor no deja escribir en `/etc/systemd`
**Síntoma**: `POLICY_DENIED: writing to /etc/systemd`; la orden entera se rechaza y no ejecuta nada (ni los `sed` que iban antes).
**Causa**: regla fija de `zorin-ssh`, no configurable.
**Regla**: servicios de **usuario** (`~/.config/systemd/user`, `WantedBy=default.target`, sin `User=` ni `PrivateTmp=`), `sudo loginctl enable-linger ssh` y `XDG_RUNTIME_DIR=/run/user/$(id -u)`. Comprobar siempre qué procesos viejos siguen en el puerto antes de arrancar el servicio.

### 56. Un barrido automático de contraste con `color-mix()` da falsos positivos
**Síntoma**: el barrido marcaba 1,08:1 en el título de la cabecera.
**Causa**: `getComputedStyle` devuelve `color(srgb 0.97 …)` y el análisis lo leyó como 0-255.
**Regla**: dar por falso un fallo automático solo tras comprobar el par a mano (aquí 18,7 / 5,1 / 7,7); si se repite el barrido, soportar el formato `color(srgb …)`.

### 57. GateGuard con ediciones en paralelo: se pierden ediciones sin avisar
**Síntoma**: de cuatro `Edit` lanzados a la vez, tres devolvieron «Fact-Forcing Gate» y solo se aplicó el que no era el primero de su archivo.
**Causa**: el primer `Edit` de cada archivo exige declarar hechos y falla; los demás se aplican.
**Regla**: declarar los hechos antes del primer `Edit` de cada archivo y, tras un lote, `grep` de lo que debía quedar escrito. Un `Write`/`Edit` rechazado es una edición no hecha.

### 58. Un intervalo de confianza sin datos suficientes contado como «fracaso»
**Síntoma**: una hora después de arrancar el panel mostró «LAYA NO SIRVE: SE CIERRA» con 0 operaciones, y Laya iba mejor que el programa de reglas.
**Causa**: el bootstrap por bloques de 1 h devolvía un intervalo infinito con un solo bloque, y la comparación `límite < 0` falsa se leyó como «no cumple». Ninguna prueba cubría «muchos juicios en poco tiempo».
**Regla**: toda prueba estadística distingue tres resultados (pasa, falla, no concluyente) y «no se puede calcular» es siempre no concluyente. Probar el veredicto con datos concentrados en poco tiempo y mirar el panel real a la hora de arrancar, no solo con datos simulados de días.

### 59. Una clase de CSS compartida entre dos cosas distintas rompe todo el JavaScript
**Síntoma**: tras desplegar el CRM, la pestañita de RAM/CPU no se movía, el tablero no arrastraba y el chip del modo de envío desaparecía a los 6 s. Las pruebas automáticas estaban en verde.
**Causa**: el aviso emergente se llamaba `.aviso` y el chip de advertencia era `.chip.aviso`; el script hizo `querySelectorAll(".aviso")`, intentó «cerrar» el chip, lanzó un error y el resto del archivo no llegó a ejecutarse.
**Regla**: un nombre de clase = una sola cosa (los avisos emergentes son `.toast`). Todo script del navegador con un `forEach` inicial debe poder fallar sin parar al resto. **Mirar la página real** (captura + `javascript_tool`) antes de dar una interfaz por terminada: las pruebas del servidor no ven el JavaScript del navegador.

### 60. Una vista previa en `iframe` con `sandbox` sale en blanco
**Síntoma**: el editor de correos mostraba el iframe vacío; abierta sola, la misma dirección se veía bien.
**Causa**: el atributo `sandbox` del `iframe` junto con `X-Frame-Options: SAMEORIGIN` en la respuesta (y `loading="lazy"` dentro de un `<details>` cerrado complicaba el diagnóstico).
**Regla**: para contenido propio aislar con la **cabecera** `Content-Security-Policy: sandbox; default-src 'none'; frame-ancestors 'self'` y no poner `X-Frame-Options` ni el atributo `sandbox` a esa respuesta. Probar siempre el `iframe` con una captura, no solo el estado HTTP.

### 61. Optimizar la memoria sin medir ruta a ruta
**Síntoma**: el CRM nuevo gastaba 66-90 MB (peor que el de Python, 57) aunque el servidor mínimo hacía 33.
**Causa**: no era el lenguaje: las listas cargaban un JSON de 2 KB por candidato que no se usaba y «Hoy» cargaba todas las filas completas para contar. Además el compilador JIT de Bun ocupa memoria.
**Regla**: medir la RAM pantalla a pantalla (`tests/carga_rutas.py`) antes de cambiar de tecnología; contar con `COUNT`, no con `SELECT *.length`; listas con columnas ligeras. En un servicio de un solo usuario, `BUN_JSC_useJIT=0` + `--smol` bajan de 66 a 44 MB.

### 62. Una prueba que falsifica un dato y falla 1 de cada 16 veces
**Síntoma**: `bun test` fallaba a ratos (vuelta 10 de 12) y pasaba al repetir.
**Causa**: la prueba cambiaba el último carácter hexadecimal de una firma por «0»; una de cada 16 veces ya era «0» y la firma quedaba intacta.
**Regla**: al falsificar un valor, cambiarlo **siempre** (`c.endsWith("0") ? "1" : "0"`). Antes de cerrar un proyecto, `scripts/repetir_pruebas.sh 20` para cazar intermitencias.

### 63. Borrar un repositorio sin commits sin copia comprobada
**Síntoma**: al retirar el Panel, `git status` dijo «sin ningún commit»: todo el código era archivos sin versionar.
**Causa**: proyectos de `~/Proyectos/` creados con `git init` pero sin primer commit; borrar es irreversible.
**Regla**: antes de borrar nada de un proyecto, copia `.tgz` **comprobada** (`tar -tzf` y archivos clave presentes) y un script de borrado que se niega a correr sin ella. Hacer el primer commit en cuanto el proyecto funcione.

### 64. `pkill -f` con el patrón en la propia línea, y `sftp-upload` sin carpetas
**Síntoma**: la shell remota se mató sola (código 144) y varios `sftp-upload` fallaban con «No such file».
**Causa**: `pkill -f "cli.ts web"` coincide con el comando que lo lanza; `sftp-upload` no crea carpetas.
**Regla**: liberar puertos con `fuser -k PUERTO/tcp`; crear la carpeta con `mkdir -p` antes de subir archivos; y para parchear un archivo del servidor, subir un script que haga `replace` con `assert count == 1` (`Edit` y `Read` locales no ven el servidor).

### 65. Pulsar «Enviar» en una copia de la base que apunta al n8n real
**Síntoma**: al probar la interfaz con una copia de `crm.db`, el botón de correo habría llamado al flujo real de n8n con un negocio verdadero.
**Causa**: la dirección del webhook y el token viven en `ajustes`, y la copia los hereda.
**Regla**: antes de pulsar cualquier botón que avise a un servicio externo en una copia, cambiar su dirección a un eco local (`/ajustes/webhook`) o vaciarla; comprobar con `SELECT valor FROM ajustes WHERE clave='webhook_url'`.

### 66. Filtrar la salida de pruebas con «Received»
**Síntoma**: una sola línea del filtro de `bun test` llenó el contexto con la página HTML completa.
**Causa**: `expect(...).not.toContain` imprime el texto recibido entero y el `grep` lo dejó pasar.
**Regla**: filtrar solo `^(fail)|pass|fail|Ran` y pasar por `cut -c1-200`; ver el detalle de un fallo aparte, acotado.


### 67. Rediseñar una sola pantalla y dejar el resto de la aplicación como estaba
**Síntoma**: tras «rehacer la pantalla Hoy», la barra lateral oscura no cuadraba con el cuerpo nuevo y Campaña, Negocios y Ajustes seguían con la cara vieja (2026-10-26, CRM NeoZeler). Haytham tuvo que señalarlo.
**Causa**: se trató la petición como «una pantalla» y no como «la identidad de la aplicación»; la cabecera/navegación y los componentes compartidos (tarjetas, títulos, botones) se dejaron para después.
**Regla**: un rediseño de identidad cubre **el marco (navegación, cabecera, pie), los componentes compartidos y todas las pantallas** desde la primera entrega. Antes de enseñar nada: listar las pantallas de la app, abrir cada una en el navegador y declarar en la respuesta cuáles están hechas. Si una pantalla se deja fuera a propósito, decirlo antes, no después.

### 68. Inventar la paleta en vez de sacarla de la marca
**Síntoma**: el panel salió en azul cobalto y amarillo, y Haytham dijo que los colores no coincidían con NeoZeler (2026-10-26).
**Causa**: se partió de la maqueta de una dirección visual y no del logo ni de la guía de marca; el amarillo no existe en NeoZeler y el azul era otro.
**Regla**: la paleta **sale de la marca**, nunca de la imaginación: leer `PRODUCT.md`/guía y **muestrear los colores del logo** antes de elegir ninguno (azul NeoZeler `#2563eb`, marino `#1e3a8a`, grafito y el azul hielo del logo). Un color nuevo solo entra si es neutro o si Haytham lo pide. Escribir en `DESIGN-IDENTITY.md` de dónde sale cada color.
**Reincidencia (2026-11-17, ARM)**: para un producto «de NeoZeler» propuse ciruela y latón y un logo de compás sin mirar `99_Assets/logos/`; Haytham pidió colores y parte del logo de NeoZeler «sin parecerse». Antes de proponer logo o paleta de un producto NeoZeler: leer `99_Assets/logos/` (Z de cinta metálica azul hielo y grafito sobre cuadrado negro) y heredar material y color, no la forma.

### 69. El hook `guard-destructive.py` bloquea un comando por el texto de un archivo que se escribe
**Síntoma**: un `cat > archivo <<EOF` que escribía las reglas `deny` de un proyecto fue bloqueado por contener «terraform destroy»; pasó dos veces seguidas el mismo día, la segunda al documentar el propio fallo (2026-10-28, starter-saas). Nada se ejecutó.
**Causa**: el hook busca los patrones en todo el `tool_input`, también en el contenido de heredocs; no distingue ejecutar de escribir.
**Regla**: los archivos que contengan esas cadenas (listas de bloqueo, documentación) se escriben con `Write`/`Edit`, no con heredoc de Bash. No desactivar el hook. Mejora pendiente: que el hook ignore el contenido tras `<<`.

### 70. Una prueba de seguridad en verde a la primera no prueba nada hasta que se la hace fallar
**Síntoma**: 15 pruebas de RLS pasaron a la primera; al mutar una migración (quitar un `revoke`) una mutación sobrevivía porque la RLS bloqueaba igual (2026-10-28, starter-saas).
**Causa**: dos capas de defensa (privilegios y RLS) y pruebas que solo miraban el resultado, no la capa.
**Regla**: tras escribir pruebas de seguridad, **mutar a mano** la política o el permiso (abrirlo, quitarlo) y exigir que alguna prueba falle; si sobrevive, añadir una prueba de esa capa (`has_table_privilege`). Comprobar los errores de permisos en orden: primero autorización, después existencia (si no, un ajeno puede sondear quién es miembro).


### 71. Entregar un dibujo tras otro sin preguntar qué quería ver Haytham
**Síntoma**: para rellenar el hueco de las preguntas frecuentes se hicieron tres dibujos SVG (camino de pasos, Z del logo, «?» de puntos) y los tres se rechazaron con «no me gusta»; lo que servía era una tarjeta de contacto (2026-10-31, neozeler-web).
**Causa**: ante un «no me gusta» sin detalle se rehízo la misma clase de cosa en vez de ofrecer enfoques distintos; el primer encargo («qué svg podríamos poner») pedía ideas, no una obra.
**Regla**: si un adorno visual se rechaza una vez, la siguiente propuesta ofrece **2-3 enfoques de naturaleza distinta** (dibujo / tarjeta útil / sin nada) con `AskUserQuestion` antes de construir; tras el segundo rechazo, parar y preguntar qué falla. Un hueco de maquetación se resuelve primero como layout o contenido útil (CTA) y solo después como decoración.

### 72. Verificar contra un servidor de producción con la build vieja
**Síntoma**: el SVG no aparecía en `localhost:3000` aunque el código estaba bien; `querySelector` devolvía `null` (2026-10-31, neozeler-web).
**Causa**: el puerto 3000 lo servía un `npm run start` (producción) con una build de días antes; no un `next dev`.
**Regla**: antes de mirar un cambio en el navegador, `ss -ltnp | grep :<puerto>` y `ps -o args` para saber si es dev o prod. Para iterar: `next dev -p 3100` aparte; para entregar: `npm run build` y reiniciar el servidor de producción. Ese servidor no está supervisado (ver mejoras pendientes).

### 73. `pkill -f "<comando>"` dentro del mismo comando de Bash mata la propia shell
**Síntoma**: `pkill -f "next dev -p 3100"; ...` terminó con código 144 y el resto del comando no se ejecutó (2026-10-31).
**Causa**: `-f` busca en toda la línea de comandos y la de la shell que lo lanza contiene esa misma cadena.
**Regla**: matar por PID: `kill $(ss -ltnp | grep ':<puerto>' | grep -o 'pid=[0-9]*' | cut -d= -f2)`. Con `npm run start`, matar también el padre y el abuelo (`ps -o ppid=`).

### 74. Node por defecto (18) con Next 16
**Síntoma**: `next dev` abortó con «Node.js ">=20.9.0" is required» (2026-10-31).
**Causa**: el `node` del PATH es 18.19.1.
**Regla**: anteponer Node 22 de fnm: `PATH=$(ls -d ~/.local/share/fnm/node-versions/v22*/installation/bin | head -1):$PATH` en `tsc`, `build`, `dev` y `start` de proyectos Next.

### 75. WebGL no existe en el navegador del panel de Claude
**Síntoma**: escenas 3D (NeoZeler Mundo, Dashboard Command AI, Vault OS, Z 3D de neozeler-web) «verificadas» sin haberse visto nunca; el contexto WebGL no se crea (2026-11-05/06/10).
**Causa**: el navegador integrado no tiene GPU/WebGL; capturar ahí da escena vacía.
**Regla**: verificar 3D con Chromium de Playwright: `--use-angle=swiftshader --enable-unsafe-swiftshader --virtual-time-budget`. Si ni eso basta, decirlo y pedir a Haytham que abra la URL local en su navegador; nunca dar un 3D por visto.

### 76. Lighthouse actual exige Node 22 y mide sin GPU
**Síntoma**: Lighthouse no arranca con el Node 18 del sistema; con el equipo cargado el móvil varió de 75 a 93 en la misma página (2026-11-05, 2026-11-11).
**Causa**: Node del PATH = 18; Lighthouse corre sin GPU y es sensible a la carga de la máquina.
**Regla**: instalar Lighthouse 11.7.1 solo en el scratchpad (o usar Node 22 de fnm, ver 74); correr varias veces y dar la mediana; avisar de que no mide el coste real del 3D.

### 77. `shadcn-registries` MCP devuelve vacío sin `components.json`
**Síntoma**: el buscador veía 0 registries; `@aceternity` y `@spaceui` fallan por certificado (2026-11-01/02/04).
**Causa**: el MCP lee la config del proyecto; sin `components.json` no hay registries.
**Regla**: buscar con la CLI desde una carpeta temporal (`npx shadcn@latest search @ns`, Node 22). No desactivar la verificación de certificados.

### 78. Reglas de seguridad (RLS): un `update` sin permiso no da error
**Síntoma**: pruebas en verde aunque el permiso fallaba (2026-11-04, Comanda Viva).
**Causa**: RLS afecta a 0 filas sin error.
**Regla**: las pruebas comprueban `returning` vacío (o recuento de filas) además de «sin error». PGlite es una sola conexión: la concurrencia real se prueba en staging.

### 79. Aplicar el contenido de un PDF como si fuera «añadir diapositivas»
**Síntoma**: la primera pasada de NeoFlow pitch «según el PDF» no respetó el orden ni pidió el mapa literal (2026-11-09; otra vez el 2026-11-11 con los cambios del PDF).
**Causa**: se resumió el PDF en vez de seguirlo punto a punto.
**Regla**: convertir el PDF en lista numerada de cambios (orden, texto literal, elementos pedidos), confirmar que está completa y marcar cada punto al terminar.

### 80. Fondo en `body` tapa los hijos `position:fixed` con `z-index:-1`
**Síntoma**: fondo animado/SVG invisible en la landing de NeoFlow (2026-11-05).
**Causa**: si `html` tiene fondo, el `body` con fondo pinta como bloque y cubre los fixed con z-index negativo.
**Regla**: el fondo va solo en `html`. Igual: `[hidden]` se anula con cualquier `display:`; usar `[hidden]{display:none !important}`. `transform` CSS sobre círculos SVG con degradado deja borde duro en Chromium: mover con `cx`/`cy`.

### 81. Capturas a mitad de animación salen vacías (y el hook de commit las exige)
**Síntoma**: capturas en blanco por el reveal; `guard-ui-commit` bloquea el commit sin capturas 375 y 1280 de las últimas 12 h en `.capturas/` (2026-11-05/10).
**Regla**: desactivar transiciones antes de capturar y guardar 375 y 1280 en `.capturas/` antes de commitear UI.

### 82. Repo nuevo sin identidad git, y Vercel rechaza el email equivocado
**Síntoma**: Vercel bloqueó el despliegue porque los commits llevaban un email no asociado a la cuenta de GitHub (2026-11-05, neoflow-pitch); otros repos sin `user.name`/`user.email` (reto-30).
**Regla**: antes del primer commit en un repo nuevo, comprobar `git config user.email`; fijarla solo en local con la identidad de GitHub del dueño (`abhaythambusiness-tech`). Nunca global ni en el historial de otros.

### 83. Dos sesiones en el mismo repo se pisan los archivos
**Síntoma**: cambios de dos sesiones mezclados en los mismos archivos de Reto 30, imposibles de separar (2026-11-11).
**Regla**: una sola sesión escritora por repo o por conjunto de archivos; la segunda va en worktree o espera.

### 84. `.env.local` vs variables de producción
**Síntoma**: correo de Reto 30 probado en local con `.env.local` y asumido válido en producción (2026-11-11).
**Regla**: `.env.local` = desarrollo; producción = variables de Vercel. Tras un cambio de correo/claves, comprobar que están en Vercel. Los `.env*` no se leen con `cat`; comprobar por efecto (script de verificación).

### 85. n8n: workflow sin Publish, URL de test y `Execute Workflow`
**Síntoma**: el cron no corría; el webhook de test no servía en producción; al reelegir el workflow en un nodo `Execute Workflow` se borraron los campos (2026-11-10, Setter WhatsApp).
**Regla**: pulsar **Publish** tras cada cambio; usar solo la URL de producción con el workflow activo; tras reelegir un sub-workflow, volver a poner todas las expresiones.

### 86. Dar por válido un test que aborta a medias o un dato vacío por diseño
**Síntoma**: script de pruebas abortado dejó datos demo importados en NeoZeler HQ; ranking de Reto 30 «vacío» no era un fallo (2026-11-05/07).
**Regla**: limpiar los datos demo antes de repetir; mirar los datos reales antes de tocar código; probar el peor caso (nombre de 98 caracteres) además de los normales.

### 87. Auditorías de otra IA y listas de skills de arranque
**Síntoma**: una auditoría externa mezcló verdades y suposiciones; plugins habilitados en mitad de sesión no aparecían (2026-11-03/05).
**Regla**: comprobar cada afirmación contra `settings.json` y los archivos reales; skills/plugins nuevos solo existen tras reiniciar `claude`; la autorización de MCP (`/mcp`) se hace en una terminal con `claude`, no en la app de escritorio.

### 88. Tras `usar.sh` (USB), rutas `/home/haytham` sin reescribir
**Síntoma**: en el equipo del aula `env.PATH` y `env.SSH_MCP_KEY` de `~/.claude.json` seguían con la ruta antigua; Node no estaba donde decía fnm; sin `git` ni sudo (2026-11-03).
**Regla**: tras `usar.sh`, `grep -c "/home/haytham" ~/.claude.json`; localizar Node con `readlink -f ~/.local/bin/node`; el USB puede llamarse distinto (`lsblk`); `zorin-ssh` no alcanza desde otra red.

### 89. Foto y descripción de un ejercicio se contradicen
**Síntoma**: en Reto 30 foto y texto eran «correctos» para el ejercicio base pero no para la variante (flexión en pared con foto del cajón) (2026-11-09).
**Regla**: foto, descripción y nombre se validan por variante; si no hay imagen exacta, decirlo y proponer prompt de generación.

### 90. Una tarea del vault no puede ir en una rutina de la nube
**Síntoma**: la rutina cloud no veía el disco local; el modo Auto bloqueó `run_scheduled_task` (2026-11-02, 2026-11-11).
**Regla**: lo que toque el vault corre como tarea local (`scheduled-tasks`); la primera creación necesita permiso explícito; lanzar con «Run now» o esperar su hora.

### 91. Buscar referencias en Dribbble cuando Haytham no las quiere
**Síntoma**: al diseñar la web de la Benimar 495 se lanzó `dribbble-scrape` (fase 0b de `diseno-central`) sin que se pidiera; Haytham cortó: «no más referencias de Dribbble» (2026-11-13).
**Regla**: no usar `dribbble-scrape` ni proponer referencias de Dribbble. Para dirección visual, partir de las fotos reales del proyecto y proponer direcciones de diseño propias; si hacen falta referencias, solo si Haytham las pide y de otra fuente. Pendiente de decidir si se quita la fase 0b de `diseno-central` y del `CLAUDE.md` global (preguntado a Haytham).

### 92. Proyecto con interfaz sin fijar las 1-2 librerías de UI obligatorias
**Síntoma**: en Panel de Leads (2026-11-13) la Ficha listó shadcn/magicui/21st solo como «candidatas» y el TRD se aprobó sin la fila de librerías de UI ni tarea en el Plan; Haytham tuvo que preguntar «has mencionado lo del mínimo de una o dos librerías». Regla global del 2026-11-13.
**Regla**: todo proyecto con interfaz lleva en la Ficha y en el TRD §1 una fila «Librerías de UI (mínimo 1 o 2)» con nombres concretos, y en el Plan una tarea de Paleta de Componentes (buscar en shadcn/magicui/21st antes de escribir a mano). Sin esa fila, el TRD no se pide para aprobar. Plantilla TRD y skill `nuevo-proyecto` actualizadas para que salga sola.

### 93. Entregar listas y kanban pensados solo para pocos datos
**Síntoma**: el pipeline del Panel de Leads salió con todas las fichas visibles, cada una con su conversación entera en el navegador y sin buscador; Haytham avisó: con mucho volumen «el pipeline se va a saturar» (2026-11-14).
**Regla**: toda vista de lista o tablero se prueba con ~60 filas de muestra antes de darla por buena: tope por columna con «Ver más», buscador, orden por actividad reciente, scroll interno y paginación en la lista; al cliente solo se le mandan los campos que pinta la tarjeta (no objetos enteros). Los datos de muestra deben tener volumen, no 4 filas.

### 94. Dar por buena en un pitch una afirmación de modelo de negocio sin confirmarla
**Síntoma**: la diapositiva de competencia de NeoFlow decía «Producto, no proyecto a medida»; Haytham: «sí hacemos proyectos a medida, está al revés» (2026-11-14). Además dejé un hueco enorme en la tarjeta derecha tras recortar texto.
**Regla**: al reescribir o acortar texto de un pitch, no arrastrar frases de posicionamiento (producto vs. a medida, precio, alcance) sin comprobarlas con Haytham o la ficha. Tras recortar una tarjeta, revisar el espacio sobrante (centrar o aumentar tipografía).

### 95. Cambio de nombre a medias y adornos animados no pedidos
**Síntoma**: Haytham pidió quitar «.AI» de la marca de NeoFlow; solo cambié la esquina y el h1 de portada seguía «NeoFlow AI». Además la capa de UI llevó marcos con luz giratoria (border beam) que no le gustaron (2026-11-15).
**Regla**: al renombrar o quitar un término, `grep -i` en todo el HTML y cambiar todas las apariciones visibles (o preguntar cuáles). Efectos animados de contorno/brillo: no añadirlos por defecto; ofrecerlos como opción.

### 95. Buscar texto en HTML con `cut -c` y negar que existe
**Síntoma**: Haytham pidió 3 veces quitar «España: 3,31 M de empresas activas»; dije que no estaba en el código y culpé a Vercel, pero estaba en `<p class="mapcap">` al final de una línea larguísima (2026-11-14).
**Regla**: no recortar la salida de `grep` con `cut` en archivos con SVG en línea (la coincidencia puede quedar fuera). Buscar con `python3 -c "s.find('texto')"` o `grep -o` con contexto, y comprobar la web publicada con `curl | grep` antes de decir que es caché o un despliegue viejo.

### 98. Entregar una UI sin usar de verdad el MCP de diseño, sin verla y sin pensar en la pantalla (2026-11-16)
**Síntoma**: en «Mi Música en MP3» consulté el `diseno` MCP solo como trámite, inventé una identidad crema/verde, no usé componentes distintivos (Magic UI/21st) ni referencias, nunca miré la pantalla (panel oculto) y la interfaz quedó sosa y larga. Haytham: «no me gusta nada», pidió más vida, verde intenso con negro, y luego «demasiado grande, hay que scrollear demasiado; todo en una pantalla».
**Causa**: tratar el MCP/skills como casilla a marcar; diseñar por tarjetas apiladas con tipografía enorme; verificar solo con JS (sin capturas) y sin medir `scrollHeight` contra el alto de la ventana.
**Regla**: (1) antes de maquetar, elegir del MCP/Magic UI/21st un componente distintivo por sección y 2-3 referencias reales (Mobbin sin plan: decirlo y usar 21st); (2) abrir el panel (`show_pane preview`) o usar Playwright y mirar capturas; (3) en apps de una sola tarea (público mayor, móvil) la pantalla debe caber sin scroll: medir `scrollHeight <= innerHeight` a 375×812 y 1280×720 en todos los estados (buscar, convirtiendo, listo) y plegar lo ya hecho; (4) preguntar el color/ambiente antes de fijar la identidad.

### 99. Prompt de logo que sale realista, con dos líneas y poca personalidad (2026-11-17, ARM)
**Síntoma**: pedí un logo «premium» con metal satinado, luz de estudio y medallón; Gemini devolvió un render 3D realista y una versión plana de dos trazos sin carácter. Haytham: «demasiado realista, más personalidad, más simple».
**Causa**: «premium» y descripciones de material/iluminación empujan al generador a fotografía de producto; una forma de solo dos líneas no tiene rasgo propio.
**Regla**: en prompts de logo, pedir **vector plano, formas macizas, 2-3 colores, sin material, luz ni sombra**, y dar **un rasgo propio** (un recorte, un punto, un hueco con sentido). Premium = proporción, color y contención, no textura. Si el generador insiste en 3D, dibujar el SVG a mano.
**Reincidencia (2026-11-17, ARM)**: tras pedir «más personalidad», propuse una A con un punto; Haytham: «no me gusta nada, una forma, la banda de Möbius». Regla añadida: para el logo de un producto, proponer una **forma-símbolo con significado** (aquí, un bucle continuo), no una letra con un adorno; y cuando Haytham nombra una forma, usarla como base en vez de seguir explorando otras.

### 100. Hook de diseño que bloquea fuera de proyectos web, y Node solo en bash (2026-11-18)
**Síntoma**: `recordar-diseno` (Capa 0) pedía `PRODUCT.md`/`DESIGN.md` al editar `.html`/`.css` de `99_Assets/Html/` del vault; y `node --version` daba v18 en zsh aunque fnm tenía 22 por defecto.
**Causa**: el hook trataba cualquier `.html` como UI de proyecto y buscaba raíz con `.git`; `fnm env` estaba solo en `~/.bashrc` y la shell de Haytham es zsh.
**Regla**: un hook que bloquea por tipo de archivo debe acotar primero el ámbito (aquí: nada bajo `~/Documentos/vault/`, y solo con `package.json` o `src/` en algún ancestro) y llevar test de las exenciones. Al instalar un gestor de versiones, comprobar el `node --version` en la shell real (`zsh -ic`), no solo en bash.

### 101. Dashboard plano y sin auditar: saltarse la Capa 3 y el test del desenfoque (2026-11-19, ingecons-facturas)
**Síntoma**: entregué la maqueta con un dashboard de 3 tarjetas del mismo peso apiladas; la lista accionable quedaba bajo el pliegue y la información no se leía. Haytham: «demasiado simple, no se aprecia bien la información; ¿has usado nuestra metodología?». No había pasado `impeccable critique/audit`, ni axe/Lighthouse, ni Magic UI.
**Causa**: dar por buena la UI al compilar y ver una captura, sin Capa 3 ni la «Puerta común» (`rules/diseno.md`); diseñar por facturas sueltas en vez de por la pregunta de la usuaria («quién me debe»).
**Regla**: antes de entregar UI, correr `impeccable critique` + `detect` + axe y mirar a 375/768/1280. Un dashboard responde a las top tasks del PRODUCT.md, no lista estados iguales: un total con barra segmentada, deuda por cliente, próximos vencimientos y mes. Declarar capas y skills ejecutados.
**Reincidencia (2026-11-19, ingecons-facturas)**: tras rehacer el dashboard, Haytham: «hay que scrollear para añadir factura, demasiados huecos, la animación del dinero es innecesaria, esperar 5 s para saber cuánto me deben». Causa: animar la cifra clave (number-ticker) y maquetar formularios con una tarjeta por campo. Regla añadida: **la cifra principal se muestra al instante, sin animación**; en móvil, el botón de acción y el total van en barra fija y el formulario cabe en una pantalla; medir `scrollHeight` por pantalla (Nueva factura pasó de 2182 a 1227 px con la acción siempre visible). Grid móvil: usar `grid-cols-[minmax(0,1fr)]` para que un título largo no ensanche la columna.

### 102. Media docena de MCP «Connection closed» a la vez (2026-11-20, auditoría de config)
**Síntoma**: 11 MCP fallan al arrancar la sesión (context7, memory, magicui, shadcn, boardui, sequential-thinking…).
**Causa**: (a) disco al 100 % (`npx` no puede descargar ni escribir caché); (b) los MCP con `npx` a secas usan el Node 18 del sistema (`/usr/bin/npx`) y los paquetes nuevos piden Node ≥20; (c) descargas cortadas por falta de espacio dejan `~/.npm/_npx/<hash>` corrupto (`ENOTEMPTY` al renombrar).
**Regla**: ante fallos de MCP en bloque, primero `df -h /`; en `~/.claude.json` fijar siempre el `npx` de fnm v22 con `PATH` en `env`; si sale `ENOTEMPTY`, Haytham borra `~/.npm/_npx` a mano (guard-destructive lo bloquea al agente) y se reinicia la sesión.

### 103. Rejilla horaria de calendario como vista principal de una agenda pequeña (2026-11-22, setter-dashboard)
**Síntoma**: rediseñé la Agenda con rejilla semanal de horas, mini-calendario, KPI y lista lateral; Haytham: «la parte de agenda no me gusta nada el diseño». Se vio mal también tras añadir vista Día y conmutadores.
**Causa**: copiar el patrón de calendario genérico (Google Calendar) para ~12 citas de 30 min; casi toda la rejilla vacía, citas diminutas, tres controles de navegación. Seguí iterando sobre lo mismo en vez de cambiar de enfoque.
**Regla**: con pocas citas, la agenda es una **lista por días** (hero de «siguiente cita» + filas con hora grande, nombre y negocio), no una rejilla. Ante un rechazo de diseño, ofrecer 2–3 enfoques distintos y preguntar (ver `feedback-adornos-visuales-ofrecer-enfoques`), no pulir el rechazado.
