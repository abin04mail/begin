from tkinter import *
# from tkinter import ttk

root = Tk()
root.title('Введите домашний адрес')
root.geometry('500x300')

for c in range(2):
    root.columnconfigure(index=c, weight=1)
for r in range(8):
    root.rowconfigure(index=r, weight=1)

# def click():
#     result = askyesno(title="Подтвержение операции", message="Подтвердить операцию?")
#     if result: showinfo("Результат", "Операция подтверждена")
#     else: showinfo("Результат", "Операция отменена")

# ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)

ent1 = Entry(width=20)
ent1.grid(row=0, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent2 = Entry(width=20)
ent2.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent3 = Entry(width=20)
ent3.grid(row=2, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent4 = Entry(width=20)
ent4.grid(row=3, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent5 = Entry(width=20)
ent5.grid(row=4, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent6 = Entry(width=20)
ent6.grid(row=5, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent7 = Entry(width=20)
ent7.grid(row=6, column=1, ipadx=6, ipady=6, padx=5, pady=5)
ent8 = Entry(width=20)
ent8.grid(row=7, column=1, ipadx=6, ipady=6, padx=5, pady=5)

label = Label(root)
label.pack()

root.mainloop()