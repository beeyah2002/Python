'''


def main():
    try:
        hours = int(input('How many hours did you work? '))
        pay_rate = float(input('Enter your hourly pay rate: '))
        gross_pay = hours * pay_rate
        print("Gross pay: $", format(gross_pay, '.2f'), sep='')
    except ValueError:
        print('Error: Hours woe=rked and hourly pay rate must')
        print('be valid integers.')
main()




def main():
    filename = input('Enter a flie: ')
    try:
        infile =  open(filename, 'r')
        contents = infile.read()
        print(contents)
        infile.close()
    except IOError:
        print("An error occurred trying to read")
        print('the file', filename)

main()
'''

def main():
    try:
        hours = int(input('How many hours did you work? '))
        pay_rate = float(input('Enter your hourly pay rate: '))
        gross_pay = hours * pay_rate
        print("Gross pay: $", format(gross_pay, '.2f'), sep='')
    except ValueError as err:
        print(err)
        
main()