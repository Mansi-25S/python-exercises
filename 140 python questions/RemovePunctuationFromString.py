punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str=""
st=input('Enter String')
for i in st:
    if i not in punctuations:
        my_str+=i

print(my_str)        
