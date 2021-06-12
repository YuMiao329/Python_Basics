from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,
                width=WIDTH,
                height=HEIGHT)
canvas.pack()
# (self, canvas, x, y, diameter, xVelocity, yVelocity, color):
volley_ball = Ball(canvas, 0, 0, 100, 3, 1, "white", 0)
tennis_ball = Ball(canvas, 0, 0, 100, 14, 3, "yellow", 0)
while True:
    volley_ball.move()
    tennis_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
