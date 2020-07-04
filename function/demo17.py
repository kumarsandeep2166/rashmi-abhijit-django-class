# Function decorator
# decorators are the type of functions which are applied on another function to return it and modify it.
# decorators accepts a function as a parameter and returns a function.
# it takes the result of a function, modifies it and returns it.

def outer(fun):
    def inner():
        value = fun()
        return value+2
    return inner

def num():
    return 10

# result is also a function as outer() returns a function
result = outer(num)
print(result())
