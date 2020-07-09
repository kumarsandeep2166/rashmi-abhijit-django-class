# howmany times an element is occured in the list
x = []
n = int(input("enter how many elements: "))
for i in range(n):
    x.append(int(input('enter the element: ')))

print('the original list is: ', x)
y = int(input('enter the element to count: '))
c=0
for i in x:
    if y==i:
        c+=1

print(y, ' is repeated ',c, ' times' )
 