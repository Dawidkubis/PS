from math import *

def generate_primes(lim):
    primes = []
    nums = list(range(2,lim + 1))
    #print(nums)

    while nums != []:
        num = nums[0]
        primes.append(num)
        for x,y in zip(nums,range(len(nums))):
            if x % num == 0 :
                del nums[y]

        #print(nums)

    #print(primes)


    return tuple(primes)

def multiples(start,end,number):
    """Finds how many multiples of 'number' are between start and end. Start is not in the interval, end is"""

    answer = 0


    dif = abs(end - start)
    #print('dif : ',dif)
    if dif < number:
        raise Exception

    a, b = start % number, end % number
    #print('a, b : ', a,'|', b)

    #if a == b:
    #    answer = dif/number
    #    return answer
    answer = (dif - b + a) / number
    return int(answer)

def BF_multiples(start,end,number):
    """Brute force version of the multiples function, goes through all the numbers and checks if they are multiples"""
    nums = []

    for i in range(start + 1,end + 1):
        if i % number == 0:
            nums.append(i)

    return len(nums)

def subsets(sets):
    x = len(sets)
    for i in range(2**x):
        yield [sets[j] for j in range(x) if (i&(1<<j))]

def multiplication(nums):
    x = 1
    for i in nums:
        x = x*i
    return x

def interval_primes(start, end):
    """Checks the amount of primes there are between start and end. Start is not in the interval, end is"""
    root = int(sqrt(end)) + 1
    primes = generate_primes(root)
    subs = subsets(primes)
    dif = end - start
    print('subs',[i for i in subs])

    for i in subs:
        x = multiplication(i)
        if len(i) % 2 == 0:
            dif = dif + x
        else:
            dif = dif - x

    return dif

start, end, number = 30, 90, 5

print(multiples(start, end, number))
print(BF_multiples(start, end, number))
