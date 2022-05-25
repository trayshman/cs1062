# search.py
# Author: Christine F. Reilly
# Functions for searching a list

# Function name: linear_search
# Function parameters:
#     List of values to search
#     The key value to try to find in the list
# Returns: The index where the key is found in the list, or -1 if the key is not found.
# Description:
# Uses the linear search algorithm to search a list. Starting at index 0, examine
# each element in the list until the key is found or the end of the list is reached.
# Assumes that the list does not contain duplicates.
def linear_search(vals, key):
    for i in range(len(vals)):
        if vals[i] == key:
            return i
    # end of loop through list
    # If program reaches this point, the key was not found in the list
    return -1
# end of linear_search function

# Function name: binary_search
# Function parameters:
#     List of values to search
#     The key value to try to find in the list
#     int - the starting position for the sublist to search
#     int - the ending position for the sublist to search
# Returns: The index where the key is found in the list, or -1 if the key is not found.
# Description:
# Using recursion, implements the binary search algorithm to search a list.
# Assumes that the list does not contain duplicates.
def binary_search(vals, key, startpos, endpos):

    # Calculate the middle position in the sublist. Use integer division
    # because list index must be an integer
    middle = (startpos + endpos) // 2

    # Print some information for tracing the recursive function calls
    print('binary_search: key is', key, '; startpos is', startpos, '; endpos is', endpos)
    print('middle is', middle, '; value at middle is', vals[middle], '\n')

    if key == vals[middle]:
        # Base case 1: found the key. Return the position where the key is found.
        return middle
    elif key < vals[middle]:
        # Key comes earlier in the list
        # Change the end position so that only the earlier part of the list
        # will be searched when this function is recursively called
        endpos = middle - 1
    else:
        # Key comes later in the list
        # Change the start position so that only the later part of the list
        # will be searched when this function is recursively called
        startpos = middle + 1

    # See if there are more words left to check
    if startpos <= endpos:
        # There are more words to check, recursively call this function
        return binary_search(vals, key, startpos, endpos)
    else:
        # Base case 2: No more words to check. The word is not in the list.
        return -1
# end of binary_search function

# Main part of the program. Create some lists and test the two search functions.

# Some lists to use
animals = ['ant', 'caterpillar', 'elephant', 'gorilla', 'salamander', 'shark', 'spider', 'walrus', 'white tail deer']
numbers = [-458, -448, -445, -437, -427, -425, -421, -379, -373, -372, -359, -343, -334, -326, -317, -287, -282, -261, -249, -239, -224, -222, -190, -171, -132, -80, -39, -31, -11, 8, 22, 41, 46, 51, 64, 75, 89, 96, 102, 112, 179, 224, 236, 250, 261, 276, 300, 337, 422, 463]

print('Searching animals')
pos = linear_search(animals, 'spider')
print('Linear search found key at position', pos)

# For binary search, startpos is 0 and endpos is the last index
pos = binary_search(animals, 'spider', 0, len(animals)-1)
print('Binary search found key at position', pos)

print('\nSearching numbers')
pos = linear_search(numbers, -317)
print('Linear search found key at position', pos)

# For binary search, startpos is 0 and endpos is the last index
pos = binary_search(numbers, -317, 0, len(numbers)-1)
print('Binary search found key at position', pos)

print('\nStarting exercise example:')
exercise = [1, 2, 5, 13, 17, 18, 24, 27, 28, 29]
pos = binary_search(exercise, 18, 0, len(exercise)-1)
print('Binary search found key at position', pos)
