def isBinaryOrNot(st):
    for i in st:
        if i in '01':
            return True
    return False

st=input('Enter a string')
p=isBinaryOrNot(st)
if p:
    print('String is binary')
else:
    print('String is not  binary')
    
