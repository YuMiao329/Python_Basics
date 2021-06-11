from tkinter import *
from tkinter import ttk

window = Tk()
###################################
notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays
tab1 = Frame(notebook)  # new frame for tab 1
notebook.add(tab1, text="Tab 1")
tab2 = Frame(notebook)  # new frame for tab 2
notebook.add(tab2, text="Tab 2")
# ----------------------------------------------------
canvas = Canvas(tab1,
                height=500,
                width=500)

blueLine = canvas.create_line(0, 0,  # starting point
                              500, 500,  # ending point
                              fill="blue",
                              width=5)  # width here is the width of outline

redLine = canvas.create_line(500, 0,  # starting point
                             0, 500,  # ending point
                             fill="red",
                             width=5)

rectangle = canvas.create_rectangle(50, 50,  # one corner of rectangle
                                    250, 250)  # second corner of rectangle

polygon = canvas.create_polygon(250, 0,
                                500, 500,
                                0, 500,  # specify 3 points of polygon then it will become a triangle
                                fill="Yellow",
                                outline="black",
                                width=5)

arc = canvas.create_arc(0, 0,  # top left in the shape of rectangle surrounding circle
                        500, 500,  # bottom right in the shape of rectangle surrounding circle
                        fill="green",
                        style=PIESLICE,  # ARC, CHORD
                        start=180,  # start a 180 angle arc at point start=90 degree
                        extent=180,  # extent the arc with 180 degrees
                        )
canvas.pack()
# ----------------------------------------------------
canvas_poke = Canvas(tab2,
                     height=500,
                     width=500)
# red top hemisphere
canvas_poke.create_arc(0, 0,
                       500, 500,
                       fill="red",
                       extent=180,
                       width=10)
# white bottom hemisphere
canvas_poke.create_arc(0, 0,
                       500, 500,
                       fill="white",
                       extent=180,
                       start=180,
                       width=10)
# oval middle part
canvas_poke.create_oval(190, 190,
                        310, 310,
                        fill="white",
                        width=10)

canvas_poke.pack()
#-----------------------------------------------------
notebook.pack(expand=True)
# ----------------------------------------------------
window.mainloop()
