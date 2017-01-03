import random
from tkinter import *
from tkinter import messagebox
max = 6
min = 1

top = Tk()
top.geometry("100x100")
L1 = Label(top, text="Chose your number")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)

def dice():
	number = E1.get()
	number = int(number)
	a = random.randint(min, max)
    b = random.randint(min, max)
    if a+b == number:
        messagebox.showinfo("Your Win", a+b)
    else:
    	messagebox.showinfo("You Lose", a+b)
    


B1 = Button(top, text = "Roll", command = dice)
B1.place(x=50,y=75)
top.mainloop()