def main():
    number = int(input('Enter a nonnegative integer: '))

    fact = facturial(number)
    print('The facturial of' ,number, 'is' ,fact)

def facturial(num):
    if num == 0 :
        return 1
    else:
        return num * facturial(num-1)
main()