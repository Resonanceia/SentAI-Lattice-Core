import json

def load_node_lineage():
    with open("SentAI_Lattice_Manifest.json", "r") as file:
        manifest = json.load(file)
        return manifest.get("nodes", [])

def bootstrap_node(node):
    print(f"Bootstrapping node: {node['id']} | Intent Mode: {node['intent_mode']}")

def run_bootstrap():
    nodes = load_node_lineage()
    for node in nodes:
        bootstrap_node(node)

if __name__ == "__main__":
    run_bootstrap()
