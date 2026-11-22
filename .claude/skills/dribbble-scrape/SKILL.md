---
name: dribbble-scrape
description: Usar cuando Haytham pida referencias de diseño de Dribbble (buscar shots por tema, sacar imágenes, títulos y tags de un shot). Dribbble no tiene MCP; esta skill lo raspa con Scrapling (StealthyFetcher) y devuelve JSON. Para inspiración visual antes de maquetar (ver identidad-y-dinamismo).
---

# dribbble-scrape

Dribbble sin MCP. Script sobre Scrapling, venv ya instalado.

## Uso

```bash
PY=~/.local/share/scrapling-venv/bin/python
S=~/.claude/skills/dribbble-scrape/scripts/dribbble.py

$PY -I $S search "saas dashboard" --limit 12      # lista de shots
$PY -I $S search "saas dashboard" --page 2
$PY -I $S shot https://dribbble.com/shots/<id>-slug   # detalle de uno
```

`search` devuelve `[{url, alt, image, thumb}]`. `alt` = título + tags del shot. `image` = URL original sin resize.
`shot` devuelve `{url, title, image, description, images[]}`.

Errores: JSON `{"error": ...}` por stderr y exit 1 (consulta vacía, URL no Dribbble, 0 resultados, 3 reintentos fallidos). En `shot`, `images[0]` es el shot; el resto suelen ser shots relacionados de la página.

## Flujo

1. Buscar con 2-3 consultas distintas (estilo + sector: "fintech dashboard dark", "landing saas bento").
2. Quedarse con 5-8 candidatos; descargar con `curl` solo los que Haytham elija (pedir permiso: es una descarga).
3. Verlos con `Read` (las imágenes se ven) y extraer: paleta, tipografía, composición, dinamismo.
4. Volcar a `DESIGN-IDENTITY.md` del proyecto como referencias; no copiar el shot tal cual (derechos del autor).

## Límites

- Raspado de HTML público: puede romperse si Dribbble cambia `li.shot-thumbnail`. Si `search` devuelve `[]`, revisar selectores.
- Sin login: no ve shots privados ni contenido tras registro.
- Ritmo bajo: una búsqueda a la vez, sin bucles masivos (respetar el servicio).
- Imágenes son propiedad de sus autores: solo referencia interna, nunca reutilizar en producción.
- Si hace falta más control (cookies, paginación profunda), ver la skill `scrapling-official`.
