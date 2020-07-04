# generate the prime number series 
# logic
# take an input upto which the series is going to be displayed.
# start a loop from 2.
# make the loop true for each time a number get checked.
# make a counter value that counts the prime numbers.

def prime_check(n):
    x=1
    for i in range(2,n):
        if n%i==0:
            x=0
            break
        else:
            x=1
    return x

x = int(input("how many prime numbers required? "))
i=2
c=1
while True:
    if prime_check(i):
        print(i)
        c+=1
    i+=1
    if c>x:
        break

