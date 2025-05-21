k=int(input('Enter you number'))
flag=False
if k==1:
    print('Enter correct number')
elif k>1:
    for i in range(2,k):
        if (k%i)==0:
            flag=True
if flag:
    print('number is not prime')
else:
    print('Number is prime.')