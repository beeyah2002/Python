
listA = [4,2,4],[3,3,3],[1,1,2],[2,1,1]
count = 1
bee = 0
lenlist = len
def totalVolume(listA):
    global count , bee
    
    for i in listA:
        for j in i :
            count *= j
            
            print(count)
        bee += count
        print(bee)


totalVolume(listA)

