emp = open('employee.txt','r')
search = input('Enter name: ')
line = emp.readline()
while line != '':
    
    if line.strip() == search:
        print('name: ',line.rstrip())
        line = emp.readline()
        print('ID:',line.rstrip())
        line = emp.readline()
        print('dept:',line.rstrip())
    line = emp.readline()
emp.close()
    
   

    
