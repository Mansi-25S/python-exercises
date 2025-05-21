lst=[23,34,23,53,65,75,5]

smallest=lst[0]

for i in lst:
    if i<smallest:
        smallest=i

print('Smallest number is ',smallest)