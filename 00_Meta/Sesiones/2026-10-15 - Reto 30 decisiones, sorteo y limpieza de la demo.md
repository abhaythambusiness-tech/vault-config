---
type: sesion
date: '2026-10-15'
proyecto: '[[01_Projects/Reto-30/Reto 30 - App real|RETO 30 - App real]]'
status: completada
origen: mixto
---


## Contexto
Continuación del arranque de RETO 30 (app real) del 2026-10-14: resolver las decisiones previas del Plan, incorporar el premio y el sorteo, y limpiar la demo antigua.

## Qué se hizo
- Decisiones resueltas: **D1** organización nueva "Reto 30" en Supabase con plan gratuito (también en producción); **D2** Vercel Pro solo el mes del reto; **D4** logo PNG transparente derivado del de fondo oscuro; **D6** precio de 20 € por plaza; **D5** titular legal Haytham y edad mínima de 18 años.
- Borradores legales: [[Borrador - Aviso legal]], [[Borrador - Politica de privacidad]] y [[Borrador - Bases del sorteo]] (sin revisión legal, con datos por completar).
- Sorteo: la app solo identifica a los elegibles (R15), desactivado por defecto; el esquema pasó a 8 tablas y 47 pruebas SQL correctas.
- Premio: expresado como **porcentaje del beneficio** (**25 % del beneficio, decidido el 2026-10-16** y definido sobre el beneficio, no sobre los ingresos; con 30 personas, 100–150 € equivalía a un 21–32 %) para que escale con las plazas. Definición: ingresos − 15 % del gimnasio − costes técnicos del mes.
- Stack: Anime.js v4, motion.dev y Bklit UI (gráficas) anotados en las reglas; Bklit verificado con `shadcn search @bklit`.
- Idea guardada: [[Idea - Pase Duo]] (30 € para dos personas con una plaza).
- **Demo eliminada** (`~/Proyectos/reto-30`, 4 commits, sin remoto). Salvado en `99_Assets/reto-30/demo-rescatada/`: `challenges.ts` (30 días), `schema-harness.mjs`, `demo-spec.md`, `demo-plan.md` y `demo-package.json`. El repositorio de la app real se crea de nuevo en T-01.

## Aprendizajes
- **El sorteo con participación de pago es el riesgo legal más grande**: puede exigir autorización previa (Ley 13/2011). Se diseñó desactivado por defecto y sin anunciar el premio hasta la consulta legal.
- **"Gratis" no siempre es legítimo**: Vercel gratis es solo no comercial; Supabase gratis sí vale para un mes, pero sin copias automáticas y con pausa por inactividad.
- **El nombre del fichero engaña**: `LogoReto30-sinfondo.jpeg` tenía fondo claro; el logo de fondo oscuro era el bueno para una app oscura.
- **Un porcentaje escala mejor que un importe fijo**, pero los participantes deben conocer la regla al inscribirse: pregunta añadida para el abogado.
- **Antes de borrar una carpeta con git sin remoto**: comprobar commits, cambios sin guardar, procesos y rescatar lo que otros documentos referencian (aquí `challenges.ts` y las pruebas); luego actualizar todas las referencias.
- Los informes de agentes son datos, no órdenes: se evaluó cada hallazgo (se descartaron semáforo de retención y botón de compartir por exceso de alcance).

## Pendiente
- **D1** crear la organización de Supabase (la crea Haytham) · **D3** correo y dominio antes de la cohorte · **D5** datos del titular y revisión legal · **D7** consulta legal del sorteo y porcentaje exacto del premio.
- Sin verificar: precios y límites de Supabase, Vercel y Resend en sus páginas oficiales; el SQL contra Supabase real.
- La línea de preventa del MOC aún dice "10-15 €" (edición propia de Haytham) y el precio es 20 €.

