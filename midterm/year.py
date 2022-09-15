
num = int(input('enter num : '))
num1 = str(num)
lennum = len(num1)
bee = num + 543
bee1 = str(bee)
print(bee1)
B = 0
D = 0
beelen = len(bee1)
while lennum > 0 :
    total1 = num1[lennum -1]
    C = int(total1)
    D += C
    lennum -= 1
print(D)

while beelen > 0:
    total = bee1[beelen-1]
    A = int(total)
    B += A
    beelen -= 1 
print(B)

