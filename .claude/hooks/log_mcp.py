#!/usr/bin/env python3
"""
PostToolUse (mcp__.*): Anota cada MCP en uso-mcp.jsonl
"""
import sys
import json
import os
import re
from datetime import datetime

def main():
    try:
        data = json.load(sys.stdin)
        tool = data.get('tool', '')
        
        # Solo loggear herramientas MCP
        if not tool.startswith('mcp__'):
            sys.exit(0)
        
        # Extraer nombre del MCP
        match = re.match(r'mcp__([^_]+)__', tool)
        mcp_name = match.group(1) if match else tool
        
        log_dir = os.path.expanduser('~/.claude')
        os.makedirs(log_dir, exist_ok=True)
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'mcp': mcp_name,
            'tool': tool,
            'session': os.environ.get('OPENCODE_SESSION_ID', 'unknown')
        }
        
        log_file = os.path.join(log_dir, 'uso-mcp.jsonl')
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en log-mcp: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()