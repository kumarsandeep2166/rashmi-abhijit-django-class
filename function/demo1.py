# how to check a number is even or odd taking input
def even_odd(a):
    # check the number is even or odd
    if a%2==0:
        print("num is even")
    else:
        print("num is odd")

x=int(input('enter a number: '))
even_odd(x)
