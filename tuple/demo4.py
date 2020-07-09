# sorting of a nested tuple
# tuple inside a tuple is called a nested tuple
tup = (10,20,30,40,50,(10,20,30,40,50),(23,12,24,34,45))
print(tup)
print(tup[5])
print(tup[5][0])
print(tup[5][1])
print(tup[5][2])
tup = ((12,'x',123.34),(13,'y',14356.90),
        (10,'z',12345.90),(11,'q',12349.00),(16,'w',1908.90))
print(tup)
print(sorted(tup))
print(sorted(tup, reverse=True))
print(sorted(tup, key=lambda x: x[1]))#sorting through letter
print(sorted(tup, key=lambda x: x[2]))#sorting through second element

