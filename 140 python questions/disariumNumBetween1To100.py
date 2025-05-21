def is_disarium(numb):
    mystr=str(numb)
    result=sum( int(k)**(index+1) for index,k in enumerate(mystr))
    return numb==result

first=int(input('Enter 1st NUMBER'))
second=int(input('Enter 2nd NUMBER'))

disarium_num=[i for i in range(first,second+1) if is_disarium(i)]
print('disarium number are as follows')
for i in disarium_num:
    print(i)
