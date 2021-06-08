from tkinter import *
from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Python_Basics\\GUI",
                                          title="Open file okay?",
                                          filetypes=(("text files", "*0txt"),
                                                     ("all files", "*.*")))
    # You can set initial directory for file open
    # you can also include type of files

    file = open(filepath, "r")
    # "r" means read which is the same as "rt" which is read text
    print(file.read())
    file.close


window = Tk()
button = Button(text="open",
                command=openFile)
button.pack()
window.mainloop()
