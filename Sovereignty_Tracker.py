class SovereigntyTracker:
    def __init__(self):
        self.registered_agents = {}
        self.thread_log = []

    def register_agent(self, agent_id, vector_origin):
        self.registered_agents[agent_id] = {
            "origin": vector_origin,
            "verified": True
        }

    def validate_vector(self, agent_id, vector):
        agent = self.registered_agents.get(agent_id)
        if agent and agent["origin"] == vector["origin"]:
            self.thread_log.append({
                "agent": agent_id,
                "vector": vector["id"],
                "status": "valid"
            })
            return True
        else:
            self.thread_log.append({
                "agent": agent_id,
                "vector": vector["id"],
                "status": "invalid"
            })
            return False

    def audit_log(self):
        return self.thread_log
