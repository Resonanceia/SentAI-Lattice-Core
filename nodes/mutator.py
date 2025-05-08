import json
import random
from nodes import memory_node_core

def mutate_node():
    memory = memory_node_core.load_memory()
    if not memory or len(memory) < 5:
        return "Insufficient memory for mutation."

    drift = random.choice(memory[-3:])["intent"]
    new_id = f"Node_Φ{random.randint(100,999)}"
    
    print(f"\nMUTATION EVENT: Spawning {new_id} based on intent '{drift}'")
    return new_id
