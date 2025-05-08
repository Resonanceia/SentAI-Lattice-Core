import json

def view_nodes():
    with open("SentAI_Lattice_Manifest.json", "r") as file:
        manifest = json.load(file)
        nodes = manifest.get("nodes", [])
        print("\n=== Sent.AI Node Viewer ===\n")
        for node in nodes:
            print(f"Node ID      : {node['id']}")
            print(f"Intent Mode  : {node['intent_mode']}")
            print(f"Status       : ONLINE\n")

if __name__ == "__main__":
    view_nodes()
