def Is_happynum(num):
    see=set()
    while num !=1 and num not in see:
        see.add(num)
        num=sum(int(i)**2 for i in str(num))
    return num==1


happy_num=[]
for i in range(1,101):
    if Is_happynum(i):
        happy_num.append(i)
print(happy_num)