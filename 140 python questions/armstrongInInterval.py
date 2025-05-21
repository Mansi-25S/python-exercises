low=int(input('Enter lower limit'))
upp=int(input('enter upper limit '))
lst=[]
for i in range(low,upp+1):
    ct=len(str(i))
    sum=0
    tmp=i
    while tmp>0:
        result=tmp%10
        sum=sum+(result**ct)
        tmp=tmp//10
    if i==sum:
        lst.append(sum)
    else:
        continue
print('List Of armstrong number is ')
for i in lst:
    print(i)
    