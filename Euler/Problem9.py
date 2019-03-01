from math import *

results = []

for x in range(1, 2000):
    for y in range(1, 2000):
        if sqrt(x**2 + y**2) % 1 == 0:
            print(x,y,' --> ',int(sqrt(x**2+y**2)))
            results.append([x,y,int(sqrt(x**2+y**2))])
