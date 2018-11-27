import time
import concurrent.futures
import socket

class Base:
    # private method
    def __init__(self):
        print("init")

    def __mainthread():
        print("__mainthread")
        for i in range(5):
            print("[mainthread] sleep...")
            time.sleep(1)

    def __socketthread():
        print("__socketthread")
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('127.0.0.1', 50001))
                s.listen(10)
                clients = []

                while True:
                    try:
                        s.settimeout(None)
                        connection, address = s.accept()
                        clients.append((connection, address))
                        while True:
                            connection.settimeout(3)
                            from_client = connection.recv(4096).decode()
                            to_client = "data: {}".format(from_client)
                            connection.sent(to_client.encode("UTF-8"))
                    except Exception as e:
                        print(e)
                        continue

    # public class method
    def start_mainthread(self):
        print("start_mainthread")
        executer = concurrent.futures.ThreadPoolExecutor(max_workers = 2)
        executer.submit(Base.__mainthread)

    def start_listen(self):
        print("start_listen")
        executer = concurrent.futures.ThreadPoolExecutor(max_workers = 2)
        executer.submit(Base.__socketthread)

    # public static method
    @staticmethod
    def func01():
        for i in range(10):
            print("sleep...")
            time.sleep(1)

if __name__ == "__main__":
    base = Base()
    #base.start_mainthread()
    base.start_listen()
