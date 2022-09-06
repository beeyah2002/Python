def main():
    num_emp = int(input('How many employee records ' +\
                'do you want to create? '))

    emp_file = open('employee.txt','w')
    for count in range(1,num_emp +1 ):
        print('Enter data for employee#', count, sep='')
        name = input('Name: ')
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')

        print()
    emp_file.close()
    print('Employee records written to employee.txt')

main()

        
