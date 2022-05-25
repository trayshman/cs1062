# CS106 Fall 2021
# Quiz 2
# Name: Ryan Jones

######################################################################
# Problem 1
print('***** Problem 1:') # Do not change this line of code

# Asks the user to enter an integer. Adds an even number to the total,
# subtracts an odd number from the total. Repeats this action, and stops when
# the total is 100 or larger.
#
# Tasks to complete in this problem:
#   * Use a while loop to keep asking for user input and adjusting the total until
#     the total is 100 or larger.
#   * Validate user input: if the user does not enter an integer the program
#     must ask the user to try again.
#   * If the user input is an even number add it to the total, if it is an
#     odd number subtract it from the total.
#   * Print the value of the total at the beginning of each loop iteration.
#   * At the end of the program print a message and the final value of the total.
#
# Your output should be similar to that shown on the document for this quiz
# on theSpring.

# Write your code for Problem 1 here:
n=0
total=0
while total<100:
    print('the current total is',total)
    n=input('enter an integer: ')
    try:
        n_int=int(n)
        if n_int%2==0:
            total+=n_int
        else:
            total-=n_int

    except:
        print('you must enter an integer')
print('all done! the total is',total)

######################################################################
# Problem 2
print('\n\n***** Problem 2:') # Do not change this line of code
#
# Ask the user to enter a positive integer (assume the user enters correct input).
# Write a for loop that prints numbers from 1 up to the number entered by the user.
# Tip: there are multiple ways to use the range function:
# range(5): sequence of values 0 to 4
# range(1, 6): sequence of values 1 to 5
# Documentation: https://docs.python.org/3/library/functions.html#func-range
#
# Your output should be similar to that shown on the document for this quiz
# on theSpring.

# Write your code for Problem 2 here:
n=int(input('How high do you want to count: '))
count=0
for j in range(n):
    count+=1
    print(count)
