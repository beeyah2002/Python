#This propgram calculates gross pay.

'''
def main():
    #Get the number of hours worked.
    hours = int(input('How many hours did you work? :'))

    #Get the hourly pay rate.
    pay_rate = float(input('Enter your hourly pay rate: '))
    
    #Calculate the gross pay.
    gross_pay = hours * pay_rate
    
    #Display the gross pay 
    print("Gross pay: $", format(gross_pay, '.2f'), sep='')
    
main()





#This propgram calculates gross pay.
def main():
    try:
        #Get the number of hours worked.
        hours = int(input('How many hours did you work? '))
        #Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))
        #Calculate the gross pay.
        gross_pay = hours * pay_rate
        #Display the gross pay 
        print("Gross pay: $", format(gross_pay, '.2f'), sep='')
    except ValueError:
        print('Error: Hours woe=rked and hourly pay rate must')
        print('be valid integers.')
main()


'''


'''
#This program displays the contents
#of a file.
def main():
    #Get the name of a file.
    filename = input('Enter a flie: ')
    try:
        #Open the file.
        infile =  open(filename, 'r')
        #Read the file's contents.
        contents = infile.read()
        #Display the file's contents.
        print(contents)

        #Close the file.
        infile.close()
    except IOError:
        print("An error occurred trying to read")
        print('the file', filename)

#Call the main function.
main()


'''

#This program displays the contents
def main():
    try:
        #Get the number of hours worked.
        hours = int(input('How many hours did you work? '))
        #Calculate the gross pay.
        pay_rate = float(input('Enter your hourly pay rate: '))
        #Display the gross pay
        gross_pay = hours * pay_rate
        print("Gross pay: $", format(gross_pay, '.2f'), sep='')
    except ValueError as err:
        print(err)

#Call the main function.     
main()







