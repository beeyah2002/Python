'''
a, b, c = input().split()
print(a,b,c)


name = input('Enter your first name: ')
lastname = input("Enter your last name: ")
ID_num = input("Enter your student ID number: ")
print('Your system login name is :',name[:3]+lastname[:3]+ID_num[-3:])

city = 'Boston'
index = 0
while index < len(city):
    print(city[index])
    index += 1

fruit = 'apple'
print(fruit.upper())


again ='y'
while again.lower()  == 'y':
    print("hello")
    print("Do you want to see that again?")
    again = input('y = yes anything else = no: ')


print( 'I    ' + 'love   '   +  ' python.'   )
print("I" +  "     love" + "    python")
print("I" + "love" + 'python')

print('-' * 20)
supernice = "nice  " * 3
print(supernice)
print( '-' * 20)

print('I   {}  python.    '.format('   love  '))
print('{}    {}    {}  '.format("I",    'love',     'python. '))


print("  I  {0}   {1}. {1}    {0}s    me."  .format('love' , 'python'))


first = 'I'
second = 'love'
third = 'Python'
print('   {}   {}    {} . '  .format(first,  second,  third))


print('  {0:8}   |    {1:>8}  ' .format('Friut'  , 'Quantity' ))
print('  {0:8}   |    {1:>8.2f}  ' .format('apple', 3.5555))
'''



