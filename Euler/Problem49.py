from itertools import permutations
from functools import reduce
from Prime import is_prime, generate_primes

def main():
    for i in [i for i in generate_primes(10_000) if i > 1_000]:
        #print(i)
        primes = [i for i in [reduce((lambda a, b: int(str(a)+str(b))), i) for i in form(i)] if is_prime(i)]
        if len(primes) > 2:
            for x in primes:
                if ((x - i) + x) in primes:
                    print(i, ' | ', x, ' --> ', ((x - i) + x))
                    break


def form(num):
    return [tuple([int(x) for x in str(i)]) for i in sorted([int(reduce((lambda a,b : str(a) + str(b)), i)) for i in list(permutations([int(i) for i in str(num)]))]) if i > num]



main()
