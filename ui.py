"""
pytube 9.0.6, Python 3

Creating a simple You Tube downloader with a simple progress indicator.progress indicator.

"""
# sample: https://www.youtube.com/watch?v=d3D7Y_ycSms

from pytube import YouTube
import os
from tkinter import *

window = Tk()
window.geometry('500x300')
window.resizable(0, 0)
window.title("youtube video downloader")

# Label(window, text ='Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()
# Label(window, text ='Paste Link Here:', font ='arial 15 bold').place(x= 160, y = 60)
link_enter = Entry(window, width = 45, textvariable = link).place(x = 35, y = 90)



# on_progress_callback takes 4 parameters.
def progress_Check(stream=None, chunk=None, file_handle=None, remaining=0):
    # Gets the percentage of the file that has been downloaded.
    percent = (100 * (file_size - remaining)) / file_size
    # Label(window, text="{:00.0f}% downloaded".format(percent), font='arial 20 bold').pack()
    print("{:00.0f}% downloaded".format(percent))


# Grabs the file path for Download
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


def start():
    # Label(window, text="Your video will be saved to: {}".format(file_path()), font='arial 20 bold').pack()
    print("Your video will be saved to: {}".format(file_path()))
    # Input
    yt_url = input("Copy and paste your YouTube URL here: ")
    # Label(window, text=yt_url, font='arial 20 bold').pack()
    print(yt_url)
    # Label(window, text="Accessing YouTube URL...", font='arial 20 bold').pack()
    print("Accessing YouTube URL...")

    # Searches for the video and sets up the callback to run the progress indicator.
    try:
        video = YouTube(yt_url, on_progress_callback=progress_Check)
    except:
        print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
        redo = start()

    # Get the first video type - usually the best quality.
    video_type = video.streams.filter(progressive=True, file_extension="mp4").first()

    # Gets the title of the video
    title = video.title

    # Prepares the file for download
    print("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    # Starts the download process
    video_type.download(file_path())

    print("Ready to download another video.\n\n")
    again = start()


file_size = 0
begin = start()

