from tkinter import *

root = Tk()

col = ['blue','green','red','cyan','magenta','yellow','black','white']

def color(item):
    draw=col.index(canvas.itemcget(item, 'fill'))
    if draw <7:
        return draw +1
    return 0

def change_rec():
    canvas.itemconfig(rec, fill=col[color(rec)])

def change_pol():
    canvas.itemconfig(pol, fill=col[color(pol)])

def change_ova():
    canvas.itemconfig(ova, fill=col[color(ova)])

canvas = Canvas(root, width=500, height=700, bg='cyan')
canvas.pack()
rec = canvas.create_rectangle(30,200,470,580,fill='blue')
ova = canvas.create_oval(400,10,480,90, fill='yellow')
pol = canvas.create_polygon(30,200,260,120,470,200, fill='red')

a=Button(text='основание', command=change_rec)
a.pack(side=BOTTOM)
b=Button(text='крыша', command=change_pol)
b.pack(side=BOTTOM)
c=Button(text='солнце', command=change_ova)
c.pack(side=BOTTOM)


root.mainloop()