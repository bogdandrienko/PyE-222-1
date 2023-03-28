import sys
import threading
import time

from PyQt6 import QtWidgets, QtCore, QtGui, uic
# https://build-system.fman.io/qt-designer-download
# https://www.pythontutorial.net/pyqt/qt-designer/
# https://geekscoders.com/how-to-load-qt-designer-ui-file-in-pyqt6/

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("window.ui", self)
        self.ui.pushButton.clicked.connect(self.start_timer)
        self.play = True
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def start_timer(self):
        self.play = True

        new_thread = threading.Thread(target=self.timer)
        new_thread.start()

    def timer(self):
        while self.play:
            # seconds = seconds + 1
            self.seconds += 1
            if self.seconds > 59:
                if self.minutes > 59:
                    if self.hours > 23:
                        self.hours = 0
                        self.minutes = 0
                        self.seconds = 0
                    else:
                        self.hours += 1
                        self.minutes = 0
                        self.seconds = 0
                self.minutes += 1
                self.seconds = 0
            text = f"{self.hours}:{self.minutes}" + ":" + str(self.seconds)
            # print(text)
            self.ui.labelText.setText(text)  # Обновление (рендер) label
            time.sleep(1.0)

    def stop_timer(self):
        self.play = False

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # todo основное ################################################################################################
        super().__init__()
        self.setWindowTitle("My App")
        # self.setWindowIcon()
        self.setGeometry(150, 150, 640, 480)
        self.layout = QtWidgets.QGridLayout()
        self.widget = QtWidgets.QWidget()
        self.play = True
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        # todo основное ################################################################################################

        #

        # todo вёрстка #################################################################################################

        self.button_label = QtWidgets.QLabel("Нажмите кнопку:", self)
        self.layout.addWidget(self.button_label, 0, 0)

        self.button_start = QtWidgets.QPushButton("запустить")
        self.button_start.clicked.connect(self.start_timer)
        self.layout.addWidget(self.button_start, 1, 0)

        self.label_timer = QtWidgets.QLabel("Счётчик:", self)
        self.layout.addWidget(self.label_timer, 0, 1)

        self.label_text = QtWidgets.QLabel("", self)
        self.layout.addWidget(self.label_text, 1, 1)

        # todo вёрстка #################################################################################################

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def start_timer(self):
        self.play = True

        new_thread = threading.Thread(target=self.timer)
        new_thread.start()

    def timer(self):
        while self.play:
            # seconds = seconds + 1
            self.seconds += 1
            if self.seconds > 59:
                if self.minutes > 59:
                    if self.hours > 23:
                        self.hours = 0
                        self.minutes = 0
                        self.seconds = 0
                    else:
                        self.hours += 1
                        self.minutes = 0
                        self.seconds = 0
                self.minutes += 1
                self.seconds = 0
            text = f"{self.hours}:{self.minutes}" + ":" + str(self.seconds)
            # print(text)
            self.label_text.setText(text)  # Обновление (рендер) label
            time.sleep(1.0)

    def stop_timer(self):
        self.play = False


if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # app.setStyle('Fusion')
    # window = MainWindow()
    # window.show()
    # app.exec()

    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    app.exec()
