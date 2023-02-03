# угадай число от 1 до 100
import random
a = random.randint(1, 100)
b=int(input('угадай число от 1 до 100 '))
c = 1
while a != b:
    if b < a:
        b = int(input("+ введи большее число "))
        c +=1
    else:
        b = int(input("- введи меньшее число "))
        c +=1
print("угадал!!!", c)
