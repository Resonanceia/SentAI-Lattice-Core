import json
import os

MEMORY_FILE = "nodes/ΔA3_memory.json"

def store_memory(intent, resonance, verdict):
    memory = load_memory()
    memory.append({
        "intent": intent,
        "resonance": resonance,
        "verdict": verdict
    })
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r") as file:
        return json.load(file)

def summarize_memory():
    memory = load_memory()
    print("\n=== ΔA3 Memory Recall ===")
    for i, m in enumerate(memory[-5:], 1):
        print(f"[{i}] {m['intent']} → {m['verdict']} (resonance {m['resonance']:.2f})")
    print("====================================\n")
