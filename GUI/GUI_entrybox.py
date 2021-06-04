from tkinter import *

window = Tk()


def submit():
    username = entry.get()
    print("Hello", username)
    # after submit user name: disable the entry box:
    # entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


# -------------------------------------
entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")
# show="*" only shows * when typing but the internal text will not change

# to initialize the initial text entry once opened
#entry.insert(0, "Spongebob")
entry.pack(side=LEFT)
# -------------------------------------
submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side=RIGHT)
# -------------------------------------
delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack(side=RIGHT)
# -------------------------------------
backspace_button = Button(window,
                          text="backspace",
                          command=backspace)
backspace_button.pack(side=RIGHT)
# -------------------------------------

window.mainloop()
