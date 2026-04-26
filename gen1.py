# gen1.py
import sys

try:
    import ruijie_scanner as scanner
except ImportError as e:
    print(f"Error: Could not load scanner module - {e}")
    print("Make sure ruijie_scanner.so is in the same directory")
    sys.exit(1)

if __name__ == "__main__":
    scanner.run_scanner()
