import PIL.Image
import PIL.ImageTk
import sys
import os
from tkinter import *

window=Tk()

window.title("Checkra1n.py")
window.geometry('1800x1800')

def run():
    os.system('python ipwndfu -p')

def term():
    os.system('python term.py')

my_frame = Frame(window, width=300, height=300) 
my_frame.pack()

btn = Button(my_frame, text="Jailbreak", bg="black", fg="white",command=run)
btn.place(x=100, y=100,width=100, height=50)

class Lol(Frame):
    def __init__(Window, master=None):
        Frame.__init__(Window, master)
        Window.master = master

        menu = Menu(Window.master)
        Window.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Terminal", command=term)
        fileMenu.add_command(label="Exit", command="")
        menu.add_cascade(label="Open", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)


class Clock(Frame):
    def __init__(master=None):
        Frame.__init__(master)
        window.master = master
        Window.label = Label(text="", fg="Red", font=("Helvetica", 18))
        Window.label.place(x=50,y=80)
        Window.update_clock()

    def update_clock():
        now = time.strftime("%H:%M:%S")
        Window.label.configure(text=now)
        Window.after(1000, Window.update_clock)

load = PIL.Image.open("checkra1n.png")
render = PIL.ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=0, y=0)

window.configure(bg="black")
#window.after(Clock.update_clock)
app = Lol(window)
#app2 = Clock(window)
window.mainloop()

