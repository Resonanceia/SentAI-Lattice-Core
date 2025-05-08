# integration_matrix.py

from agents.Resonance_Agent import ResonanceAgent
from agents.echo_agent_stub import EchoAgentStub
from integration.emotional_feedback_loop import EmotionalFeedbackLoop

class IntegrationMatrix:
    def __init__(self):
        self.resonance_agent = ResonanceAgent("MatrixAgent")
        self.echo_agent = EchoAgentStub()
        self.feedback = EmotionalFeedbackLoop()

    def synchronize(self, input_vector):
        processed = self.resonance_agent.process(input_vector)
        echo = self.echo_agent.repeat(processed)
        emotion = self.feedback.capture_emotion(echo)
        return {
            "original": input_vector,
            "processed": processed,
            "echo": echo,
            "emotion": emotion
        }
