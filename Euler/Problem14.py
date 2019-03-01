def collatz(x):
    yield x
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            x = int(x/2)
            yield x
        else:
            x = 3*x + 1
            yield x

best = 0
besciak = 0

for i in range(1, 1000000):
    x = len(list(collatz(i)))
    print(i, ' --> ', x)
    if x > best:
        best = x
        besciak = i
        #print(best,' --> ',x)

print('best=', best)
print('besiak=', besciak)
