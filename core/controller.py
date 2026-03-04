from .main import run


class RoutingController:

    def __init__(self):
        self.interface_connected = False
        self.daw_running = False
        self.current_mode = "internal"

    def interface_connected_event(self):

        self.interface_connected = True
        self.apply_policy()

    def interface_disconnected_event(self):

        self.interface_connected = False
        self.apply_policy()

    def daw_started_event(self):

        self.daw_running = True
        self.apply_policy()

    def daw_closed_event(self):

        self.daw_running = False
        self.apply_policy()

    def apply_policy(self):

        if self.daw_running:
            run("external", "both")
            self.current_mode = "external"
            return

        if self.interface_connected:
            run("external", "both")
            self.current_mode = "external"
            return

        run("internal", "both")
        self.current_mode = "internal"
