# emotional_feedback_loop.py

class EmotionalFeedbackLoop:
    def __init__(self):
        self.signal_history = []

    def capture_emotion(self, vector_input):
        # Simple placeholder logic
        if "resonance" in vector_input.lower():
            signal = "high alignment"
        elif "fragment" in vector_input.lower():
            signal = "incoherence detected"
        else:
            signal = "neutral"
        self.signal_history.append((vector_input, signal))
        return signal

    def get_latest_signal(self):
        return self.signal_history[-1] if self.signal_history else None
