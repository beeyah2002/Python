word = input('Enter word : ')
upperword = word.upper()
cut = upperword.split() # เป็นลิสต์เเล้ว 

pig = ''
lenword = len(cut)
for i in range(lenword):
    bee = cut[i]
    if bee.startswith("A") or bee.startswith("E") or bee.startswith("I") or bee.startswith("O") or bee.startswith("U") :
        pig = bee + 'HAY'
        
    elif bee.startswith("A") == False or bee.startswith("E") == False or bee.startswith("I") == False or  bee.startswith("O") == False  or bee.startswith("U") == False :
        pig = bee[1:] + (bee[0] + 'AY')
    space = pig + ' '
    print(space,end='')
        
        

