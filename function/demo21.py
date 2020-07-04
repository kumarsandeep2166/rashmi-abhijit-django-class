# Generator
# generators are the functions that are used to return a sequence of values.
# it is defined as an ordinary function statement but uses 'yields' keyword.
def mygen(x,y):
    while x>=y:
        yield y
        y+=1

g=mygen(10,5)

for i in g:
    print('i= ',i)
# incase of generator in python the meaning of yield statement is as same as the return statement

# def next(i: Iterator[_T])
# Return the next item from the iterator. If default is given and the iterator is exhausted,
#  it is returned instead of raising StopIteration.
def kaigen():
    yield 'a'
    yield 'b'
    yield 'c'
    yield 'd'

h =kaigen()
print(next(h))
print(next(h))
print(next(h))
print(next(h))
# print(next(h)) gives error
