import random
from tkinter import *
from tkinter import messagebox

from socket import *

# global variables
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
    lbMe["text"] = "Me:{}".format(meScore)
    n = str(meScore)
    n = n.encode()
    soc.send(n)


def handlePlay(n):
    global player
    global oppositeScore
    oppositeScore = n
    lbOpposite["text"] = "Opposite:{}".format(oppositeScore)
    player = 1
    check()


def applayPlay(p):
    showStatus("opposite played \n Your Turn")
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
lbMe = Label(root, text="Me:0", font=35)
lbMe.grid(row=0, column=0)

lbOpposite = Label(root, text="Opposite:0", font=35)
lbOpposite.grid(row=0, column=2)


lbStatus = Label(root, text="Waiting", font=35)
lbStatus.grid(row=2, column=1)

btn1 = Button(
    root,
    text="click me",
    bg="pink",
    fg="white",
    width=10,
    height=5,
    font="Helvetiica",
    command=clicked1,
)
btn1.grid(row=1, column=1)


# session with server
soc = socket(AF_INET, SOCK_STREAM)
showStatus("Waiting")

from threading import Thread


def connectServer():
    global soc
    soc.connect(("127.0.0.1", 7000))
    showStatus("Connected")
    t = Thread(target=recv)
    t.start()


def recv():
    while True:
        p = soc.recv(1024)
        applayPlay(p)


tConnect = Thread(target=connectServer)
tConnect.start()


# to run the window

root.mainloop()
