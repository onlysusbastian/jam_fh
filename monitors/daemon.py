from core.controller import RoutingController
from monitors.device_monitor import DeviceMonitor


def main():

    controller = RoutingController()

    monitor = DeviceMonitor(controller)

    monitor.start()


if __name__ == "__main__":
    main()
