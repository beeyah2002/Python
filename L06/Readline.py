#This program reads the contents of the 
#philosophers.txt file one line as a time.
def main():
    #Open a file named philosopher.txt
    infile = open('philosophers.txt' , 'r')

    #Read five lines from th file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()
    line5 = infile.readline()


    #Close the files.
    infile.close()


    #Print the data that was read into
    #memory
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)

#call the main function.
main()



