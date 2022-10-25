#this program demonstrates how number that are
#raed from a file must be converted g=from stings
#before they are used in a math operation.
def main():
    #Open a file for reading.
    infile = open('Number.txt','r')

    #read three numbers from the file.
    num1 =int(infile.readline())
    num2 =int(infile.readline())
    num3 =int(infile.readline())

    #close the file.
    infile.close()

    #Display the numbers and their total.
    tatal = num1 + num2 + num3
    print('The number are:', num1 ,num2 ,num3)
    print('Their tatal is:', tatal)

#call the main function
main()