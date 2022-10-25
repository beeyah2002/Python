'''
#This program simulates 10 tosses of a coin.
import random

#Constants
HEADS = 1
TALLS = 2
TOSSES = 10

def main():
    for toss in range(TOSSES):
        if random.randint(HEADS,TALLS) == HEADS:
            print('Heads')
        else:
            print('Tails')

#call the main fuction
main()





DISCOUNT_PERCENTAGE = 0.20

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - discount(reg_price)
    print("The sale price is $", format(sale_price, ',.2f'), sep=" ")

def get_regular_price():
    price = float(input("Enter the item's regular price "))
    return price

def discount(price):
    return price * DISCOUNT_PERCENTAGE
main()

'''









def get_name():
    first = input('Enter your first name : ')
    last = input('Enter tour last name: ')
    return first,last

first_name, last_name = get_name()
print('First name:', first_name, ' last name :' ,last_name)
