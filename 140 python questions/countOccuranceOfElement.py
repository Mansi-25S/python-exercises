lst=[23,34,56,34,76,87,88,88,56,34,23]
p=[]
for i in lst:
    if i in p:
        continue
    else:
        p.append(i)
        print(i,'=>',lst.count(i))