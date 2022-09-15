num = (input('enter binary: '))
lennum = len(num)
list1 = []
g = 0
KEEP = 0
while lennum > 0:
    bee = int(num[lennum - 1])
    keep1 = bee * (2**g)
    g += 1
    KEEP += keep1
    lennum -= 1
print(KEEP)




