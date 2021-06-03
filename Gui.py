from tkinter import *
from pytube import YouTube
import os




window = Tk()
window.geometry('500x500')
window.resizable(0, 0)
window.title("youtube video downloader")

Label(window, text='Youtube Video Downloader', font='arial 20 bold').pack()

link = StringVar()
Label(window, text='Paste Link Here:', font='arial 15 bold').pack()
ready = Label(window, text="", font='arial 15 bold')
link_enter = Entry(window, width=45, textvariable=link).pack()


sb = Scrollbar(window)
sb.pack(side=RIGHT, fill=BOTH)
myDownloads = Listbox(window, yscrollcommand=sb.set)
myDownloads.insert(END, "YOUR DOWNLOADS:")




def progress_Check(stream=None, chunk=None, file_handle=None, remaining=None):
    # Gets the percentage of the file that has been downloaded.
    percent = (100 * (file_size - remaining)) / file_size
    # myDownloads.insert(END, "{:00.0f}% downloaded".format(percent))
    # Label(window, text="{:00.0f}% downloaded".format(percent), font='arial 20 bold').pack()
    # print("{:00.0f}% downloaded".format(percent))

# Grabs the file path for Download
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path

# myDownloads.insert(END, "\nYour video will be saved to: {}".format(file_path()))
Label(window, text="Your video will be saved to: {}".format(file_path()), font='arial 15 bold').pack()

def start():
    # Label(window, text="Your video will be saved to: {}".format(file_path()), font='arial 15 bold').pack()
    # print("Your video will be saved to: {}".format(file_path()))
    # Input
    # Label(window, text="Copy and paste your YouTube URL here: ", font='arial 15 bold').pack()
    yt_url = link
    # Label(window, text=yt_url, font='arial 20 bold').pack()
    # print(yt_url)

    # Label(window, text="Accessing YouTube URL...", font='arial 10 bold').pack()
    # print("Accessing YouTube URL...")

    # Searches for the video and sets up the callback to run the progress indicator.

    try:
        video = YouTube(yt_url.get(), on_progress_callback=progress_Check)

        # Get the first video type - usually the best quality.
        video_type = video.streams.filter(progressive=True, file_extension="mp4").first()

        # Gets the title of the video
        title = video.title

        # Prepares the file for download
        myDownloads.insert(END, "Fetching: {}...".format(title))
        myDownloads.insert(END, "100% downloaded")
        # Label(window, text="Fetching: {}...".format(title), font='arial 10 bold').pack()
        # print("Fetching: {}...".format(title))
        global file_size
        file_size = video_type.filesize
        # Starts the download process
        video_type.download(file_path())

        ready.config(text="Ready to download another video.\n\n", font='arial 15 bold', fg="blue")
        ready.pack()
        # myDownloads.insert(END, "Ready to download another video.\n\n")
        # print("Ready to download another video.\n\n")

    except:
        error.config(text="ERROR. Check your connection or url. \nPlease try again.", font='arial 15 bold', fg="red")
        error.pack()
        ready.config(text="")
        # "ERROR. Check your connection or url. Please try again."
        # myDownloads.insert(END, "ERROR. Check your connection or url. Please try again.")
        # print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
        # start()
def removeLabel():
    if error != None:
        error.config(text="")

def combinedCommands():
    removeLabel()
    start()




Button(window, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2, command=combinedCommands).pack()

myDownloads.pack()
# sb.config(command=myDownloads.yview)
error = Label(window, text="", font='arial 10 bold')


window.mainloop()