def multi_num(a,b):
    for i in range(a,b+1):
        for j in range(1,13):
            print('{} x {} = {}'.format(i,j,i*j))
        print("*" * 100)


multi_num(1,9)