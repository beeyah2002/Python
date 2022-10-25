#This program reasds and displays the contents
#of the philosophers.txt file.
def main():
    #Open a file named philosopher.txt
    infile = open('philosophers.txt' , 'r')
    #Read the file's contents.
    file_contents = infile.read()

    #Close the files.
    infile.close()

    #Print the data that was read into
    print(file_contents)
#Call the main function.
main()




