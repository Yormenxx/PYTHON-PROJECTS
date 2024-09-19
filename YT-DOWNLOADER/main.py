import shutil
from tkinter import *
from tkinter import filedialog

from PIL import ImageTk, Image
from moviepy.editor import VideoFileClip
from pytube import YouTube
import os
root = Tk()

root.title("Youtube downloader")

root.geometry("800x600")

root.config(bg="gray11")

root.iconbitmap("yt.ico")


def select_path():
    path = filedialog.askdirectory()
    path_down.config(text=path)


def download_file():



    url = str(input("url:- "))
    user_path = YouTube(url)
    root.title('Downloading...')

    mp4_video = user_path.streams.filter(only_audio=True).first()
    downloaded_file = mp4_video.download()
    base, ext = os.path.splitext(downloaded_file)

    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    root.title('Download Complete! Download Another File...')


lbl_img = Image.open("youtube-logo-9.png")
lbl_img = lbl_img.resize((400, 100))

img = ImageTk.PhotoImage(lbl_img)

lbl_img = Label(root, image=img)
lbl_img.pack(pady=50)

link_input = Entry(root, width=100, bd=2)
link_input.pack()

link_campo = Label(root, text="Ingrese la URL del video a descargar", font=('Arial', 15), fg="white", bg="gray11")
link_campo.pack(pady=30)

path_down = Label(root, text="Selecciona la ruta para almacenar el video", font=('Arial', 20), fg="white", bg="gray11")
path_down.pack()

btn1 = Button(root, text="Inspeccionar ruta", width=30, borderwidth=3, font=('Arial', 13), command=select_path)
btn1.pack(pady=20)

btn2 = Button(root, text="DESCARGAR", width=30, borderwidth=3, font=('Arial', 13), fg="red", command=download_file)
btn2.pack(pady=20)



root.mainloop()
