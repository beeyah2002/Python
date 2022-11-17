width = int(input("Enter your width: "))
length = int(input("Enter you length: "))

def sumcount(num1,num2):
    bee = 0
    money = 1000
    count = num1 * num2
    divcount = count // 1600 
    modcount = count % 1600
    if modcount == 0 :
        print(divcount)
        if money > 10000 :
            print("10000")
        else: 
            print(money)
    elif modcount != 0:
        divcount += 1
        print(divcount)
        money *= divcount
        if money > 10000 :
            print("10000")
        else: 
            print(money)
    
        
sumcount(width,length)