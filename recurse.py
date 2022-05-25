def line_pos():
    front = input('is there a  person in front of you (y/n) ')
    if front == 'n':
        print('in line_pos function: front of the line')
        return 1
    else:
        ahead_pos = line_pos()
        print('in line_pos function: ahead_pos =', ahead_pos)

        return ahead_pos + 1


print('What is my position in this line?')
my_pos = line_pos()
print('I am at position', my_pos)
