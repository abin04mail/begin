from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, INFO, showinfo

root = Tk()
root.title('Введите домашний адрес')
root.geometry('480x240')

def ok():
    showinfo(message='Данные отправлены', icon=INFO, default=OK)

def cancel():
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)
    ent4.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent8.delete(0, END)
    
fr= Frame(root, borderwidth=1, width=30, height=260, bg='Gainsboro')

for c in range(2):
    fr.columnconfigure(index=c, weight=1)
    for r in range(8):
        fr.rowconfigure(index=r, weight=1)

ent1 = Entry(fr, width=40, bg='White')
ent1.grid(row=0, column=1, padx=5)
ent2 = Entry(fr, width=40, bg='White')
ent2.grid(row=1, column=1, padx=5)
ent3 = Entry(fr, width=40, bg='White')
ent3.grid(row=2, column=1, padx=5)
ent4 = Entry(fr, width=40, bg='White')
ent4.grid(row=3, column=1, padx=5)
ent5 = Entry(fr, width=40, bg='White')
ent5.grid(row=4, column=1, padx=5)
ent6 = Entry(fr, width=40, bg='White')
ent6.grid(row=5, column=1, padx=5)
ent7 = Entry(fr, width=40, bg='White')
ent7.grid(row=6, column=1, padx=5)
ent8 = Entry(fr, width=40, bg='White')
ent8.grid(row=7, column=1, padx=5)

lab1 = Label(fr, width=20, text='Имя:', anchor=E)
lab1.grid(row=0, column=0)
lab2 = Label(fr, width=20, text='Фамилия:', anchor=E)
lab2.grid(row=1, column=0)
lab3 = Label(fr, width=20, text='Адрес1:', anchor=E)
lab3.grid(row=2, column=0)
lab4 = Label(fr, width=20, text='Адрес2:', anchor=E)
lab4.grid(row=3, column=0)
lab5 = Label(fr, width=20, text='Город:', anchor=E)
lab5.grid(row=4, column=0)
lab6 = Label(fr, width=20, text='Регион:', anchor=E)
lab6.grid(row=5, column=0)
lab7 = Label(fr, width=20, text='Почтовый индекс:', anchor=E)
lab7.grid(row=6, column=0)
lab8 = Label(fr, width=20, text='Страна:', anchor=E)
lab8.grid(row=7, column=0)

fr.pack(anchor=N, fill=X, padx=5, pady=5)

btn1=ttk.Button(text="Очистить", command=cancel)
btn1.place(x=240, y=200, width=110, height=30)
btn2=ttk.Button(text="Отправить", command=ok)
btn2.place(x=360, y=200, width=110, height=30)

root.mainloop()