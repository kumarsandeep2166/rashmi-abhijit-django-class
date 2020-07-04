# find out factorial of a number
# 5! = 5*4*3*2*1
# 10! = 10*9*8*7*6*5*4*3*2*1
def fact(n):
    # logic for finding factorial
    f = 1
    while (n>=1):
        f*=n
        n-=1
    return f

print("factorial of n is :", fact(5))
print("factorial of n is :", fact(10))

# display factorial of numbers from 1 to 10
# range() is itself an array
for i in range(1,11):
    print("factorial of {} is:{}".format(i, fact(i)))
