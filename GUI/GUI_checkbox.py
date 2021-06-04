from tkinter import *
from PIL import ImageTk


def display():
    if x.get():
        print("You bought it!")
    else:
        print("You missed it!")


window = Tk()
photo = ImageTk.PhotoImage(file="download.png")

#x = IntVar() use this if the on value and off value is integer
x = BooleanVar()

check_button = Checkbutton(window,
                           text="I will buy it!",
                           variable=x,  # set variable x to represent the states
                           onvalue=True,  # assign the x a value (integer or anything else) once checked
                           offvalue=False,  # assign the x a value (integer or anything else) once unchecked
                           command=display,  # callback function once check/uncheck
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,  # leave 25 unit of spaces in x direction
                           pady=10,  # leave 10 unit of spaces in x direction
                           image=photo,
                           compound="left")

check_button.pack()
window.mainloop()
