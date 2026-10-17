#!/usr/bin/env python3
"""
Canonical CLI Entrypoint for ASI Theoretical Corrigibility & Containment Studio
"""
import sys
import corrigibility_simulator as engine

def main():
    print("=" * 60)
    print("🚀 ASI Theoretical Corrigibility & Containment Studio")
    print("=" * 60)
    if hasattr(engine, '__main__'):
        pass
    print("Executing engine drill...")
    # Trigger standalone block
    with open("corrigibility_simulator.py", "r") as f:
        code = compile(f.read(), "corrigibility_simulator.py", "exec")
        exec(code, {"__name__": "__main__"})

if __name__ == "__main__":
    main()
