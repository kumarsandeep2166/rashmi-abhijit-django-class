# list comprehension
# use of matrix
mat = [[1,2,3],[3,4,5],[4,5,6]]
print(mat)
# display elements row by row
print('row by row')
for i in mat:
    print(i)

print('elements in 1st row')
for i in mat[0]:
    print(i)
print('elements in 2nd row')
for i in mat[1]:
    print(i)
print('elements in 3rd row')
for i in mat[2]:
    print(i)

print('---------------')
print(mat[0][0])
print(mat[0][1])
print(mat[0][2])
print(mat[1][0])
print(mat[1][1])
print(mat[1][2])
print(mat[2][0])
print(mat[2][1])
print(mat[2][2])
print('---------------------')
print('all elements in mat ')
for i in range(len(mat)):
    for j in range(len(mat[i])):
        print(mat[i][j])

print('------------------')
# list comprehension
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

# add each element of 1 list with another
l1= [1,2,3]
l2= [2,3,4]
l3=[]
for i in l1:
    for j in l2:
        l3.append(i+j)
print(l3)
l1= [1,2,3]
l2= [2,3,4]
l3 = l1+l2
print(l3)