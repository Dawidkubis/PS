def find_LCM(nums):
    t = False
    x = 1
    while t == False:
        print(x)
        t = True
        for num in nums:
            if x % num != 0:
                t = False
                break
        if t == False:
            x = x + 1
            continue
        else:
            print('answer : '  + str(x))
            break



nums = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
#find_LCM(nums)
print(find_LCM(nums))
