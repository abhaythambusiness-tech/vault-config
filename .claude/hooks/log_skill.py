#!/usr/bin/env python3
"""
PostToolUse (Skill): Anota cada skill en ~/.claude/uso-skills/uso.jsonl
"""
import sys
import json
import os
from datetime import datetime

def main():
    try:
        data = json.load(sys.stdin)
        skill_name = data.get('tool_input', {}).get('skill', '')
        
        if not skill_name:
            sys.exit(0)
        
        log_dir = os.path.expanduser('~/.claude/uso-skills')
        os.makedirs(log_dir, exist_ok=True)
        
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'skill': skill_name,
            'session': os.environ.get('OPENCODE_SESSION_ID', 'unknown')
        }
        
        log_file = os.path.join(log_dir, 'uso.jsonl')
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        
        sys.exit(0)
    except Exception as e:
        print(f"Error en log-skill: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()