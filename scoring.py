class DeviceScore:
    def __init__(self, node, score):
        self.node = node
        self.score = score

    def __repr__(self):
        return f"<DeviceScore {self.node.node_name} score={self.score}>"

def score_node(node):
    score = 0

    # Prefer USB interfaces
    if node.bus == "usb":
        score += 10

    # Internal audio fallback
    elif node.bus == "pci":
        score += 5

    # Channel count bonus
    if node.channels >= 2:
        score += 2

    return score

def score_nodes(nodes):
    scored = []

    for node in nodes:
        s = score_node(node)
        scored.append(DeviceScore(node, s))

    return scored
