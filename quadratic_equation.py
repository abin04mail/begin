def quadratic_solve(a:float, b:float, c:float): # ax^2+bx+c=0
    if c == 0 and a != 0: # ax^2 + bx=0 -> x = 0, -b/a
        return sorted([0, round(-b/a,3)])
    elif a == 0:
        return [round(-c/b,5)]
    else:
        d=b*b - 4*a*c
        if d == 0:
            return [ round(-b/(2*a),3)]
        elif d > 0:
            return sorted([round((d**0.5 - b)/(2*a),3), round((-(d**0.5) - b)/(2*a),3)])

def test():
 
    tests=[
        [1, 1, -10], [-3, 2, 18]
    ]
    results=[
        [-3.701, 2.701], [-2.138,2.805]
    ]
    i=1
    for a in tests:
        if quadratic_solve(a[0], a[1], a[2]) == results[i-1]:
            print(f'Test №{i} прошел успешно')
        i+=1


test()