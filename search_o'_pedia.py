from tkinter import *
import tkinter.messagebox as tmsg
import wikipedia

root=Tk()
root.geometry("1000x1100")
root.title("Search o' pedia")

nameValue=StringVar()

Label(text="Welcome to Search o' pedia",bg="white",fg="black",relief=RAISED,width=100).pack(pady=10)
Label(text="Enter what you want to search",width=100).pack(pady=10)
Entry(textvariable=nameValue,justify=CENTER).pack(pady=10)
def search():
    a=nameValue.get()
    b=wikipedia.summary(a)
    l1.configure(text=b,wraplength=1000,justify=CENTER,padx=10,pady=10)

def clear():
    l1.configure(text="")
 
def quit():
    value = tmsg.askquestion("Search o' pedia","Do you really want to quit ?")
    if value=="yes":
        a=tmsg.askquestion("Rate us","Did you enjoyed it ?")
        if a=="yes":
            f=open('/storage/emulated/0/Python/a.txt','w+')
            f.write(a)
            f.close()
            root.destroy()
        else:
            f=open('/storage/emulated/0/Python/a.txt','w+')
            f.write(a)
            f.close()
            tmsg.showinfo("ok","We will work on Searchepedia")
            root.destroy()
frame=Frame(relief=GROOVE).pack()    
Button(text="Search",bg="black",fg="cyan",command=search).pack(pady=10)
Button(text="Clear",bg="black",fg="cyan",command=clear).pack(pady=10)
Button(text="Quit",bg="black",fg="cyan",command=quit).pack(pady=10)
l1=Label(frame,text="",bg="white",fg="black",font=("Arial",6,"italic"))
l1.pack(expand=True)
root.mainloop()