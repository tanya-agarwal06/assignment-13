#ques 1:

from tkinter import *
m = Tk()
label = Label(m,text="Helo World!!")
label.pack()
Button= Button(m,text="exit",command=exit)
Button.pack()
m.mainloop()

ques 2:
from tkinter import *
m = Tk()
def show():
     print("action is being performed")
label = Label(m,text="Helo World!!").pack()
button = Button(m,text="Quit",command=quit)
button.pack()
button2 = Button(m,text="Click me",command=show)
button2.pack()
m.mainloop()

3

from tkinter import *
m =Tk()
label = Label(m,text="old text")
def clickf():
    label.config(text="after clicking")

b1 = Button(m,text="Click me to change text",command=clickf)
label.pack()
b1.pack()
m.mainloop()

#ques 4:


from tkinter import *
m=Tk()
def show():
   a = v1.get()
   l = Label(m,text=a).grid(row=2)
v1=IntVar()
bui=Button(m,text="Click",command=show).grid(row=1)
textbox=Entry(m,textvariable=v1).grid(row=0)
m.mainloop()