#This program gets three names from the user
#and write them to a file.
def main():
    #Get three names
    print('Enter the names of three freinds.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Freind #3: ')

    #Open a file named friends.txt
    myfile = open('friend.txt' , 'w')

    #write the names to the file.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    #Close the file
    myfile.close()
    print('The names were written to friends.txt')
#Call the main function.
main()