# coverting a strin into a dictionary
str = 'a=12,b=23,5=y,3=z,c=15'
lst = []
for i in str.split(','):
    y = i.split('=')
    lst.append(y)
print('the new list: ', lst)
d = dict(lst)
print('the converted dict is:', d)
d1={}
for k,v in d.items():
    d1[k]=v
print('the final dictionary is:', d1)

