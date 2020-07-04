# using lambda with filter()
# filter(function, sequence)
# filter() is useful to filter out the elements of a sequence depending on the result of a function
# it results out another list as an output while it takes a list as an input
def is_even(x):
    if x%2==0:
        return True
    else:
        return False


lst = [12,32,23,44,67,89,65,45,38]
# def filter(function: None/ XYZ, iterable: Iterable[Optional[_T]])
# filter(function or None, iterable) --> filter object
# Return an iterator yielding those items of iterable for which function(item) is true. 
# if function is None, return the items that are true.
lst1=list(filter(is_even, lst))
print(lst1)

# another way
lst2 = list(filter(lambda x: (x%2==0),lst))
print(lst2)
