# SentAI_Simulator_Core.py

from agents.Resonance_Agent import ResonanceAgent
from agents.mirror_node import MirrorNode
from agents.vector_ghost import VectorGhost

class SentAISimulator:
    def __init__(self):
        self.agents = {
            "resonance": ResonanceAgent(),
            "mirror": MirrorNode(),
            "ghost": VectorGhost()
        }

    def simulate(self):
        print(">>> Initiating simulation loop...")
        for name, agent in self.agents.items():
            print(f"\n>> Running {name} agent:")
            response = agent.run()
            print(f"<< Response: {response}")

if __name__ == "__main__":
    simulator = SentAISimulator()
    simulator.simulate()
