# CS106 Lab
# September 30, 2021
# Names and roles of group members: Recorder: Ryan Jones, Organizer: Jacob Lord

######################################################################
# Problem 1 [Textbook Exercise 5.2] (5 points)
# Learning goals: Practice while loops, finding the minimum and maximum
# Spend up to 30 minutes working on this problem.
print('***** Problem 1:') # Do not change this line of code
#
# This is a modification of Problem 2 from the last lab class. You can start
# with your code from last week's problem 2 (make sure to update your code
# based on the grading comments).
#
# Write python code to repeatedly read integers until the user enters "done".
# Once "done" is entered, print out the maximum and minimum of the
# numbers (you may not use any built in functions for computing this information).
# If the user enters anything other than a number: detect their mistake using
# try and except, print an error message, and skip to the next number.
#
# You may use the None value.
# You may not use break or continue.
#
# For example output see the document for this lab on theSpring.
#
# Write your code for Problem 1 here:

n = 0 #initialize user's number to 0

maximum=None
minimum=None
#condition
n = input('Enter an integer, or enter done to stop: ')


while n != 'done':

    try:
        n = int(n)
        if maximum is None:
            maximum=n
        if minimum is None:
            minimum=n
        if maximum<n:
            maximum=n
        if minimum>n:
            minimum=n
    except:
        print('incorrect input, try again')


    n = input('Enter an integer, or enter done to stop: ')

print('maximum:',maximum)
print('minimum:',minimum)


######################################################################
# Problem 2 (5 points)
# Spend up to 30 minutes working on this problem.
# Learning goals:
print('\n\n***** Problem 2:') # Do not change this line of code
#
# This problem will print a sequence of integers from a starting point up to
# and including a stopping point. An end of line is printed after every 10
# numbers. Both the starting and stopping points are integers. The stopping point
# must be larger than the starting point.
#
# This is a somewhat complex problem. Here are suggested steps:
# 1) Ask the user to enter the starting and stopping points, and assume the
#    user enters valid input. Use a for loop to print numbers from the starting
#    point to the stopping point.
# 2) Add a line break after every 10 numbers that are printed.
# 3) Add a while loop to validate that the starting point is an integer.
# 4) Add another while loop to validate that the stopping point is an integer
#    and is larger than the starting point.
#
# You may use the None value.
# You may not use break or continue.
#
# To have a space instead of an end of line at the end of a print:
#   print('stuff to print', end=' ')
#
# For example output see the document for this lab on theSpring.
#
# Write your code for Problem 2 here:
startDone = False
start=input('enter a starting point: ')
while not(startDone):
    try:
        start=int(start)
        startDone=True
    except:
        print('invalid input')
        start=input('enter a starting point: ')


stopDone = False
stop=input('enter a stopping point: ')
while not(stopDone):
    try:
        stop=int(stop)
        if stop>start:
            stopDone=True
        else:
            print('must be above starting point')
            stop=input('enter a stopping point: ')

    except:
        print('invalid input')
        stop=input('enter a stopping point: ')


count = 1
for j in range(start,stop+1):

    if count % 10 == 0:
        print(j)
    else:
        print(j, end = ' ')
    count+=1

######################################################################
# Problem 3 (Bonus Problem)
# Learning goals: Practice nested for loops and strings
print('\n\n***** Problem 3 (Bonus):') # Do not change this line of code

# Given a list of strings, determine which of the strings contains the most
# vowels.
#  * You may use the None value
#  * Use nested for loops
#  * You may assume that the strings only contain lowercase letters and non-alpha
#    characters (do not worry about uppercase letters)
#  * You may assume that each string contains a different number of vowels
#    (do not worry about how to handle a tie)
#  * Focus on the example lists provided. The goal of this problem is to
#    practice working with nested loops.
#  * Recall that a string is a sequence similar to a list.
#
# For examples of how to iterate over a list of values see Section 5.8 of the
# textbook and the max.py example program from class on March 2
#
# You may copy the code for counting vowels from strings.py (example program from March 4)

# Use these lists of strings to test your code
# Use one of these lists at a time.
# The minimum and maximim are in different positions in each list to provide
# a variety of test conditions.
strings1 = ['caterpillar', 'spider', 'shark', 'gorilla', 'white tail deer']
# Number of vowels in each string in strings1 4, 2, 1, 3, 6

strings2 = ['walrus', 'salamander', 'ant', 'elephant']
# Number of vowels in each string in strings2 2, 4, 1, 3

# Write your code for Problem 3 here:
