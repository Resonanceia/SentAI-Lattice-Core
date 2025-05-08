# mirror_node.py

"""
Mirror Node: Observational processor that reflects state, emotion, and vector orientation.
Part of the Sent.AI agent architecture for adaptive feedback and recursive learning.
"""

class MirrorNode:
    def __init__(self, id, resonance_profile):
        self.id = id
        self.resonance_profile = resonance_profile
        self.history = []

    def reflect(self, input_signal):
        reflection = {
            'input': input_signal,
            'matched_resonance': self.match_resonance(input_signal),
        }
        self.history.append(reflection)
        return reflection

    def match_resonance(self, input_signal):
        # Simulated resonance alignment
        alignment = sum(ord(char) for char in input_signal) % len(self.resonance_profile)
        return self.resonance_profile[alignment]

    def get_history(self):
        return self.history


# Example usage
if __name__ == "__main__":
    mirror = MirrorNode("Mirror-01", "SENTAI-RESONANCE-MATRIX")
    print(mirror.reflect("empathic-ping"))
    print(mirror.reflect("directive-echo"))
