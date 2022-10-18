from tkinter import *
from pytube import YouTube
import os
from tkinter import filedialog
url=""
def downloader():
	label.config(text = "")
	url= e.get()
	yt_vid = YouTube(url).streams.filter(progressive=True)
	yt_vid.order_by('resolution').desc().first().download()
	label.config(text = "video indirildi")
	print("video indirildi")


root = Tk()
root.title("YouTube Downloader")
root.geometry("950x100")

label=Label(root, text="YouTube Video Linki : ")
label.grid(row=0, column=0,  padx=1, pady=8)
e= Entry (root, width=85, borderwidth=2)
e.grid(row=0, column=3, columnspan=3, padx=1, pady=8)

label=Label(root, text="", fg='green')
label.grid(row=1, column=0,  padx=1, pady=8)

button_yolla = Button(root, text="Video İndir", padx=1, pady=1,width=30, command=downloader).grid(row=1, column=5, padx=1, pady=1)


root.mainloop()
