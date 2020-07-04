# using lambda with map function
# map(function, sequence)
# using map() we can perform some action on the elements present in the sequence.
# it is also simmilar to filter() but it acts on each element and may change the elements.

# find out squares of each element present in the list

# def map(func: Callable[[_T1], _S], iter1: Iterable[_T1])
# map(func, *iterables) --> map object

# Make an iterator that computes the function using arguments from each of the iterables.
#  Stops when the shortest iterable is exhausted.
def squares(x):
    return x*x

lst = [1,2,3,4,5,6,7,8,9]

lst1 = list(map(squares, lst))
print(lst1)

# another way
lst2 = list(map(lambda x: x*x, lst))
print(lst2)