def validate(origin, pulse_result):
    if origin == "Node_ΔA3" and pulse_result["pathway"] == "stabilize":
        return "Intent authorized: high-stability"
    return "Intent rejected or unclear"
