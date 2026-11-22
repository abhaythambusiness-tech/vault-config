---
type: sesion
date: '2026-10-14'
proyecto: '[[01_Projects/Reto-30/Reto 30 - App real|RETO 30 - App real]]'
status: completada
origen: mixto
---


## Contexto
Primer uso real de la skill `/nuevo-proyecto`: Haytham pidió hacer RETO 30 diseñando toda la estructura y la interfaz, con solo tres ejercicios por nivel (los elegirá él después). Ya existía una demo en `~/Proyectos/reto-30` y notas 01–06 en el vault.

## Qué se hizo
- Carpeta `01_Projects/Reto-30/Software/` con los 6 documentos (PRD, TRD, UI/UX, AppFlow, Backend Schema y Plan), **todos aprobados**.
- Notas antiguas de Reto 30 corregidas: fuera NeoZeler (es un proyecto de Haytham y Pedro).
- Esquema SQL (7 tablas, RLS, funciones) validado en Postgres local con 31 comprobaciones.
- Ficha [[01_Projects/Reto-30/Reto 30 - App real]], MOC actualizado, README de la app y enlaces en `CLAUDE.md` y `GEMINI.md`.
- Recurso nuevo: [[Fuentes de Ejercicios y Multimedia Fitness]].

## Decisiones de negocio y de diseño
- Pago en efectivo en Factory Training; la app no gestiona pagos y un admin activa cada plaza.
- El día siguiente se abre a las 07:00 (hora de Madrid); saltar un día resetea la racha, no el progreso.
- Dirección visual: la del logo real (negro y lima), no la de la demo (papel y naranja); sin squircle.
- Consentimiento en la app para que gerencia vea nombres completos.
- Se graban solo algunos ejercicios clave; el resto con datasets y APIs.

## Aprendizajes
- **Leer lo que ya existe antes del PRD** destapó dos contradicciones (marca y reparto con NeoZeler) que habrían salido caras en el diseño.
- **El cliente simulado funcionó**: dos agentes encontraron 20 atascos reales (pantalla de admin que faltaba, reglas R1/R2 que chocaban, vocabulario técnico, cobro invisible). Se aplicó lo útil y se descartó lo que excedía v1.
- **Cada decisión del usuario cascadea** a documentos ya aprobados: conviene listar el cambio y pedir permiso (se hizo).
- **PGlite** permite validar SQL con RLS sin Docker; un fallo inicial era del script de prueba (rol que no se restablecía), no del esquema.
- **Nunca nombrar personas inventadas** (la dueña del gimnasio): usar el cargo. Registrado en memoria y en la skill.
- El gate de primera escritura rechaza siempre el primer intento: declarar los hechos antes y reenviar.

## Pendiente
- Seis decisiones previas a construir (D1–D6 del Plan): Supabase, hosting, correo, logo transparente, textos legales y precio.
- Starter Kits sigue siendo solo inventario; ningún kit extraído.
- Sin verificar: costes y condiciones de Supabase y del hosting; SQL contra Supabase real; context7 caído durante toda la sesión.

