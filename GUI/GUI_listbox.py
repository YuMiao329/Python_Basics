# listbox = A listing of selectable text item within
# it's own container

from tkinter import *
from PIL import ImageTk

window = Tk()

listbox = Listbox(window,
                  )
listbox.pack()

listbox.insert(1, "pizza")  # insert "pizza" at the first position in the list box
listbox.insert(2, "garlic bread")
listbox.insert(3, "chicken")
listbox.insert(4, "soup")
listbox.insert(5, "spaghetti")


window.mainloop()