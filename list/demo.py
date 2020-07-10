lst = [12,23,34,45, 'python', 'arpita',12.45,10+6j]
# extract all elements from list
for i in lst:
    print(i)
print('----------------------')
# extract each element using while loop
i=0
n= len(lst)
while i<n:
    print(lst[i])
    i+=1

# slicing
# lst[start:end:step size]
print(lst[0:7:2])
print(lst[::-1]) #reverse the list elements
print(lst[0])
print('extract elements from 2nd to 7th element from list')
for i in lst[2:7]:
    print(i)