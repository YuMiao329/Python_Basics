from tkinter import *


def submit():
    input = text.get("1.0", END)
    print(input)


window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Times New Roman", 25),
            # the font size is correlated with the window size
            # so we also want to limit the window size while
            # the font size is also changed
            height=8,
            width=20,
            padx=20,
            # make the text area not close to the edges
            pady=20,
            fg="purple")
text.pack()

button = Button(window,
                text="submit",
                command=submit)
button.pack()

window.mainloop()
