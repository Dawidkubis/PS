import random
import math
from copy import deepcopy
import time

"""----------------------------"""

# def start(seznam):
#
#     output = []
#     for i in range(0,len(seznam),2):
#         #print(i)
#         output.append([seznam[i]])
#
#         if i + 1 != len(seznam):
#             output[-1].append(seznam[i+1])
#
#             if output[-1][0] > output[-1][1]:
#
#                 output[-1][0],output[-1][1] = output[-1][1],output[-1][0]
#
#     return output

# def weld(seznam):
#     #o = start(seznam)
#     output = ssf(o)
#     #print('output : ',output)
#     return output[0]

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
        #print('SEZNAM :', seznam)

        output.append([])
        while seznam[0] != [] and seznam[1] != []:
            #print('seznamy :', seznam[0], seznam[1])

            #a,b = seznam[0][0], seznam[1][0]

            if seznam[0][0][0] < seznam[1][0][0]:
                if len(output[-1]) != 0:
                    if seznam[0][0][0] < output[-1][-1][0] or seznam[0][0][1] > output[-1][-1][1]:
                        output[-1].append(seznam[0].pop(0))
                    else:
                        seznam[0].pop(0)
                else:
                    output[-1].append(seznam[0].pop(0))
            else:
                if len(output[-1]) != 0:
                    if seznam[1][0][0] < output[-1][-1][0] or seznam[1][0][1] > output[-1][-1][1]:
                        output[-1].append(seznam[1].pop(0))
                    else:
                        seznam[1].pop(0)
                else:
                    output[-1].append(seznam[1].pop(0))

        #print()
        #print('OUTPUT1 :', output)
        if seznam[0] != []:
            #print('out of:', seznam[0][0], seznam[0][0][0], output[-1])
            while seznam[0] != [] and seznam[0][0][0] > output[-1][-1][0] and seznam[0][0][1] <= output[-1][-1][1]:
                seznam[0].pop(0)
            for i in seznam[0]:
                output[-1].append(i)
        else:
            #print('index', seznam[1][0][0], output[-1][0])
            while seznam[1] != [] and seznam[1][0][0] > output[-1][-1][0] and seznam[1][0][1] <= output[-1][-1][1]:
                seznam[1].pop(0)
            for i in seznam[1]:
                output[-1].append(i)

        #print('seznam', seznam)
        #print(seznam[0], seznam[1])
        del seznam[1], seznam[0]

        #print('output2 :', output)

    #print('output3 :', output)
    if zbytek != []:
        output.append(zbytek)
    #print('output : ',output)
    #print('len(output) : ',len(output))
    if len(output) > 1:
        #print('REKURZE')
        output = ssf(output)
        return output
    else:
        return output[0]

def primes(limit):
    number = 1
    primelist = []
    prime = 1
    while True:
        prime += 1
        isprime = True
        for i in primelist:
            if prime % i == 0:
                isprime = False
                break

        if number > limit:
            primelist.pop(0)
            primelist.pop(-1)
            return tuple(primelist)
        if not isprime:
            continue
        if isprime:
            primelist.append(prime)
            number = number * prime

def main(limit):
    then = time.time()
    primelist = primes(limit)
    print('primelist', primelist)
    numberlist = []
    for i in range(0, math.floor(math.log(limit, 2) + 1)):
        numberlist.append([2**i, i + 1, [i]])
    #print('z', numberlist)
    for prime in primelist:
        oldnumberlist = deepcopy(numberlist)
        numberlist = [[]]
        for number in oldnumberlist:
            #print(number)
            #print('zbyva :', number, math.floor(math.log(limit / lastprime ** number[2][-1], prime)))
            #print('prime ** exp', lastprime ** number[2][-1])
            #print('limit', limit)
            add = deepcopy(number)
            add[2].append(0)
            numberlist[0].append(add)

            numberlist.append([])
            #print('numberlist', numberlist)
            #print('number', number)
            exp = 1
            while exp <= number[2][-1] and number[0] * prime ** exp < limit:
                add = deepcopy(number)
                add[0] = add[0] * prime ** exp
                add[1] = add[1] * (exp + 1)
                add[2].append(exp)
                numberlist[-1].append(add)
                exp += 1
            if numberlist[-1] == []:
                numberlist.pop(-1)
            # print('numberlist')
            # for i in numberlist:
            #     print(i)
            #print('x', numberlist)
        #print()
        #print('VSTUP :', numberlist)
        #print()
        numberlist = ssf(numberlist)
        print('prime', prime, 'len', len(numberlist))
        #print('po serazeni :', numberlist)
    print('TIME :', time.time()-then)
    return numberlist

"""----------------------------"""
