# CS106 Fall 2021
# Quiz 4
# Name: Ryan Jones

# STUDENT MUST WRITE THIS FUNCTION
# Function name: divisible
# Function parameters:
#    integer - value to test
#    integer - number to see if the value is divisible by
# Returns: True if the first parameter is divisible by the second parameter, False otherwise.
# Description:
# This function determines if the first parameter is divisible by the second
# paramter. This problem is similar to Problem 2 from Weekly Quiz 1.
def divisible(x,y):
    if x%y==0:
        return True
    else:
        return False

# end of divisible function

# This code tests the divisible function
# An error message prints if any test fails.
# Do not modify this test code. You may add more tests.
print('starting testing')
result = divisible(49, 7)
if result != True:
    print('ERROR: 49 should be divisible by 7')

result = divisible(1024, 16)
if result != True:
    print('ERROR: 1024 should be divisible by 16')

result = divisible(100, 3)
if result != False:
    print('ERROR: 100 should not be divisible by 3')

result = divisible(511, 25)
if result != False:
    print('ERROR: 511 should not be divisible by 25')
print('finished testing')
