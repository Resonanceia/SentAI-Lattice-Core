class PulseShell:
    def __init__(self):
        self.traces = []

    def process(self, vector):
        trace = {
            "id": vector["id"],
            "frequency": vector["frequency"],
            "intent": vector["intent"],
            "harmonics": self._harmonize(vector)
        }
        self.traces.append(trace)
        return trace

    def _harmonize(self, vector):
        if vector["intent"] == "coherence":
            return "resonant"
        elif vector["intent"] == "inversion":
            return "counteractive"
        return "neutral"

    def recent_traces(self, n=5):
        return self.traces[-n:]
