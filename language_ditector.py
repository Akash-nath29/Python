from tkinter import *
from langdetect import detect
from langcodes import *

root = Tk()
root.geometry('1000x800')
root.title('DetectLang')
root.config(bg='#121212')

def check():
    if my_text.compare('end-1c', '==', '1.0'):
        my_label.config(text='Hey !! Put some text in textbox')
    else:
        code = detect(my_text.get('1.0' ,END))
        my_result = Language.make(language=code).display_name()
        my_label.config(text=f'Your text is {my_result}')

my_text=Text(root,bg='#1d1b1f',fg='#fff',insertbackground='#fff',width=50,height=10)
my_text.pack(padx=10,pady=20)

Button(root,text='Check',bg='#000',fg='#42d4f5',command=check).pack(padx=20,pady=20)

my_label = Label(root,text='',bg='#121212',fg='#fff')
my_label.pack(padx=10,pady=20)

root.mainloop()