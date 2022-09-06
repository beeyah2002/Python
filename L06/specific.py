
def main():
    empfile = open("employee.txt",'r')
    keep = empfile.readline()
    name = input('Enter name your want to find : ')
    
    while keep != '':
        if name in keep :
            keep = empfile.readline()
            print('Name', keep.rstrip())
            keep = empfile.readline()
            print('ID:',keep.rstrip())
            keep = empfile.readline()
            print('dept:',keep.rstrip())
            keep = empfile.readline()

main()
