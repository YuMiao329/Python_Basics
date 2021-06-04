from tkinter import *
from PIL import ImageTk

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("420x420")  # setting size of the window
window.title("Bro Code first GUI program")  # change title of the window

icon = ImageTk.PhotoImage(file='download.png')  # change the image into an usable icon
window.iconphoto(True, icon)  # setting the image into the icon
window.config(background="black")  # setting the background color
# you could also set HEX color from google:
# window.config(background="#5cfcff")
window.mainloop()  # place window on computer screen, listen for events
