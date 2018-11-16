import random
import math
from copy import deepcopy

"""----------------------------"""

def vecimeci(seznam):
    work = deepcopy(seznam)
    output = []
    outputt = []

    highscore = 0
    lowscore = 0

    while len(work) > 1:
        #print(work)
        highscore = 0
        lowscore = 0
        for i in range(len(work)):
            #print('i,work[highscore] : ', i, work[highscore])
            if work[i] > work[highscore]:
                highscore = i
            if work[i] < work[lowscore]:
                lowscore = i
                #print('HIGHSCORE : ',work[highscore])
        #print('\n--------------------------\n')
        output.insert(0,work.pop(highscore))
        if lowscore >= highscore:
            lowscore = lowscore - 1
        outputt.append(work.pop(lowscore))

    output = outputt + work + output
    return output

"""----------------------------"""

seznam = list(range(10000))

random.shuffle(seznam)

print(seznam)
print()
output = vecimeci(seznam)
print(output)
