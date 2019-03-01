import math
from functools import reduce
from Prime import generate_primes, prime_div

def generate_tris():
    sum = 0
    max = 1
    while True:
        sum += max
        yield sum
        max += 1

def count_divs(prime_divs):
    x = 1
    for i in set(prime_divs):
        x *= prime_divs.count(i)+1

    return x

for i in generate_tris():
    x = count_divs(prime_div(i))
    print(i, ' --> ', x)
    if x > 500:
        print('THE NUMBER UR LOOKIN FOR IS ... ', i)
        break
