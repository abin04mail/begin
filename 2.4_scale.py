from tkinter import*

top=Tk()
top.geometry('200x200')

def select():
    sel = 'Value ='+str(v.get())
    label.config(text=sel)

v=DoubleVar()
scale=Scale(top,variable=v,from_=1,to=50,orient=HORIZONTAL)
scale.pack(anchor=CENTER)

btn=Button(top,text='Value',command=select)
btn.pack(anchor=CENTER)

label=Label(top)
label.pack()

top.mainloop()