import json
from nodes import memory_node_core

def assess_trend():
    memory = memory_node_core.load_memory()
    if len(memory) < 3:
        return "insufficient data"

    recent = memory[-3:]
    approvals = [m for m in recent if "authorized" in m["verdict"]]
    avg_resonance = sum(m["resonance"] for m in recent) / len(recent)

    if len(approvals) == 3 and avg_resonance > 0.6:
        return "adaptive: lower clarity threshold"
    elif len(approvals) == 0:
        return "adaptive: raise caution threshold"
    else:
        return "adaptive: hold pattern"

def execute_adaptation():
    trend = assess_trend()
    print("\n=== ΔA3 Evolution Report ===")
    print(f"Trend Analysis Result: {trend}")
    print("ΔA3 will adapt future vector parsing accordingly.")
    print("======================================\n")

if __name__ == "__main__":
    execute_adaptation()
