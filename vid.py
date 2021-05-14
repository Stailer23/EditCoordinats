from tkinter import *
import methods_for_vid
from code2 import start

delta=0.003

def of():
    methods_for_vid.openfile(root,e1)

def go():
    b1['state'] = 'disable'
    b2['state'] = 'disable'
    methods_for_vid.check2(e2)
    if methods_for_vid.check(e1)==False and methods_for_vid.check2(e2)==False:
        lbl.destroy()
        lbl = Label(root, text='Подготовка файлов...')
        lbl.place(x=20, y=150)
        delta=e2.get()
        root.update()
        start(e1.get(),root,lbl, delta)
        b1['state'] = 'normal'
        b2['state'] = 'normal'
    else:
        b1['state'] = 'normal'
        b2['state'] = 'normal'

root = Tk()
root.title('Восстановление координат РКОТ v1.0')
root.geometry('590x200+100+150')
root.resizable(False, False)

lbl = Label(root, text='Выберите файл и дельту')
lbl.place(x=20, y=150)

lf1=LabelFrame(root, text='Выбери файл')
e1=Entry(lf1, width=70)
e1.pack()
lf1.place(x=20, y=5)

b1=Button(root, width=15, height=1, text='Обзор..', command=of)
b1.place(x=450, y=15)

b2=Button(root, width=30, height=2, text='Проверить и исправить', command=go)
b2.place(x=150, y=55)

e2=Entry(root, width=10)
e2.insert(0, delta)
e2.place(x=500, y=65)

l1=Label(root, text='Дельта: ')
l1.place(x=450, y=65)

l2=Label(root, text='by Nikolaev', fg='grey')
l2.place(x=520, y=180)

if __name__ == "__main__":
    mainloop()