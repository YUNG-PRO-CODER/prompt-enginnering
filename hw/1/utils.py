import os
from datetime import datetime

def print_header(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

def print_section(title):
    print("\n" + "-" * 50)
    print(title)
    print("-" * 50)

def save_output(text):
    os.makedirs("results", exist_ok=True)
    with open("results/outputs.txt", "a", encoding="utf-8") as f:
        f.write(f"\n\n[{datetime.now()}]\n{text}\n")