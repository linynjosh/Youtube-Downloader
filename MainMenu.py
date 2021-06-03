from tkinter import *

window = Tk()

window.title("My App")

window.geometry('350x200')

label = Label(window, text="Welcome!", font=("Arial Bold", 20))
label.grid(column=0, row=0)

def clicked():
    label.configure(text="Downloading...")

text = Entry(window, width=10)
text.grid(column=20, row=60)

button1 = Button(window, text="Youtube Downloader", fg="blue", command=clicked)
button1.grid(column=20, row=20)

button2 = Button(window, text="Web Scrapper", bg="orange", fg="blue")
button2.grid(column=20, row=40)

window.mainloop()
