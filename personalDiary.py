from tkinter import *
import tkinter.messagebox as tmsg
from datetime import *
from PIL import Image , ImageTk
from time import strftime
from pickle import *

root = Tk()
root.geometry('1000x1800')
root.title('My Diary')
root.config(bg='#121212')

def addDiary():
    window = Tk()
    window.geometry('1000x1400')
    window.title('Add')
    window.config(bg='#121212')
    
    def add():
        diary=my_text.get('1.0','end-1c')
        text_to = '['+date.today().strftime('%d %B')+']'+'  '+diary
        my_listbox.insert(END,'¤'+'.  '+text_to)
        window.destroy()
        dump(my_listbox.get(0,my_listbox.size()),open('/storage/emulated/0/projects-python/personalDiary/diary.dat','wb'))
    
    current_time = strftime('%H:%M:%S')
    Label(window,text=(date.today().strftime("%d %B")+' '+current_time),bg='#121212',fg='#fff',font=('poppins',10,'bold')).pack(anchor = NW,padx=(10,350),pady=5)
    
    frame_text = Frame(window,bg='#121212')
    frame_text.pack(padx=10,pady=20)

    scrollbar=Scrollbar(frame_text,bg='#1d1b1f')
    scrollbar.pack(side=RIGHT,fill=Y)
    
    scrollbar_horizontal = Scrollbar(frame_text,orient="horizontal",bg='#1d1b1f')
    scrollbar_horizontal.pack(side=BOTTOM,fill=X)
    
    my_text = Text(frame_text,bg='#1d1b1f',fg='#fff',insertbackground='#fff',width=50,height=20,yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_horizontal.set)
    my_text.pack(padx=10,pady=10)
    
    scrollbar.config(command=my_listbox.yview)
    scrollbar_horizontal.config(command=my_listbox.xview)
    Button(window,text='Add',bg='#1d1b1f',fg='#c0eb34',command=add).pack(padx=10,pady=20)
    window.mainloop()

def dltDiary():
    removing_data=my_listbox.curselection()[0]
    my_listbox.delete(removing_data)
    tmsg.showinfo('My Diary','Memory removed !!')
    dump(my_listbox.get(0,my_listbox.size()),open('/storage/emulated/0/projects-python/personalDiary/diary.dat','wb'))
    
def reloadDiary():
    loading_diary=load(open('/storage/emulated/0/projects-python/personalDiary/diary.dat','rb'))
    for diary in loading_diary:
        my_listbox.insert(END,diary)
        
def seeDiary():
    see = Tk()
    see.geometry('1000x1300')
    see.title('My Diary')
    see.config(bg='#121212')
    
    
    frame_diary = Frame(see,bg='#121212')
    frame_diary.pack(padx=10,pady=20)
    
    scrollbar=Scrollbar(frame_diary,bg='#1d1b1f')
    scrollbar.pack(side=RIGHT,fill=Y)
    
    scrollbar_horizontal = Scrollbar(frame_diary,orient="horizontal",bg='#1d1b1f')
    scrollbar_horizontal.pack(side=BOTTOM,fill=X)
    
    my_diary = Text(frame_diary,bg='#121212' ,fg='#fff',insertbackground='#fff',width=50,height=20,wrap = WORD,yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_horizontal.set)
    my_diary.pack(padx=10,pady=10)
    
    scrollbar.config(command=my_diary.yview)
    scrollbar_horizontal.config(command=my_diary.xview)
    
    
    
    frame_button_seeDiary = Frame(see,bg='#121212')
    frame_button_seeDiary.pack(padx=10,pady=20)
    
    btn_ok = Button(frame_button_seeDiary,text='OK',bg='#121212',fg='#7bff08',activebackground ='#121212',activeforeground='#ff0000',command= see.destroy)
    btn_ok.grid(row=0,column=0,padx=(0,150),pady=20)
    
    btn_save = Button(frame_button_seeDiary, text='Save',bg='#121212',fg='#7bff08')
    btn_save.grid(row=0,column=1,padx=(150,0),pady=20)
    for i in my_listbox.curselection():
        my_diary.insert(1.0,my_listbox.get(i))
    if my_listbox.get(i) == my_diary.get(1.0,'end-1c'):
        btn_save.config(state=DISABLED)
    elif my_listbox.get(i)!=my_diary.get(1.0,'end-1c'):
        btn_save.config(state=NORMAL)
        
    see.mainloop()

frame_top = Frame(root,bg='#121212')
frame_top.pack(padx=10,pady=20)

Label(frame_top,text=date.today().strftime("%B-%d %A"),bg='#121212',fg='#fff',font=('poppins',10,'bold')).grid(row=0,column=0,padx=(0,100),pady=5)


frame_listbox = Frame(root,bg='#121212')
frame_listbox.pack(padx=10,pady=10)

scrollbar=Scrollbar(frame_listbox,bg='#1d1b1f')
scrollbar.pack(side=RIGHT,fill=Y)

scrollbar_horizontal = Scrollbar(frame_listbox,orient="horizontal",bg='#1d1b1f')
scrollbar_horizontal.pack(side=BOTTOM,fill=X)

my_listbox = Listbox(frame_listbox,bg='#1d1b1f',fg='#fff',width=50,height=20,yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_horizontal.set)
my_listbox.pack(padx=10,pady=10)

scrollbar.config(command=my_listbox.yview)
scrollbar_horizontal.config(command=my_listbox.xview)

btn_frame = Frame(root,bg='#121212')
btn_frame.pack(padx=10,pady=20)

btn_img = Image.open('/storage/emulated/0/Pictures/PicsArt/addButton2.png')

btn_photo = ImageTk.PhotoImage(btn_img)

btn_img2 = Image.open('/storage/emulated/0/Pictures/PhotoCompressor/dltButton.jpg')

btn_photo2 = ImageTk.PhotoImage(btn_img2)

btn_img3 = Image.open('/storage/emulated/0/Pictures/PhotoCompressor/reloadButton2.jpg')

btn_photo3 = ImageTk.PhotoImage(btn_img3)

btn_img4 = Image.open('/storage/emulated/0/Pictures/PhotoCompressor/seeDiary.jpg')

btn_photo4 = ImageTk.PhotoImage(btn_img4)

Button(btn_frame,image = btn_photo,width=140,height=140,borderwidth=0,bg='#121212',fg='#121212',activebackground='#121212',command = addDiary).grid(row=0,column=2,padx=(100,0),pady=20)

Button(frame_top,image=btn_photo3,bg='#121212',activebackground ='#121212',width=100,height=100,command=reloadDiary).grid(row=0,column=2,padx=(150,0),pady=20)

Button(btn_frame,image=btn_photo4,width=140,height=140,bg='#121212',fg='#121212',activebackground='#121212',command = seeDiary).grid(row=0,column=1,padx=(100,100),pady=20)

Button(btn_frame,image = btn_photo2,width=140,height=140,borderwidth=0,bg='#121212',fg='#121212',command=dltDiary).grid(row=0,column=0,padx=(0,100),pady=20)



root.mainloop()