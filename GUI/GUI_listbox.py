# listbox = A listing of selectable text item within
# it's own container

from tkinter import *
from PIL import ImageTk

window = Tk()


def submit():
    food = []

    for index in listbox.curselection():
        print(index)
        food.insert(index, listbox.get(index))
        # this will add the item from listbox at index: index
        # to the food array at index: index
    print("You have ordered: ")

    for index in food:
        print(index)
    # print("You have ordered:", listbox.get(listbox.curselection()))
    # This is for single selection (selectmode=SINGLE)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    # here, we insert at the index of listbox,size()
    # because if there are 5 items, the size will be 5
    # but the last index will be 4 (because index starts from 0)
    # Now the listbox.size will increase by one to be 6
    listbox.config(height=listbox.size())
    # here, we resize the box size by setting it as size of 6


def delete():
    # listbox.delete(listbox.curselection())
    # This is for single selection (selectmode=SINGLE)
    for index in reversed(listbox.curselection()):
        # here we add reversed before the listbox.curselection()
        # is because if no reversed, the listbox will change size
        # at each run, and the index will be mismatched
        # add reversed is to delete from bottom to top so
        # the upper indexes will not be changed after each deletion
        listbox.delete(index)

    listbox.config(height=listbox.size())


listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, "pizza")  # insert "pizza" at the first position in the list box
listbox.insert(2, "garlic bread")
listbox.insert(3, "chicken")
listbox.insert(4, "soup")
listbox.insert(5, "spaghetti")

listbox.config(height=listbox.size())
# this will make the height of listbox to be as consistent with
# the contents available inside of the listbox

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,
                      text="Submit",
                      command=submit)
submitButton.pack()

addButton = Button(window,
                   text="add",
                   command=add)
addButton.pack()

deleteButton = Button(window,
                      text="delete",
                      command=delete)
deleteButton.pack()

print(listbox.size())
window.mainloop()
