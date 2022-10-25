#This program reads and displays the comtents
#of the plilosophera.txt file.
def main():
    #Open a file named philosophers.txt.
    outfile = open('philosophers.txt','w')


#Read the file's contents.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    outfile.write('Teeraporn\n')
    outfile.write('nutthawuth\n')

    #Close the file.
    outfile.close()
#call the main function.
main()