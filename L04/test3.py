'''
balloon = "Anirach has a balloon."
print(" ".join(balloon))
print("".join(reversed(balloon)))
print(",".join(["Shark" , "crustaceans", "plankton"]))

balloon = "Anirach has a balloon"
print(balloon.split())
print(balloon.split("a"))

date_string = '11/26/2014'
date_list = date_string.split('/')
print('Month:' , date_list[0])
print('day:' , date_list[1])
print('Year:' , date_list[2])
print(date_list)


balloon = '      Aniach has a balloon        '
print('[',balloon.strip(),']')
print('[',balloon.lstrip(),']')
print('[',balloon.rstrip(),']')

balloon = '###Anirach has a balloon###'
print('[',balloon.strip('#'),']')
print('[',balloon.rstrip('#'),']')


balloon = 'Anirach has a balloon'
print(balloon.find("has"))


string = 'Four score and seven years ago'
position = string.find('seven')
if position != -1:
    print('The word "seven" was found at index', position)
else:
    print('The word "seven was not found.')

balloon = 'Anirach has a balloon'
print(balloon.replace("has","had"))


filename = input('Enter the filename: ')
if filename.endswith('.txt'):
    print('That is the name of a text file.')
elif filename.endswith('.py'):
    print('That is the name of a Python source file.')
elif filename.endswith(".doc"):
    print("That is the name of a word processing document.")
else:
    print('Unknown file type')
  

number = "5"
letter = "abcdef!"
space = "        "
print(number.isnumeric())
print(letter.isalpha())
print(space.isspace())

movie = '2001 : A SAMMMY ODYSSEY'
book = "A thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"
print(movie.isalnum())
print(movie.isupper())

print(book.istitle())
print(book.isupper())

print(poem.istitle())
print(poem.islower()


text = input('Enter a string : ')
print("This is what iI found about that string")
if text.isalnum() == True :
    print("the string is alphanumeric.")
if text.isalpha() == True:
    print("The string contains only alphabetic characters.")
if text.isnumeric() == True:
    print("The string contains only digits")
if text.islower() == True :
    print("The letter in the string are all lowercase.")
if text.isupper() == True:
    print("the letter in the string are all uppercase.")

'''
inputmsg = input("In put string you want to swap words: ")
print(inputmsg.split())
saparatewords = inputmsg.split()

print("saparate words")
for i in saparatewords:
    print(i)

print("Modify each words")
print(len(saparatewords))
for j in range(len(saparatewords)):
    saparatewords[j] = 'G' + saparatewords[j]
    print(saparatewords[j])

print(saparatewords)
print(" ".join(saparatewords),)