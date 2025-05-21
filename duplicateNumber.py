lst=[1,2,3,4,3,2,1,2,1]
ls=[]
for i in lst:
    if i not in ls:
        ls.append(i)
    else:
        continue
        

for j in ls:
    print(f'{j}',f":",f"{lst.count(j)}")
