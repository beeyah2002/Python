money = int(input("Enter your first money : "))

keep1 = 0
keep2 = 0
keep3 = 0
if money <= 20000 or money > 100:
    if money >= 1000:
        mon1000 = money // 1000
        mod = money % 1000
        
        keep1 += mon1000
    else:
        keep1 += 0
    if mod >= 500:
        mod500 = mod // 500
        mod = mod % 500
        
        keep2 += mod500
    else:
        keep2 += 0
    if mod >= 100:
        mon100 = mod // 100
        mod = mod % 100
        
        keep3 += mon100
    else:
        keep3 += 0
else:
    print("you need to press more money")

money2 = int(input("Enter your second money (don't want to make order press [0]) :"))
if money2 == 0:
    pass
elif money2 < 100 :
    pass

elif money2 <= 20000 :
    if money2 >= 1000:
        mon21000 = money2 // 1000
        mod2 = money2 % 1000
        #print(mon21000)
        keep1 += mon21000
    else:
        print("0")
    if mod2 >= 500:
        mon2500 = mod2 // 500
        mod2 = mod2 % 500
        #print(mon2500)
        keep2 += mon2500
    else:
        print("0")
    if mod2 >= 100:
        mon2100 = mod2 // 100
        mod = mod2 % 100
        #print(mon2100)
        keep3 += mon2100
    else:
        print("0")
else:
    print("you need to press more money")



print(keep1)
print(keep2)
print(keep3)