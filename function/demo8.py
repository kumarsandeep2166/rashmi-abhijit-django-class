# arguments
# formal arguments
# actual arguments
def sum(a,b): # formal arguments
    c=a+b
    print(c)

x=10; y=20
sum(x,y) # actual argument
# actual arguments are following types

# positional argument

def join(s1,s2,s3):
    s4= s1+s2+s3
    print(s4)

join('Hello',' ', 'Python!!!!')

# keyword argument
def store(item, price):
    print('item= {}'.format((item)), 'price= {}'.format((price)))
    print()

store(item='note5', price=12300)
store(price=12300, item='note5')

# default argument
def store1(item, price=1000):
    print('item= {}'.format((item)), 'price= {}'.format((price)))
    print()

store1(item='note5', price=12300)
store1(item='note5')

# variable length argument
def marks(a, b):
    return a+b

x=marks(12,12)
print(x)

# varible length argument
# *args stores all the values in the form of list
def variable_example(a,b, *args):
    print("formal argument is=",a)
    sum=0
    for i in args:
        sum+=i
    print("sum of all elements are=", (a+sum))
    print("sum of  elements in args are=", sum)

variable_example(12,90,34,45,67)

def add(*args):
    sum=0
    for i in args:
        sum+=i
    print("sum of all elements are: ", sum)

add(12,13)
add(12,13,23)
add(12,13,23,45)
add(12,13,67,45,68)


# keyword variable length argument
# kwargs store elements in a dictionary in key and value pair format
# {'a':10, 'b':12, 'c':13, 'd':14}
def display(**kwargs):
    for x,y in kwargs.items(): # items() extracts each key and value associated with the key as pair of elements
        print("key= ",x, "and ", "value is: ", y)

display(name='a', age=10, roll=1234, college='asmit')
display(a=10, b=12, c=13, d=14,e=34,f=45,g=56)


