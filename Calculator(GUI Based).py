from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('1000x800')
root.config(bg='#121212')
root.title('Calculator')

val = ''

def btn_one():
    global val
    val = val+'1'
    problem.set(val)
    
def btn_two():
    global val
    val = val + '2'
    problem.set(val)
    
def btn_three():
    global val
    val = val + '3'
    problem.set(val)
    
def btn_four():
    global val
    val = val+'4'
    problem.set(val)
    
def btn_five():
    global val
    val = val+'5'
    problem.set(val)
    
def btn_six():
    global val
    val = val+'6'
    problem.set(val)
    
def btn_seven():
    global val
    val = val+'7'
    problem.set(val)
    
def btn_eight():
    global val
    val = val+'8'
    problem.set(val)
    
def btn_nine():
    global val
    val = val+'9'
    problem.set(val)
    
def btn_zero():
    global val
    val = val+'0'
    problem.set(val)
    
def btn_plus():
    global val
    val = val+'+'
    problem.set(val)
    
def btn_minus():
    global val 
    val = val+'-'
    problem.set(val)
    
def btn_multiply():
    global val
    val = val + '*'
    problem.set(val)
    
def btn_divide():
    global val
    val = val+'/'
    problem.set(val)
    
def btn_ac():
    global val
    val = ''
    problem.set(val)
    
def btn_equal():
    global val
    solve = problem.get()
    try:
        val = eval(solve)
        problem.set(val)
    except ZeroDivisionError :
        tmsg.showwarning('Calculator','Can\'t divide by 0')


frame_entry = Frame(root,borderwidth=5,relief=FLAT,bg='#121212')
frame_entry.pack(padx=10,pady=20,side=TOP)

problem = StringVar()

entry_nums = Entry(frame_entry,textvariable=problem , bg='#1d1b1f',fg='#fff',insertbackground='#fff',justify=RIGHT,font=('helvetica',16))
entry_nums.pack(padx=10,pady=10)

frame_keys = Frame(root,borderwidth=5,relief=FLAT,bg='#121212')
frame_keys.pack(padx=10,pady=20)

frame_row_first = Frame(frame_keys,borderwidth=2,relief=FLAT,bg='#121212')
frame_row_first.pack(padx=10,pady=5)

Button(frame_row_first,text='7',bg='#121212',fg='#fff',command=btn_seven).grid(row=0,column=0,padx=10)

Button(frame_row_first,text='8',bg='#121212',fg='#fff',command=btn_eight).grid(row=0,column=1,padx=10)

Button(frame_row_first,text='9',bg='#121212',fg='#fff',command=btn_nine).grid(row=0,column=2,padx=10)

Button(frame_row_first,text='+',bg='#121212',fg='#fff',command = btn_plus).grid(row=0,column=3,padx=10)

frame_row_second = Frame(frame_keys,borderwidth=2,relief=FLAT,bg='#121212')
frame_row_second.pack(padx=10,pady=5)

Button(frame_row_second,text='4',bg='#121212',fg='#fff',command=btn_four).grid(row=0,column=0,padx=10)

Button(frame_row_second,text='5',bg='#121212',fg='#fff',command=btn_five).grid(row=0,column=1,padx=10)

Button(frame_row_second,text='6',bg='#121212',fg='#fff',command=btn_six).grid(row=0,column=2,padx=10)

Button(frame_row_second,text='-',bg='#121212',fg='#fff',command=btn_minus).grid(row=0,column=3,padx=10)

frame_row_third = Frame(frame_keys,borderwidth=2,relief=FLAT,bg='#121212')
frame_row_third.pack(padx=10,pady=5)

Button(frame_row_third,text='1',bg='#121212',fg='#fff',command=btn_one).grid(row=0,column=0,padx=10)

Button(frame_row_third,text='2',bg='#121212',fg='#fff',command=btn_two).grid(row=0,column=1,padx=10)

Button(frame_row_third,text='3',bg='#121212',fg='#fff',command=btn_three).grid(row=0,column=2,padx=10)

Button(frame_row_third,text='×',bg='#121212',fg='#fff',command=btn_multiply).grid(row=0,column=3,padx=10)

frame_row_fourth = Frame(frame_keys,borderwidth=2,relief=FLAT,bg='#121212')
frame_row_fourth.pack(padx=10,pady=5)

Button(frame_row_fourth,text='AC',bg='#121212',fg='#fff',command=btn_ac).grid(row=0,column=0,padx=10)

Button(frame_row_fourth,text='0',bg='#121212',fg='#fff',command=btn_zero).grid(row=0,column=1,padx=10)

Button(frame_row_fourth,text='=',bg='#121212',fg='#fff',command=btn_equal).grid(row=0,column=2,padx=10)

Button(frame_row_fourth,text='÷',bg='#121212',fg='#fff',command=btn_divide).grid(row=0,column=3,padx=10)

root.mainloop()
