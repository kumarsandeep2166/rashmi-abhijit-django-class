# find out first occurance of an element in a tuple
# tup = (12,23,43,23,12,34,45,67)
# take inputs in the form of string separated by commas
str = input('enter elements:').split(',')
# store all the elements in the form of list
lst = [int(num) for num in str]
# list is converted to tuple
tup = tuple(lst)

x = int(input('enter the element to search:'))
try:
    pos = tup.index(x)
    print('index of 12 is:', pos+1)
except:
    print('item not present')