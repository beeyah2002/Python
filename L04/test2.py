text = 'anirachmingkhwan'
index = 1
outputtext = 3
for i in range(len(text)):
    if i == index:
        print(text[i].lower(),end="")
        index += outputtext
        outputtext += 1
    else:
        print(text[i].upper(),end="")
