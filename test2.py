def nmsq(n):
    for x in range(n):
        for y in range(n):
            print(n+y -x,end='')
        print('\n')

while True:
    print(nmsq(int(input('cislo : '))))
