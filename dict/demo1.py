# basic dictionary
d = {'name':'x', 'college': 'ASMIT', 'year':'2nd'}
print('name is: ',d['name'])
print('college is: ',d['college'])
print('year is: ',d['year'])
# the value can be accessed through key only.
# return all the keys and values
print('all the keys are:', d.keys())
print('all the values are:', d.values())

d={'a':12, 'b':13,'c':14,'d':15,'e':16,'f':10, 'g':13,'a':17}
print(d)
print('all the items are:', d.items())
d1 = d.copy()
print(d1)
s = sum(d.values())
print('sum of all values of d is:', s)
d.update({'k':89})
print(d)
