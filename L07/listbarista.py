NUM_EMPLOYEE = 6 

def main():
    hours = [0] * NUM_EMPLOYEE
    for index in range(NUM_EMPLOYEE):
        print('Enter the hours worhed by employee: ',index + 1, ': ',sep='',end='')
        hours[index] = float(input())
    pay_rate = float(input('Enter the hourly pay rate : '))
    for index in range(NUM_EMPLOYEE):
        gross_pay = hours[index] * pay_rate
        print('Gross pay for employee ' , index + 1, ': $', format(gross_pay, ',.2f'), sep='')

main()