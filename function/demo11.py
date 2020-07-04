# passing a group of elements to a function
def calculate(lst):
    """find out the sum and average of all values of list"""
    sum = 0    
    n=len(lst) # total length of list
    for i in lst:
        sum+=i
        avg = sum/n
    return sum, avg

# take mutiple inputs in a single line
lst = [int(x) for x in input().split(',')]

x,y =calculate(lst)
print('total = ',x)
print('average=',y)

