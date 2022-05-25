# Your name:

# CS106 Spring 2021
# Exam 1 Practice Problem
# insurance.py: Determines the home insurance rate for a customer based on thier
# credit score, age, and payment history.

# DO NOT MODIFY THIS BLOCK OF CODE
# Get input from the user. Assume the user enters valid input.
credit = int(input('What is your credit score? '))
age = int(input('What is your age? '))
payment = input('Have you made a late payment (y/n)? ')
if payment == 'n':
    late = False
else:
    late = True
print('----------')
# END OF BLOCK THAT SHOULD NOT BE MODIFIED

# MAKE CORRECTIONS IN THE CONDITIONAL EXPRESSIONS BELOW
# DO NOT ADD, REMOVE, OR REORDER lines of code.
# The criteria for qualifying for the best rate are provided on the PDF file.
# You may alter one or more of the lines marked below.
# Do not change any other line.
if not late: # You may alter this line
    if credit >= 750 and age > 30: # You may alter this line
        print('Rate: best')
    elif credit >= 650 and age > 45: # You may alter this line
        print('Rate: best')
    else:
        print('Rate: average')
else:
    print('Rate: average')
