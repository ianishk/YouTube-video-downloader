from pytube import YouTube
from tkinter import *

window = Tk()
window.title("youtube downloader")
window.geometry("600x200")

url = Label(window, text="Enter the url of the youtube video        : ", font=("Arial Bold", 10))
url.grid(column=0, row=0)

urlv = Entry(window, width=50)
urlv.grid(column=1, row=0)

path = Label(window, text="Enter the Destination path of the video: ", font=("Arial Bold", 10))
path.grid(column=0, row=1)

pathv = Entry(window, width=50)
pathv.grid(column=1, row=1)

def clicked():
    furl = str(urlv.get())
    fpath = str(pathv.get())
    YouTube(furl).streams.first().download(output_path=fpath)

dbtn = Button(window, text="Download", command=clicked)
dbtn.grid(column=1, row=2)

window.mainloop()
