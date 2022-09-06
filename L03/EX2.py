import random

print("What is my magic number( 1 to 100) ? ")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and ntries != mynumber:
    msg = str(ntries) + '>>'
    if(ntries == 6):
        print("last chance")
    yourguess = int(input(msg))
    if yourguess > mynumber:
        print("-->>too high")
    elif yourguess < mynumber:
        print("-->>too low")
    ntries += 1
if yourguess == mynumber:
    print("Yes! it's" ,mynumber)    
else:
    print("sorry! my number is" , mynumber)     