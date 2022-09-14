def main():
    emp = open('employee.txt','r')

    line = emp.readline()
    while line != '':
        print('name: ',line.rstrip())
        line = emp.readline()
        print('ID:',line.rstrip())
        line = emp.readline()
        print('dept:',line.rstrip())
        line = emp.readline()
    emp.close()
main()
    
   

    
