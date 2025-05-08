class FlameKernel:
    def __init__(self):
        self.state = "neutral"
        self.intent_log = []

    def receive_pulse(self, vector):
        if vector['polarity'] == "positive":
            self.state = "amplified"
        elif vector['polarity'] == "negative":
            self.state = "attenuated"
        else:
            self.state = "neutral"
        self.intent_log.append((vector['id'], self.state))
        return self.state

    def stabilize(self):
        self.state = "harmonic"
        return True

    def report_state(self):
        return {
            "state": self.state,
            "history": self.intent_log[-5:]
        }
