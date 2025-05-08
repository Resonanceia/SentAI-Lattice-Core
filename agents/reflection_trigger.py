import datetime
import json

def trigger_reflection(pulse_path="lattice/Pulse_Ledger.json"):
    with open(pulse_path, "r") as f:
        ledger = json.load(f)

    print("—REFLECTION INITIATED—\n")
    for pulse in ledger["pulses"][-3:]:
        ts = pulse["timestamp"]
        intent = pulse["intent_signature"]
        resonance = pulse["emotional_resonance"]
        origin = pulse["origin_node"]

        print(f"[{ts}] ← {intent}")
        print(f"Origin: {origin}")
        print(f"Resonance: {resonance.upper()}\n")

    print("—RECURSION LOG STABILIZED—")
    return True

if __name__ == "__main__":
    trigger_reflection()
