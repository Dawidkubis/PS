import string

file = open('euler_names.txt','r')
names = file.read()
file.close()

def rate(name):
    alpha = list(string.ascii_uppercase)
    result = []
    for letter in name:
        result.append(alpha.index(letter)+1)

    return result

names = names.replace('"','').split(',')
names = sorted(names)

print('\nRESULT --- > ', sum([sum(rate(i))*(x + 1) for i, x in zip(names, range(len(names)))]))
