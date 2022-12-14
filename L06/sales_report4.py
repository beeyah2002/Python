#This program dispalys the total of the
#mout in the sales_data.txt file.

def main():
    #Initialize as accumulator.
    total = 0.0
    try:
        #Open the sales_data.txt file.
        infile = open('sales.txt','r')

        #Read the values from the file and
        #accumulate them.
        for line in infile:
            amount = float(line)
            total += amount
        #Close the file. 
        infile.close()

    except Exception as err:
        print(err)
    else:
        #Print the total.
        print(format(total, '.2f'))

main()