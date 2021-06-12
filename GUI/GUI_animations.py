from tkinter import *
from PIL import ImageTk
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2
# set constant values as CAPITAL LETTERS
# ---------------------------------------------------------------------
window = Tk()
# ---------------------------------------------------------------------
canvas = Canvas(window,
                width=WIDTH,
                height=HEIGHT)
canvas.pack()
# ---------------------------------------------------------------------
# get the background image
bg_image = ImageTk.PhotoImage(file="hamburger.jpg")
mybg_image = canvas.create_image(0, 0,  # set coordinates where the image will appear in the canvas
                               image=bg_image,
                               anchor=NW)
# get the moving image
photo_image = ImageTk.PhotoImage(file="hotdog.jpg")
my_image = canvas.create_image(0, 0,  # set coordinates where the image will appear in the canvas
                               image=photo_image,
                               anchor=NW)  # make sure the image does not go out side of the canvas
# set make canvas usable image
image_width = photo_image.width()
image_height = photo_image.height()
# ---------------------------------------------------------------------
# while the console runs, it executes followings:
while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    # here if the x coords is larger or equal to to the x-axis boundary
    # or if the x coords is smaller than 0,
    # we reverse the x velocity to let if bounce back
    # since initial x coords is 0, we could not let
    # coordinates[0] <= 0. Or it will not move forward.
    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        # here we make sure if the right portion of image hit the right end of
        # boundary, it will bounce back
        xVelocity = -xVelocity
    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        # here we make sure if the bottom portion of image hit the bottom end of
        # boundary, it will bounce back
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)
# ---------------------------------------------------------------------
window.mainloop()
