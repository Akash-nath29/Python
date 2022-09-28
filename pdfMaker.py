from tkinter import *
from tkinter.filedialog import asksaveasfilename 
from fpdf import FPDF

root = Tk()
root.geometry('1000x1500')
root.title('PDF It')
root.config(bg='#121212')


def create_pdf():
    path = asksaveasfilename(filetypes=[('PDF','*.pdf')])
    text_to_add = my_text.get('1.0',END)
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_font('helvetica','',16)
    pdf.cell(40,10,text_to_add)
    pdf.output(path)

Label(root,text='Enter your text',bg='#121212',fg='#fff').pack(padx=10,pady=20,side=TOP)


my_text = Text(root,bg='#1d1b1f',fg='#fff',insertbackground = '#fff',wrap = WORD)

my_text.pack(padx=10,pady=20,ipadx=20,ipady=20,fill=BOTH)


Button(root,text='Create PDF',bg='#000',fg='#3ef1f7',command=create_pdf).pack(padx=10,pady=20)

root.mainloop()