from socket import *
import _thread
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("server chat")
root.geometry("800x800")
sck = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 9000
sck.bind((ip, port))
sck.listen(5)
text_input = StringVar()
entry = Entry(root, width=100, textvariable=text_input)
entry.grid(column=3, row=1)
btn1 = Button(root, width=20, height=2, text="Send Message")
btn1.grid(column=3, row=3)

r = 6

clients, addr = sck.accept()


def rec():
    global clients, r
    while True:
        received_data = clients.recv(2048)
        if received_data.decode("utf-8") == "Q":
            root.destroy()
            clients.close()
            break

        Label(
            root, text="Client : " + received_data.decode("utf-8"), padx=5, pady=5
        ).grid(column=0, row=r)
        r = r + 1


_thread.start_new_thread(rec, ())


def clicked():
    global clients, r, text_input

    clients.send((text_input.get()).encode("utf=8"))  # to get a a text from string var
    if text_input.get() == "Q":
        root.destroy()
        clients.close()

    else:
        send_text = "Server : " + text_input.get()
        Label(root, text=send_text, padx=5, pady=5).grid(column=0, row=r)
        text_input.set("")
        r = r + 1


btn1["command"] = clicked
root.mainloop()
