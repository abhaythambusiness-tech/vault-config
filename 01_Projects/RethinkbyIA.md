---
date: '2026-10-02'
negocio: RETHINKBY.IA
persona: Estefanía Teniente
repo: ~/Proyectos/rethinkbyia
status: completado
tags:
- consultoria
- inteligencia-artificial
- marca-personal
- nextjs
- tailwind
- multipage
type: proyecto
origen: mixto
---

# Proyecto RETHINKBY.IA — Estefanía Teniente

## Resumen
Sitio web multipágina de alta gama para **Estefanía Teniente**, consultora de estrategia de negocio e Inteligencia Artificial humanizada bajo la marca comercial **RETHINKBY.IA**.
Diseñado para posicionarla como el nexo estratégico entre negocio y tecnología, transmitir autoridad ejecutiva, rigor y calidez humana, y captar contactos de empresas y directivos.

- **Repositorio local**: `~/Proyectos/rethinkbyia/`
- **GitHub**: https://github.com/abhaythambusiness-tech/rethinkbyia (privado)
- **Stack**: Next.js 16 (App Router), React 19, TypeScript estricto, Tailwind CSS v4 con tokens `@theme`, lucide-react, motion, react-hook-form + zod.
- **Identidad**: Paleta rosa empolvado (`#D69A8F`), rosa claro (`#F2D9D3`), crema cálido (`#F7EFEA`), negro carbón (`#222222`) y degradado Rose Gold. Tipografías `Playfair Display`, `Montserrat` y `Allura`.
- **Assets integrados**: Logos oficiales (monograma RA, horizontal, vertical, negativo y favicon) y fotografías profesionales tratadas en marco de arco suave (jardín tropical en hero y terraza marina en sobre mí).

## Arquitectura de Rutas Entregadas
- `/`: Inicio con sticky header, hero, banda de 4 pilares, extracto de biografía, KPIs interactivos animados, 6 valores de esencia, catálogo anticipado de servicios, cita manuscrita, CTA final y footer corporativo oscuro con logo negativo.
- `/sobre-mi`: Trayectoria de +15 años, principios de adopción de IA, perfil de Ingeniería Informática y metodología.
- `/servicios`: Catálogo modular dirigido por datos (`data/services.ts`) con estado "Próximamente" y captura de email "Avísame al lanzar".
- `/servicios/[slug]`: Plantilla dinámica SSG con propuesta de valor, beneficios, metodología paso a paso, FAQ en acordeón y CTA.
- `/contacto`: Formulario con validación Zod en tiempo real, garantías de confidencialidad y canales de contacto directo.
- `/recursos`: Centro de pensamiento y blog preparado para escalabilidad.
- `/aviso-legal`, `/privacidad`, `/cookies`: Textos legales completos conforme a LSSI-CE, RGPD y LOPDGDD, con banner de consentimiento interactivo.

## Estado del Proyecto
- [x] Especificación `spec.md` con Spec Kit de GitHub.
- [x] Repositorio Git inicializado en `~/Proyectos/rethinkbyia/` con commit en rama `main`.
- [x] Generación y optimización de assets de marca (PNG transparentes, negativos, favicon y WebP/AVIF).
- [x] Build estático de producción completado con 17 rutas pre-renderizadas sin errores ni warnings.
- [x] README con guía técnica y documentación paso a paso para añadir nuevos servicios al catálogo.

