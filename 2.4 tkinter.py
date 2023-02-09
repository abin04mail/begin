from tkinter import *
# color = ['#7FFFD4','white', 'gray', 'brown','yelow', 'blue', 'red', 'green',
#          'pink', 'magenta', 'black']

# def get_next(item):
#     curr = colors.index(Canvas.itemcget(item, 'fill'))
#     if curr != len(colors) - 1:
#         return curr +1
#     return 0

# def change_square():
#     Canvas.itemconfig(square, fill=colors[get_next(square)])

# def change_roof():
#     Canvas.itemconfig(roof, fill=colors[get_next(roof)])

# def change_sun():
#     Canvas.itemconfig(sun, fill=colors[get_next(sun)])

root = Tk()
# root.title('Приложение')
# root.geometry('700x500')
# a1=Label(text='text')
# a2=Entry(text='поле ввода')
# a3=Button(text='это кнопка')
# a1.pack(side=BOTTOM)
# a2.pack(side=BOTTOM)
# a3.pack(side=BOTTOM)

# bt = Button(width=50, height=20, bg='cyan', activebackground='red', text='это кнопка')
# bt.pack()

# bt1 = Button(width=15, height=10, bg='red')
# bt2 = Button(width=15, height=10, bg='blue')
# bt3 = Button(width=15, height=10, bg='green')
# bt4 = Button(width=15, height=10, bg='cyan')
# bt1.pack(side=LEFT)
# bt2.pack(side=RIGHT)
# bt3.pack(side=TOP)
# bt4.pack(side=BOTTOM)

# сортировка вводимой строки
# ent = Entry(root, width=20, bg='black', fg='white')
# ent.pack()
# def str_to_sort_list(event):
#     s = ent.get()
#     s = s.split()
#     s.sort()
#     lab['text']= ' '.join(s)

# ent = Entry(width=20)
# but = Button(text="Преобразовать") #, command=str_to_sort_list)
# lab = Label(width=20, bg='black',fg='white')

# but.bind('<Button-1>', str_to_sort_list)

# ent.pack()
# but.pack()
# lab.pack()

# def button_1():
#     l['text'] = str(int(a.get())*2)

# a = Entry(root, width=15, bg='gray', fg='cyan', font='consolas')
# a.pack()
# Button(root, text='умножить на 2', width=15,
#        height=2, bg='white', command=button_1).pack()
# l = Label(root, width=15, bg='gray', fg='cyan', font='consolas')
# l.pack()

# canv = Canvas(root, width=200, height=200, bg='white')
# canv.pack()
# canv.create_line(10,10,150,150)
# canv.create_rectangle(10,10,150,150)
# canv.create_oval(10,10,150,150)
# canv.create_polygon(15,15,190,190,110,50, fill='yellow',outline='black',
#                     activeoutline='red', dash=(30,20,10),width=3)

def change():
    canvas.itemconfig(square, fill='blue')
    print(canvas.itemcget(square, 'fill'))

side=200
canvas_widtch, canvas_height=300, 300
x, y=20, 20
canvas = Canvas(root, width=canvas_widtch, height=canvas_height, bg='white')
canvas.pack()
square = canvas.create_rectangle(x,y,x+side,y+side,fill='Yellow')
a=Button(text='1244', command=change)
a.pack(side=BOTTOM)


root.mainloop()