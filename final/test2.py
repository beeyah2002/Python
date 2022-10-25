def highestDigit(num):
    change = str(num)
    change1 = sorted(change)
    beelen = len(change1)
    print(change1[beelen-1])

highestDigit(379)
highestDigit(2)
highestDigit(377401)
