
bee = [19,5,45,2,77]
def  sumTwoSmallestNums(num):
    listA= []
    for i in num:
        if i > 0 :
            listA.append(i)
    cat = sorted(listA)
    count = cat[0] + cat[1]
    print(count)
    
            




sumTwoSmallestNums(bee)