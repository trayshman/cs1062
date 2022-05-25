#Print a square of stars

size = int(input('what size of square? '))

#print size rows, each row has size stars
# outer loop prints each row
for i in range(size):
    # inner loop prints each item in a row
    for j in range(size):
        print('*', end=' ')
    #end of innder loop
    print()
#end of outer loop
