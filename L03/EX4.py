again = 'y'
while again == 'y':
    wholesale = float(input("Enter item's wholesale cost: "))
    retail_price = wholesale * 2.5
    print("retaial price : $%.2f." %(retail_price))
    again = input("Do you have another item? (Enter y for yes) : ")
