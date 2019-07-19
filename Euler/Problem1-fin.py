
nums = []


for num in range(1,1000):
    if num%3==0 or num%5 == 0:
        nums.append(num)
        #print(num)

#print(nums)

suma = 0

for num in nums:
    suma = suma + num

print(suma)
