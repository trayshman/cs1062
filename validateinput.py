#DO NOT PUT INPUTS IN THE TRY THINGY

done = False #flag variable

while not(done):
    try:
        x = int(input('Enter an integer: '))
        done = True

    except:
        print('incorrect input, try again')
print ('You entered the number:',x)
