from tkinter import *

root = Tk()

a = ['blue','green','red','cyan','magenta','yellow','black','white']

def color(item):
    col=a.index(canvas(item, 'fill'))
    if col <7:
        return col +1
    return 0

def change1():
    canvas.itemconfig(rec, fill=a[color(rec)])

def change2():
    canvas.itemconfig(pol, fill=a[color(pol)])

def change3():
    canvas.itemconfig(ova, fill=a[color(ova)])

canvas = Canvas(root, width=500, height=700, bg='white')
canvas.pack()
rec = canvas.create_rectangle(30,200,470,580,fill='Blue')
ova = canvas.create_oval(400,10,480,90, fill='Yellow')
pol = canvas.create_polygon(30,200,260,120,470,200, fill='red')

a=Button(text='основание', command=change1)
a.pack(side=BOTTOM)
b=Button(text='крыша', command=change2)
b.pack(side=BOTTOM)
c=Button(text='солнце', command=change3)
c.pack(side=BOTTOM)


root.mainloop()