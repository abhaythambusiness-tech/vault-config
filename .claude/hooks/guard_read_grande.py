#!/usr/bin/env python3
"""
PreToolUse (Read): Bloquea leer >800 líneas sin offset/limit
"""
import sys
import json

def main():
    try:
        data = json.load(sys.stdin)
        tool_input = data.get('tool_input', {})
        limit = tool_input.get('limit')
        offset = tool_input.get('offset')
        
        # Si no hay limit u offset, y es un archivo grande potencial
        if limit is None and offset is None:
            file_path = tool_input.get('file_path', '')
            # Extensiones que suelen ser grandes
            large_extensions = ['.log', '.json', '.csv', '.md', '.txt', '.py', '.js', '.ts']
            if any(file_path.endswith(ext) for ext in large_extensions):
                print("Bloqueado por guard-read-grande: Lectura de archivo grande sin offset/limit. Usa offset y limit para archivos >800 líneas.", file=sys.stderr)
                sys.exit(2)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en guard-read-grande: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()