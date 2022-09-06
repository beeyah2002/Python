hour = float(input("Enter the number of hours worked : "))
pay_rate = float(input("Enter the hourly pay rate : "))
if hour >= 40:
    gross_payover = ( 40 * pay_rate ) + ((hour - 40)*(pay_rate*1.5))
    print("The gross pay is :${:,.2f} " .format(gross_payover))
else:
    gross_pay = (hour * pay_rate)
    print("The gross pay is :${:,.2f} " .format(gross_pay))
    