from pytube import YouTube
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def download_mp3():
    try:
        yt = YouTube(youtube_url.get())
        streams = yt.streams.filter(only_audio=True).first()
        streams.download(filename=f"{yt.title}.mp3", output_path=directory)
        fail_success.configure(text='Download Successful', foreground='green')
    except:
        fail_success.configure(text='Download Failed', foreground='red')


def download_mp4():
    try:
        yt = YouTube(youtube_url.get())
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=directory)
        fail_success.configure(text='Download Successful', foreground='green')
    except:
        fail_success.configure(text='Download Failed', foreground='red')


def get_dir():
    path = filedialog.askdirectory()
    write_path = open('Youtube_Directory.txt', 'w')
    write_path.write(f'{path}')
    write_path.close()
    dir_var = open('Youtube_Directory.txt', 'r')
    current_path = dir_var.read()
    dir_var.close()
    dir_text.configure(text=f'Current Directory: {current_path}')
    if current_path:
        fail_success.configure(text='')


# window
window = tk.Tk()
window.title('Youtube to mp3/mp4')
window.geometry('490x150')

# title
title_display = ttk.Label(master=window, text='Please enter a Youtube url', font='Calibri 24 bold')
title_display.grid(row=0)

# user input
input_frame = ttk.Frame(master=window)
input_frame.grid(row=4)

# entry field
youtube_url = tk.StringVar()
url_entry = ttk.Entry(width=50, master=input_frame, textvariable=youtube_url)
url_entry.grid(row=0, column=0, padx=10)
# mp3 download button
mp3_button = ttk.Button(master=input_frame, text='mp3', command=download_mp3)
mp3_button.grid(row=0, column=1)
# mp4 download button
mp4_button = ttk.Button(master=input_frame, text='mp4', command=download_mp4)
mp4_button.grid(row=0, column=2)

# directory
try:
    current_dir = open('Youtube_Directory.txt', 'r')
    directory = current_dir.read()
    current_dir.close()
except:
    current_dir = open('Youtube_Directory.txt', 'x')
    current_dir.close()
    current_dir = open('Youtube_Directory.txt', 'r')
    directory = current_dir.read()
    current_dir.close()

dir_text = ttk.Label(master=window, text=f'Current Directory: {directory}')
dir_button = ttk.Button(master=window, text='Directory', command=get_dir)
dir_text.grid(row=5)
dir_button.grid(row=6)

# fail/success label
fail_success = ttk.Label(master=window, text='')
fail_success.grid(row=2)
if directory == '':
    fail_success.configure(text='Please Select a Directory', foreground='orange')

# run
window.mainloop()
