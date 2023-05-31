from socket import *
from threading import Thread

host = "127.0.0.1"
port = 10000
sck = socket(AF_INET, SOCK_STREAM)
sck.bind((host, port))
sck.listen()
clients = []
alises = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handlle_clients(client):
    message = client.recv(1024)
    broadcast(message)


def receive():
    while True:
        print("Server is running and listening .....")

        client, addr = sck.accept()
        print(f"connection is esstablished with client with{str(addr)}")
        client.send("alias?".encode("utf-8"))  # alias is a pattern
        alias = client.recv(2048)
        alises.append(alias)
        clients.append(client)
        print(f"the alias  of this client is {alias}")
        broadcast(f"{alias} is connected to chat room".encode("utf-8"))
        client.send("You are connected".encode("utf-8"))
        t = Thread(target=handlle_clients, args=(client,))
        t.start()


receive()
