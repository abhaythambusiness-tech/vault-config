---
date: '2026-10-22'
type: sesion
proyecto: '[[01_Projects/Laya Leads]]'
tags:
- scraping
- leads
- neozeler
origen: mixto
---


# Sesión — 2026-10-22: Laya Leads, clasificación y ciclo automático

> [!resumen] En cristiano
> Hicimos que el scraper gaste menos memoria, que ponga nota a cada empresa (pyme, facturación aproximada, necesidad de web, capacidad de pago, prioridad A/B/C/D y qué venderle) y que **busque solo prospectos nuevos cada 2 horas** en el servidor. Se probó una segunda pasada con `curl_cffi` para las webs bloqueadas: rescató poco (7 %).

## Contexto

Continuación de [[01_Projects/Laya Leads]] (primera tanda del mismo día: 866 webs leídas, Laya NO PASA, CSV por reglas). Haytham pidió cuánta RAM gasta, si se podía optimizar, propuestas para clasificar mejor y venderles webs, una alternativa más barata que Scrapling y que siguiera buscando en segundo plano.

## Qué se hizo

- Medida de RAM y optimización: descarga en trozos con tope de 800 KB; pico de 34 MB por proceso (145 MB con 4 hilos). Mi primera estimación (150-300 MB) era alta.
- Nuevo `clasificacion.py` con reglas y 5 pruebas; señales nuevas en `extraccion.py` (tienda, reservas, anuncios, WhatsApp, formulario, redes, precios, sedes). Se releyeron las ~850 webs para añadirlas.
- Segunda pasada `rescatar` con `curl_cffi` 0.16.3: 10 de 144 recuperadas.
- Exportación con tres segmentos (`a_llamar_ya`, `correo_frio`, `descartar`) y umbrales calibrados con la distribución real: A ≥ 35, B ≥ 25 (58 A / 161 B / 639 C / 18 D).
- Comando `ciclo` y timer de systemd de usuario cada 2 h: zona nueva (33 municipios de Málaga), rastreo de pendientes, rescate y exportación. Primera zona, Marbella: 252 empresas nuevas.
- Ficha del vault, README del proyecto y `librerias.md` actualizados.

## Decisiones tomadas

- **Scrapling descartado** para este proyecto (navegador pesado); `curl_cffi` como único apoyo y con User-Agent identificable, respetando `robots.txt`.
- Clasificación **por reglas, no por Laya** (regla del vault: Laya no pasó la prueba).
- El ciclo escribe `leads_actual.csv`; el CSV de la primera tanda no se sobrescribe.
- Estados nuevos en texto libre (`sin_acceso_2`) en vez de migrar el esquema.

## Aprendizajes (para futuras sesiones)

- Con rastreos antiguos sin señales de conversión, casi todo caía en C: releer **antes** de calibrar umbrales.
- La relectura de 854 webs tardó ~19 min con 4 hilos (~50 webs/min), no los ~80 que calculé a ojo en los primeros minutos.
- El rescate con la huella TLS de Chrome no arregla casi nada: los fallos son webs caídas, JavaScript o bloqueos reales.
- `python -I` ignora `PYTHONPATH`; `zorin-ssh` no deja `sqlite3` ni pipes en `read-command` (detalle en `librerias.md`).
- Detalles técnicos y cifras medidas en `~/.claude/rules/librerias.md`, sección «Laya Leads».

## Próximos pasos

- Ver cuántas empresas trae cada zona y revisar que Marbella y las siguientes sean de Málaga.
- Revisar a mano ~30 webs de tier A para validar la clasificación.
- Sustituir los supuestos de facturación por datos de las primeras llamadas.
- Decidir si se amplía a otras provincias.

## Relacionado

- [[00_Meta/Registro de Sesiones|Registro de Sesiones]]
- [[01_Projects/Laya Leads]]

