'''
for i in range(1,3):
    for j in range(2,5):
        print(i,j)
'''
'''
for i in range(4):
    for j in range(i):
        print( i,j)
'''
'''
k = 4
while k < 100 :
    print(k)
    k += 2
'''
'''
max = 5
total = 0.0
print(("This program calculate the sum of"))
print(max, 'numbers you will enter.')
for couter in range(max):
    number = int(input('Enter a number: '))
    total = total + number 
print('The total is' , total)
'''
'''
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for val in numbers:
    sum += val
    print(sum)
print("the sum is" ,sum)
'''
'''
rows = int(input("How many rows? :"))
columns = int(input("How many columns?:"))
for i in range(rows):
    star = '*' * columns
    print(star)
'''
'''
score = int(input("Enter test score: "))
while score < 0 or score > 100:
    print('Error: the score cannot be negative')
    print('or greater than 100.')
    score = int(input('Enter the correct score: '))
'''
'''
for hour in range(24):
    for minute in range(60):
        for second in range(60):
            print(hour,':' ,minute, ':', second)
'''

'''    
for letter in 'Teeraporn Petchrote' :
    if letter == 'e' or letter == 'o':
        continue
    print('Current letter :' , letter)
'''





number = int(input('Enter number: '))
for i in range(1,101):
    print(i,end=" ")
    if i % number == 0:
       print('\n')
