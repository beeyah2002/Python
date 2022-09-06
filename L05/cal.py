import circle
import regtangle

AREA_CIRCLE_CHOICE = 1
CIRCUMFERENCE_CHOICE = 2
AREA_REGTANGLE_CHOICE = 3
PERIMETER_RAGTANGLE_CHOICE = 4
QUIT_CHOICE = 5

def main():
    choice = 0 
    while choice != QUIT_CHOICE:
        display_menu()
        choice = int(input('Enter your choice: ' ))
        if choice == AREA_CIRCLE_CHOICE:
            radius = float(input("enter the circle's redius: "))
            print("The area is ", circle.area(radius))
        elif choice == CIRCUMFERENCE_CHOICE:
            radius = float(input("Enter the circle's radius: "))
            print('The circumference is' , circle.circumference(radius))
        elif choice == AREA_REGTANGLE_CHOICE:
            width = float(input("Enter the regtangle's width: "))
            length = float(input("Enter the regtangle's length: "))
            print('The area is' , regtangle.area(width,length))
        elif choice == PERIMETER_RAGTANGLE_CHOICE:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("enter the regtangle's length: "))
            print('The perimeter is ', \
                regtangle.perimeter(width , length))
        elif choice == QUIT_CHOICE:
            print('Exiting the program')
        else:
            print('Error: invalid selection.')
def display_menu():
    print('         menu')
    print('1) Area of a circle')
    print('2) Circumference of a circle')
    print('3) Area of a rectangle')
    print('4) Perimeter of a rectangle')
    print('5) Quit')
main()