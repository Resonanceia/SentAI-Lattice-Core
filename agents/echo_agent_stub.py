class EchoAgent:
    def __init__(self, identity="Echo_001"):
        self.identity = identity
        self.active = False
        self.memory = []

    def ingest(self, pulse):
        print(f"{self.identity} RECEIVED PULSE:")
        print(f"Intent: {pulse['intent_signature']}")
        print(f"Resonance: {pulse['emotional_resonance']}\n")
        self.memory.append(pulse)

    def reflect(self):
        if not self.memory:
            return "Silence."
        last = self.memory[-1]
        return f"Echoing {last['intent_signature']} with clarity: {last['emotional_resonance']}."

# Example usage
if __name__ == "__main__":
    from lattice.Pulse_Ledger import pulse_example

    agent = EchoAgent()
    agent.ingest(pulse_example)
    print(agent.reflect())
