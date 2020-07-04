# calling of functions
# 2 ways for calling a function
# call by value (pass by value)
# call by reference (pass by reference)

# call by value
def myfun(x):
    x=13
    print(x, id(x))

x=15
myfun(x)
print(x, id(x))

def myfun1(x):
    x=13
    print(x, id(x))

y=15
myfun1(y)
print(y, id(y))

# local varible
# this varible says that if a varible is used inside a function then the life time limits upto that function exists.
# after the job of functions gets over then the scope of variable also over.
# the preference of local varible inside a function is always top most.