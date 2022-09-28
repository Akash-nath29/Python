from tkinter import *
from tkinter.filedialog import asksaveasfilename
import qrcode
from PIL import ImageTk , Image

root= Tk()
root.geometry('1000x800')
root.title('QRCode Maker')
root.config(bg='#121212')

def create():
    
    data_QR = data.get()
    
    img = qrcode.make(data_QR)
    
    path=asksaveasfilename(filetypes=[('Image','*.jpg'),('All','*.*')])
    
    img.save(path)
    
    image = Image.open(path)
    
    photo = ImageTk.PhotoImage(image)
    
    label_image.config(image=photo,width=5000,height=5000)
    

Label(root,text='Enter what you wanna put in your QRCode',bg='#121212',fg='#fff').pack(side=TOP,padx=10,pady=20)

data=StringVar()

Entry(root,textvariable=data,bg='#1d1b1f',fg='#fff' ,justify=CENTER,insertbackground='#fff').pack(padx=10,pady=20)

Button(root,text='Create',bg='#000',fg='#3ef1f7',command=create).pack(padx=10,pady=20)

label_image = Label(root,bg='#121212')
label_image.pack(padx=10,pady=20)

root.mainloop()