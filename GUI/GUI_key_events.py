from tkinter import *


def doSomething(event):
    print("You hit a return: " + event.keysym)
    label.config(text=event.keysym)  # change displayed label with key pressed


def quitTab(event):
    print("You hit: " + event.keysym, "so you quit")
    label.config(text=event.keysym)  # change displayed label with key pressed
    quit()


def hitAny(event):
    print("you hit any key: " + event.keysym)
    label.config(text=event.keysym)  # change displayed label with key pressed


window = Tk()

# window.bind(event,
#            function)
#

window.bind("<Return>",
            doSomething)

window.bind("<q>",
            quitTab)

window.bind("<Key>",
            hitAny)

label = Label(window,
              font=("Times New Roman", 25)
              )
label.pack()
#display the key pressed

window.mainloop()
