from tkinter import *

def list(run1):
    if run1 == '':
        lab['text']='0'
    else:
        lab['text']=str(eval(run1))

def calc(cntrl):
    if cntrl == "C":
        list('')
    elif cntrl == "DEL":
        list(lab['text'][0: -1])
    elif cntrl == "X^2":
        list(str((eval(lab["text"]))**2))
    elif cntrl == "=":
        list(lab["text"])
    else:
        if lab['text'] == "0":
            lab['text'] = ""
        lab['text'] = lab['text']+cntrl

root = Tk()
root["bg"] = "black"
root.geometry("305x330+500+300")
root.title("Калькулятор")
root.resizable(False, False)
lab = Label(text='0', bg="black", foreground="white")
lab.place(x=10, y=20)
but = [
    "C", "DEL", "+", "=",
    "1", "2", "3", "/",
    "4", "5", "6", "+",
    "7", "8", "9", "-",
    "()", "0", ")", "X^2"
]
x = 10
y = 60
for i in but:
    j =lambda k=i: calc(k)
    Button(text=i, bg="white", command=j).place(x=x, y=y, width=70, height=50)
    x+=72
    if x>280:
        x=10
        y+=52

root.mainloop()