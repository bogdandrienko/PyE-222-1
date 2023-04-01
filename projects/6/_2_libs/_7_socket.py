# TCP и UDP
# TCP - безопасный и медленный (он ждёт сообщение о соединении, если пакеты не пришли, он их досылает)
# UDP - небезопасный и быстрый (он не ждёт сообщение о соединении, если пакеты не пришли, он их не досылает)

# socket == ip:port (only 1 program)

# ip
# cmd -> ipconfig (192.168.0.128) | sh -> ip a

# port
# 192.168.0.128:22
# 192.168.0.128:21
# 192.168.0.128:80 (TCP HTTP)
# 192.168.0.128:443 (TCP HTTPS)
# localhost:8000 - django
# 127.0.0.1:8000 - django
# 127.0.0.1:8001 - django
# 127.0.0.1:8080 - django

# skype, zoom, diskord, telegram, anydesk....

import socket
import threading
import multiprocessing
import tkinter


def process_server():
    def new_connection(__connection: any) -> None:
        print("\n...connection started...")
        while True:
            try:
                data = __connection.recv(1024)
                __connection.send(
                    f"""{data.decode(encoding="utf8")[::-1]}""".encode(encoding="utf8")
                )
                print(f'[request]: {bytes(data).decode("utf8")} {type(data)}')
            except Exception as error:
                print(str(error))
                __connection.close()
                print("\n...close connection...")

    host = "127.0.0.1"
    port = 8000

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen(5)
    print("\n...server started...")

    while True:
        try:
            print("\n...listen...")
            connection, address = my_socket.accept()
            if connection:
                threading.Thread(target=new_connection, args=(connection,)).start()
        except Exception as error:
            print(str(error))
            break
    my_socket.close()
    print("\n...close server...")




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
    server = multiprocessing.Process(target=process_server, args=(), kwargs={})
    server.start()

    client = multiprocessing.Process(target=process_client, args=(), kwargs={})
    client.start()

    server.join()
    client.join()
