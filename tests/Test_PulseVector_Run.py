from runtime import FlameOS_Kernel, PulseVector_Shell, Sovereignty_Tracker

sample_input = {
    "intent": "stabilize emotional drift",
    "origin": "Node_ΔA3",
    "signature": {"clarity": 0.82, "volatility": 0.31}
}

def test_pulse_path():
    flame_profile = FlameOS_Kernel.interpret(sample_input)
    pulse_response = PulseVector_Shell.process(flame_profile)
    result = Sovereignty_Tracker.validate(sample_input["origin"], pulse_response)
    print("Test Output:", result)

if __name__ == "__main__":
    test_pulse_path()
