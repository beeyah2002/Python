def findBigestNum(nums):
    bigest = nums[0]
    for i in nums:
        if i > bigest:
            bigest = i
    return(bigest)

listnum = [4,5,17,3,2,9]

print(findBigestNum(listnum))
print(max(listnum))
print(min(listnum))

def find3Sum(nums):
    sum3 = nums[0]
    for i in nums:
        if i % 3 == 0 :
            sum3 += i
    return(sum3)

print(find3Sum(listnum))



