# anonymous function or lambdas
def square(x):
    return x*x

x=square(10)
print(x)

# lambdas are used to express the function in a single line
# lambda argument_list : expression
# lambda argument_list(variables) : expression

f = lambda x: x*x
print(f(5))
print(f(10))

# calculate sum of two numbers

f = lambda x,y: x+y
print(f(5,2))

# find out biggest number between 2 numbers

big = lambda x,y: x if x>y else y
# result condition condition result
a,b = [int(x) for x in input('enter two numbers: ').split(',')]
print('biggest between a and b is:', big(a,b))

# [int(x) for x in input().split(',')]
# take multiple inputs from the same line 
a,b,c = [int(x) for x in input('enter some numbers:').split(',')]
print(a,b,c)
