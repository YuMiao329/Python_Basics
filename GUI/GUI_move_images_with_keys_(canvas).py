from tkinter import *
from PIL import ImageTk


def move_up(event):
    canvas.move(myImage_for_canvas, 0, -10)


def move_left(event):
    canvas.move(myImage_for_canvas, -10, 0)


def move_down(event):
    canvas.move(myImage_for_canvas, 0, 10)


def move_right(event):
    canvas.move(myImage_for_canvas, 10, 0)


# --------------------------------------------------
window = Tk()
# --------------------------------------------------
myImage = ImageTk.PhotoImage(file="download.png")

# --------------------------------------------------
window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)
# --------------------------------------------------
canvas = Canvas(window,
                width=500,
                height=500)
canvas.pack()
# --------------------------------------------------
myImage_for_canvas = canvas.create_image(0, 0,
                                         image=myImage,
                                         anchor=NW)
# here we move our into usable image for canvas and
# we use ANCHOR for locking the image at top left corner
# --------------------------------------------------
window.mainloop()
