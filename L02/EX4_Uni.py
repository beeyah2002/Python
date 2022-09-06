print("Please select Operation")
print(" 1. Add + \n 2. Subtract - \n 3. Multiply * \n 4. Divide /")
select = int(input("Select oparation form 1, 2, 3, 4: "))
if select == 0 or select >= 5:
    print("operation Error")
else:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number:  "))
    if select == 1:
        total = number_1 + number_2
        print(" %d + %d = %d " %(number_1,number_2,total))
    elif select == 2:
        total = number_1 - number_2
        print(" %d - %d = %d " %(number_1,number_2,total))
    elif select == 3:
        total = number_1 * number_2
        print(" %d x %d = %d " %(number_1,number_2,total))
    elif select == 4:
        total = number_1 / number_2
        print(" %d / %d = %d " %(number_1,number_2,total))




    
