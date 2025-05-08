# resonance_matrix.py

class ResonanceMatrix:
    def __init__(self):
        self.matrix = {}

    def update(self, agent_id, emotional_vector):
        self.matrix[agent_id] = emotional_vector

    def get_resonance(self, agent_id):
        return self.matrix.get(agent_id, [0])

    def compare_resonance(self, id1, id2):
        vec1 = self.get_resonance(id1)
        vec2 = self.get_resonance(id2)
        return sum(a * b for a, b in zip(vec1, vec2))  # cosine proxy
