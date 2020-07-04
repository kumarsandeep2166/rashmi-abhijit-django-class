# how to check a number is even or odd taking input
def even_odd(a):
    # check the number is even or odd
    if a%2==0:
        print("num is even")
    else:
        print("num is odd")

x=int(input("Enter the number: "))
even_odd(x)