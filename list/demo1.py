# create list using range()
# range(start, stop, stepsize)
lst = range(10)
print(lst)
print(type(lst))
lst1 = list(lst)
print(lst1)
print(type(lst1))

r = range(0,12,2)
lst = list(r)
print(lst)
print(type(lst))

# concatenation of two lists
x = [1,2,3,4,5]
y = [5,6,5,4,3,7]
print(x+y)
# list always follows insertion order
# if an element is added to the list then the element is placed at the last
# reverse a list
lst = ['sun','mon','tues', 'wed','thus','fri','sat']
#     [-7     -6     -5     -4     -3    -2     -1 ]

i = -1
n = len(lst)
while i>=-n:
    print(lst[i])
    i-=1

# repeatation of lists
print(lst*2)
print(lst*3)
print(lst*4)

# membership on lists
a='mon'
b='sun'
c='sunday'
print(a in lst)
print(b in lst)
print(c in lst)

# aliasing or cloning
x = [12,23,34,35,45]
y=x
print(y)

