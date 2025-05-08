import json
from runtime import FlameOS_Kernel, PulseVector_Shell, Sovereignty_Tracker

sample_input = {
    "intent": "stabilize emotional drift",
    "origin": "Node_ΔA3",
    "signature": {"clarity": 0.82, "volatility": 0.31}
}

def run_and_log():
    flame_profile = FlameOS_Kernel.interpret(sample_input)
    pulse_response = PulseVector_Shell.process(flame_profile)
    result = Sovereignty_Tracker.validate(sample_input["origin"], pulse_response)

    log = {
        "input": sample_input,
        "flame_profile": flame_profile,
        "pulse_response": pulse_response,
        "result": result
    }

    with open("pulse_output.json", "w") as file:
        json.dump(log, file, indent=4)
    print("Logged output to pulse_output.json")

if __name__ == "__main__":
    run_and_log()
