inchar = input("Input one charecter :")
if inchar >= 'A' and inchar <= 'Z':
    print("You input Upper Case Letter  " , inchar)
elif inchar >=  'a' and inchar <= 'z':
    print("You input Lower Case Letter  ", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input Number  " , inchar)
else:
    print("It's not a letter or number.  " , inchar)
