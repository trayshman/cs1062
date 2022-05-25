# CS106 Fall 2021
# Quiz 6
# Name: Ryan Jones

# Follow the steps outlined below to complete this program.
# This problem is similar to textbook Exercise 11.1.
# This problem builds on Problem 1 from the November 11 lab.
#
# Copy your code for Problem 1 from the November 11 lab to create a dictionary
# of how many messages were sent from each email address.
#
# Use this dictionary to create a list of (count, email) tuples from the dictionary.
# Then sort this list in reverse order and print the five email addresses that
# have the most messages, along with the asociated number of messages.

# Step 1: Copy your code for Problem 1 from the November 11 lab to read the
# mailbox file (mbox-short.txt or mbox.txt) and create a dictionary.
# Step 1-a (code provided): Open the file.
# fname = 'mbox-short.txt'
fname = 'mbox.txt'
fhand = open(fname)

# Step 1-b: Create an empty dictionary object
dic=dict()
# Step 1-c: Read the file. Use a dictionary to keep a count of how many email
# messages are sent by each sender.
# To identify the email addresses, look for lines in the file that begin with
# 'From:' The email address is the second word on these lines.
for line in fhand:
    good_line = line.strip()
    if good_line.startswith('From:'):
        parts=good_line.split()
        if parts[1] not in dic:
            dic[parts[1]]=1
        else:
            dic[parts[1]]+=1



# Step 1-d: Close the input file
fhand.close()

# Step 2: Using the dictionary you created in Step 1, create a list of
# (count, email) tuples
# create a list for the [value, key] tuples
vk=[]

#fill the list with (value, key) tuples
for key, val in list(dic.items()):
    # add a tuple to the value-key list
    vk.append( (val, key) )
#end of iterating through the dictionary




# Step 3: Sort the list you created in Step 2 in descending order of number of
# emails sent.

vk.sort(reverse=True)




# Step 4: print the five email addresses that have the most messages, along
# with the asociated number of messages.
val,key=(vk[0])
print(key,val)
val,key=(vk[1])
print(key,val)
val,key=(vk[2])
print(key,val)
val,key=(vk[3])
print(key,val)
val,key=(vk[4])
print(key,val)
