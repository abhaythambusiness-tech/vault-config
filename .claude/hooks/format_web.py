#!/usr/bin/env python3
"""
PostToolUse (Edit|Write): Prettier sobre web
"""
import sys
import json
import subprocess
import os

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        file_path = data.get('tool_input', {}).get('file_path', '')
        
        # Solo formatear archivos web
        web_extensions = ['.ts', '.tsx', '.js', '.jsx', '.json', '.css', '.scss', '.html', '.vue', '.svelte', '.astro']
        if not any(file_path.endswith(ext) for ext in web_extensions):
            sys.exit(0)
        
        # Ejecutar prettier si existe
        try:
            result = subprocess.run(
                ['npx', 'prettier', '--write', file_path],
                capture_output=True,
                text=True,
                timeout=10,
                cwd=os.getcwd()
            )
            if result.returncode != 0:
                print(f"Prettier warning: {result.stderr}", file=sys.stderr)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass  # Silencioso si no hay prettier
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en format-web: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()