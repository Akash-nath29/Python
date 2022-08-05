from tkinter import *
from datetime import *
import tkinter.messagebox as tmsg
from PIL import Image , ImageTk
from pickle import *

root = Tk()
root.geometry('1000x1600')
root.title('Task Planner')
root.config(bg = '#121212')
score = 0
def add_task_one():
    
    window = Tk()
    window.geometry('1000x800')
    window.config(bg='#121212')
    window.title('Add Task')
    
    def add_task_two():
        global score
        data = my_text.get('1.0','end-1c')
        if data!='':
            now=datetime.now()
            time=now.strftime("%H:%M:%S")
            
            my_listbox.insert(END,'¤'+' ['+time+'] '+data)
            window.destroy()
            my_label.config(text=f'{my_listbox.size()} tasks here , {score} tasks deleted')
            dump(my_listbox.get(0,my_listbox.size()),open('/storage/emulated/0/pythonprojects.py/TaskPlannerVersion2.0/task.dat','wb'))
        else:
            tmsg.showwarning('Warning','Enter a Task to Add')
            
    Label(window,text='Enter Task in a few words',bg='#121212',fg='#fff').pack(padx=10,pady=20)
    
    my_text = Text(window,bg='#121212',fg='#fff',insertbackground='#fff',height=10)
    my_text.pack(padx=10,pady=20)
    
    Button(window,text='Add',bg='#1af053',fg='#000',command = add_task_two).pack(padx=10,pady=20)
    window.mainloop()
def dlt_task():
    try:
        global score
        removing_data=my_listbox.curselection()[0]
        my_listbox.delete(removing_data)
        tmsg.showinfo('Task Planner','Task removed !!')
        dump(my_listbox.get(0,my_listbox.size()),open('/storage/emulated/0/pythonprojects.py/TaskPlannerVersion2.0/task.dat','wb'))
        score+=1
        if my_listbox.size() == 0:
            my_label.config(text='Nothing here')
            
        else:
            my_label.config(text=f'{my_listbox.size()} tasks here ,{score} tasks deleted')
    except:
        tmsg.showwarning('Warning','Select a Task to Remove')
        
def reload_tasks():
    loading_task=load(open('/storage/emulated/0/pythonprojects.py/TaskPlannerVersion2.0/task.dat','rb'))
    for tasks in loading_task:
        my_listbox.insert(END,tasks)
         
        
frame_time_and_reload = Frame(root,bg='#121212')
frame_time_and_reload.pack(padx=10)

ph_img = Image.open('/storage/emulated/0/Pictures/PicsArt/reload_button.jpg')
reload_img = ImageTk.PhotoImage(ph_img)

Label(frame_time_and_reload,text=date.today().strftime("%B-%d %A"),bg='#121212',fg='#fff',font=('poppins',10,'bold')).grid(row=0,column=0,padx=(0,250),pady=5)

Button(frame_time_and_reload,image = reload_img,command=reload_tasks).grid(row=0,column=1,padx=(10,0),pady=20)

frame_listbox = Frame(root,bg='#121212')
frame_listbox.pack(padx=10,pady=20)

scrollbar=Scrollbar(frame_listbox,bg='#1d1b1f')
scrollbar.pack(side=RIGHT,fill=Y)

scrollbar_horizontal = Scrollbar(frame_listbox,orient="horizontal",bg='#1d1b1f')
scrollbar_horizontal.pack(side=BOTTOM,fill=X)

my_listbox = Listbox(frame_listbox,bg='#1d1b1f',fg='#fff',width=50,height=20,yscrollcommand=scrollbar.set,xscrollcommand=scrollbar_horizontal.set)
my_listbox.pack(padx=10,pady=10)

scrollbar.config(command=my_listbox.yview)
scrollbar_horizontal.config(command=my_listbox.xview)

frame_buttons = Frame(root,borderwidth=10,bg='#121212')

frame_buttons.pack(padx=10,pady=20)

Button(frame_buttons,text='Add Task',bg='#1af053',fg='#000',command=add_task_one).grid(row=0,column=0,padx=10,pady=20)

Button(frame_buttons,text='Delete Task',bg='#f01a1a',fg='#fff',command=dlt_task).grid(row=0,column=1,padx=10,pady=20)

my_label = Label(root,text='No Task here' ,bg='#1e2126',fg='#fff',font=('Helvetica',7))
my_label.pack(padx=10,pady=20)

root.mainloop()