from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)
    # (1) in ms, and (2) do what function


# -----------------------------------------------
window = Tk()
# -----------------------------------------------
time_label = Label(window,
                   font=("Times New Roman", 50),
                   fg="#00FF00",
                   bg="black")
time_label.pack()
# -----------------------------------------------
day_label = Label(window,
                  font=("Times New Roman", 40),
                  fg="#00FF00",
                  bg="black")
day_label.pack()
# -----------------------------------------------
date_label = Label(window,
                   font=("Times New Roman", 45),
                   fg="#00FF00",
                   bg="black")
date_label.pack()
# -----------------------------------------------
update()
# -----------------------------------------------
window.mainloop()
