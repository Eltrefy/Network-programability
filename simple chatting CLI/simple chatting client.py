from socket import *
from threading import *
from tkinter import *
from tkinter import messagebox

sck = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 8470
sck.connect((ip, port))

while True:
    text_input = input("client message :")
    sck.send(text_input.encode("utf=8"))
    if text_input == "Q":
        break
    # print("client message :", text_input)
    recevied_data = sck.recv(2048)
    if recevied_data.decode("utf=8") == "Q":
        break
    print("Server message ::", recevied_data.decode("utf=8"))

sck.close()
