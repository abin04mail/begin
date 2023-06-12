def quadratic_solve(a:float, b:float, c:float):           # ax^2+bx+c=0
    if c == 0 and a != 0:                                 # ax^2 + bx=0 -> x = 0, -b/a
        return sorted([0, (-b/a)])
    elif a == 0:                                          # bx+c=0 -> x=-c/b
        return [(-c/b)]
    else:
        d=b*b - 4*a*c
        if d == 0:
            return [-b/(2*a)]
        elif d > 0:
            return [((d**0.5 - b)/(2*a)), ((-(d**0.5) - b)/(2*a))]
# a= float(input('введите коэффициент a: '))
# b= float(input('введите коэффициент b: '))
# c= float(input('введите коэффициент c: '))             


a = int(input('введите ваше число '))
b = int(input('введите ваше число '))
c = int(input('введите ваше число '))

D = (b * b - (4 * a * c))
if a==0:
    print('X2=', -c/b)
elif D < 0:
    print('нет корней')
elif D == 0:
    print('один корень равный', -b/(2*a))
else:
    x = (-b + (D**0.5))
    x_1 = (x / (2*a))

    print('X1=',(x_1),end='')

    x_2 = (-b - (D**0.5))
    x_3 = (x_2 / (2*a))
    print(' X2=',x_3)

print(quadratic_solve(a,b,c))