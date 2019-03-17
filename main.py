import hashlib
from tkinter import *


def hashing(text):
    return hashlib.md5(text.encode()).hexdigest()


def readFromFile():
    f = open('in.txt', 'r')
    a = f.read()
    f.close()
    return a


def writeToFile(text):
    f = open('out.txt', 'w')
    f.truncate(0)
    f.write(text)
    f.close()
    return


root = Tk()
root.title("Hash")
root.geometry('200x200')


def openBtn():
    E1.insert(0, readFromFile())


def execBtn():
    E2.delete(0, 'end')
    E2.insert(0, hashing(E1.get()))
    writeToFile(E2.get())


openButton = Button(root, text="Open", width=10, command=openBtn).place(x=10, y=10)
execButton = Button(root, text="Exec", width=10, command=execBtn).place(x=100, y=10)

L1 = Label(root, text="Text")
L1.place(x=10, y=50)
E1 = Entry(root, width=50)
E1.place(x=50, y=50)

L2 = Label(root, text="Hash")
L2.place(x=10, y=100)
E2 = Entry(root)
E2.place(x=50, y=100)

root.mainloop()
