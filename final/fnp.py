station = int(input("enter your station: "))
if station > 3:
    print("You choose station wrong!!")
else: 
    if station == 1:
        money = int(input("Enter your money: "))
        if money > 27:
            count = money - 27
            if count >= 10 :
                count10 = count // 10 
                mod = count % 10
                print(count10)
            else:
                print('0')
            if mod >= 5:
                count5 = mod // 5
                mod = mod % 5
                print(count5)
            else:
                print('0')
            if mod >= 2 :
                count2 = mod // 2
                mod = mod  % 2
                print(count2)
            else:
                print('0')
            if mod < 2 :
                count1 = mod // 1
                mod = mod % 1
                print(count1)
            else:
                print('0')
        else:
            print("You need to pay more than fare ")
    elif station == 2:
        money = int(input("Enter your money: "))
        if money > 35:
            count = money - 35
            if count >= 10 :
                count10 = count // 10 
                mod = count % 10
                print(count10)
            else:
                print('0')
            if mod >= 5:
                count5 = mod // 5
                mod = mod % 5
                print(count5)
            else:
                print('0')
            if mod >= 2 :
                count2 = mod // 2
                mod = mod  % 2
                print(count2)
            else:
                print('0')
            if mod < 2 :
                count1 = mod // 1
                mod = mod % 1
                print(count1)
            else:
                print('0')
        else:
            print("You need to pay more than fare ")

    elif station == 3:
        money = int(input("Enter your money: "))
        if money > 42:
            count = money - 42
            if count >= 10 :
                count10 = count // 10 
                mod = count % 10
                print(count10)
            else:
                print('0')
            if mod >= 5:
                count5 = mod // 5
                mod = mod % 5
                print(count5)
            else:
                print('0')
            if mod >= 2 :
                count2 = mod // 2
                mod = mod  % 2
                print(count2)
            else:
                print('0')
            if mod < 2 :
                count1 = mod // 1
                mod = mod % 1
                print(count1)
            else:
                print('0')
        

