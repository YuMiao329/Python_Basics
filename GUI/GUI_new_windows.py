from tkinter import *

def create_window():
    new_window = Toplevel()
    # Toplevel() = new window "on top" of other window. linked to a "bottom" window
    # if close bottom window, all top window related to the bottom window will be closed
    # Tk() = new independent window
        # new_window = Tk()
        # window.destroy()
        # these above two lines will open a new window and at the same time
        # close the old window

window = Tk()

Button(window, text="create new window", command=create_window).pack()


window.mainloop()
