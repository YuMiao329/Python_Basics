from tkinter import *
from PIL import ImageTk


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() - 10)


def move_left(event):
    label.place(x=label.winfo_x() - 10, y=label.winfo_y())


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y() + 10)


def move_right(event):
    label.place(x=label.winfo_x() + 10, y=label.winfo_y())

#--------------------------------------------------
window = Tk()
#--------------------------------------------------
myImage = ImageTk.PhotoImage(file="hotdog.jpg")
window.geometry("500x500")
# initialize the window size using geometry
#--------------------------------------------------
window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
#--------------------------------------------------
label = Label(window,
              image=myImage,
              # bg="red"  # you could set the background color if you would like to
              )
label.place(x=0, y=0)
#--------------------------------------------------
window.mainloop()
