total=0
count=0
integ=int(input('enter a number: '))

while total<100:
    count+=1
    total+=integ
    integ=int(input('enter a number: '))

average=total/count

print('sum is',total,'average is',average)
