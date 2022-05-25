#ask user to input a strings
#print the string in reverse

s = input('Enter a string: ')

# Example A: using a for loop
# start loop at index of last character
#move backwards through the string to the beginning
print('\nYour string in reverse: ')
for i in range(-1,-(len(s)+1), -1):
    # print each character of the string
    #print each char of a strings
    #print (s[i])
    print(s[i], end='')
#end loop
print()


print('\nYour string in reverse (while loop): ')

b = len(s) - 1

while b >= 0:
    
    print(s[b], end='')
    b-=1
#end loop

print()
