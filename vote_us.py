# vote_us.py
# Author: Christine F. Reilly
# This program determines if the user can vote in elections in the United States.

age = int(input('Enter your age: '))
citizen = bool(input('Enter True if you are a United States citizen, False if not: '))

if citizen and age >= 18:
    print('You may vote')
else:
    print('You may not vote')
