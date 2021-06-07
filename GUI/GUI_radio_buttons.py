# radio button =  similar to check box, but you can only select one from a group

from tkinter import *
from PIL import ImageTk

food = ["pizza", "hamburger", "hotdog"]


def orderfood():
    if x.get() == 0:
        print("You ordered pizza")
    elif x.get() == 1:
        print("You ordered a hamburger")
    elif x.get() == 2:
        print("You ordered a hotdog")
    else:
        print("What")


window = Tk()

pizzaImg = ImageTk.PhotoImage(file="pizza.jpg")
hamburgerImg = ImageTk.PhotoImage(file="hamburger.jpg")
hotdogImg = ImageTk.PhotoImage(file="hotdog.jpg")

foodImg = [pizzaImg, hamburgerImg, hotdogImg]

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],  # adds text to radio buttons
                              variable=x,  # group radiobuttons together if they share the same value
                              value=index,  # this assigns each radiobutton a different value
                              padx=25,  # adds padding on x axis
                              font=("Impact", 50),
                              image=foodImg[index],  # add images to radio buttons
                              compound="left",  # adds image with texts
                              indicatoron=0,  # this will eliminate circle indicators
                              width=1000,  # this sets width of radio button
                              command=orderfood  # this will create a call back with each button push to
                              # the orderfood function.
                              # Remember: orderfood function callback don't have ()
                              )

    # we need to give each a unique variable value
    # otherwise, they all have same value and all will be selected
    # default is 0

    radiobutton.pack(anchor=W)  # anchor=W will align then to the left

window.mainloop()
