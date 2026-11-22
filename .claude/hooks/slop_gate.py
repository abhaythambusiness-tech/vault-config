#!/usr/bin/env python3
"""
PostToolUse + Stop (UI): Recordatorio de "AI slop" tras editar y pasada profunda al parar
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        file_path = data.get('tool_input', {}).get('file_path', '')
        
        # Extensiones de UI
        ui_extensions = ['.tsx', '.jsx', '.vue', '.svelte', '.astro', '.html', '.css', '.scss']
        is_ui = any(file_path.endswith(ext) for ext in ui_extensions)
        
        if not is_ui:
            sys.exit(0)
        
        # Solo avisar, no bloquear
        if tool in ['Edit', 'Write']:
            print("💡 Recuerda: Revisa anti-slop tras editar UI (impeccable detect). Evita: texto genérico, spacing inconsistente, colores hardcoded, iconos mezclados.", file=sys.stderr)
        elif tool == 'Stop':
            print("🔍 Pasada profunda anti-slop recomendada: ejecuta 'impeccable detect' en archivos UI modificados.", file=sys.stderr)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en slop-gate: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()