def digitalClock(timevi):
    bee = timevi // 3600
    bee1 = timevi % 3600
    bee2 = bee1 // 60
    bee3 = bee1 % 60
    if bee < 10 :
        change = "0" + str(bee)
    else:
        change = str(bee)
    if bee2 < 10 :
        change1 = "0" + str(bee2)
    else:
        change1 = str(bee2)
    if bee3 < 10 :
        change2 = "0" + str(bee3)
    else:
        change2 = str(bee3)
    print(change,":",change1,":",change2)

    



digitalClock(5025)