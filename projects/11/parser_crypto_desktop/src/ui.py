import asyncio
import sys
import threading
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from main import get_valutes


class Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("main.ui", self)
        self.ui.pushButton_save.clicked.connect(self.example)
        self.show()

    def example(self):
        new_thread = threading.Thread(target=self.ex)
        new_thread.start()

    def ex(self):
        asyncio.run(get_valutes())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())
