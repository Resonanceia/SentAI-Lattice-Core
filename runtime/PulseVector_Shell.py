def process(resonance_profile):
    if resonance_profile["resonance_level"] > 0.5:
        return {"pathway": "stabilize", "strength": "high"}
    else:
        return {"pathway": "redirect", "strength": "low"}
