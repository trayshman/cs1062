# reverse_input.py
# Author: Christine F. Reilly
# Using recursion, ask the user to input a series of strings then print the
# strings in reverse order of how they were entered.

# Function name: reverse_input
# Function parameter: none
# Returns: nothing (void function)
# Description:
# Using recursion, ask the user to input a series of strings then print the
# strings in reverse order of how they were entered.
def rev_string():
    word = input('Enter a word or type stop to "stop" entering input: ')
    if word == 'stop':
        # base case, do not ask for more input
        # As the function calls unwind the words will print in reverse
        print('\n....Your words, in reverse order:')
    else:
        # keep asking for input by making a recursive call to this function
        rev_string()

        # After the recursive function call returns, print this instance's word
        print(word)
# end of rev_string function

# Main part of program:
print('This program will print the words you enter in reverse order')
rev_string()
