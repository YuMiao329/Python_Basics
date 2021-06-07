from tkinter import *
from tkinter import messagebox

# import messagebox library

window = Tk()


def click():
    messagebox.showinfo(title="This is an info message box",
                        message="You are a person")
    # while(True):
    #    messagebox.showwarning(title="WARNING",
    #                        message="You have a virus!")

    messagebox.showerror(title="error box",
                         message="Something is wrong")

    if messagebox.askokcancel(title="ask ok cancel",
                              message="do you want to do the thing"):
        print("You did a thing!")
    else:
        print("You canceled a thing!")

    if messagebox.askretrycancel(title="ask retry cancel",
                                 message="do you want retry the thing"):
        print("You retried a thing!")
    else:
        print("You canceled a thing!")

    if messagebox.askyesno(title="ask yes / no",
                           message="Do you like cake?"):
        print("I like cake too!")
    else:
        print("Why do you not like cake?")

    answer = messagebox.askquestion(title="ask question",
                                    message="Do you like pie?")
    if answer == "yes":
        print("I like pie too!")
    else:
        print("Why do you not like pie?")


button = Button(window,
                command=click,
                text="Click me")
button.pack()

window.mainloop()
