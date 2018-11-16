def multiply_arr(arr):
    x = 1
    for i in arr:
        x = x * i
        #print(x)
    return x

def int_to_arr(num):
    num = str(num)
    arr = []
    #print(num)

    for i in num:
        arr.append(int(i))

    return arr

nums = 9874715852386
nums = int_to_arr(nums)
print(multiply_arr(nums))
