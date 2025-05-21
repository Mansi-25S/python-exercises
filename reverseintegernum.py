num=int(input('Enter number'))
sum=0
p=num
t=num
ct=0
while p>0:
    ct+=1
    p=p/10
print (p)
while num>0:
    temp=num%10
    sum=sum*10+(temp**p)
    num=num//10

print(sum)
if (t==sum):
    print('Armstring')
else:
    print('not')