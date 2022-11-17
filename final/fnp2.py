keep0 = 0
keep1 = 0
keep2 = 0
keep3 = 0
keep4 = 0
keep5 = 0
keep6 = 0
keep7 = 0
keep8 = 0
keep9 = 0
num = int(input('Enter number:'))
while num < 10 and num > -1:
    
    if  num == 0 :
        keep0 += 1
    elif  num == 1 :
        keep1 += 1
    elif  num == 2 :
        keep2 += 1
    elif  num == 3 :
        keep3 += 1
    elif  num == 4 :
        keep4 += 1
    elif  num == 5 :
        keep5 += 1
    elif  num == 6 :
        keep6 += 1
    elif  num == 7 :
        keep7 += 1
    elif  num == 8 :
        keep8 += 1
    elif  num == 9 :
        keep9 += 1
    if num > 10 and num <= -1:
        break
    num = int(input('Enter number:'))
print("0 = " ,keep0)
print("1 = " ,keep1)
print("2 = " ,keep2)
print("3 = " ,keep3)
print("4 = " ,keep4)
print("5 = " ,keep5)
print("6 = " ,keep6)
print("7 = " ,keep7)
print("8 = " ,keep8)
print("9 = " ,keep9)

