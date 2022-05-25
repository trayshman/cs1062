# regex2_demo.py
# Author: Christine F. Reilly
# Demonstration of regular expressions (Part 2)

import re # Import the regular expressions module

# Function to extract the year from the date line that is part of the email header.
# Modified from the version of this function in regex1_demo.py
# Use curly braces to specify the year is four digits repeated
# Parameter: sting - name of the file
def print_years(fname):
    fhand = open(fname) # Open the input file

    # Iterate through the lines in the file
    for line in fhand:
        line = line.strip() # remove leading and trailing whitespace

        # Search for lines that are the Date: lines in an email message
        # Print the year part of the date
        # Match the four repeating digits of the year using \d{4}
        years = re.findall('^Date:\s*[a-zA-Z]+,\s*[0-9]+\s*[a-zA-Z]+\s(\d{4})', line)
        for y in years:
            print(y)
# end of print_years function



# Main part of program

##### Example 1: Escape character
print('Example 1: Escape character')
# Regular expression to match a price in a string
# Price begins with a $, followed by one or more digit and period characters
# Note that the period is not a special character when it is inside the square
# brackets that list a set of matching characters
price_regex = '\$[0-9.]+'
price = re.findall(price_regex, 'Coffee: $1.50; Latte $3; Hot chocolate: $2.45')
for p in price:
    print(p)

##### Example 2: Escape character for backslash
print('\nExample 2: Escape character for backslash')
# To escape the backslash, use four backslash characters because the backslash
# is also a string escape character in Python.
# Regular expression to match a backslash and one or more non-whitespace
# characters that immediately follows the backslash
# The first four backslashes are to match a single backslash in the expression.
# then we use \S+ to match one or more non-whitespace characters
slash_regex = '\\\\\S+'
# Note: writing double backslash in the string because the backslash is also
# an escape character in Python!
e = 'The \\backslash character is \\special in regular expressions'
print(e) # Notice that only a single backslash prints in each instance
slash = re.findall(slash_regex, e)
for s in slash:
    print(s)


# File name for example functions
file_name = 'mbox-regex.txt'

##### Example 3
print('\nExample 3: matching a repeating pattern')
print_years(file_name)

##### Example 4
print('\nExample 4: match a phone number')
e = 'Office Phone: 518-580-5448'
phone = re.findall('\d{3}-\d{3}-\d{4}', e)
for p in phone:
    print(p)


##### Example 5
print('\nExample 5: Greedy vs. Non-greedy match')
words = 'woof woofwoof root root-toot'

print('Greedy match:')
goo = re.findall('(\S*oo\S*)', words)
for o in goo:
    print(o)

print('\nNon-greedy match:')
noo = re.findall('(\S*?oo\S*?)', words)
for o in noo:
    print(o)
