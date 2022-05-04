from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import tkinter.messagebox as tmsg
from PIL import Image , ImageTk

root=Tk()
root.geometry("1000x1200")
root.title("NoteIt")
root.config(bg="#121212")
file_path=None

def set_file_path(path):
    global file_path
    file_path=path

def open_file():
    path=askopenfilename(filetypes=[('All','*.*'),('Text','*.txt'),('Python','*.py'),('HTML','*.html'),('Javascript','*.js'),('C','*.c'),('C++','*.c'),('C#','*.cs'),('Image','*.jpg')])
   # if path(filetype[('Image','*.jpg')]):#==('Image','*.jpg'):
#       img=ImageTk.PhotoImage(Image.open(path))
#       win=Tk()
#       win.geometry('500x500')
#       win.title(path)
#       def close():
#           root.destroy()
#       label=Label(image=img)
#       label.pack()
#       Button(win,text="Close",bg="black",fg="cyan",command=close)
#    else:
    with open(path,'r') as file:
        written_text=file.read()
        text_area.delete('1.0',END)
        text_area.insert('1.0',written_text)
        file.close()
        set_file_path(path)
    label1.config(text=path)

def clear_file():
    text_area.delete('1.0',END)
    label1.config(text="")

def save_file():
    if file_path==None:
        path=asksaveasfilename(filetypes=[('All','*.*'),('Text','*.txt'),('Python','*.py'),('HTML','*.html'),('Javascript','*.js'),('C','*.c'),('C++','*.c'),('C#','*.cs')])
    else:
        path=file_path
    with open(path,'w+') as file:
        saving_file=text_area.get('1.0',END)
        file.write(saving_file)
        file.close()
        set_file_path(path)
        label1.config(text=path)
    
#def save_as():
#    pass

def Exit():
    if file_path==None:
        ans=tmsg.askquestion("NoteIt","File isn't saved.Wanna save it ?")
        if ans=="yes":
            save_file()
        else:
            root.destroy()
    else:
        root.destroy()

def cut_text():
    text_area.event_generate(("<<Cut>>"))

def copy_text():
    text_area.event_generate(("<<Copy>>"))
    
def paste_text():
    text_area.event_generate(("<<Paste>>"))

def font_family():
    from tkinter import font
    def font_chooser(e):
        new_font=my_font.config(family=my_listbox.get(my_listbox.curselection()))
        text_area.config(font=new_font)
    my_font=font.Font()
    app=Tk()
    app.geometry('500x500')
    app.title('Fonts(Under development)')
    my_scrollbar=Scrollbar(app)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_listbox=Listbox(app,selectmode=SINGLE,yscrollcommand=my_scrollbar.set)
    my_listbox.pack()
    my_scrollbar.config(command=my_listbox.yview)
    for f in font.families():
        my_listbox.insert(END,f)
    my_listbox.bind('<ButtonRelease-1>',font_chooser)
    app.mainloop()

def help_user():
    tmsg.showinfo("NoteIt","You can use\n'Open' to open a file ,\n'New' to create new file ,\n'Save' to save existing files ,\n'Save As' to save new files ,\n'Clear' to clear texts ,\n'Exit' to exit NoteIt")

def about_us():
    tmsg.showinfo("NoteIt","NoteIt is a simple text editor made with \n Python by Akash Nath , 17 years old\nschool boy from India.\nHope you enjoyed it. Thank You")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

menubar=Menu(root)

#file menu
filemenu=Menu(menubar)

filemenu.add_command(label="Open",command=open_file)
filemenu.add_command(label="New",command=clear_file)
filemenu.add_command(label="Save",command=save_file)
filemenu.add_command(label="Save As",command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Clear",command=clear_file)
filemenu.add_command(label="Exit",command=Exit)

menubar.add_cascade(label="File",menu=filemenu)

#edit menu
editmenu=Menu(menubar)

editmenu.add_command(label="Cut",command=cut_text)
editmenu.add_command(label="Copy",command=copy_text)
editmenu.add_command(label="Paste",command=paste_text)
editmenu.add_separator()

editmenu.add_command(label="Font",command=font_family)

menubar.add_cascade(label="Edit",menu=editmenu)

#others menu
others=Menu(menubar)

others.add_command(label="Help",command=help_user)
others.add_command(label="About Us",command=about_us)
menubar.add_cascade(label="Others",menu=others)


root.config(menu=menubar)

my_font=('Helvetica',7)

text_area=Text(root,bg="#121212",fg="white",insertbackground="white",font=my_font,height=20,wrap=WORD, yscrollcommand=scrollbar.set)
text_area.pack(padx=30,pady=20,fill=BOTH, expand=True)

scrollbar.config(command=text_area.yview)

label1=Label(root,bg="#ffffff",fg="black",wraplength=800)
label1.pack(padx=30,pady=10,fill=X,side=BOTTOM)

#label2=Label(root,bg="white",fg="white")
#label2.pack(side=LEFT,fill=Y)

root.mainloop()