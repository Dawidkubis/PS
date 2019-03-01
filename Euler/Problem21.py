from Prime import prime_div, generate_primes, subsets, is_prime, divs

numbers = list(range(1,100_000))
num = 0
amicable = []
while numbers != []:
    num = numbers[0]
    x = sum(list(set(list(divs(num))))[:-1])
    if sum(list(set(list(divs( x ))))[:-1]) == num and x != num:
        amicable.append(num)
        amicable.append(x)
        numbers.pop(numbers.index(x))
    numbers.pop(0)
