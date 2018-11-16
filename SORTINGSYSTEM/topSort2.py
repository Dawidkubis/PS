import random
import math
from copy import deepcopy

"""----------------------------"""

def start(seznam):
    global a

    output = []
    for i in range(0,len(seznam),2):
        #print(i)
        output.append([seznam[i]])

        if i + 1 != len(seznam):
            output[-1].append(seznam[i+1])

            a += 1
            if output[-1][0] > output[-1][1]:

                output[-1][0],output[-1][1] = output[-1][1],output[-1][0]

    return output

def weld(seznam):
    o = start(seznam)
    output = ssf(o)
    #print('output : ',output)
    return output[0]

def ssf(seznam):
    global a

    output = []
    #seznam = deepcopy(listek)
    zbytek = []
    #print('seznam : ',seznam)
    #print()
    if len(seznam) % 2 != 0:
        zbytek = seznam.pop(-1)
        #print('zbytek',zbytek)
    #print('seznam : ',seznam)

    while seznam != []:

        output.append([])
        while seznam[0] != [] and seznam[1] != []:


            #a,b = seznam[0][0], seznam[1][0]

            a += 1
            if seznam[0][0] < seznam[1][0]:
                output[-1].append(seznam[0].pop(0))
            else:
                output[-1].append(seznam[1].pop(0))


        if seznam[0] == []:
            for i in seznam[1]:
                output[-1].append(i)
        elif seznam[1] == []:
            for i in seznam[0]:
                output[-1].append(i)

        #print('seznam', seznam)
        #print(seznam[0], seznam[1])
        del seznam[1], seznam[0]

    if zbytek != []:
        output.append(zbytek)
    #print('output : ',output)
    #print('len(output) : ',len(output))
    if len(output) > 1:
        output = ssf(output)

    #print('output2 : ', output)
    return output

def vecimeci(seznam):
    global a
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
            a += 2
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

def simon(function, generations, population):
    global a
    fc = function
    superlist = []
    for i in range(1, generations + 1):
        print('huujaja', i)
        a = 0
        for i2 in range(population):
            seznam = list(range(i))
            random.shuffle(seznam)
            fc(seznam)
        a = a / population
        superlist.append(a)

    output = []
    for i in range(1, generations):
        x = i + 1
        growth = (x**2 - x) / 2
        output.append(superlist[i] / growth)

    for i in range(10):
        print()

    return output


for i in simon(vecimeci, 100, 10):
    print(i)
