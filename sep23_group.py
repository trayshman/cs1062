# CS106 Lab
# September 23, 2021
# Names and roles of group members: Recorder: Ryan Jones, Organizer: Yuqian Sun

# Importing the random module for use in the lab problems
import random

######################################################################
# Problem 1 (5 points)
# Learning goal: Practice random number functions, conditional execution, while loops
# Spend up to 30 minutes working on this problem.
print('***** Problem 1:') # Do not change this line of code
#
# Write Python code to simulate playing with a Magic 8 Ball toy. A Magic 8 Ball
# is a fortune telling toy. The player asks a yes-no question and the Magic 8
# Ball randomly chooses an answer from a group of possible answers.
#
# For your program, you will use 5 possible answers. Your program must give
# each of these possible answers with equal probability. The answers your
# program will give are:
#    Yes
#    No
#    Maybe
#    Ask Again Later
#    I Don't Know
#
# Your program should use a while loop to keep playing the Magic 8 Ball game
# until the user enters "done". The user can enter anything for their question,
# there is no need to do validation for "correct" input.
#
# For example output and a link to a more detailed description of the Magic 8
# Ball game, see the document for this lab on theSpring.
#
# Suggested steps for working on this problem:
#   1) Use a while loop to keep prompting for user input until the user enters "done".
#   2) Use a random number function and conditional execution to answer the question.
#
# Write your code for Problem 1 here:

question=0
print('The magic 8 ball will answer your questions')

while question != 'done':
    question=input('Enter a question: ')
    if question != 'done':
        answer=random.randint(1,5)
        print('The magic 8 ball answers...')
        if answer==1:
            print('Yes')
        if answer==2:
            print('No')
        if answer==3:
            print('Maybe')
        if answer==4:
            print('Ask again later')
        if answer==5:
            print('I dont know')
    else:
        print('Thank you for playing!')


######################################################################
# Problem 2 (Textbook Exercise 5.1) (5 points)
# Spend up to 30 minutes working on this problem.
# Learning goal: practice while loops
print('\n\n***** Problem 2:') # Do not change this line of code
#
# This program modifies and builds upon the sum_inputs.py example from class on 9/22.
#
# Write python code to repeatedly read numbers until the user enters "done".
# Once "done" is entered, print out the total, count, and average of the
# numbers (you may not use any built in functions for computing this information).
# If the user enters anything other than a number: detect their mistake using
# try and except, print an error message, and skip to the next number.
#
# For example output see the exercise in the textbook and the document for this
# lab on theSpring.
#
# You can solve this problem without using break or continue!
#
# Write your code for Problem 2 here:
#initialization
n = 0 #initialize user's number to 0
total = 0 # Initialize the sum of user's numbers to 0
count=0
#condition
n = input('Enter an integer, or enter done to stop: ')

while n != 'done':
    #assume user enters correct input
    try:
        int_n = int(n)
        count+=1
        total += int_n
    except:
        print('incorrect input, try again')


    n = input('Enter an integer, or enter done to stop: ')

print('the total is:', total)
print('the count is:',count)
print('the average is:',total/count)



######################################################################
# Problem 3
# Bonus Problem: Work on this if you finish problems 1 and 2, use this for
# practice with study groups.
# Learning goal: practice while loops, input validation, and using functions from
# the random module.
print('\n\n***** Problem 3 (Bonus):') # Do not change this line of code
#
# This problem builds upon the roll_dice.py example from class on 9/17.
# This is the exercise on the last slide from class on 9/22, plus an additional
# feature.
#
# Write Python code to simulate rolling a n-sided die (such as 10-sided or
# 20-sided) many times. Obtain user input for the number of sides the die has
# and for the number of times to roll the die. Validate that the user enters an
# integer greater than zero for both of these inputs. Print a message to tell
# the user the result of each roll of the die.
#
# You can use a while loop for rolling the die many times. This is a task where
# we typically use a for loop, but it is possible to use a while loop. We did
# not have demonstrations of a counter while loop in class. Think about what
# the condition is for this while loop and what variables you need.
#
# For example output see the document for this lab on theSpring.
#
# Write your code for Problem 3 here:
