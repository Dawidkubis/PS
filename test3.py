import numpy as np

def sq(num):

    arra = np.arange(num**2).reshape(num,num)
    for x in range(num):
        for y in range(num):
            arra[x,y] =int(num+y-x)

    return arra
