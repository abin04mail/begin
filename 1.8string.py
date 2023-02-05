a = input("введите слово ")
if len(a)>4:
    print("четвертая буква : ", a[3])
else:
    print("НЕТ")
print("последняя буква ", a[len(a)-1])