'''
bee = 'y'
while bee == 'y':
    wholesales = float(input("Enter the item's whole sale cost: "))
    retial_price = wholesales * 2.5
    print("retial price is %.2f " %(retial_price))
    bee= input("Enter y for yes : ")
'''
'''
rows = int(input("How many row: "))
column = int(input("How many column: "))
for i in [rows]:
    print('*' * i * column)
'''
'''
score = int(input("enter a test score : "))
while score < 0 or score > 100:
    print("Error: The score cannot be nagative" )
    print('or greater than 100.')
    score = int(input('Enter the correct score : '))
''''''
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(hour , ':', minute, ':', second)
'''
for letter in 'Teeraporn Petcgrote' :
    if letter  == 'e' or letter == 'P':
        pass
    print('current letter :', letter)
