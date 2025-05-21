lst=[23,45,67,10,2,13,67,88]
large=lst[0]

for i in lst:
    if i > large:
        large=i

print('Largest number is ',large)
