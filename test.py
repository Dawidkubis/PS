#!/usr/bin/python

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



