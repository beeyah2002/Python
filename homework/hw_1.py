word = input('Enter word: ')
countword = 0
countvowel = 0
countB = 0
listA = []
lenword = len(word)
for i in range(lenword):
    keep = word[i]
    if  keep == " ":
        continue
    countword += 1
print('Number of letters:',countword)

for j in range(lenword):
    keep1 = word[j]
    if keep1.lower() == 'a' or keep1.lower() == 'e' or keep1.lower() == 'i' or keep1.lower() == 'o' or keep1.lower() == 'u':
        countvowel += 1
print('Number of vowels: ',countvowel)

for b in range(lenword):
    keep2 = word[b]
    if keep2.isupper() == True:
        listA.append(keep2)
        countB += 1
print('Number of Capital:',countB ,listA)






    




    
