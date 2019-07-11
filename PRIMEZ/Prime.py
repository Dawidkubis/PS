#!/usr/bin/python -i
import math
import os
import time
from copy import deepcopy
from functools import reduce

def is_prime (number):
    prime = True

    root = int(math.sqrt(number)) + 1

    for i in generate_primes(root):
        if number % i == 0:
            prime = False
            break
    return prime
'''
def flatten_old(lyst):
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
'''
def flatten(lst):
    result = deepcopy(lst)

    i = 0
    while i < len(result) + move:

        if type(result[i]) in (list, tuple):
            print(result[i])
            temp = result.pop(i)
            result = result + temp
            i -= len(temp)

        i += 1
    return result


def generate_primes(lim):
    primes = []
    nums = list(range(2, lim))
    while nums != []:
        primes.append(nums[0])
        nums = [i for i in nums if i%primes[-1] != 0]
    return primes

def prime_div(num):
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

def subsets(*sets):
    #sets = flatten(sets)
    x = len(sets)
    for i in range(2**x):
        yield [sets[j] for j in range(x) if (i&(1<<j))]

def divs(num):
    for i in subsets(*prime_div(num)):
        if i == []:
            yield 1
            continue
        yield reduce((lambda a,b:a*b), i)

"""---------------------------------------"""
#num = int(input('number : '))
#print(num)
#print(type(num))
