print("please select operation - ")
print(" 1 = add + \n 2 = subtract- \n 3 = multiply * \n 4 = divide /")
select = int(input("select number to calculate: " ))
num1 = int
num2 = int

if select == 1:
    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))  
    print(" %d + %d = %d " % (num1 ,num2, num1 + num2))
elif select == 2:
    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))  
    print(" %d - %d = %d " %(num1 , num2 ,num1 - num2))
elif select == 3:
    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))  
    print(" %d x %d = %d " %(num1 ,num2,num1 * num2))
elif select == 4:
    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))  
    print(" %d / %d = %d " %(num1,num2,num1 / num2))
else:
    print('WTF')
