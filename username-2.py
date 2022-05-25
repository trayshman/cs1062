# CS106 Fall 2021
# Exam 2 Practice Problem B-2
# Fix the errors in this program, as instructed within the code.
#
# username.py: Open the file and read each line of the file. Extract the
# username part of the email addresses of people who sent a message.
#
# The sender's email address is in a line of the form:
# From: stephen.marquard@uct.ac.za
# The username is found between 'From: ' and the '@' character.
#
# Write output to the console (screen).
# Output each username and the line number where it was found in the file.
# At the end of the program, output the total count of usernames that were
# found in the file.

fname = 'mbox-short.txt'
fhand = open(fname)

line_num = 0
count = 0

for line in fhand:
    line = line.strip()

    ####################
    # Start of block of code that contains errors
    # There are three errors in this block of code.
    # To fix the errors you may:
    #    * Edit the code on a line.
    #    * Move a line of code to a different place in this block.
    # You may not:
    #    * Add new lines of code.
    #    * Delete lines of code.

    line_num += 1
    if line.startswith('From:'):

        start = line.find(':')
        end = line.find('@')
        username = line[start:end]
        username = username.strip()
        print('line', line_num, ':', username)
        count += 1

    # End of block of code that contains errors
    ####################

print('found', count, 'usernames')
