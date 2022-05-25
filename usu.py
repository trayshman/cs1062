# count the number of vowels in a string

s = input('enter a string: ')

lower_s = s.lower() #lower method returns string with all lower case letters

v = 0 #counter variable for number of vowels

for c in lower_s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        # the character is a vowel
        v += 1 # increment the counter
    # end of if a vowel
# end of loop through characters in string s

print(s, ': contains', v, 'vowels')
