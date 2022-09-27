#display
#search
#add
#modify
#delete
records ={'6506022620095' : ['Anirach Mingkhwan','Anirach@gmail.com','0817320766']}
def main():
    again = 'y'
    while again == 'y':
        print("1.display \n2.search \n3.Add \n4.Modify \n5.delete")
        num = int(input('Enter your choice: '))
        if num == 1:
            print('Display')
            display()
        elif num == 2:
            print('Search')
            search()
        elif num == 3:
            print('Add')
            add()
        elif num == 4:
            print('Modify')
            modify()
        elif num == 5:
            print('delete')
            delete()
        again = input('Do you wanna do more [press y for yes]')
        if again != 'y':
            print('Exit')

    
def display():
    
    print(records)
def search():  
    search = input('what id do you wanna search: ')
    if search in records:
        print(search + ':',  records[search])
    else:
            print('not found')
def add():
    addid = input('What ID do you wanna add : ')
    addname = input('What name do you wanna add : ')
    addemail = input('What email da you wanna add : ')
    addcall = input('What phone number doyou wanna add: ')
    keep1 = []
    keep1.append(addname)
    keep1.append(addemail)
    keep1.append(addcall)
    records[addid] = keep1

def modify():
    keep3=[]
    keep2 = input('What ID do you wanna modify : ')
    addname = input('What name do you wanna add : ')
    addemail = input('What email da you wanna add : ')
    addcall = input('What phone number doyou wanna add: ')
    keep3.append(addname)
    keep3.append(addemail)
    keep3.append(addcall)
    if keep2 in records:
        print('yes')
        records[keep2] = keep3
        print(records)
    else:
        print('None')
def delete():
    removeid = input('What ID do you wanna delete : ')
    if removeid in records:
        print(records[removeid])
        (records.pop(removeid))
    print(records)

main()

