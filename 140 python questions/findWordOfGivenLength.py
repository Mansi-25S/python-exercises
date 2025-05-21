def greaterFruit(lst,p):
    lk=[]
    for i in lst:
        if len(i) > p:
            lk.append(i)
    return lk



word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon fruit","Papaya",'Orange','watermelon']
n=7

lst=greaterFruit(word_list,n)

for i in lst:
    print(i)