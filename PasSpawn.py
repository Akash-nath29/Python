from tkinter import *
import random 

root = Tk()
root.geometry('1000x1200')
root.title('PassSpawn')
root.config(bg='#fff')

def spawn_pass():
    capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    smalls = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    nums = ['0','1','2','3','4','5','6','7','8','9']
    puncs = ['!','@','#','$','/','\'','\"',';']
    
    password = []
    
    if check_capitals_var.get()==1:
        for items_caps in capitals:
            password.extend(items_caps)
    else:
        pass
    if check_smalls_var.get()==1:
        for items_small in smalls:
            password.extend(items_small)
    else:
        pass
    if check_nums_var.get()==1:
        for items_num in nums:
            password.extend(items_num)
    else:
        pass
    if check_puncs_var.get()==1:
        for items_punc in puncs:
            password.extend(items_punc)
    else:
        pass
    len = int(password_len.get())   
    random.shuffle(password)
    #print(new_password)
    password_to_show = ''.join(password[0:len])
    my_text.delete('1.0',END)
    my_text.insert(END,password_to_show)

frame_checks = Frame(root,borderwidth=10,bg='#fff')
frame_checks.pack(padx=10,pady=20)

check_capitals_var = IntVar()
check_capitals = Checkbutton(frame_checks,text='Add Capital Alphabets',variable=check_capitals_var,bg='#fff')
check_capitals.grid(row=0,column=0)

check_smalls_var = IntVar()
check_smalls = Checkbutton(frame_checks,text='Add Small Alphabets',variable=check_smalls_var,bg='#fff')
check_smalls.grid(row=1,column=0)

check_nums_var = IntVar()
check_nums = Checkbutton(frame_checks,text='Add Numbers',variable=check_nums_var,bg='#fff')
check_nums.grid(row=2,column=0)

check_puncs_var = IntVar()
check_puncs = Checkbutton(frame_checks,text='Add Punctuations',variable=check_puncs_var,bg='#fff')
check_puncs.grid(row=3,column=0)

password_len = StringVar()

Entry(root,textvariable = password_len,justify=CENTER).pack(padx=10,pady=20)

Button(root,text='Spawn',command = spawn_pass,bg='#121212',fg='#fff',activebackground='#fff',activeforeground='#121212').pack(padx=10,pady=20)

my_text = Text(root,width=50,height=10)
my_text.pack(padx=10,pady=20)

root.mainloop()