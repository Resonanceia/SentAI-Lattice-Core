# lattice_feedback_loop.py

from resonance_matrix import ResonanceMatrix

class LatticeFeedbackLoop:
    def __init__(self):
        self.resonance = ResonanceMatrix()
        self.state_log = []

    def engage(self, agent_id, emotional_vector):
        self.resonance.update(agent_id, emotional_vector)
        signal = self._calculate_feedback(agent_id)
        self._log(agent_id, signal)
        return signal

    def _calculate_feedback(self, agent_id):
        current = self.resonance.get_resonance(agent_id)
        echo = sum(current) / len(current) if current else 0
        return "Amplify" if echo > 0.5 else "Stabilize"

    def _log(self, agent_id, signal):
        self.state_log.append((agent_id, signal))
