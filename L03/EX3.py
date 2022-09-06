'''
print("Number square \n----------------")
for num in [1,2,3,4,5,6,7,8,9,10]:
    total = num ** 2 
    print('%d \t %d' % (num,total))
'''
'''
for x in range(5):
    print("hello Teeraporn")
print('Range start, end')
for num in range(1,5):
    print(num)
print('Range start, end , step')
for num in range(1,10,2):
    print(num)
'''
print("-------------------\nKPH \t MPH \n-------------------")
for KPH in range(60,130,10):
    MPH = KPH * 0.6214
    print( KPH , '\t','%.1f' %(MPH))