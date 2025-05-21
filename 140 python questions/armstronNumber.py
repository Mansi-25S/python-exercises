num=input('Enter number')
ct=len(num)
tmp=int(num)
sum=0
while tmp>0:
    result=tmp%10
    sum=sum+(result**ct)
    print(sum)
    tmp=tmp//10

if int(num)==sum:
    print('Number is armstrong')
else:
    print('Number is not armstrong')