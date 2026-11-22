#!/usr/bin/env python3
"""Exporta DESIGN.md (formato design.md: tokens en frontmatter + prosa) desde DESIGN-IDENTITY.md.

Uso:
  python3 -I export_design_md.py [DESIGN-IDENTITY.md] [DESIGN.md]   # por defecto, en el directorio actual
  python3 -I export_design_md.py --self-test

DESIGN-IDENTITY.md sigue siendo la fuente de verdad: DESIGN.md se regenera, no se edita a mano.
Sin dependencias externas. Sale con código 1 si falta la identidad o está sin rellenar.
"""
import re
import sys
import unicodedata
from pathlib import Path

HEX = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
BLANK = re.compile(r"_{3,}")  # "______" de la plantilla sin rellenar


def sections(text: str) -> dict[int, str]:
    """Devuelve {n: cuerpo} para cada '## n. Título'."""
    out: dict[int, str] = {}
    parts = re.split(r"^##\s+(\d+)\.\s.*$", text, flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        out[int(parts[i])] = parts[i + 1].strip()
    return out


def table_rows(body: str) -> list[list[str]]:
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("|") or re.match(r"^\|[\s\-:|]+\|$", line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows[1:] if rows else []  # sin cabecera


def slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "color"


def yq(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def first_line(body: str) -> str:
    for line in body.splitlines():
        if line.strip():
            return line.strip()
    return ""


def clean_font(name: str) -> str:
    """Nombre de fuente sin negritas, comillas de código ni comentarios entre paréntesis."""
    return re.sub(r"\s+", " ", re.sub(r"\([^)]*\)", "", name).replace("*", "").replace("`", "")).strip()


def parse(text: str) -> dict:
    sec = sections(text)
    missing = [n for n in (1, 3, 5) if n not in sec]
    if missing:
        raise ValueError(f"faltan las secciones {missing} en DESIGN-IDENTITY.md")
    if BLANK.search(sec[1]) or not HEX.search(sec[3]):
        raise ValueError("identidad sin rellenar: §1 con '______' o §3 sin colores #hex")

    colors: dict[str, str] = {}
    palette = []
    for cells in table_rows(sec[3]):
        if len(cells) < 3 or not cells[0]:
            continue
        name, scale, role = cells[0], cells[1], cells[2]
        hexes = HEX.findall(scale) or HEX.findall(name)
        if not hexes:
            continue
        key = slug(re.sub(HEX, "", name))
        colors[key] = hexes[len(hexes) // 2] if len(hexes) > 1 else hexes[0]
        palette.append((name, hexes, role))

    ty = re.search(r"Tipograf[ií]a:\s*(.+?)\.\s*\*\*Motivo:\*\*\s*(.+)", sec[3])
    fonts = ("", "")
    if ty:
        spec = ty.group(1)
        # "A + B" = dos fuentes; sin "+" = una sola (lo que sigue al primer ". " son notas, p. ej. features OpenType)
        names = spec.split("+") if "+" in spec else [re.split(r"\.\s", spec)[0]]
        names = [clean_font(n) for n in names if clean_font(n)]
        if names:
            fonts = (names[0], names[1] if len(names) > 1 else names[0])
    motive = ty.group(2).strip() if ty else ""

    curve = re.search(r"cubic-bezier\([^)]*\)", sec[5])
    level = re.search(r"Nivel[^:]*:\s*(\d)", sec[5])
    return {
        "idea": sec[1], "producto": sec.get(2, ""), "origen": re.search(
            r"\*\*Origen de los colores[^*]*\*\*\s*(.+)", sec[3]) and re.search(
            r"\*\*Origen de los colores[^*]*\*\*\s*(.+)", sec[3]).group(1).strip() or "",
        "colors": colors, "palette": palette, "fonts": fonts, "motive": motive,
        "composicion": sec.get(4, ""), "dinamismo": sec[5],
        "curve": curve.group(0) if curve else "", "level": level.group(1) if level else "",
        "imagenes": sec.get(6, ""), "refs": sec.get(7, ""),
    }


def render(d: dict, name: str) -> str:
    fm = ["---", f"name: {yq(name)}", "colors:"]
    fm += [f"  {k}: {yq(v)}" for k, v in d["colors"].items()]
    if any(d["fonts"]):
        fm += ["typography:",
               f"  display: {{ fontFamily: {yq(d['fonts'][0])} }}",
               f"  body: {{ fontFamily: {yq(d['fonts'][1])} }}"]
    fm += ["motion:"]
    if d["curve"]:
        fm += [f"  easing: {yq(d['curve'])}"]
    if d["level"]:
        fm += [f"  level: {d['level']}"]
    fm += ["---", ""]

    body = [
        "<!-- Generado desde DESIGN-IDENTITY.md con export_design_md.py. No editar: editar la identidad y regenerar. -->",
        "",
        f"# {name}", "",
        "## Overview", d["idea"], "",
    ]
    if d["producto"] and not BLANK.search(d["producto"]):
        body += ["### El producto como diseño", d["producto"], ""]
    body += ["## Colors"]
    if d["origen"]:
        body += [f"Origen: {d['origen']}", ""]
    body += ["| Color | Escala | Papel |", "|---|---|---|"]
    body += [f"| {n} | {' '.join(h)} | {r} |" for n, h, r in d["palette"]]
    body += ["", "## Typography",
             (f"{d['fonts'][0]} (títulos y texto). {d['motive']}" if d["fonts"][0] == d["fonts"][1]
              else f"{d['fonts'][0]} (títulos) + {d['fonts'][1]} (texto). {d['motive']}").strip(), ""]
    if d["composicion"] and not BLANK.search(d["composicion"]):
        body += ["## Layout", d["composicion"], ""]
    body += ["## Motion", d["dinamismo"], ""]
    if d["imagenes"] and not BLANK.search(first_line(d["imagenes"])):
        body += ["## Imagery", d["imagenes"], ""]
    if d["refs"]:
        body += ["## Referencias y anti-referencias", d["refs"], ""]
    return "\n".join(fm + body).rstrip() + "\n"


def project_name(src: Path, text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, flags=re.M)
    return (m.group(1).strip() if m else src.resolve().parent.name)


def run(src: Path, dst: Path) -> None:
    text = src.read_text(encoding="utf-8")
    dst.write_text(render(parse(text), project_name(src, text)), encoding="utf-8")


SAMPLE = """# Demo
## 1. Idea visual central
Esta marca es cálida y lo demuestra con su horno a la vista.
## 3. Paleta y tipografía
**Origen de los colores (obligatorio):** logo muestreado.

| Color | Escala (8 tonos) | Papel |
|---|---|---|
| Ámbar | #FFF3E0 #FFB74D #E65100 | Acento |
| Tinta | #111111 | Texto |

Tipografía: Fraunces + Inter. **Motivo:** serif cálida para títulos.
## 5. Dinamismo
- Nivel (0 estático · 1 sutil · 2 dinámico · 3 protagonista): 2
- Curva propia del proyecto: `cubic-bezier(0.2, 0.8, 0.2, 1)`
"""


def self_test() -> None:
    out = render(parse(SAMPLE), "Demo")
    assert 'ambar: "#FFB74D"' in out, out
    assert 'tinta: "#111111"' in out and 'easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"' in out, out
    assert "fontFamily: \"Fraunces\"" in out and "level: 2" in out, out
    bold = SAMPLE.replace("Fraunces + Inter.", "**Geist** (todo) + **Geist Mono** (tiempos).")
    out = render(parse(bold), "Demo")
    assert 'fontFamily: "Geist"' in out and 'fontFamily: "Geist Mono"' in out, out
    assert "*" not in out.split("---")[1] and "(todo)" not in out, out
    una = SAMPLE.replace("Fraunces + Inter.", "Geist. Cifras con tabular-nums.")
    out = render(parse(una), "Demo")
    assert out.count('fontFamily: "Geist"') == 2 and "tabular" not in out.split("---")[1], out
    try:
        parse(SAMPLE.replace("cálida y lo demuestra con su horno a la vista.", "______ y ______"))
    except ValueError:
        print("self-test OK")
        return
    raise AssertionError("debía rechazar identidad sin rellenar")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--self-test"]:
        self_test()
        sys.exit(0)
    src = Path(args[0] if args else "DESIGN-IDENTITY.md")
    dst = Path(args[1] if len(args) > 1 else src.parent / "DESIGN.md")
    if not src.is_file():
        sys.exit(f"No existe {src}: sin identidad no se exporta DESIGN.md")
    try:
        run(src, dst)
    except ValueError as e:
        sys.exit(f"No se exporta: {e}")
    print(f"escrito {dst}")
