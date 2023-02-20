def roman_to_int(stroka):
    """
        перевод числа из римской с.с. в арабскую
        число не более 3000
    """
    # if stroka=='IV':
    #     return 4
    # elif stroka=='LVIII':
    #     return 58
    # elif stroka=='MCMXCIV':
    #     return 1994
    # elif stroka=='XCIX':
    #     return 99
    # elif stroka=='LXXX':
    #     return 80
    # elif stroka=='LXIX':
    #     return 69

    arab_itog = 0
    rim=('I', 'V', 'X', 'L', 'C', 'D', 'M', 'W')
    arab=(1, 5, 10, 50, 100, 500, 1000, 5000)
    pos=len(stroka)-1
    while pos>-1:
        for min, max in ([0, 1], [0, 2], [2, 3], [2, 4], [4, 5], [4, 6], [6, 7]):
            if pos>-1 and stroka[pos]==rim[min]:
                while pos>-1 and stroka[pos]==rim[min]:
                    arab_itog += arab[min]
                    pos-=1
            if pos>-1 and stroka[pos]==rim[max]:
                arab_itog += arab[max]
                pos-=1
                if pos>-1 and stroka[pos]==rim[min]:
                    arab_itog -= arab[min]
                    pos-=1
    return arab_itog
        


def int_to_roman(number):
    """
        перевод из арабской с.с. в римскую
        число не более 3000
    """
    rim_itog=''
    stroka = str(number)
    rim=('I', 'V', 'X', 'L', 'C', 'D', 'M', 'W')
    pos = len(stroka)
    for min, mid, max, k in ([0, 1, 2, -1], [2, 3, 4, -2], [4, 5, 6, -3], [6, 7, 7, -4]):
        arab={1: (min), 2: (min, min), 3: (min, min, min), 4: (min, mid), 5: (mid), 
            6: (mid, min), 7: (mid, min, min), 8: (mid, min, min, min), 9: (min, max)}
        if k >= -pos and stroka[k] != "0":
            a = arab.get(int(stroka[k]))
            b=(len(a) if type(a)==tuple else 1)
            for i in range(b-1, -1, -1):
                rim_itog = rim[(a[i] if type(a)==tuple else a)] + rim_itog

    return rim_itog

#print(int_to_roman(1568))



    # if stroka==4:
    #     return 'IV'
    # elif stroka==58:
    #     return 'LVIII'
    # elif stroka==1994:
    #     return 'MCMXCIV'
    # elif stroka==99:
    #     return 'XCIX'
    # elif stroka==80:
    #     return 'LXXX'
    # elif stroka==69:
    #     return 'LXIX'
    # elif stroka==26:
    #     return 'XXVI'