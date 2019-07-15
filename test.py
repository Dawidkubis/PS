#!/usr/bin/python
from sys import argv
from subprocess import * 

print('well, hello there')
print('nice')

def maxwell (name):
    output = []
    for x in range(len(name)):
        output.insert(0,name[x])
    x = ''
    for i in output:
        x = x+str(i)
    return x
print('lol')
for i in range(100):
    print(i)

def retart(a,b,c):
    return a+b+c*(a-b+c)

for i in range(100):
    print(retart(i, i/2, i/3))

for i in range(100):
    print(sys.argv)
