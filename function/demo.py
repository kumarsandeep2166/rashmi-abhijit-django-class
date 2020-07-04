# calling of functions
# 1st way
def add():
    a=10
    b=20
    c=a+b
    print("sum of a,b is:",c)
    print("sum of {},{} is: {}".format(a,b,c))

add()

# 2nd way
# in this case the function only prints the output when it is called inside a print statement
def add1(a,b):
    c = a+b
    return c

print("sum of a and b is: ",add1(10,12))
print("sum of a and b is: ",add1(10.25,12.56))

# 3rd way
# multiple return statement
def sum(a,b):
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    g=a%b
    h=a//b
    i=a**b
    return c,d,e,f,g,h,i

print(sum(12,3))
q,w,e,r,t,y,u = sum(12,3)
print("sum is: ",q)
print("sub is: ",w)
print("multiplication is: ",e)
print("division is: ",r)
print("modulus is: ",t)
print("floor division is: ",y)
print("exponention is: ",u)

# 4th way
def another(a,b):
    c = a+b
    return c

x=another(12,34)
print("sum is:",x)
