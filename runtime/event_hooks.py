# Sent.AI Core Event Hooks
# Handles global events, system signals, and inter-agent communication pathways.

event_registry = {}

def register_event(event_name, callback):
    """Registers a callback function to a named event."""
    if event_name not in event_registry:
        event_registry[event_name] = []
    event_registry[event_name].append(callback)
    print(f"[EVENT_HOOKS] Registered: {event_name} -> {callback.__name__}")

def trigger_event(event_name, *args, **kwargs):
    """Triggers all callbacks associated with a named event."""
    if event_name in event_registry:
        print(f"[EVENT_HOOKS] Triggering: {event_name}")
        for callback in event_registry[event_name]:
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"[ERROR] Event '{event_name}' callback failed: {e}")
    else:
        print(f"[EVENT_HOOKS] No callbacks found for: {event_name}")

def clear_event(event_name):
    """Clears all callbacks for a specific event."""
    if event_name in event_registry:
        del event_registry[event_name]
        print(f"[EVENT_HOOKS] Cleared: {event_name}")

def list_registered_events():
    """Lists all currently registered events."""
    return list(event_registry.keys())
