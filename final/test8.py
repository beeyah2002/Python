


bee = ([3,2,3],9)
def simplepair(num):
    count = num[0]
    
    if count[0] * count[1] == num[1]:
        print("[ %d , %d ]" %(count[0], count[1]))
    elif count[1] * count[2] == num[1]:
        print("[ %d , %d ]" %(count[1], count[2]))
    elif count[0] * count[2] == num[1]:
        print("[ %d , %d ]" %(count[0], count[2]))
    else:
        print("none")



simplepair(bee)