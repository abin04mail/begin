try:
    a = int(input("введите от 1 до 9 - какой столбец таблицы вывести "))
    if a > 0 and a < 10:
        for i in range(1, 10):
            print(i, " * ", a, " = ", i * a)
    else:
        print("неверный введен номер столбца")
except BaseException:
    print("введен неверный символ")
