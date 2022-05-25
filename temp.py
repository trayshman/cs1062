
# temp=int(input('Enter a room temperature '))
# if temp >= 65 and temp <= 80:
#     print('The temperature is good')
# elif temp < 65:
#     print('Turn the heat on')
# else:
#     print('Turn the AC on')

temp=int(input('Enter a room temperature '))
if temp > 80:
    print('Turn the AC on')
elif temp < 65:
    print('Turn the heat on')
else:
    print('The temperature is good')
