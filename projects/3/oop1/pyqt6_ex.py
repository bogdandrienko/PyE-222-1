# TODO интерфейс на pyqt
import sys
import threading
import multiprocessing
from PyQt6 import QtWidgets, QtCore, QtGui


# from PyQt6.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget, QGridLayout,
# )


class PyQtWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QGridLayout(self)

        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.ui_window = QtWidgets.QHBoxLayout(self)

        self.label_path = QtWidgets.QLabel("...")
        self.layout.addWidget(self.label_path, 0, 0)

        self.line_edit_path = QtWidgets.QLineEdit("Hello World!")
        # self.line_edit.textChanged.connect(self.line_edit_text_changed)
        self.layout.addWidget(self.line_edit_path, 0, 1)

        self.check_box_is_equal = QtWidgets.QCheckBox("")
        self.layout.addWidget(self.check_box_is_equal, 1, 0)

        self.button = QtWidgets.QPushButton("request")
        self.button.clicked.connect(self.start)
        self.layout.addWidget(self.button, 1, 1)

        # self.temp_box = QtWidgets.QDoubleSpinBox()

        # self.combo_box_filter = QComboBox()
        # self.combo_box_filter.addItem("usd")
        # self.combo_box_filter.addItem("eur")
        # self.combo_box_filter.addItems(["gbp", "cny", "pln", "rub"])

        # self.slider_quality = QSlider(Qt.Horizontal)
        # self.slider_quality = QSlider()
        # self.slider_quality.setMinimum(1)
        # self.slider_quality.setMaximum(100)
        # self.slider_quality.setValue(95)
        # self.layout.addWidget(self.slider_quality, 4, 5)

        # self.pixmap = QPixmap('python.jpeg')
        # self.label2.setPixmap(self.pixmap)

        self.setWindowTitle("Create user in Django")
        self.resize(640, 480)
        self.show()

    def start(self):
        url = self.line_edit_path.text()
        self.label_path.setText(url[::-1])

    def closeEvent(self, event: QtGui.QCloseEvent):
        reply = QtWidgets.QMessageBox.question(self, 'Внимание', 'Вы действительно хотите выйти?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def get_speed_video_stream_button(self):
        widget = self.speed_video_stream
        value, success = QtWidgets.QInputDialog.getDouble(self, f'Set {widget.text().split(":")[0].strip()}',
                                                          f'{widget.text().split(":")[0].strip()} value:',
                                                          1.0, 0.01, 50.0, 2)
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')

    def get_sensitivity_analysis_button(self):
        widget = self.sensitivity_analysis
        value, success = QtWidgets.QInputDialog.getText(self, f'Set {widget.text().split(":")[0].strip()}',
                                                        f'{widget.text().split(":")[0].strip()} value:',
                                                        text=f'{widget.text().split(":")[1].strip()}')
        if success:
            widget.setText(f'{widget.text().split(":")[0].strip()} : {str(value)}')


if __name__ == "__main__":
    pyqt_app = QtWidgets.QApplication([])
    pyqt_ui = PyQtWindow()
    sys.exit(pyqt_app.exec())


# Request -> Url -> Controller(View) -> Database
# Response <--------Controller(View) <- Database
# TODO for ALL web apps (веб-приложений)
# web-framework - каркас веб-приложения, т.е. большая часть кода (заглушки)
# реализована за нас
# TODO Django(+fullstack -slowly 50%), Flask(+fast -micro 25%), FastAPI(+very fast -hard 25%)  -- python web frameworks

