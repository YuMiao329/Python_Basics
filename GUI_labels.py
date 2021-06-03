from tkinter import *
from PIL import ImageTk

# label =  an area widget that holds text and/or an image within a window

window = Tk()
# we pass window as the argument of Label
# this is as the container

photo = ImageTk.PhotoImage(file='download.png')

label = Label(window,
              text="Hello Bro",
              font=('Arial', 40, 'bold'),
              fg='green',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')  # fg is fore ground color, bg is background color
#                       relief is the border style, bd is the boarder size
#                       padx and pady sets the padding around text
#                       image inserts an image into this window
#                       compound sets the image below the text
label.pack()
# label.place(x=0, y=0)  # to set the widget on the upper left corner set x and y to 0
# label.place(x=100, y=100)  # to set the widget at set x and y to 100
window.mainloop()
