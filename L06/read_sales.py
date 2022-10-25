#this program reads all of the values in 
#the dales.txt file.
def main():
    #Open the sales.txt for reading.
    sales_file = open('sales.txt', 'r')

    #read the first line from the file,but
    #don't convert to a number yat. We still
    #need to test for an emty string
    line = sales_file.readline()

    while line != '':
        #Convert line to a float
        amount = float(line)

        #Format and display the amout
        print(format(amount,'.2f'))

        #Read the next line
        line = sales_file.readline()
    #Close the file
    sales_file.close()
main()
