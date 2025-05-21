def is_happys(en):
    go = set()
    while en!=1 and en not in go():
        go.add(en)
        en=sum(int(en)**2 for i in str(en))        
    return en==1

enn=int(input('enter number'))
if is_happys(enn):
    print('Is happy number')
else:
    print('Not a happy number')
