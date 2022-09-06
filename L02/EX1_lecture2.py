first_test_score = float(input("Enter first test score: "))
second_test_score = float(input("Enter second test score: "))
third_test_score = float(input("Enter third test score: "))
average = (first_test_score + second_test_score + third_test_score) / 3
print("your average is : %.2f " % (average))
if average > 95:
    print("congratulate the user")