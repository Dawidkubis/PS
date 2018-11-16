numeros = []

def flip(list):
    new = []
    for i in list:
        new.insert(0,i)

    #print(new)
    return new

def is_palindrome(number):
    number = str(number)
    is_palindrome = True
    index = 0
    for letter in number:
        #print(index)
        #print(letter + ' : ' + number[-(index + 1)])
        if letter != number[-(index + 1)]:
            is_palindrome = False
            break
        index = index + 1
    return is_palindrome

for i in range(100,1000):
    numeros.append(i)

#print(numeros)

numeros = flip(numeros);
numeros_copy = numeros[:]

results = []

for a in numeros:
    for b in numeros_copy:
        if a*b<900000:
            break
        results.append(a*b)

#print(results)

#for result in results:
    #print(result)

for result in results:
    if is_palindrome(result) == True:
        print(result)
        break
