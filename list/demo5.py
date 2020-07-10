# finding common eleemnts in 2 lists
s1 = [1,2,3,4,5,6,7]
s2 = [4,5,6,7,8,9,10]

x= set(s1)
y = set(s2)
z=x.intersection(y)
lst = list(z)
print(lst)