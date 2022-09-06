x = 15
y = 2
print('x + y = ' ,x+y )
print('x - y =' ,x-y)
print('x * y =' ,x*y)
print('x / y =' , x/y)
print('x % y =' ,x%y)
print('x // y =' , x//y)
print('x ** y = ',x**y)



x = 10
y = 12
print( 'x > y is' ,x>y)
print( 'x < y is' , x<y)
print( 'x == Y is' ,x==y)
print( 'x != y is' ,x!=y)
print( 'x >= y is' ,x>=y)



x = True
y = False
print( ' x and y is ' , x and y)
print( ' x or y is' , x or y)
print( ' not x is' , not x)


x1 = 5 
y1 = 5
x2 = 'hello'
y2 = 'hello'
x3 = [ 1,2,3]
y3 = [1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)

x = 'Hello world'
y = {1 : 'a', 2 : 'b'} 
print('H' in x )
print('hello' not in x)
print(1 in y)
print('a' in y)

first_name = input('Enter your first name: ')
last_name = input("Enter your last name: ")
print('hello' ,first_name,last_name)

name = input('What your name? ')
age = int(input('What is your age? '))
income = float(input('what is your income' ))

print('Here is the data you entered: ') 
print('name:', name)
print('age: ' , age)
print('Income: ' , format(income, '12,.2f'))


a,b,c = input().split()
print("a = " ,a)
print("b = " , b)
print("c = " ,c)

a,b,c = [int(e) for e in input().split()]
print("a = " ,a)
print("b = " ,b)
print('c = ' ,c)

a,b,c = [float(e) for e in input().split()]
print("a = " ,a)
print("b = " ,b)
print('c = ' ,c)