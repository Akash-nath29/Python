from tkinter import *
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox as tmsg
import pytube

root=Tk()
root.geometry('1000x500')
root.title('DownTube')
root.config(bg='#121212')

def download():
    path = asksaveasfilename(filetypes=[('Video','*.mp4')])
    try:
        link = url.get()
        yt = pytube.YouTube(link)
        stream = yt.streams.first()
        stream.download(path)
    except Exception as e:
        tmsg.showwarning('DownTube','Some Error Occured'+e)
        
    

Label(root,text='Enter video URL',bg='#121212',fg='#fff').pack(padx=10,pady=20)

url = StringVar()
Entry(root,textvariable=url,bg='#1d1b1f',fg='#fff',insertbackground='#fff',justify=CENTER).pack(padx=10,pady=20)

Button(root,text='Download',bg='#000',fg='#0daeff',command=download).pack(padx=10,pady=20)

root.mainloop()