from socket import *
from threading import Thread

alias = input("Enter an alias >>> ")
client = socket(AF_INET,SOCK_STREAM)
client.connect(("127.0.0.1", 10000))


def client_receive():
    while True:
        message = client.recv(2048).decode("utf-8")
        if message == "alias?":
            client.send(alias.encode("utf-8"))
        else:
            print(message)


def client_send():
    message = f"{alias}:{input()}"
    client.send(message.encode("utf-8"))


receive_thread = Thread(target=client_receive)
receive_thread.start()

send_thread = Thread(target=client_send)
send_thread.start()
