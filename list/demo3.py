# sort the elements using bubble sort technique
# take an empty list
x = []

# store the elements into the array
n = int(input('enter the number of elements: '))

# append the elements into the list
i = 0
while i<n:
    x.append(input('enter the elements: '))
    i+=1
print('the original list is: ', x)
# bubble sort technique
flag = False
# outer loop will continue that much number of elements are present
# inner loop will check each element and will continue that much number of times
for i in range(n-1):
    for j in range(n-1-i): # j wil continue 1 leeser than i
        if x[j]>x[j+1]:
            t = x[j]
            x[j] = x[j+1] # here the smallest element is assigned to the biigest element
            # or the next index value is assigned to current index value if current index is greater than next index
            x[j+1] =t
            flag = True #swapping done, hence flag is True
    if flag == False: # if no swapping then list is in sorted order
        break #come out of loop
    else:
        flag=False #assign the initial value to flag
print('sorted list is:', x)

# [20, 10, 30, 15, 12]
# [10, 20, 30, 15, 12]
# [10, 20, 15, 12, 30]
# [10, 15, 12, 20, 30]
# [10, 12, 15, 20, 30]

# for 0 in range(4):
    # for j in range(4) no of time: 4
# for 1 in range(4):
    # for j in range(5-1-1)no of time: 3
# for 2 in range(4):
    # for j in range(5-1-2)no of time: 2
# for 3 in range(4):
    # for j in range(5-1-3)no of time: 1
# for 4 in range(4):not valid case
    # for j in range(5-1-4)

