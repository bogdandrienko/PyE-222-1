import socket
import threading
import multiprocessing


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


if __name__ == '__main__':
    server = multiprocessing.Process(target=process_server, args=(), kwargs={})
    server.start()

    server.join()
