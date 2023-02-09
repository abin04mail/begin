from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Калькулятор')
root.geometry('200x250')

def calc1():
    c=int(ent1.get())+int(ent2.get())
    lab.config(text=str(c))
def calc2():
    c=int(ent1.get())-int(ent2.get())
    lab.config(text=str(c))
def calc3():
    c=int(ent1.get())*int(ent2.get())
    lab.config(text=str(c))
def calc4():
    c=int(ent1.get())/int(ent2.get())
    lab.config(text=str(c))
def calc5():
    c=int(ent1.get())//int(ent2.get())
    lab.config(text=str(c))
def calc6():
    c=int(ent1.get())**int(ent2.get())
    lab.config(text=str(c))

ent1 = Entry(root, width=20, bg='black', fg='white')
ent1.pack()
ent2 = Entry(root, width=20, bg='black', fg='white')
ent2.pack()

btn1=ttk.Button(text='+', command=calc1)
btn1.pack(side=TOP)
btn2=ttk.Button(text='-', command=calc2)
btn2.pack(side=TOP)
btn3=ttk.Button(text='*', command=calc3)
btn3.pack(side=TOP)
btn4=ttk.Button(text='/', command=calc4)
btn4.pack(side=TOP)
btn5=ttk.Button(text='//', command=calc5)
btn5.pack(side=TOP)
btn6=ttk.Button(text='**', command=calc6)
btn6.pack(side=TOP)

lab = ttk.Label(root,width=15, text='    ')
lab.pack(side=BOTTOM)

root.mainloop()