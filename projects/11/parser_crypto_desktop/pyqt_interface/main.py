"""Точка входа - сборка и запуск."""

import sys
from PyQt6.QtWidgets import QApplication
from ui import Ui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
