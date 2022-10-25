#This propgram uses the for lop to read 
#all of the values in the sales.txt file

def main():
    #Open the sales.txt files for reading 
    sales_file = open('sales.txt' , 'r')

    #Read all the all lines from the file.
    for line in sales_file:
        #Convet line to a float.
        amount = float(line)
        #Format and display the amout.
        print(format(amount  ,'.2f'))
    #Close the file
    sales_file.close()
main()





