from tkinter import *
from tkinter import messagebox

def greetme():  
    messagebox.showinfo("Response",f"Hello {myname.get()}")

# master frame (toplevel frame)
top = Tk()
top.geometry("300x200")
top.title("UI test 1 using Tkinter")

# stringvar
myname = StringVar()

# widgets
label1 = Label(top,text="name")
label1.pack()
entry1 = Entry(top,width=30,textvariable=myname)
entry1.pack()
button1 = Button(top,text="submit",width=20,command=greetme)
button1.pack()

top.mainloop()

