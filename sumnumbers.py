#initialization
n = 0 #initialize user's number to 0
total = 0 # Initialize the sum of user's numbers to 0
count=0
#condition
n = input('Enter an integer, or enter done to stop: ')

while n != 'done':
    #assume user enters correct input
    try:
        int_n = int(n)
        count+=1
        total += int_n
    except:
        print('incorrect input, try again')


    n = input('Enter an integer, or enter done to stop: ')

print('the total is:', total)
print('the count is:',count)
print('the average is:',total/count)
