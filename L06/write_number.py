#this propgram demonstrates how numbers
#must be convert to string before they
#are writen to a text file.

def main():
    #Open a file for writing.
    outfile = open('Number.txt', 'w')

    #Get three numbers from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter amother number: '))

    #Write the number to the file.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3)  + '\n')

    #Close the file.
    outfile.close()
    print('Data written to number.txt')

#call the main function.
main()
