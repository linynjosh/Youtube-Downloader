from tkinter import *
from pytube import YouTube





window = Tk()
window.geometry('500x300')
window.resizable(0, 0)
window.title("youtube video downloader")

Label(window, text ='Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()
Label(window, text ='Paste Link Here:', font ='arial 15 bold').place(x= 160, y = 60)
link_enter = Entry(window, width = 45, textvariable = link).place(x = 35, y = 90)


def Downloader():
    yt = YouTube(str(link.get()))
    yt.captions.all()
    video = yt.streams.first()

    video.download()
    label = Label(window, text='DOWNLOADED', font='arial 15')
    label.place(x=180, y=210)


Button(window, text ='DOWNLOAD', font ='arial 15 bold', bg ='pale violet red', padx = 2, command = Downloader).place(x=180, y = 150)
window.mainloop()