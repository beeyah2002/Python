from operator import le


word = input('Enter word: ')
countword = 0
countvowel = 0
lenword = len(word)
for i in range(lenword):
    keep = word[i]
    if  keep == " ":
        continue
    countword += 1
print('Number of letters:',countword)

for j in range(lenword):
    keep1 = word[j]
    if keep.lower() == 'a' or keep.lower() == 'e' or keep.lower() == 'i' or keep.lower() == 'o' or keep.lower() == 'u':
        countvowel += 1
print(countvowel)



    




    
