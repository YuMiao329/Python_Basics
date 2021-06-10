from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 200
    download = 0
    speed = 1  # could be interpreted as 1ms/time unit
    while download < GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB) * 100
        # this will increase the percent with each occurrence

        download += speed
        # this will increase the download with the speed

        percent.set(str(int((download / GB) * 100)) + "%")
        # you could set stringVar with a string
        # just like the form of print() function

        text.set(str(download) + "/" + str(GB) + " GB completed")

        window.update_idletasks()
        # this will update the progress bar for each
        # time delay


# ------------------------------------------------------------------
window = Tk()
# ------------------------------------------------------------------
percent = StringVar()
text = StringVar()
# ------------------------------------------------------------------
bar = Progressbar(window,
                  orient=HORIZONTAL,
                  # you can also change this to vertical form
                  length=300)
bar.pack(pady=10)
# you have to put bar.pack in a new line here
# ------------------------------------------------------------------
percentLabel = Label(window,
                     textvariable=percent).pack()
# text_variable will update the text for each iteration
# ------------------------------------------------------------------
taskLabel = Label(window,
                  textvariable=text).pack()
# ------------------------------------------------------------------
button = Button(window,
                text="download",
                command=start).pack()
# ------------------------------------------------------------------
window.mainloop()
