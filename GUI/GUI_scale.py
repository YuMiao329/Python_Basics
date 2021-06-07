from tkinter import *
from PIL import ImageTk

window = Tk()

hotImg = ImageTk.PhotoImage(file="hotdog.jpg")
hotLabel = Label(image=hotImg)
hotLabel.pack()


def submit_temp():
    print("The temperature is: " + str(scale.get()) + " degrees C")


scale = Scale(window,
              from_=100, to=0,
              length=100,  # set the length of the scale bar
              orient=VERTICAL,  # could be set as horizontal (orientation of the scale bar)
              font=("Times New Roman", 20),
              tickinterval=10,  # numerical indicator of the scale intervals
              # showvalue=0,  # hide current value if show value=0#
              resolution=5,  # set the step of increment
              troughcolor="#69EAFF",  # set the bar trail to specific color
              fg="#FF1C00",  # set the font color
              bg="#111111",  # set the background color

              )

scale.set(50)  # set the initial scale value to 50
scale.set((scale["from"] - scale["to"]) / 2 + scale["to"])  # (generalize) set the initial scale value to the middle of
# the scale bar/value


scale.pack()

coldImg = ImageTk.PhotoImage(file="download.png")
coldLabel = Label(image=coldImg)
coldLabel.pack()

button = Button(window,
                text="submit",
                command=submit_temp,
                )

button.pack()
window.mainloop()
