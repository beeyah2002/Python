
def capToFront(string1):
    lenbee = len(string1)
    count = []
    mini = []
    for i in string1:
        if i.isupper():
            count.append(i)
        elif i.islower():
            mini.append(i)
    print("".join(count) + ''.join(mini))
capToFront("hApPy")
capToFront("moveMENT")
capToFront('shOrtCAKE')