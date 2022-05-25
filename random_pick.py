# random_pick.py
# Author: Christine F. Reilly
# This program demonstrates the use of while loops. The user picks a number,
# then a loop is used to generate a random number until the user's number is
# generated. A while loop is also used to validate the user input.

# Import Python's random module so we can use the functions from that module
# in this program
import random

# Get a number from the user
# Use a loop to keep asking for input until the user enters expected input
# Initialize n to an "incorrect" value
n = -1
while n < 1 or n > 10:
    try:
        n = int(input('Enter an integer between 1 and 10 (inclusive): '))
    except:
        print('Please enter a whole number.')

# Declare the random number variable
# (this is also part of loop initialization for this program)
r = -1

# Declare a variable to count the number of 'guesses' the computer makes,
# and initialize this variable to zero
# (this is also part of loop initialization for this program)
count = 0

# Use a while loop to generate a random number until the user's number
# is generated
while n != r:
    r = random.randint(1,10)
    print('Random number:', r)

    # The += operator adds to the variable then assigns the new value to the variable
    # This statement is equivalent to count = count + 1
    count += 1

# After the loop
print('I found your number! It took me', count, 'guesses')
