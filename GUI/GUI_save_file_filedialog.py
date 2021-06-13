from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="D:\\Python_Basics\\GUI",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])

    if file is None:
        return
    # include this statement because if we exit in the middle
    # of selecting saving location, there will be no more
    # error message shown in the command window.

    # create empty file in the selected directory
    file_text = str(text.get(1.0, END))
    # file_text = input("Enter some text: ")
    # this could change file text from the text area to console area

    file.write(file_text)
    file.close()


window = Tk()
button = Button(text="save",
                command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
