from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)  # widget that manages a collection of windows/displays

# --------------------------------------------------------------------------------------
tab1 = Frame(notebook)  # new frame for tab 1
notebook.add(tab1, text="Tab 1")
Label(tab1, text="Hello, this is tab 1", width=50, height=25).pack()

# --------------------------------------------------------------------------------------
tab2 = Frame(notebook)  # new frame for tab 2
notebook.add(tab2, text="Tab 2")
Label(tab2, text="Hello, this is tab 2", width=50, height=25).pack()

# --------------------------------------------------------------------------------------
notebook.pack(expand=True)
# expand = expand to fill any space not otherwise used # here stays in the center
# fill = will fill space on x and y axis # will normalize the units with tabs in fixed place

window.mainloop()
