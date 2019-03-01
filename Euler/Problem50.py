from Prime import is_prime, generate_primes

def possible_lenghts(nums):
    result = []
    for i in range(len(nums)):
        result.append(nums[:])
        nums.pop(0)
    return result

def main():
    primes = generate_primes(4_000)
    best = 0

    for i in range(1, len(primes)):
        for x in possible_lenghts(primes[:i]):
            sumec = sum(x)
            if is_prime(sumec) and len(x) > best:
                best = len(x)

                print(sumec, ' ---> ', best)

main()
