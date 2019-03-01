from itertools import permutations
from functools import reduce

numbers = [0,1,2,3,4,5,6,7,8,9]
pms = list(permutations(numbers))

print('\nReSUlt --> ', reduce((lambda a,b:a+b),[str(i) for i in pms[999_999]]))d
