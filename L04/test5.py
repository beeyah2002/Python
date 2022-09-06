'''
คำนวณราคารูปถ่าย 1 นิ้ว หรือ 2 นิ้ว โดย อินพุต ชื่อลูกค้า ขนาดรูปที่ต้องการ และจำนวน 
    ถ้า เป็น รูป 1 นิ้ว 
        ราคาโหลละ 65 บาท 
    ถ้าเป็นรูป 2 นิ้ว 
        ราคา โหลละ 80 บาท
    ถ้าเป็น โพลาลอยด์ เเผ่นละ 70 บาท 
    ถ้าสั่ง 3 โหล จะได้ส่วนลด 5 % ยกเว้น โพลลาลอยด์ 
'''
name = input('Enter your name : ')
print('Type of Photo \n1. One inch\n2. Two inch\n3. Polaroid')
select = int(input("select type: "))
if select == 3:
    order = int(input('ใส่จำนวนเเผ่นที่ต้องการ'))
    price = order * 70
    
    print("show details")
    print("Your name is ",name )
    print("Type of photo is Polaroid")
    print("Amount is " ,order)
    print("Total price is 70*%d = %d" %(order,price))
    print("No discount ")
    print("net price =" ,price)

else:
    order = int(input("จำนวนที่ต้องการ(โหล): "))
    if select == 1 and order < 3:
        price = order * 65
        print("show details")
        print("Your name is ",name )
        print("Type of photo is One inch")
        print("Amount is " ,order)
        print("Total price is 65*%d = %d" %(order,price))
        print("No discount ")
        print("net price =" ,price)
        
    if select == 1 and order >= 3:
        price = order * 65
        discount = order * 65 * 0.05
        totaldis = price - discount

        print("show details")
        print("Your name is ",name )
        print("Type of photo is One inch")
        print("Amount is " ,order)
        print("Total price is 65*%d = %d" %(order,price))
        print("Discount =",discount)
        print("net price =" ,totaldis)
    if select == 2 and order < 3:
        price = order * 80
        print("show details")
        print("Your name is ",name )
        print("Type of photo is Two inch")
        print("Amount is " ,order)
        print("Total price is 80*%d = %d" %(order,price))
        print("No discount ")
        print("net price =" ,price)
    if select == 2 and order >= 3:
        price = order * 80  
        discount = order * 80 * 0.05
        totaldis = price - discount
        print("show details")
        print("Your name is ",name )
        print("Type of photo is One inch")
        print("Amount is " ,order)
        print("Total price is 80*%d = %d" %(order,price))
        print("Discount =",discount)
        print("net price =" ,totaldis)

