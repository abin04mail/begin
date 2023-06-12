# a=int(input('Введите а: '))
# b=int(input('Введите в: '))
# def calc(a, b):
#     print('сумма чисел:', a+b)
#     print('разность чисел: ',a-b)
#     print('произведение чисел: ',a*b)
#     print('частное чисел: ',a/b)
#     print('целочисленное деление',a//b)
#     print('остаток от деления',a%b)
#     print('формула: ',(a**10+b**10)**0.5)
# calc(a,b)

# цена строки, если цена символа 60 коп.
# s=input('введите строку')
# print(f'цена строки' {len(s)*60//100} руб. {len(s)*60%100} коп.')

# макс. число выпавших подряд решек
# s= input() # вводим строку
# c,i=0,0 # создаем переменные для посчета индекса и для нахождения мак элемента
# # ООРОРОРРРРРОРОРРОРОРРР
# while i<len(s): # запускаем цикл 
#     if s[i]=='Р': # если встречаем букву Р
#         temp=0 # создаем переменную чтобы посчитать их кол-во подряд 
#         while i<len(s) and s[i]!='О':# тут счтиаем их кол-во
#             temp+=1 #
#             i+=1 # прибавляем один чтобы идти по индексам 
#         c=max(temp,c) # проверяем максимальный длину
#     i+=1# прибавляем один чтобы идти по индексам 
# print(c)

# макс. число выпавших подряд решек. Альтернативное решение.
#s=s.replace('О',',') # заменяет в строке значения на нужное вам 
# print(s)
# s=s.split('О') # разъединяет значения через указаный элемент и добавялет их в список 
# print(s)
# print(len(max(s)))

# вывод записи строки квадратного уравнения
# a= int(input('введите коэффициент а: '))
# b= int(input('введите коэффициент b: '))
# c= int(input('введите коэффициент c: '))
# if a==b==c==0:
#     print('0=0')
# else:
#     if a!=0:
#         print(a,'*x^2',end='')
#     if b<0:
#         print(b,'*x',end='')
#     elif b>0:
#         print('+',b,'*x',end='')
#     if c<0:
#         print(c,end='')
#     elif c>0:
#         print('+',c ,end='')
#     print('=0')

# вывод записи строки квадратного уравнения. Альтернативное решение.
# def get_n(x):
#     if x > 0:
#         return '+'
#     return '-'
# def solve(a, b, c):
#     res = '=0'
#     if a == 0 and b == 0 and c == 0:
#         return '0=0'
#     if c != 0:
#         res = get_n(c)+str(abs(c))+res  # -7=0
#     if b != 0:
#         if b == 1 or b == -1:
#             res = get_n(b)+'x'+res  # -x-7=0
#         res = get_n(b)+str(abs(b))+'x'+res  # -2x-7=0
#     if a != 0:
#         if a == -1:
#             res = '-x^2'+res
#         elif a == 1:
#             res = 'x^2'+res
#         else:
#             res = str(a)+'x^2'+res
#     return res
# print(solve(2, 0, -10))

# def one(*args): # получился картеж
#     print(type(args))
# one(1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1)

# def two(**kwargs): # создает словарь
#     print(type(kwargs)==dict)
# two(a=1,b=2,c=[1,1,1,1],d='asdfg',e={1:2})

# split() преобразует строку в список по разделителю
# d='Банан,Яблоко,Ананас,Помело,Клубника'
# d=d.split(',')
# print(d)
# d=','.join(d)# соединяет значения списка в строку 
# print(d)

# передаем картеж аргументов в функцию
# def meat(*args):
#     summ=0
#     count=0
#     for i in args:
#         if type(i)==(int or float):
#             summ+=i
#             count+=1
#     print(summ/count)
# meat(1,6,'jhkj', 5, 6)

# анонимные функции
# d=[1,2,3,4,5,6,7]
# a=list(map(lambda x: (x+2)**2, d))
# print(a)

# d=[1,2,3,4,5,6,7]
# a=list(filter(lambda x: True if x%2==0 else False, d))
# print(a)

# f=[23,12,32,555,23,11111,10,1,2,0,3,2,123423,56456467,56756645,3,2]
# a=list(filter(lambda x: True if (x%5==0 and x<101) else False, f))
# b=list(map(lambda x: (x**2+100), a))
# print(b)

# strs=['gjhgjgdf','hgjh','hggfdsfdg','jjhfs','jhkjtkjgddr']
# a=list(filter(lambda x: True if len(x)<11 else False, strs))
# b=list(map(lambda x: x.upper(),a))
# print(b)

# all возвращает True если все значения в списке верные, any возвращает True если хоть одно значение истинно
# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: True if x in command else False, ignore))
# a=['ip','poi','fgh']
# print(ignore_command(a))

# isdigit проверяет есть ли в строке буквы, если да то False иначе True
# проверить IP-адрес на правильность ввода( нет букв и число от 0 до 255)
# print(all(map(lambda x: True if x.isdijit() and -1<int(x) and int(x)<256 else False,(input('введите IP-адрес: ').split('.')))))


#zip 
# a=[1,2,3,4,5,6,7]
# b=['a','b','c','d','e']
# for i in zip(a,b):
#     print(i)

# a=[1,2,3,4,5,6,7]
# b=['a','b','c','d','e']
# c=[7,6,5,4,3,2,1]
# d=['e','d','c','b','a']
# for i,j,k,l in zip(a,b,c,d):
#     print(i,j,k,l)

# colors=['black','white','bluw','red']
# for i in enumerate(colors,1):
#     print(i)
# for i,j in enumerate(colors,1):
#     print(i,j)

#<capital> is the capital of <country>, population equal <population> people.
#Moscow is the capital of Russia, population equal 145934462 people.
# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
# for i,j,k in zip(countries,capitals,population):
# #    print(i, ' is the capital of ', j,', population equal ', k,' people')
#     print(f'{i} is the capital of {j} population equal {k} people')

# import random
# b=[random.randint(1,10) for i in range(10)]
# print(b)
