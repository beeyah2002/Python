def main():
    print("Want increase data employee '1' ")
    print("Want edit data employee '2' ")
    enter = int(input('enter choice: '))
    if enter == 1:
        add()
    elif enter == 2:
        modi()
    
def add():       
    emp = open('employee.txt','a')
    print("increase data employee")
    add1 = input('Enter name of employee: ')
    add2 = input('Enter ID: ' )
    add3 = input('Enter department: ')

    emp.write(add1 + '\n')
    emp.write(add2 + '\n')
    emp.write(add3 + '\n')
    print('Employee records written to employee.txt')
    
    
def modi():
    emp = open('employee.txt',"r")
    print('edit data employee')
    mod = input('Enter edit employee: ')
    showd = emp.readline()
    while showd != '':
        
        if showd.strip() == mod:
            keep1 = showd.rstrip()
            showd = emp.readline()
            keep2 = showd.rstrip()
            showd = emp.readline()
            keep3 = showd.rstrip()
            print('Name: ',keep1)
            print('ID: ',keep2)
            print('idept: ',keep3)
        showd = emp.readline()
    emp.close()

    rangedata = []
    files = open('employee.txt','r')
    for save in files.readlines():
        rangedata.append(save)
        

    remove_name =[]
    remove_id = []
    remove_dept = []
    name = input('Enter new name: ')
    id = input('Enter ID: ')
    dept = input('Enter department: ')

    for newname in rangedata:
        new1 = newname.replace(keep1,name)
        remove_name.append(new1)

    for newid in rangedata:
        new2 = newid.replace(keep2,id)
        remove_id.append(new2)

    for newdept in rangedata:
        new3 = newdept.replace(keep3,dept)
        remove_dept.append(new3)
    print(remove_dept)
    files.close()
    files=open('employee.txt','w')
    for data in remove_dept:
        files.write(data)
    files.close()

main()








'''
def main1(bee):
    bee = open('employee.txt', 'a')
    name = input('name: ')
    id = input('ID: ')
    dept = input('dept: ')
    bee.write(name + '\n')
    bee.write(id + '\n')
    bee.write(dept + '\n')
'''




