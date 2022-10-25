#This program calculate the gross pay for 
#each of Magan's baristas.

#NUM_EMPLOYEE is osed as a constant for the 
#size of the list
NUM_EMPLOYEE = 6 

def main():
    #Cerate a list to hold employee hours.
    hours = [0] * NUM_EMPLOYEE
    for index in range(NUM_EMPLOYEE):
        print('Enter the hours worhed by employee: ',index + 1, ': ',sep='',end='')
        hours[index] = float(input())

    #Gat the hourly pay rate.
    pay_rate = float(input('Enter the hourly pay rate : '))
    
    #Displays eacg employee's gross pay.
    for index in range(NUM_EMPLOYEE):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ' , index + 1, ': $', format(gross_pay, ',.2f'), sep='')

#call the main function.
main()