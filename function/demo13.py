# find out factorial of a number using recursion
# when a function calls itself then it is called as recursion
def factorial(n):
    if n==0:
        result=1
    else:
        result = n*factorial(n-1)
    return result
# result = n*factorial(n-1) 
# factorial(5) = 5*factorial(4)
            # = 5*4*factorial(3)
            # = 5*4*3*factorial(2)
            # = 5*4*3*2*factorial(1)
            # = 5*4*3*2*1*factorial(0)

print('factorial of 5 is: ', factorial(5))
for i in range(1,11):
    print("factorial of {} is {}".format(i, factorial(i)))
