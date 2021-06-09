# frame = a rectangular container to group and hole widgets

from tkinter import *

window = Tk()

# button = Button(window,
#                text="W",
#                font=("Consolas", 25),
#                width=3)
# button.pack()

# to put every button into the frame so the size of buttons will not flow around
frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
# relief is the boarder of the frame
frame.pack(side=BOTTOM)
# set the frame to the bottom of the window
#frame.place(x=100, y=100)
# set the frame with units relative to the upper left corner


# Create each button if no need to specify name
Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
# Put ASD in a line from the left direction to the right
Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

window.mainloop()
