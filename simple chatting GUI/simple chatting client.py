from socket import *
import _thread
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("client chat")
root.geometry("800x800")
sck = socket(AF_INET, SOCK_STREAM)
ip = "127.0.0.1"
port = 9000
sck.connect((ip, port))
text_input = StringVar()
entry = Entry(root, width=100, textvariable=text_input)
entry.grid(column=3, row=1)
btn1 = Button(root, width=20, height=2, text="Send Message")
btn1.grid(column=3, row=3)

r = 6


def rec():
    global sck, r
    while True:
        received_data = sck.recv(2048)
        if received_data.decode("utf-8") == "Q":
            sck.close()
            root.destroy()
        Label(
            root, text="Server : " + received_data.decode("utf-8"), padx=5, pady=5
        ).grid(column=0, row=r)
        r = r + 1


_thread.start_new_thread(rec, ())


def clicked():
    global sck, r, text_input

    sck.send((text_input.get()).encode("utf=8"))  # to get a a text from string var
    if text_input.get() == "Q":
        root.destroy()
        sck.close()
    send_text = "client : " + text_input.get()
    Label(root, text=send_text, padx=5, pady=5).grid(column=0, row=r)
    text_input.set("")
    r = r + 1


btn1["command"] = clicked
root.mainloop()
