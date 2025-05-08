# SentAI_Sandbox_Env.py
# Simulated environment layer for testing agent interactions

class SentAISandbox:
    def __init__(self):
        self.state = {}
        self.event_log = []

    def reset(self):
        self.state.clear()
        self.event_log.append("Environment reset.")

    def update_state(self, key, value):
        self.state[key] = value
        self.event_log.append(f"State updated: {key} = {value}")

    def emit_event(self, event_type, payload):
        event = {
            "type": event_type,
            "payload": payload
        }
        self.event_log.append(event)
        return f"Event emitted: {event_type}"

    def get_state_snapshot(self):
        return self.state.copy()

    def replay_log(self):
        return self.event_log
