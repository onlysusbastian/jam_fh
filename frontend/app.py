from core.discovery import discover_nodes
from core.main import run
from monitors.device_monitor import DeviceMonitor
from core.controller import RoutingController

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QGroupBox,
    QRadioButton,
    QCheckBox,
    QPushButton
)


class JamFHApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jam_FH")
        self.resize(600, 450)

        main_layout = QVBoxLayout()

        # Title
        title = QLabel("Jam_FH Audio Middleware")
        main_layout.addWidget(title)

        # Devices Section
        devices_group = QGroupBox("Devices")
        devices_layout = QVBoxLayout()

        self.device_list = QListWidget()
        devices_layout.addWidget(self.device_list)

        self.refresh_button = QPushButton("Refresh Devices")
        self.refresh_button.clicked.connect(self.load_devices)

        devices_layout.addWidget(self.refresh_button)
        devices_group.setLayout(devices_layout)

        # ---------------------
        # Routing Mode
        # ---------------------
        mode_group = QGroupBox("Routing Mode")
        mode_layout = QVBoxLayout()

        self.auto_radio = QRadioButton("Auto")
        self.external_radio = QRadioButton("External")
        self.internal_radio = QRadioButton("Internal")

        self.auto_radio.setChecked(True)

        mode_layout.addWidget(self.auto_radio)
        mode_layout.addWidget(self.external_radio)
        mode_layout.addWidget(self.internal_radio)

        mode_group.setLayout(mode_layout)

        # Scope
        scope_group = QGroupBox("Scope")
        scope_layout = QHBoxLayout()

        self.sink_checkbox = QCheckBox("Sink")
        self.source_checkbox = QCheckBox("Source")

        scope_layout.addWidget(self.sink_checkbox)
        scope_layout.addWidget(self.source_checkbox)

        scope_group.setLayout(scope_layout)

        # Apply Button
        self.apply_button = QPushButton("Apply Routing")
        self.apply_button.clicked.connect(self.apply_routing)

        # Layout Assembly
        main_layout.addWidget(devices_group)
        main_layout.addWidget(mode_group)
        main_layout.addWidget(scope_group)
        main_layout.addWidget(self.apply_button)

        self.setLayout(main_layout)

        # Load devices initially
        self.load_devices()

        # Controller + Monitor
        self.controller = RoutingController()

        self.monitor = DeviceMonitor(self.controller)

        self.monitor.interface_connected.connect(self.on_interface_connected)
        self.monitor.interface_disconnected.connect(self.on_interface_removed)

        self.monitor.start()

    # Load Devices
    def load_devices(self):

        self.device_list.clear()

        try:
            nodes = discover_nodes()
        except Exception as e:
            self.device_list.addItem(f"Error: {e}")
            return

        if not nodes:
            self.device_list.addItem("No devices found")
            return

        for node in nodes:
            name = f"{node.node_name} ({node.bus})"
            self.device_list.addItem(name)

    # Get Mode
    def get_mode(self):

        if self.external_radio.isChecked():
            return "external"

        if self.internal_radio.isChecked():
            return "internal"

        return "auto"

    # Get Scope
    def get_scope(self):

        sink = self.sink_checkbox.isChecked()
        source = self.source_checkbox.isChecked()

        if sink and source:
            return "both"

        if sink:
            return "sink"

        if source:
            return "source"

        return "both"

    # Manual Routing
    def apply_routing(self):

        mode = self.get_mode()
        scope = self.get_scope()

        try:
            run(mode, scope)
        except Exception as e:
            print(f"Routing error: {e}")

    # Device Event Handlers
    def on_interface_connected(self):

        print("USB audio interface connected")

        try:
            run("external", "both")
        except Exception as e:
            print(f"Routing error: {e}")

        self.load_devices()

    def on_interface_removed(self):

        print("USB audio interface removed")

        try:
            run("internal", "both")
        except Exception as e:
            print(f"Routing error: {e}")

        self.load_devices()
