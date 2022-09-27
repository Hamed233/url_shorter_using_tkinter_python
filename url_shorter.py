#### STEPS:
   ## 1) Import modules (pyshorteners, tkinter)
   ## 2) Design app using "tkinter" module
   ## 3) Create main function to convert url using "pyshorteners" modules

import pyshorteners
from tkinter import *

def converterFunction():
    typeTiny = pyshorteners.Shortener()
    longUrl = entryBox.get()
    shortUrl = typeTiny.tinyurl.short(longUrl)
    print(shortUrl)
    entryBox.delete(0, END)
    entryBox.insert(0, shortUrl)

gui = Tk()
gui.geometry("400x200")
gui.title("URL Shorter")

titleLabel = Label(gui, text="URL Shorter", fg="blue", font=("Century", 20, "bold"))
titleLabel.pack(pady=20)

entryLabel = Label(gui, text="Enter URL: ", font=("Century", 10))
entryLabel.pack(anchor="w")

entryBox = Entry(gui, width=43, font=("Century", 12))
entryBox.pack()
btn = Button(gui, text="Convert", command=converterFunction, bg="blue", fg="white", font=("Century", 15, "bold"), height=1, width=10)
btn.pack(pady=12)

gui.mainloop()