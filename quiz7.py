# CS106 Fall 2021
# Quiz 7
# Name: Ryan Jones

import re # Import the regular expressions module

# Quiz 7: Write this regular expression
# This regular expression is used below to extract the pieces in the pathname,
# not including the drive letter.
# Hints:
#  1) There is a backslash before the matching text
#  2) The matching text contains non-backslash characters
all_regex = '[^\\\\][a-zA-Z0-9]*[a-zA-Z0-9-.]+'

############################################################
# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have completed the functions above, your regular expression must work
# with the code that is provided below.


# Function uses findall to match a pattern from a regular expression, then prints
# the items found
# Parameters:
#    search_str (string) The string to search
#    regex (string) The regular expression to use in the search
def extract(search_str, regex):

    pieces = re.findall(regex, search_str)
    for p in pieces:
        print(p)


# Extract the pieces (text between backslashes) from a Windows style file pathname
# Example strings:
# Note - using double backslash in the strings to escape the backslash in the string
path1 = 'C:\\Users\\creilly\\Documents\\regex.ppt'
path2 = 'D:\\Media\\Video\\December\\03\\2021\\class-video.mp4'

print('Pathname: ' + path1)
print('\nAll pieces of pathname:')
extract(path1, all_regex)

print('\n******************************\n')

print('Pathname: ' + path2)
print('\nAll pieces of pathname:')
extract(path2, all_regex)
