print('HANDCRAFTED BEVERAGES')
print("==============================================")
print("ESPRESSO \t \t 12 Oz \t 16 Oz \t 20 Oz ")
print("Caffe' Latte \t \t 110 \t 125 \t 140")
print("Capuccino \t \t 110 \t 125 \t 140")
print("Caffe' moccha \t \t 125 \t 140 \t 155")
print("Caramel Macchiato \t 135 \t 150 \t 165")
print("White Chocolate Mocha  \t 135 \t 150 \t 165")
print("caffe' Americano  \t 100 \t 115 \t 130")
print('COFFEE')
print('==============================================')
print('Frechly Brewed Coffee  \t 100 \t 115 \t 130')
print('CHOCOLATE')
print('==============================================')
print('Signature Chocolate  \t 125 \t 140 \t 155')
print('_______________________________________________')
print('CUSTOMIZE ANY DRINK')
print('-Flavor +15 bath/drink \n vanila, Hazelnut, Caramel, Rasberry or Sugar-Free Vanila')
print('-Espresso Shot + 15 bath/shot\n-Soy +15 bath/drink \n')


print('press 1 = Caffe\' Latte \npress 2 = Capuccino \npress 3 = Caffe\' mocha \npress 4 = caramel macchiato \npress 5 = White Chocolate Mocha \npress 6 = Caffe\' Americano ')
print('-press 7 = Freshly Brewed Coffee \npress 8 = Signature Chocolate')
count = 'y'
while count == 'y':
    main = int(input("what drink : "))
    if main == 1  :
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 110 
        elif cup == 2:
            pay = 125
        elif cup == 3:
            pay = 140

    if main == 2 :
        ch = 'Caffe\' Latte'
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 110 
        elif cup == 2:
            pay = 125
        elif cup == 3:
            pay = 140

    if main == 3:
        ch = 'Capuccino'
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 125 
        elif cup == 2:
            pay = 140
        elif cup == 3:
            pay = 155

    if main == 4:
        ch = 'Caramel Macchiato'
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 135 
        elif cup == 2:
            pay = 150
        elif cup == 3:
            pay = 165

    if main == 5:
        ch = 'White Chocolate Mocha'
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 135 
        elif cup == 2:
            pay = 150
        elif cup == 3:
            pay = 165 

    if main == 6:
        ch = 'caffe\' Americano '
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 100 
        elif cup == 2:
            pay = 115
        elif cup == 3:
            pay = 130       

    if main == 7:
        ch = 'Freshly Brewed Coffee'
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 100 
        elif cup == 2:
            pay = 115
        elif cup == 3:
            pay = 130   

    if main == 8:
        ch = 'Freshly Brewed Coffee'
        print('press 1  = 12 Oz\npress 2 = 16 Oz\npress 3 20 Oz \n')
        cup = int(input('What size do you want? : '))
        if cup == 1:
            pay = 125
        elif cup == 2:
            pay = 140
        elif cup == 3:
            pay = 155   
    print('any thing alse ?\npress 1 for')    
    anything = ()
    record = open('recordcoffee.txt', 'a')
    rec1 = record.write(ch)







