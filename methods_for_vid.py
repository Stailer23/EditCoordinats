from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import messagebox as mb

def openfile(root, e1):
    root.withdraw()
    filename = askopenfilename(filetypes=(("Excel xlsm", "*.xlsm"), ("All files", "*.*")))
    root.deiconify()
    e1.delete(0, END)
    e1.insert(0, filename)
    return filename

def check(e1):
    okno1 = e1.get()
    if '.xlsm' not in okno1:
        mb.showerror('Не тупи..', 'Неверно выбран файл!')
        return True
    else: return False

def check2(e2):
    okno=e2.get()
    try: float(okno)
    except:  mb.showerror('Не дробное число!', 'Разделителем в поле "Дельта" должна быть точка!')
    else: return False


