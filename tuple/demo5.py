# insert an element into a tuple
# x = [10, 20, 30, 40, 50, 60]
#      0   1   2   3   4   5
nums = (10,20,30,40,50,60)
print(nums)
pos = int(input("enter the position number:"))

# copy from 0th element to pos-1 into another tuple i.e. num1
num1 = nums[0:pos-1]
print(num1)
lst = [int(input('enter the number u want to insert:'))]
new = tuple(lst)
num1 = num1+new
print(num1)
nums = num1+nums[pos-1:]
print(nums)

# 'pos'
# 0 to pos-1 + new element + pos-1 to all 