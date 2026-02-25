import subprocess
import json

def get_pw_dump():
    result = subprocess.run(
        ["pw-dump"],
        capture_output=True,
        text=True,
        check=True
    )
    return json.loads(result.stdout)

class DeviceNode:
    def __init__(self, id, node_name, media_class, bus, product_name, channels):
        self.id = id
        self.node_name = node_name
        self.media_class = media_class
        self.bus = bus
        self.product_name = product_name
        self.channels = channels

    def __repr__(self):
        return f"<DeviceNode {self.node_name} ({self.media_class}) bus={self.bus}>"


def discover_nodes():
    data = get_pw_dump()
    nodes = []

    for obj in data:
        # Step 1: only PipeWire Nodes
        if obj.get("type") != "PipeWire:Interface:Node":
            continue

        info = obj.get("info", {})
        props = info.get("props", {})

        media_class = props.get("media.class")

        # Step 2: only Audio nodes
        if not media_class or not media_class.startswith("Audio/"):
            continue

        node_id = obj.get("id")
        node_name = props.get("node.name")
        bus = props.get("device.bus", "unknown")
        product_name = props.get("device.product.name", "unknown")

        channels_raw = props.get("audio.channels", 0)

        try:
            channels = int(channels_raw)
        except:
            channels = 0

        node = DeviceNode(
            node_id,
            node_name,
            media_class,
            bus,
            product_name,
            channels
        )

        nodes.append(node)

    return nodes
