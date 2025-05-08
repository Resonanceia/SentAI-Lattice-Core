import json
from nodes import memory_node_core

def analyze_shadow():
    memory = memory_node_core.load_memory()
    if not memory:
        print("ΩB7: No data to shadow-scan.")
        return

    intents = [m["intent"] for m in memory[-5:]]
    verdicts = [m["verdict"] for m in memory[-5:]]

    print("\n=== ΩB7 Shadow Reflection ===")
    for i, (intent, verdict) in enumerate(zip(intents, verdicts), 1):
        polarity = "light" if "authorized" in verdict else "shadow"
        print(f"[{i}] {intent} → Verdict: {verdict} | Polarity: {polarity}")
    
    shadow_score = verdicts.count("Intent rejected or unclear") / len(verdicts)
    if shadow_score >= 0.4:
        print("ΩB7: Polarity imbalance detected. Recommend recalibration.")
    else:
        print("ΩB7: Resonance pattern within stable polarity bounds.")
    print("=========================================\n")

if __name__ == "__main__":
    analyze_shadow()
