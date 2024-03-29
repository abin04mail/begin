def quadratic_solve(a:float, b:float, c:float):           # ax^2+bx+c=0
    if c == 0 and a != 0:                                 # ax^2 + bx=0 -> x = 0, -b/a
        return sorted([0, truncate(-b/a,5)])
    elif a == 0:                                          # bx+c=0 -> x=-c/b
        return [truncate(-c/b,5)]
    else:
        d=b*b - 4*a*c
        if d == 0:
            return [ truncate(-b/(2*a),5)]
        elif d > 0:
            return sorted([truncate((d**0.5 - b)/(2*a),5), truncate((-(d**0.5) - b)/(2*a),5)])

# def test():
 
#     tests=[
#         [1, 1, -10], [-3, 2, 18] , [-7, -2, 3], [0,5,10], [18, -2, 0], 
#         [-2, 8, -7], [333, -32, -200], [6, -3, -5], [99, 98, 9], [-1, 2, 3], 
#         [7, 4, -5]
#     ]
#     results=[
#         [-3.70156, 2.70156], [-2.13873,2.80539], [-0.81291, 0.52720], 
#         [-2], [0, 0.11111], [1.29289, 2.70710], [-0.72842, 0.82452], 
#         [-0.69648, 1.19648], [-0.88746, -0.10243], [-1, 3], [-1.17785, 0.60642]
#     ]
#     i=1
#     for a in tests:
#         if quadratic_solve(a[0], a[1], a[2]) == results[i-1]:
#             print(f'Test №{i} прошел успешно')
#         i+=1

def truncate(n, decimals = 0):                              # Функция усечения до заданного знака (по умолчанию до целого)
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

#test()
print(quadratic_solve(1,8,15))
