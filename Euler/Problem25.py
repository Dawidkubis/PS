
def fib():
    a = 0
    b = 1
    while True:
        c = a + b
        yield c
        a = b
        b = c

x = 2
for i in fib():
    if len(str(i))>=1000:
        break
    x += 1
print(x)
