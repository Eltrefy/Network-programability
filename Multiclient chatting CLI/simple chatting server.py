from socket import *
from threading import *
from tkinter import *
from tkinter import messagebox

sck = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 8470
sck.bind((ip, port))
sck.listen(5)
client, addr = sck.accept()
# print("connection from", client[0])

while True:
    recived_data = client.recv(2048)
    if recived_data.decode("utf=8") == "Q":
        break
    print("client messsage :", recived_data.decode("utf=8"))
    text_input = input("server message:")
    client.send(text_input.encode("utf=8"))
    if text_input == "Q":
        break
    # print("Server message", text_input)


sck.close()
