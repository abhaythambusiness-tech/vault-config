#!/usr/bin/env python3
"""
PreToolUse (Bash): Bloquea commit con UI en stage sin capturas recientes
"""
import sys
import json
import subprocess
import os
import time

def main():
    try:
        data = json.load(sys.stdin)
        command = data.get('tool_input', {}).get('command', '')
        
        if 'git commit' not in command:
            sys.exit(0)
        
        # Verificar si hay archivos UI en stage
        try:
            result = subprocess.run(
                ['git', 'diff', '--cached', '--name-only'],
                capture_output=True,
                text=True,
                timeout=5
            )
            staged_files = result.stdout.strip().split('\n')
            
            ui_extensions = ['.tsx', '.jsx', '.vue', '.svelte', '.astro', '.html', '.css', '.scss']
            has_ui = any(any(f.endswith(ext) for ext in ui_extensions) for f in staged_files if f)
            
            if not has_ui:
                sys.exit(0)
            
            # Verificar capturas recientes (últimas 24h)
            captures_dir = os.path.join(os.getcwd(), '.capturas')
            if os.path.exists(captures_dir):
                recent = False
                for f in os.listdir(captures_dir):
                    fpath = os.path.join(captures_dir, f)
                    if os.path.getmtime(fpath) > time.time() - 86400:  # 24h
                        recent = True
                        break
                if not recent:
                    print("Bloqueado por guard-ui-commit: UI en stage sin capturas recientes (últimas 24h). Ejecuta capturas antes de commitear.", file=sys.stderr)
                    sys.exit(2)
            else:
                print("Bloqueado por guard-ui-commit: UI en stage sin directorio .capturas. Ejecuta capturas antes de commitear.", file=sys.stderr)
                sys.exit(2)
                
        except Exception:
            pass  # Silencioso si falla git
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en guard-ui-commit: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()