def numberSplit(number):
    if number % 2 == 0:
        count = number / 2
        print("[ %d , %d ]" %(count,count))
    else :  
        count1 = number // 2  #หาร -4 
        count = (number - count1) 
        
      
        print(count)
        #print("[ %d , %d ]" %(count1,count1 + count))


numberSplit(-9)


