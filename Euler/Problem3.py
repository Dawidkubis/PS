import math

def isprime (number):
    prime = True

    root = math.sqrt(number)
    root = int(root)

    for i in range (2,root + 1):
        if number % i == 0:
            prime = False
            break
    return prime

number = 600851475143
root = math.sqrt(number)

root = int(root)

print(root)

primes = []

for i in range(2,root):
    if isprime(i) == True:
        primes.append(i)
        #print(i)

result = 0
for i in primes:
    if number % i == 0:
        result = i

print('the result is = '+str(result))
