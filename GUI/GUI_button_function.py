from tkinter import *
from PIL import ImageTk

count = 0


def click():
    global count  # set this as global because every time the execution
    #               the count number will come back to the main as increment
    count += 1
    print("You clicked the button!", count, " times")


window = Tk()
photo = ImageTk.PhotoImage(file="download.png")
# add several parameters onto the button function
button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")

# make activeforeground is the same as the fg and
# make activebackground is the same as the bg
# so every click won't change the color of the text and the background

button.pack()

window.mainloop()
