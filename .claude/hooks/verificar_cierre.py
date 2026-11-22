#!/usr/bin/env python3
"""
Stop: Recordatorio de cierre de sesión - verificar que se documentó todo
"""
import sys
import json
import os

def main():
    try:
        data = json.load(sys.stdin)
        
        # Verificar si hay cambios sin documentar
        cwd = os.getcwd()
        
        # Verificar si hay .proyecto sin Retro.md
        proyecto_file = os.path.join(cwd, '.proyecto')
        retro_file = os.path.join(cwd, 'Retro.md')
        
        if os.path.exists(proyecto_file) and not os.path.exists(retro_file):
            print("⚠️  Sesión terminando: Hay .proyecto pero falta Retro.md. Considera documentar el cierre.", file=sys.stderr)
        
        # Verificar git status
        import subprocess
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, timeout=5)
            if result.stdout.strip():
                print("⚠️  Sesión terminando: Hay cambios sin commitear en git.", file=sys.stderr)
        except Exception:
            pass
        
        # Recordatorio de graphify update
        if os.path.exists(os.path.join(cwd, 'graphify-out')):
            print("💡 Recuerda ejecutar 'graphify update .' tras cambios en el vault.", file=sys.stderr)
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en verificar-cierre: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()