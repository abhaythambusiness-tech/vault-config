---
date: '2026-10-08'
negocio: Factory Training
repo: ~/Proyectos/reto-30
status: activo
tags:
- reto-30
- fitness
- habitos
- gamificacion
- factory-training
- moc
type: proyecto
origen: mixto
---

# RETO 30 — Master Hub & MOC

> **"30 días. 30 retos. 3 niveles. 1 objetivo: no abandonar."**

Centro de control y documentación estratégica del proyecto **RETO 30**, diseñado para socios de **Factory Training**.

---

## 📌 Resumen Ejecutivo
- **Concepto**: Reto online gamificado de 30 días para fidelizar, crear hábitos y fomentar la constancia en el entrenamiento mediante una experiencia web estilo Duolingo.
- **Cliente / Partner Piloto**: Factory Training.
- **Repositorio de Código (fuera del vault)**: `~/Proyectos/reto-30`: la demo (Next.js, Tailwind, shadcn/ui) **se eliminó el 2026-10-15**; el repositorio de la app real se crea en la tarea T-01 del Plan.
- **Documentación Original en Assets**:
  - [[99_Assets/reto-30/RETO 30.pdf|RETO 30 (Resumen)]]
  - [[99_Assets/reto-30/RETO 30 Detallado.pdf|RETO 30 (Detallado)]]
- **Sesión Previa**: [[00_Meta/Sesiones/2026-10-06 - MCP de shadcn y demo RETO 30|Sesión 2026-10-06 — Demo web]]

---

## 🗺️ Mapa de Notas del Proyecto

0. [[01_Projects/Reto-30/Idea Original - Factory Training 30 dias|Idea Original (2026-10-02)]]
   - Ficha inicial de ideación, revenue split (15 % gimnasio), enfoque para no deportistas y [conversación original de Claude](https://claude.ai/share/d43827c3-cc5a-4b29-8bc3-473a6a0eee67).
1. [[01_Projects/Reto-30/01 - Propuesta y Modelo de Negocio|01 — Propuesta y Modelo de Negocio]]
   - Qué es, público objetivo, propuesta de valor, reparto económico (15-20 €, 15 % Factory Training) y roles.
2. [[01_Projects/Reto-30/02 - Mecanica del Reto y Gamificacion|02 — Mecánica del Reto y Gamificación]]
   - Sistema de niveles (Fácil, Medio, Avanzado), categorías diarias (ejercicio, movilidad, hábitos, recuperación, alimentación), retos especiales semanales y recompensas.
3. [[01_Projects/Reto-30/03 - Contenidos y Produccion Audiovisual|03 — Contenidos y Producción Audiovisual]]
   - Formato pedagógico de microvídeos (el porqué del hábito + técnica del ejercicio), guionización y checklist de producción.
4. [[01_Projects/Reto-30/04 - Roadmap y Validacion MVP|04 — Roadmap y Validación MVP]]
   - Estrategia de lanzamiento Fase 1 (cohorte de 20-30 socios), preguntas abiertas de validación y fases de escalado.
5. [[01_Projects/Reto-30/05 - Identidad Visual y Branding|05 — Identidad Visual y Branding]]
   - Manual de marca, dirección estética atlética premium, paleta de color (matte black, dark grey, electric lime green), concepto de logotipo (escudo + streak + rayo).
6. [[01_Projects/Reto-30/06 - Automatizacion de Inscripciones (n8n)|06 — Automatización de Inscripciones (n8n)]]
   - Flujo automatizado de checkout Stripe, webhook n8n, onboarding y acceso a la plataforma. **Obsoleta para la app real**: el pago es en efectivo en Factory Training y la app no gestiona pagos.
7. [[01_Projects/Reto-30/Reto 30 - App real|07 — App real]]
   - Ficha y 6 documentos de diseño aprobados (PRD, TRD, UI/UX, AppFlow, Backend Schema y Plan) en `Software/`. Aún sin código.

---

## 🔗 Relaciones
- Proyecto de Haytham y Pedro, con Factory Training como cliente piloto.
- Código de la app: `~/Proyectos/reto-30` (por crear en la tarea T-01 del Plan)

---

## 🎯 Estado Actual y Próximos Pasos
- [ ] Especificación de concepto y propuesta comercial.
- [ ] Wireframes y demo visual en frontend local (demo eliminada el 2026-10-15; lo útil está en `99_Assets/reto-30/demo-rescatada/`).
- [ ] Documentación de la app real: 6 documentos aprobados el 2026-10-14 ([[01_Projects/Reto-30/Reto 30 - App real|ficha]]), con la ampliación del 2026-10-17 ([[Cambios de diseno - Ranking, comodines, sorteo y Duo]]): ranking, comodines, reto extra, cronómetro, correo diario y plan Dúo. Fecha de inicio sin fijar.
- [ ] Seis decisiones previas a construir (Supabase, hosting, correo, logo, textos legales y precio), en el §1.1 del Plan.
- [ ] Validación comercial con gerencia de Factory Training (recompensas y canal de difusión).
- [ ] Grabación y edición de microvídeos de la Fase 1 solo para algunos ejercicios clave (el resto con dataset/API, ver [[Fuentes de Ejercicios y Multimedia Fitness]]).
- [ ] Lanzamiento de preventa/captación de la primera cohorte (20-30 participantes a 20 € por plaza).

