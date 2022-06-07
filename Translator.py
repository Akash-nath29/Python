from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob

root=Tk()
root.geometry('1000x700')
root.title('Translator')

def translate_it():
    translated_text.delete('1.0',END)
    try:
        
        for key,value in languages.items():
            if value == original_combo.get():
                from_language_key = key
                
                
        for key,value in languages.items():
            if value == translated_combo.get():
                to_language_key = key
                
                
        words = textblob.TextBlob(original_text.get('1.0',END))
        
        words = words.translate(from_lang = from_language_key,to = to_language_key)
        
        translated_text.insert('1.0',words)
        
    except Exception as e:
        messagebox.showerror('Error!',e)

def clear():
    original_text.delete('1.0',END)
    translated_text.delete('1.0',END)

languages = googletrans.LANGUAGES
language_list = list(languages.values())

original_text=Text(root,width=20,height=15,font=('Helvetica',5))
original_text.grid(row=0,column=0,padx=30,pady=20)


translated_text=Text(root,width=20,height=15,font=('Helvetica',5))
translated_text.grid(row=0,column=2,padx=30,pady=20)

button=Button(root,text='Translate',bg="#000",fg="#00ffff",font=('Helvetica',5),command=translate_it)
button.grid(row=0,column=1,padx=10,pady=10)


original_combo = ttk.Combobox(root,width=12,value=language_list)
original_combo.current(21)
original_combo.grid(row=1,column=0)

translated_combo = ttk.Combobox(root,width=12,value=language_list)
translated_combo.current(8)
translated_combo.grid(row=1,column=2)

button2=Button(root,text="Clear",bg="#000",fg="#00ffff",font=('Helvetica',5),command=clear)
button2.grid(row=1,column=1,padx=10,pady=20)


root.mainloop()