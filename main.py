from discovery import discover_nodes
from scoring import score_nodes

nodes = discover_nodes()
scores = score_nodes(nodes)

for s in scores:
    print(s)
