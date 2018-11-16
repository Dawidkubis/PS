import math
import os
import time
from copy import deepcopy

primez = []
file = 'primes.txt'

def is_prime (number):#actualize -> divide only by primes
    prime = True

    root = int(math.sqrt(number)) + 1

    for i in range(2, root):
        if number % i == 0:
            prime = False
            break
    return prime

def get_primes(file):
    global primez

    primez = []

    save = open(file,'r')
    for i in save.readlines():
        primez.append(int(i))

    if 2 not in primez:
        primez.append(2)

def flatten(lyst):
    output = []
    for i in lyst:
        if i == []:
            continue
        if (type(i) == list or type(i) == tuple):
            #print('RECURSION')
            #print('if1 : ', output)
            for x in flatten(i):
                output.append(x)
        else:
            output.append(i)
            #print('if2 : ', output)

    return output

def generate_primes_old(lim):
    pass

def generate_primes(lim):
    global primez
    get_primes(file)
    root = int(math.sqrt(lim)) + 1


    primes = [i for i in primez if i < lim]
    nums = list(range(primes[-1]+1,lim + 1))
    #print(nums)
    limyt = len(primes)


    primes = primes + nums

    #print('nums : ',nums)
    #print('limyt : ',limyt)
    #print('root : ', root)
    #print('primes : ',primes)


    for prime in primes:
        if prime > root or primes[limyt:] == []:
            break
        if prime == -1:
            continue
        for num, index in zip(primes[limyt:],range(limyt, len(primes))):
            #print(num,index)
            if num % prime == 0 and not num is prime:
                #print('index : ', index, '|','num : ',num,'|','prime : ',prime)
                primes[index] = -1
    #print('primes : ',primes)

    primes = [i for i in primes if i != -1]

    primes_save(tuple(primes),file)

    return tuple(primes)

def primes_save(primes,file): # add get_primes() and upgrade
    primes = list(primes)
    nums = []
    #print('hey')
    #for i in primes:
    #    if is_prime(i) != True: PRIME CONTROL
    #        raise Exception
    try:
        save = open(file,'r+')
        #print(save)
    except:
        print('oh, fuck')
        raise Exception

    o = save.read()
    nums = o.split('\n')
    #print(nums)

    for i, x in zip(nums,range(len(nums))):
        #print(nums[x] is i)
        #print(i)
        #print(type(i))
        if i == ' ' or i == '\n' or i == '\t' or i == '':
            del nums[x]
            #print('deleting...')
    #print('nums : ' + str(nums))

    for num,x in zip(nums,range(len(nums))):
        nums[x] = int(num)
    #print(nums)

    if len(nums) == 0:
        print('nums is probably blank...')
        save = open(file,'w')
        for prime in primes:
            save.write(str(prime) + '\n')
        return

    save = open(file,'w')

    #print('primes' + str(primes))


    for p in range(len(primes)):
        if primes[p] in nums:
            continue
        for n in range(len(nums)):
            if primes[p] < nums[n]:
                nums.insert(n, primes[p])
                break
            if n + 1 == len(nums):
                nums.append(primes[p])

    del primes
    #print('nums  : '+str(nums) )

    for num in nums:
        save.write(str(num)+'\n')
        #print(num)

    save.close()



def prime_div (num):

    root = int(math.sqrt(num) + 1)
    #print('half : '+str(half))
    primes = generate_primes(root)
    #print('primes' + str(primes))
    divs = []
    for p in primes:
        if num % p == 0:
            divs.append(p)
            t = prime_div(int(num / p))
            for i in t:
                divs.append(i)
            break
    #print(divs)
    if divs == [] and num != 1:
        divs.append(num)

    return tuple(divs)

def multiplication(nums):
    x = 1
    for i in nums:
        x = x*i
    return x

def subsets_old(*sets):
    sets = flatten(sets)
    x = len(sets)
    for i in range(2**x):
        yield [sets[j] for j in range(x) if (i&(1<<j))]

def subsets(*sets):
    sets = flatten(sets)
    pass

def divs(num):
    for i in subsets(prime_div(num)):
        yield multiplication(i)

"""---------------------------------------"""
file = 'primes.txt'
#num = int(input('number : '))
#print(num)
#print(type(num))
divs(128)
