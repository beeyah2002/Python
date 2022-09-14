def main():

    file = open('employee.txt','r')
    search = input('Enter name : ')
    line = file.readline()
    #if line.strip() == search:
    while line != '':

        if line.strip() == search:
            keep_1 = line.rstrip()
            line = file.readline()
            keep_2 = line.rstrip()
            line = file.readline()
            keep_3 = line.rstrip()
            print('Name:',keep_1)
            print('ID:',keep_2)
            print('Dept:',keep_3)
        line = file.readline()
    file.close()

    sum = []
    filee = open('employee.txt','r')
    for read in filee.readlines():
        sum.append(read)
    print(sum)  
        
    remove_name = []
    remove_id = []
    remove_dept = []
    
    re_name = input('Enter name : ')
    re_id = input('Enter ID : ')
    re_dept = input('Enter dept : ')

    for name in sum:
        ch = name.replace(keep_1,re_name)
        remove_name.append(ch)

    for id in remove_name:
        ch = id.replace(keep_2,re_id)
        remove_id.append(ch)

    for dept in remove_id:
        ch = dept.replace(keep_3,re_dept)
        remove_dept.append(ch)
    print(remove_dept)
    file.close()
    file = open('employee.txt','w')
    for i in remove_dept:
        file.write(i)
    file.close()

main()