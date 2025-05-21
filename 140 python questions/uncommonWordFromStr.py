first=input('Enter 1st string')
second=input('Enter 2nd String')
lst1 = set(first.split())
print(lst1)
lst2=set(second.split())

r=lst1.symmetric_difference(lst2)
uncommenword=list(r)
print(uncommenword)