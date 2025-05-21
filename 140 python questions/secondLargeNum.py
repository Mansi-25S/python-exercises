lst=[23,342,535,366,266,235,757]
lst.sort(reverse=True)
if len(lst)>=2:
    number=lst[1]
    print('Second large number is ',number)
else:
    print('Do not have second large number ')
    