#This program uses recursion to xalculate
#the facturial of a number
def main():
    #gat a number from the user.
    number = int(input('Enter a nonnegative integer: '))

    #Get the facturial of the number.
    fact = facturial(number)

    #Display the facturial.
    print('The facturial of' ,number, 'is' ,fact)


#The facturial function uses recursion to
#calculate the facturail if it's argument,
#which is a assumed to be nonnegative.
def facturial(num):
    if num == 0 :
        return 1
    else:
        return num * facturial(num-1)
#call the main function.
main()