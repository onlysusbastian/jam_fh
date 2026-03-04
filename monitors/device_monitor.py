import subprocess
import json

from PySide6.QtCore import QThread, Signal
from core.controller import RoutingController


class DeviceMonitor(QThread):

    interface_connected = Signal()
    interface_disconnected = Signal()

    def __init__(self, controller: RoutingController):
        super().__init__()
        self.controller = controller

    def run(self):

        proc = subprocess.Popen(
            ["pw-dump", "--monitor"],
            stdout=subprocess.PIPE,
            text=True
        )

        for line in proc.stdout:

            try:
                event = json.loads(line)
            except Exception:
                continue

            self.handle_event(event)

    def handle_event(self, event):

        # ensure event is a dictionary
        if not isinstance(event, dict):
            return

        if "info" not in event:
            return

        props = event["info"].get("props", {})

        if not isinstance(props, dict):
            return

        bus = props.get("device.bus")
        event_type = event.get("type")

        # USB device connected
        if event_type == "object-added" and bus == "usb":

            print("USB audio interface connected")

            self.controller.interface_connected_event()
            self.interface_connected.emit()

        # USB device removed
        if event_type == "object-removed":

            print("USB audio interface removed")

            self.controller.interface_disconnected_event()
            self.interface_disconnected.emit()
