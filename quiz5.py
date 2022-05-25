# CS106 Fall 2021
# Quiz 5
# Name: Ryan Jones

# Follow the steps outlined below to complete this program.
# The program reads words from a file and stores the words as keys in a dictionary.
# The value associated with each key is the number of times that word occurrs
# in the file.
# Then the program repeatidly prompts the user to enter a word and uses the
# dictionary to determine if the user's word occurred in the file.

# Step 1: Open the input file
fhand = open('words.txt')

# Step 2: Create an empty dictionary
quiz5=dict()

# Step 3: Create a dictionary that contains each word from the input file as
# the key, and the number of times that word occurs in the input file as the value.
for line in fhand:
    good_line=line.strip()
    parts=good_line.split()
    for c in parts:
        if c not in quiz5:
            quiz5[c]=1
        else:
            quiz5[c]+=1


# Step 4: Close the input file

fhand.close()
# Step 5: Ask the user to enter a word. Using the dictionary, print
# the number of times that word occurred in the file.
word=input('enter a word, or enter "stop" to stop: ')
while word != 'stop':
    if word in quiz5:
        print(word,'occured',quiz5[word],'times')
        word=input('enter a word or enter "stop" to stop: ')
    else:
        print('sorry,',word,'is not in file')
        word=input('enter a word or enter "stop" to stop: ')
