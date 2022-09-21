heroes = ['Ironman' ,'Thor', 'Hulk','Superman', 'Spiderman']
def main():
    again = 'y'    
    while again == 'y':
        print('1.show heoes \n2.Add Hero \n3.Insert Heroes \n4.Remove Heroes \n5.display sorted Heroes \n6.exit')
        main1 = int(input("enter choice : "))
        
        if main1 == 1:
            hero()
        elif main1 == 2:
            hero1()
        elif main1 == 3:
            hero2()
        elif main1 == 4:
            hero3()
        elif main1 == 5:
            hero4()
        elif main1 == 6:
            hero5()    
        again = input('Do you want to do more  y for yes : ')

def hero():
    keep1 = heroes
    print(keep1)
                
def hero1():
    addhero = input('Enter hero you wnna add : ')
    heroes.append(addhero)
    hero()
    
def hero2():
    index1  = int(input('Enter index you wanna insert word: '))
    word = input('Enter hero\'s name you wanna insert : ')
    heroes.insert(index1,word)
    hero()

def hero3():
    hero()
    word = input('Enter heroes you wanna remove : ')
    heroes.remove(word)
    hero() 
    
def hero4():
    hero()
    heroes.sort()
    hero()

def hero5():
    searchhero = input('Enter hero you wanna find : ')
    bee = searchhero[0].upper()
    keep = bee + searchhero[1: ]
    if keep in heroes:
        print( 'it\'s exit' )
    else:
        print('It\'s not exit')  

main()