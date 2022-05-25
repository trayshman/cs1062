# CS106 Fall 2021
# Final Exam Practice Problem B-2
# word_list.py

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: read_file
# Function parameter:
#    string - The name of the file
# Returns: A list of words read from the file
# Description:
# This function opens an input file and reads the words from this file into a list.
# It is assumed that the file contains no punctuation and that the words are separated
# by space.

def read_file(fname):
    a=[]
    f_read=open(fname)
    for line in f_read:
        words=line.split()
        for c in words:
            a.append(c)
    print(a)
    return a

# end of read_file function

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: avg_word_length
# Function parameter:
#    list - A list of strings
# Returns: The average length of the strings in the list.
# Description:
# This function calculates the average length of the strings in the list.
def avg_word_length(list):
    count=0
    avgcount=0
    for word in list:
        avgcount+=len(word)
        count+=1

    avg=avgcount/count
    return avg


# end of avg_word_length function

############################################################
# STUDENT MUST WRITE THIS FUNCTION
# Function name: small_words
# Function parameter:
#    list - A list of strings
#    int - An integer
# Returns: A list of strings.
# Description:
# This function returns a list of strings where the length of each string in the
# list is less than the integer parameter.

def small_words(list,num):
    swaglist=[]
    for i in list:
        if len(i)<num:
            swaglist.append(i)

    return swaglist


# end of small_words function

# DO NOT MODIFY THE CODE BELOW THIS LINE
# You may comment lines out while you are testing the code you write.
# When you have written the functions above, your functions must work with the
# code that is provided below.

# Main part of program

# Read the file
my_words = read_file('words.txt')
print('Number of words in the file:', len(my_words))


# NOTE: If you do not complete the read_file function, uncomment the line
# below and use this list of words for testing the other two functions.
#my_words = ['Writing', 'programs', 'or', 'programming', 'is', 'a', 'very', 'creative', 'and', 'rewarding', 'activity', 'You', 'can', 'write', 'programs', 'for', 'many', 'reasons']

alen = avg_word_length(my_words)
print('Average number of letters in the words:', alen)

# round the length
alen_int = round(alen)

shorter = small_words(my_words, alen_int)
print('From the list of', len(my_words), 'words,', len(shorter), 'have fewer than average letters')
