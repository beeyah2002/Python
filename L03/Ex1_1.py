keep_going = 'y'
while keep_going == 'y':
    sale = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))
    commission = sale * comm_rate
    print('The commission rate is $', format(commission, ',.2f'), sep='')

    keep_going = input('Do you want to calculate another' + \
                            'commission (Enter y for yes) : ')