from tkinter import *

# grid() = geometry manager that organizes widgets in a table-like structure
# in a parent

window = Tk()
#----------------------------------------------------------------------------
titleLabel = Label(window,
                   text="Enter your info",
                   font="Arial, 25").grid(row=0, column=0, columnspan=2)
#----------------------------------------------------------------------------
firstNameLabel = Label(window,
                       text="First name: ",
                       width=20,
                       bg="red").grid(row=1, column=0)
# the grid starts from the top left corner with index 0,0
firstNameEntry = Entry(window).grid(row=1, column=1)
# the entry will be in the right of the label with 0,1
#----------------------------------------------------------------------------
lastNameLabel = Label(window,
                      text="Last name: ",
                      bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2, column=1)
#----------------------------------------------------------------------------
emailLabel = Label(window,
                   text="Email: ",
                   bg="blue",
                   width=30).grid(row=3, column=0)
# here if width is 30, then the whole first column elements will
# accommodate to 30 unit
emailEntry = Entry(window).grid(row=3, column=1)
#----------------------------------------------------------------------------
submitButton = Button(window,
                      text="Submit",
                      ).grid(row=4, column=0, columnspan=2)
# column span=2 will make sure the the button is in between the first
# two columns
#----------------------------------------------------------------------------
window.mainloop()
