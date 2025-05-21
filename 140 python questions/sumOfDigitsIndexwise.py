temp=int(input('Enter number'))
num=str(temp)

result= sum(int(i)**(index+1) for index, i in enumerate(num))

if result==temp:
    print('disarium number')
else:
    print('Not a disarium number')
