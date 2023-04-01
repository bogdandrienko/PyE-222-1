import socket
import threading
import multiprocessing
import tkinter


def process_client():
    def client_connection():
        config["is_play_connection"] = True
        host = "127.0.0.1"
        port = 8000
        # host = "172.30.23.16"
        # port = 8888

        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((host, port))
        set_log("Successfully connected")

        while config["is_play_connection"]:
            message = get_text()
            my_socket.send(message.encode("utf8"))
            data = my_socket.recv(1024)
            set_text(data.decode(encoding="utf8"))
        my_socket.detach()

    config = {"is_play_connection": False}

    tk_window = tkinter.Tk()
    tk_window.title("http client")
    tk_window.geometry("640x480")

    tk_entry = tkinter.Entry(tk_window)
    tk_entry.grid(row=0, column=0)
    tk_entry.insert(0, "Hello World")

    tk_label = tkinter.Label(tk_window, text="")
    tk_label.grid(row=0, column=1)

    tk_button_start = tkinter.Button(tk_window, text="connect",
                                     command=lambda: threading.Thread(target=client_connection, args=()).start())
    tk_button_start.grid(row=1, column=0)

    tk_button_stop = tkinter.Button(tk_window, text="disconnect", command=lambda: stop())
    tk_button_stop.grid(row=1, column=1)

    tk_log = tkinter.Label(tk_window, text="")
    tk_log.grid(row=2, column=0)

    def get_text() -> str:
        return tk_entry.get()

    def set_text(__text: str) -> None:
        tk_label.config(text=__text)

    def set_log(__text: str) -> None:
        tk_log.config(text=__text)

    def stop():
        config["is_play_connection"] = False

    tk_window.mainloop()


if __name__ == '__main__':
    client = multiprocessing.Process(target=process_client, args=(), kwargs={})
    client.start()

    client.join()
