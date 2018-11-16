import math
import os

def isprime (number): #actualize (divide only by primes)
    prime = True

    root = math.sqrt(number)
    root = int(root) + 1

    for i in range (2, root):
        if number % i == 0:
            prime = False
            break
    return prime

#def get_primes():      add it

def generate_primes(lim):   # add funcition get_primes
    primes = []
    nums = list(range(2,lim + 1))
    #print(nums)

    while nums != []:
        num = nums[0]
        if isprime(num):
            primes.append(num)
            for x,y in zip(nums,range(len(nums))):
                if x % num == 0 :
                    del nums[y]

        #print(nums)

    #print(primes)

    #primes_save(tuple(primes),'primes.txt')

    return tuple(primes)

def primes_save(primes,file):
    primes = list(primes)
    nums = []
    #print('hey')
    for i in primes:
        if isprime(i) != True:
            raise Exception
    try:
        save = open(file,'r')
        #print(save)
    except:
        print('oh, fuck')
        raise Exception

    o = save.read()
    nums = o.split('\n')
    #print(nums)

    for i,x in zip(nums,range(len(nums))):
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

    if isprime(num):
        return num,

    half = int(num / 2) + 1
    #print('half : '+str(half))
    primes = generate_primes(half)
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
    return tuple(divs)

def divs(num): # find a good way to find all of them
    prime_divs = prime_div(num)

"""---------------------------------------"""

x = generate_primes(2000000)
y = 0
for i in x:
    y = y + i

print(y)
