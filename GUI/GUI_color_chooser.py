from tkinter import *
from tkinter import colorchooser  # this is the submodule


def click():
    color_selected = colorchooser.askcolor()
    # eg: ((128.5, 128.5, 255.99609375), '#8080ff')
    colorHex = color_selected[1]
    window.config(bg=colorHex)


window = Tk()
window.geometry("420x420")
button = Button(text="click me",
                command=click)
button.pack()

window.mainloop()
