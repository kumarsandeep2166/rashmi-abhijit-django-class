# reduce function
# reduce(function, sequence)
# to use reduce we have to import functools module
# reduce function limits a sequence to a single value
from functools import *
lst = [1,2,3,4,5,6,7]
result = reduce(lambda x,y:x*y, lst)
print(result)
