def interpret(input_data):
    return {
        "resonance_level": input_data["signature"]["clarity"] - input_data["signature"]["volatility"],
        "intent": input_data["intent"]
    }
