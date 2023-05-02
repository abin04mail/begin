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


# s=input('введите строку')
# print('цена строки', len(s)*60//100,'руб. ', 100*(len(s)*0.6-int(len(s)*0.6)),'коп.')

# s=input('введите строку ')
# max=0
# count=1
# for i in range(len(s)):
#     if s[i]=='p':
#         if s[i]==s[i-1]:
#             count+=1
#     else:
#         if count>max:
#             max==count
#             count=0
# print(max)

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

# def meat(*args):
#     summ=0
#     count=0
#     for i in args:
#         if type(i)==(int or float):
#             summ+=i
#             count+=1
#     print(summ/count)
#
# meat(1,6,'jhkj', 5, 6)
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


# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any(map(lambda x: True if x in command else False, ignore))
# a=['ip','poi','fgh']
# print(ignore_command(a))

# print(all(map(lambda x: True if x.isdijit() and -1<int(x) and int(x)<256 else False,(input('введите IP-адрес: ').split('.')))))

#<capital> is the capital of <country>, population equal <population> people.
#Moscow is the capital of Russia, population equal 145934462 people.
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
for i,j,k in zip(countries,capitals,population):
#    print(i, ' is the capital of ', j,', population equal ', k,' people')
    print(f'{i} is the capital of {j} population equal {k} people')
