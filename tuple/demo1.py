# empty tuple
tup = ()
print(tup)

# tuple with one element
# tuple with one element always follwed by comma
tup = (1,)
print(tup)
print(type(tup))
tup = (1)
print(tup)
print(type(tup))

tup=(12,23,43,45.43,'hyderabad')
print(tup)
for i in tup:
    print(i)
# tup[3]=34
# print(tup) tuple object doen't support item assignment
# basic operation
print(len(tup))
print(tup*3)
t1 = tup*3
print(t1)
print(tup)

# functions of tuple
tup= (12,23,43,54,56,43,43,76,79,78)
print('length or size of tuple: ', len(tup))
print('max  of tuple: ', max(tup))
print('min of tuple: ', min(tup))
print('index of 43: ', tup.index(43))
print('count the number of 43 : ', tup.count(43))
print('ascending sorted tuple=', sorted(tup))
print('descending sorted tuple=', sorted(tup, reverse=True))

