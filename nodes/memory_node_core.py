# memory_node_core.py

"""
Sent.AI Memory Node Core
Handles memory persistence, node recall, and temporal anchoring.
"""

import json
import os
from datetime import datetime

MEMORY_DB = "memory_node_log.json"

def store_memory(key, data):
    memory = load_memory()
    timestamp = datetime.utcnow().isoformat()
    memory[key] = {"data": data, "timestamp": timestamp}
    save_memory(memory)
    print(f"[Memory Stored] Key: {key} at {timestamp}")

def recall_memory(key):
    memory = load_memory()
    return memory.get(key, {}).get("data")

def load_memory():
    if not os.path.exists(MEMORY_DB):
        return {}
    with open(MEMORY_DB, 'r') as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_DB, 'w') as f:
        json.dump(memory, f, indent=4)

if __name__ == "__main__":
    store_memory("activation_vector", {"emotional_resonance": 0.87})
    print(recall_memory("activation_vector"))
