def removeIndexFromStr(mystr,remove_num):
    if remove_num<0 or remove_num>len(mystr):
        return "Invalid entry"
    else:
        res=mystr[:remove_num]+mystr[remove_num+1:]
        return print('The remove string is ',res)


p=input('Enter String')
n=int(input('Enter number of charater to remove'))
temp=removeIndexFromStr(p,n)
print(temp)