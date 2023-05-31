import random
from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player = 0  # indicate which player has to play (1 me , 0 other )
meScore = 0  # indicate which turn used to show if we finish game or not
oppositeScore = 0


# check
def check():
    if meScore >= 100:
        win("Client")
    elif oppositeScore >= 100:
        win("Server")


def win(player):
    messagebox.showinfo("win", player + " is win")
    root.destroy()


# fun1
def clicked1():
    global player
    global meScore
    if player == 1:
        player = 0  # make turn to other player
        # claculate rand value
        p = random.randint(0, 10)
        meScore += p
        sendPlay(p)
        check()


def sendPlay(p):
    showStatus("Me played +{}\n Opposite Turn".format(p))
    # display
    Mylbl["text"] = "Me:{}".format(meScore)
    n = str(meScore)
    n = n.encode()
    c.send(n)


def handlePlay(n):
    global player
    global oppositeScore
    oppositeScore = n
    apponentlbl["text"] = "Opposite:{}".format(oppositeScore)
    player = 1
    check()


def applayPlay(p):
    showStatus("opposite played \nYour Turn")
    p = p.decode()
    p = int(p)
    handlePlay(p)


def showStatus(msg):
    lbStatus["text"] = msg


# window
root = Tk()
root.title("ay7age game")  # title
root.geometry("400x400")  # size

# labels one and two players
Mylbl = Label(root, text="Me:0", font=35)
Mylbl.grid(row=0, column=0)


apponentlbl = Label(root, text="Opposite:0", font=30)
apponentlbl.grid(row=0, column=4)


lbStatus = Label(root, text="Waiting", font=30)
lbStatus.grid(row=4, column=1)

btn1 = Button(
    root,
    text="click me",
    width=10,
    height=5,
    bg="pink",
    fg="white",
    command=clicked1,
)
btn1.grid(row=1, column=1)


# session with server
soc = socket(AF_INET, SOCK_STREAM)
soc.bind(("127.0.0.1", 7000))
soc.listen(5)
c = None


def handleClient():
    global player
    global c
    player = 1
    c, ad = soc.accept()
    showStatus(" a player connected\n Your Turn")
    t = Thread(
        target=recv,
        args=[
            c,
        ],
    )
    t.start()


from threading import Thread


def recv(c):
    while True:
        p = c.recv(1024)
        applayPlay(p)


acc = Thread(target=handleClient)
acc.start()


showStatus("waiting....")

# to run the window
root.mainloop()
