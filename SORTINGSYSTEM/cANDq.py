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

def superSort(seznam, first = True):
    print(first)
    output = []
    if first:
        seznam = start(seznam)
    #print('seznam : ',seznam)
    #print()
    for i in range(0, len(seznam) - len(seznam) % 2 , 2):
        #print(seznam[i])

        a, b = 0, 0

        output.append([])
        while seznam[i] != [] and seznam[i+1] != []:

            #print('output : ', output)
            a, b = seznam[i][0], seznam[i + 1][0]

            if a < b:
                output[-1].append(seznam[i].pop(0))
            else:
                output[-1].append(seznam[i + 1].pop(0))
        for i in seznam[i]:
            output[-1].append(i)
        if i + 1 < len(seznam):
            for i in seznam[i + 1]:
                output[-1].append(i)

    #print('output1 : ', output)
    if len(seznam) % 2 == 1:
        #print("hello")
        output.append(seznam[-1])
    if len(output) > 1:
        output = superSort(output, first = False)
    #print('output2 : ', output)
    if first:
        return output[0]
    else:
        return output
"""----------------------------"""

seznam = list(range(0, 10**5))

random.shuffle(seznam)

print(seznam)
print()
output = superSort(seznam)
print(output)
