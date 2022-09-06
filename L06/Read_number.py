def main():
    infile = open('Number.txt','r')

    num1 =int(infile.readline())
    num2 =int(infile.readline())
    num3 =int(infile.readline())

    infile.close()

    tatal = num1 + num2 + num3
    print('The number are:', num1 ,num2 ,num3)
    print('Their tatal is:', tatal)
main()