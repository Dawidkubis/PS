import random
import math
from copy import deepcopy

"""----------------------------"""

def ssf(seznam):
    work = deepcopy(seznam)
    output = []

    highscore = 0

    while not work == []:
        #print(work)
        highscore = 0
        for i in range(len(work)):
            #print('i,work[highscore] : ', i, work[highscore])
            if work[i] > work[highscore]:
                highscore = i
                #print('HIGHSCORE : ',work[highscore])
        #print('\n--------------------------\n')
        output.insert(0,work.pop(highscore))


    return output
"""----------------------------"""

seznam = list(range(10**3))

random.shuffle(seznam)

print(seznam)
print()
output = ssf(seznam)
print(output)
