# sorting of elements in dictionary
d = {10:'red', 12:'blue', 13:'orange', 5:'black',20:'white',15:'purple', 23:'pink'}
# key wise sorting
c1 = sorted(d.items(), key=lambda t: t[0] )
print('key wise sorting: ', c1)
# value wise sorting
c2 = sorted(d.items(), key= lambda t:t[1])
print('value wise sorting: ', c2)

# convert lists into dictionary 
x = ['a','b','c','d','e','f','t']
y = [12,23,43,56,87,89]
z = zip(x,y)
d = dict(z)
print(d)
