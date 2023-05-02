import numpy
import random
def matr(n,m):
    a=numpy.zeros([n, m])
    for i in range(n):
        for j in range(m):
            a[i, j]=random.randint(-10,10)
    return a