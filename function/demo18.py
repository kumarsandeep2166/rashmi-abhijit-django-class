# Function decorator
# decorators are the type of functions which are applied on another function to return it and modify it.
# decorators accepts a function as a parameter and returns a function.
# it takes the result of a function, modifies it and returns it.

def outer(fun):
    def inner():
        value = fun()
        return value+2
    return inner

@outer # @outer is the decorator symbol
def num():
    return 10
print(num())

# on the above while calling of num() the num() automatically passed to decorator @outer as a parameter.
# means at first outer() took 'num' as a parameter and returned it.
# so after the call of num() it gets called by outer()
# outer() used num() as a parameter.



