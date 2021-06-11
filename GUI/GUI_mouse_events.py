from tkinter import *


def doSomething(event):
    print(str(event.num) + "# mouse coordinates " + str(event.x) + "," + str(event.y))


def releaseMouse(event):
    print(str(event.num) + "# mouse released coordinates " + str(event.x) + "," + str(event.y))


def whereEnter(event):
    print("Mouse entered from coordinates " + str(event.x) + "," + str(event.y))


def whereLeave(event):
    print("Mouse left to coordinates " + str(event.x) + "," + str(event.y))


def inMotion(event):
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))


window = Tk()

# window.bind(event, function)
window.bind("<Button-1>", doSomething)  # left mouse click
window.bind("<Button-2>", doSomething)  # scroll wheel
window.bind("<Button-3>", doSomething)  # right mouse click
window.bind("<ButtonRelease>", releaseMouse)  # right mouse click
window.bind("<Enter>", whereEnter)  # where the mose first entered the place
window.bind("<Leave>", whereLeave)  # where the mose left to the place
window.bind("<Motion>", inMotion)  # where the mose left to the place

window.mainloop()
