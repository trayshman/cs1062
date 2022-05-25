# traverse_list.py
# Author: Christine F. Reilly
# Examples of using a for loop to traverse a list

a_list = [78, 95, 99, 13, 76, 12, 39, 10, 24, 26, 22, 55, 25, 16, 80, 88, 28, 85, 1, 46]

###################################
# Example 1: access each item in a list
# Count the number of items in a_list that are greater than 50
count = 0

# Use a for loop to access each item in the list
for x in a_list:
    if x > 50:
        count += 1
# End of loop

print(count, 'items in a_list are greater than 50')

print('\n') # print blank lines between examples

###################################
# Example 2: multiply each item in the list by 2
print('a_list before multiply:', a_list)

a_len = len(a_list) # get the length of a_list (nubmer of items in a_list)

# Use a for loop to iterate over each index of a_list
for i in range(a_len):
    # Multiply the value at position i by 2, save the new value into the same position
    a_list[i] = a_list[i] * 2
# End of loop

print('a_list after multiply:', a_list)

print('\n') # print blank lines between examples

###################################
# Another Example: use negative index to traverse list from end to beginning
# Also demonstrates putting the len function inside the range function

# Print the list in reverse order
# index of last item is -1
# index of firs item is -(list length)
# Generate a range starting at -1, up to but not including len(a_list) + 1,
#   with a step of -1
print('Printing a_list in reverse order')
for i in range(-1, -(len(a_list)+1), -1):
    print(a_list[i])
