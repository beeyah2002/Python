num = int(input('Enter Number: '))
listb = []
num1 = num

while num1 > 0 :
    
    listb.append(str(num1 % 2))
    num1 = int(num1 / 2)
    
listb.reverse()
print(''.join(listb))