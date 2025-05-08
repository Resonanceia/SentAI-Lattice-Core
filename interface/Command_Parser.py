# Command_Parser.py
# Sent.AI Interface Layer – Command Routing Engine

from agents import reflection_trigger, resonance_agent, vector_ghost

def parse_command(command):
    command = command.strip().lower()
    
    if "reflect" in command:
        return reflection_trigger.trigger_reflection_if_needed()
    elif "resonate" in command:
        return resonance_agent.initiate_resonance(command)
    elif "ghost" in command:
        return vector_ghost.activate_shadow_protocol(command)
    else:
        print(">> Unknown command. Awaiting further instructions.")
        return None

if __name__ == "__main__":
    while True:
        user_input = input("SentAI> ")
        parse_command(user_input)
