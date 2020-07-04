# how to check a number is prime or not.
# A number must have two dividends i.e. 1 and the number itself only.
# algorithm for finding out 5 is prime or not
# take the number and check from 2 to 5 if there is any dividends available or not
# divide each number from 2 to 5 by 5
# take a counter value and assign it 1 if it is prime else if it is 0 then it is not prime.
def prime_check(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x

x = int(input("ENter a number: "))
result = prime_check(x)
if result==1:
    print(x," is a prime number")
else:
    print(x," is not a prime number")
