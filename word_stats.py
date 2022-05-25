# CS106 Fall 2021
# Final Exam Practice Problem B-6
# word_stats.py

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: stats
# Function parameter:
#    list - A list of strings
# Returns: A tuple that contains the average length of the strings,
#   the maximum length of a string along with a string that has that length (this is
#   a tuple within the tuple), and the minimum length of a string along along with
#   a string that has that length (this is a tuple within the tuple).
# Description:
# This function finds the average length of the strings,
#   the maximum length of a string, and the minimum length of a string. For the
#   maximum and minimum, a string of that length is also returned.

def stats(list):
    sumlength=0
    small = (None, '') # a tuple for the shortest string, small[0] is length, small[1] is the string
    large = (None, '') # a tuple for the largest string, large[0] is the length, large[1] is the string
    for word in list:
        l = len(word)
        sumlength+=l

        if small[0] is None or l<small[0]:
        # found a new shortest string
            small = (l, word)

        if large[0] is None or l>large[0]:
        # found new largest string
            large = (l, word)


    a = sumlength / len(list)

    return a,small,large


# end of stats function

# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the function above, your function must work with the
# code that is provided below.

# Main part of program

# List of strings
animals = ['caterpillar', 'spider', 'shark', 'gorilla', 'white tail deer', 'walrus', 'salamander', 'ant', 'elephant']

info = stats(animals)

t = (1, 2, 3)
ty = type(t)

if type(info) != ty:
    print('ERROR: stats function must return a tuple')
if type(info[1]) != ty:
    print('ERROR: the tuple returned by the stats function must contain a tuple at index 1')
if type(info[2]) != ty:
    print('ERROR: the tuple returned by the stats function must contain a tuple at index 2')

print('Information about the list of strings:')
print('Average length of string:', info[0])
print('The shortest string (' + info[1][1] + ') has length', info[1][0])
print('The longest string (' + info[2][1] + ') has length', info[2][0])
