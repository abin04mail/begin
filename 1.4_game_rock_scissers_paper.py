try:
    a = int(input("первый игрок введите: 1-камень, 2-ножницы, 3-бумага "))
    b = int(input("второой игрок введите: 1-камень, 2-ножницы, 3-бумага "))
    if (a > 0 and a < 4) and (b > 0 and b < 4) :
        if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
            print ("победил первый игрок")
        elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
            print ("победил второй игрок")
        elif a==b:
            print("Ничья")
except BaseException:
    print("введено неверное значение")
