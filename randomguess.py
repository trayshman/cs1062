import random

n = -1 #not a valid input

while n < 1 or n >10: #condition

    try:
        #update the loop control variable
        n = int(input("Enter integer between 1 and 10 (inclusive): "))
    except:
        print('please enter a whole number')



r = -1 #initialize to something that is not a valid user guess

count = 0 #count number of guesses

while n != r:
    r = random.randint(1,10) #computer guessing user's number
    print('Is your number '+str(r) + '?')
    count += 1

print('It took me',count,'guesses to find your number')
