import random


userString=input('enter a string: ')
upper=random.randint(0,len(userString)-1)
caps=''
print('Letters all uppercase starting at position',upper)
for i in userString[upper:]:
    b=i.upper()
    caps+=b

print(userString[:upper],end='')
print(caps)
