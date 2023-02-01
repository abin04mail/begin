a = int(input('введите первое число'))
b = int(input('введите второе число'))
c = input('введите действие')
if c == "+":
    print (a+b)
elif c == "-":
    print(a-b)
elif c == "*":
    print(a*b)
elif c == "/":
    if b != 0:
        print(a/b)
    else:
        print("ошибка деления на 0")
elif c == "**":
    print(a**b)
else:
    print("ошибка ввода")