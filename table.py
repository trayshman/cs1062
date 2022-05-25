# CS106 Fall 2021
# Final Exam Practice Problem B-3
# table.py: The code to create a list of lists contains logic and/or semantic
# errors. Correct these errors so that the program output matches the sample
# output. Rules for corrections:
#   * You may only modify the lines marked with the "fix this line" comment.
#   * You may not add or delete lines of code.
#   * Recommended approach: Make a copy of the section of code, comment out the
#     original and make your changes to the copy. This allows you to easily see the
#     original function while you work on this problem.
#   * Tip: The errors are related to the concepts of lists.

size = int(input('Enter an integer for the table size: '))

table = []

# Start of code that contains errors

# Create a list of lists (a table)
# The table has size number of rows and size number of columns (using the
# variable size from above).
# The values in each row count up from 0 to size-1
for i in range(size):
    row = []
    for j in range(size): # fix this line
        row.append(j) # fix this line
    table.append(row) # fix this line

# End of code that contains errors

# Print the table
for row in table:
    for col in row:
        print(col, end=' ')
    print()
