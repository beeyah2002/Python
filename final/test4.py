
listA = [4,2,4],[3,3,3],[1,1,2],[2,1,1]
count = 1
bee = 0
sumcout = 0
listkeep = []

def totalVolume(listB):
    global count,bee,sumcout,listkeep
    for i in listB:
        while  bee < len(i):
            count *= i[bee]
            bee += 1   
listkeep.append(count)
totalVolume(listA)

