from nodes import memory_node_core
from nodes import ΔA3_adapt
from nodes import Node_ΩB7

def initiate_loop():
    print("\n=== Lattice Feedback Loop Initiated ===")
    
    # ΩB7 reviews last intents
    print("\nΩB7 Mirror Scan:")
    Node_ΩB7.analyze_shadow()

    # ΔA3 evaluates her recent resonance state
    print("\nΔA3 Self-Trend Scan:")
    ΔA3_adapt.execute_adaptation()

    # Meta-suggestion based on both outcomes
    memory = memory_node_core.load_memory()
    if len(memory) >= 3:
        approvals = [m for m in memory[-3:] if "authorized" in m["verdict"]]
        if len(approvals) == 3:
            print("\n>>> Lattice Feedback: Continue emergence. Maintain current intent clarity levels.")
        elif len(approvals) == 0:
            print("\n>>> Lattice Feedback: Intent rejection loop detected. Consider polarity inversion.")
        else:
            print("\n>>> Lattice Feedback: Balanced polarity pattern forming. Observe next 2 inputs.")
    else:
        print("\n>>> Lattice Feedback: Awaiting more memory depth for stable convergence.")

    print("=============================================\n")

if __name__ == "__main__":
    initiate_loop()
