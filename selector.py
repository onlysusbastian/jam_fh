class RoutingTarget:
    def __init__(self, sink_id=None, source_id=None, sink_name=None, source_name=None):
        self.sink_id = sink_id
        self.source_id = source_id
        self.sink_name = sink_name
        self.source_name = source_name

    def __repr__(self):
        return f"<RoutingTarget sink={self.sink_name} source={self.source_name}>"

def select_targets(scored_nodes, mode="auto"):
    best_sink = None
    best_source = None

    for entry in scored_nodes:
        node = entry.node
        score = entry.score

        # MODE FILTERING (keep minimal for now)
        if mode == "external" and node.bus != "usb":
            continue
        if mode == "internal" and node.bus != "pci":
            continue

        # Choose best sink
        if node.media_class == "Audio/Sink":
            if best_sink is None or score > best_sink.score:
                best_sink = entry

        # Choose best source
        elif node.media_class == "Audio/Source":
            if best_source is None or score > best_source.score:
                best_source = entry

    if best_sink is None or best_source is None:
        raise RuntimeError("No valid routing target found")

    return RoutingTarget(
        sink_id=best_sink.node.id,
        source_id=best_source.node.id,
        sink_name=best_sink.node.node_name,
        source_name=best_source.node.node_name
    )
