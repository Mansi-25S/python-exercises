lst=[23,34,56,78,45,22,65,44,77]
p=[]
for i in lst:
    if i%2==0:
        continue
    else:
        p.append(i)

print('All odd number are ')
for i in p:
    print(i)