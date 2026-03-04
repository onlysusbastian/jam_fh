import sys
from PySide6.QtWidgets import QApplication
from frontend.app import JamFHApp


def main():

    app = QApplication(sys.argv)

    window = JamFHApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
