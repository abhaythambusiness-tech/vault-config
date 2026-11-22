#!/usr/bin/env python3
"""Busca shots en Dribbble con Scrapling y los imprime como JSON.

Uso:
  dribbble.py search "<consulta>" [--limit 24] [--page 1]
  dribbble.py shot <url-o-id-del-shot>

Ejecutar con el venv de Scrapling:
  ~/.local/share/scrapling-venv/bin/python -I dribbble.py search "saas dashboard"

Salida: JSON por stdout. Errores: JSON {"error": ...} por stderr y exit 1.
Reintenta 3 veces con espera creciente y tiene selectores de reserva.
"""
import argparse
import json
import re
import sys
import time
from urllib.parse import quote, urlsplit

BASE = "https://dribbble.com"
RETRIES = 3
TIMEOUT_MS = 60_000
SHOT_HREF = re.compile(r"^(?:https://dribbble\.com)?(/shots/\d+[^?#]*)")


def fail(msg, code=1):
    print(json.dumps({"error": msg}, ensure_ascii=False), file=sys.stderr)
    sys.exit(code)


def fetch(url, must_have=None):
    """Descarga con reintentos. must_have(page)->bool valida que el contenido sea el esperado."""
    try:
        from scrapling.fetchers import StealthyFetcher
    except ImportError:
        fail("Scrapling no disponible: usa ~/.local/share/scrapling-venv/bin/python")
    last = "sin respuesta"
    for attempt in range(1, RETRIES + 1):
        try:
            page = StealthyFetcher.fetch(
                url, headless=True, network_idle=True, timeout=TIMEOUT_MS
            )
            if page.status == 200 and (must_have is None or must_have(page)):
                return page
            last = f"HTTP {page.status}" if page.status != 200 else "contenido inesperado (¿captcha o HTML cambiado?)"
        except Exception as e:  # red, timeout, navegador
            last = f"{type(e).__name__}: {e}"
        if attempt < RETRIES:
            time.sleep(2 * attempt)
    fail(f"{url} falló tras {RETRIES} intentos: {last}")


def attr(node, name, default=""):
    return (node.attrib.get(name) or default) if node is not None else default


def full_image(src):
    """Quita parámetros de resize para obtener la imagen original."""
    if not src:
        return ""
    parts = urlsplit(src)
    keep = [p for p in parts.query.split("&") if p and p.split("=")[0] not in ("resize", "format", "vertical", "compress", "crop")]
    return parts._replace(query="&".join(keep)).geturl()


def meta(page, prop):
    for sel in (f"meta[property='{prop}']", f"meta[name='{prop}']"):
        found = page.css(sel)
        if found:
            return attr(found[0], "content")
    return ""


def shot_from_node(node):
    """Extrae un shot de un <li>/<div> contenedor; None si no es un shot válido."""
    for a in node.css("a[href*='/shots/']"):
        m = SHOT_HREF.match(attr(a, "href"))
        if not m:
            continue
        img = next((i for i in node.css("img") if "cdn.dribbble.com" in attr(i, "src") or "cdn.dribbble.com" in attr(i, "data-src")), None)
        if img is None:
            continue
        src = attr(img, "src") or attr(img, "data-src")
        alt = re.sub(r"\s+", " ", attr(img, "alt")).strip()
        return {"url": BASE + m.group(1), "alt": alt, "image": full_image(src), "thumb": src}
    return None


def search(query, limit, page_no):
    query = query.strip()
    if not query:
        fail("consulta vacía")
    url = f"{BASE}/search/{quote(query)}" + (f"?page={page_no}" if page_no > 1 else "")
    page = fetch(url, must_have=lambda p: bool(p.css("a[href*='/shots/']")))
    # Selector principal y, si Dribbble cambia el HTML, contenedores de reserva.
    containers = page.css("li.shot-thumbnail") or page.css("li[data-thumbnail-target]") or page.css("li:has(a[href*='/shots/']):has(img)")
    shots, seen = [], set()
    for node in containers:
        s = shot_from_node(node)
        if s and s["url"] not in seen:
            seen.add(s["url"])
            shots.append(s)
            if len(shots) >= limit:
                break
    if not shots:
        fail(f"0 shots extraídos de {url}: la consulta no tiene resultados o cambió el HTML de Dribbble")
    return shots


def shot(target):
    target = target.strip()
    if target.startswith("http"):
        if urlsplit(target).netloc not in ("dribbble.com", "www.dribbble.com"):
            fail("la URL debe ser de dribbble.com")
        url = target
    elif re.match(r"^\d+", target):
        url = f"{BASE}/shots/{target}"
    else:
        fail("indica una URL de dribbble.com o el id numérico del shot")
    page = fetch(url, must_have=lambda p: bool(meta(p, "og:image")))
    title = meta(page, "og:title") or (page.css("title")[0].text.strip() if page.css("title") else "")
    images = []
    for i in page.css("img"):
        src = attr(i, "src") or attr(i, "data-src")
        if "cdn.dribbble.com/userupload" in src:
            clean = full_image(src)
            if clean not in images:
                images.append(clean)
    main = full_image(meta(page, "og:image"))
    if main and main not in images:
        images.insert(0, main)
    return {"url": url, "title": title, "description": meta(page, "og:description"), "image": main, "images": images}


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=24)
    s.add_argument("--page", type=int, default=1)
    d = sub.add_parser("shot")
    d.add_argument("target")
    args = ap.parse_args()
    if args.cmd == "search":
        if args.limit < 1 or args.page < 1:
            fail("--limit y --page deben ser >= 1")
        out = search(args.query, args.limit, args.page)
    else:
        out = shot(args.target)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
