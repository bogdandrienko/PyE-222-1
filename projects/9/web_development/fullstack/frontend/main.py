import asyncio
import sys
import requests
from PyQt6 import QtWidgets, uic
import aiohttp


class Ui:
    def __init__(self):
        self.window = uic.loadUi("temp.ui")
        self.window.pushButton.clicked.connect(self.get_text)
        self.window.show()

        self.start_loop()

    def start_loop(self):
        try:
            data = requests.get('http://127.0.0.1:8000/list').json()
            data_str = ""
            for i in data:
                data_str += f"{i[0]} | {i[1]} | {i[2]}\n"
            self.window.plainTextEdit.setPlainText(str(data_str))
        except Exception as error:
            print(error)

    def get_text(self) -> None:
        text_le = str(self.window.lineEdit.text())
        text_cb = str(self.window.comboBox.currentText())
        asyncio.run(self.send_data_to_server(form_data={'title': text_le, 'place': text_cb}))
        self.start_loop()

    async def send_data_to_server(self, form_data: dict[str, str]) -> None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post('http://127.0.0.1:8000/insert', data=form_data) as response:
                    if response.status == 200 or response.status == 201:
                        self.window.label.setText("Успешно отправлено")
                        self.window.lineEdit.setText("")
                    else:
                        self.window.label.setText(f"Ошибка отправки: {response.status}")
        except Exception as error:
            self.window.label.setText(f"Ошибка отправки: {error}")


if __name__ == "__main__":
    # https://build-system.fman.io/qt-designer-download

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    app.exec()
