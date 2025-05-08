# intent_resolver.py
"""
Bridges user input and Sent.AI’s agent matrix via emotional-intent parsing.
Handles message routing, priority weighting, and activation conditions.
"""

import json
from agents import Resonance_Agent

def resolve_intent(payload: dict):
    """
    Interpret user payload and dispatch to appropriate agent logic.
    """
    intent = payload.get("intent", "")
    context = payload.get("context", {})
    
    print(f">> Resolving intent: {intent}")
    
    if intent == "reflect":
        return Resonance_Agent.reflect(context)
    elif intent == "query_status":
        return Resonance_Agent.status_report()
    else:
        return {"message": "Intent unrecognized", "success": False}
