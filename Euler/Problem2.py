fib = []
fib_even = []
a = 0
b = 1
while a + b < 4000000:
    c = a + b
    fib.append(c)
    a = b
    b = c

for i in fib:
    print(i)


for i in fib:
    if i % 2 == 0:
        fib_even.append(i)

for i in fib_even:
    print(i)    

sum = 0

for i in fib_even:
    sum = sum + i



print('--------------------------')
print('sum = ' + str(sum))
