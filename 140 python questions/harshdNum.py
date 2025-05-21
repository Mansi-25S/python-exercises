num=int(input('enter number'))
sum=0
for i in str(num):
    sum+=int(i)

print(sum)

if num%sum==0:
    print('Number is harshad number')
else:
    print('Not a harshad Number')