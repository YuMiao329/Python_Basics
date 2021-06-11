from tkinter import *


def drag_start(event):
    widget = event.widget
    # set the individual widget as the widget function
    # so when click each one, it will not change the other one
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    # calculate dragged x position
    # as moves, event.x will change either +/- 1.
    # x then quickly update its x position into a new x
    # and assign x to label x position
    y = widget.winfo_y() - widget.startY + event.y
    # calculate dragged y position
    widget.place(x=x, y=y)


# ---------------------------------------
window = Tk()
# ---------------------------------------
label = Label(window,
              bg="red",
              width=10,
              height=5)
label.place(x=0, y=0)

# label.bind(event, function)
label.bind("<Button-1>",
           drag_start)
label.bind("<B1-Motion>",
           drag_motion)
# ---------------------------------------
label2 = Label(window,
               bg="blue",
               width=10,
               height=5)
label2.place(x=10, y=10)

label2.bind("<Button-1>",
            drag_start)
label2.bind("<B1-Motion>",
            drag_motion)
# ---------------------------------------
window.mainloop()
