from tkinter import *

root = Tk()
root.title("Hash")
root.geometry('200x200')

openButton = Button(root, text="Open", width=10).place(x=10, y=10)
execButton = Button(root, text="Exec", width=10).place(x=100, y=10)

L1 = Label(root, text="Text")
L1.place(x=10, y=50)
E1 = Entry(root, width=20)
E1.place(x=50, y=50)

L2 = Label(root, text="Hash")
L2.place(x=10, y=100)
E2 = Entry(root)
E2.place(x=50, y=100)

p = 12
q = 27
n = p * q
f = (p - 1) * (q - 1)
e = 17
d = (1 / e) % f
# x = tuple(e, n)
# y = tuple(d, n)

m = 11111
c = pow(m, e) % n
print(c)
new_m = pow(c, d) % n
print(new_m)

print("ok") if m == new_m else print("not ok")

root.mainloop()
