import random
import math

"""----------------------------"""

def start(seznam):

    output = []
    for i in range(0,len(seznam),2):
        #print(i)
        output.append([seznam[i]])

        if i + 1 != len(seznam):
            output[-1].append(seznam[i+1])

            if output[-1][0] > output[-1][1]:

                output[-1][0],output[-1][1] = output[-1][1],output[-1][0]

    return output

def weld(seznam):
    o = start(seznam)
    output = ssf(o)
    #print('output : ',output)
    return output[0]

def ssf(seznam):
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
        print('REKURZE')
        output = ssf(output)

    #print('output2 : ', output)
    return output

"""----------------------------"""

seznam = list(range(10**5))

random.shuffle(seznam)

print(seznam)
print()
output = weld(seznam)
print(output)
