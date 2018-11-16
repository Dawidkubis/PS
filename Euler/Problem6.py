def arraySum(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    return sum

def array_sqrt(arr):
    answer = []
    for i in arr:
        answer.append(i**2)

    return answer
x = []
for i in range(1,101):
    x.append(i)

y = array_sqrt(x)

print(x,y)

x = arraySum(x)
x = x ** 2
y = arraySum(y)

print(x,y)

print('difference : ' + str(abs(x-y)))
