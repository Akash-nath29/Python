from tkinter import *
import tkinter.messagebox as tmsg
from pickle import *

root=Tk()
root.geometry('1000x1330')
root.title('WhatToDo')
root.config(bg="#B6C9C6")

def add_task():
    data=task.get()
    if data!='':
        task_list.insert(END,data)
        task.set('')
    else:
        tmsg.showwarning('Warning','Enter a Task to Add')

def remove_task():
    try:
        removing_data=task_list.curselection()[0]
        task_list.delete(removing_data)
    except:
        tmsg.showwarning('Warning','Select a Task to Remove')


def load_task():
    loading_task=load(open('/storage/emulated/0/Python/ToDoApp/tasks.dat','rb'))
    for tasks in loading_task:
        task_list.insert(END,tasks)
    
def save_task():
    tasks=task_list.get(0,task_list.size())
    dump(tasks,open('/storage/emulated/0/Python/ToDoApp/tasks.dat','wb'))

frame_tasks=Frame(root)
frame_tasks.pack()

scrollbar=Scrollbar(frame_tasks)
scrollbar.pack(side=RIGHT,fill=Y)

task_list=Listbox(frame_tasks,width=50,height=15,yscrollcommand=scrollbar.set)
task_list.pack()

scrollbar.config(command=task_list.yview)

task=StringVar()
task_input=Entry(root,textvariable=task,width=50)
task_input.pack()

button_add_task=Button(root,text="Add Task",bg="#000",fg="cyan" ,width=50,command=add_task)
button_add_task.pack()

button_remove_task=Button(root,text="Remove Task",bg="#000",fg="cyan",width=50,command=remove_task)
button_remove_task.pack()

button_remove_task=Button(root,text="Load Task",bg="#000",fg="cyan",width=50,command=load_task)
button_remove_task.pack()

button_remove_task=Button(root,text="Save Task",bg="#000",fg="cyan",width=50,command=save_task)
button_remove_task.pack()

button_remove_task=Button(root,text="Quit",bg="#000",fg="cyan",width=50,command=exit)
button_remove_task.pack()

root.mainloop()