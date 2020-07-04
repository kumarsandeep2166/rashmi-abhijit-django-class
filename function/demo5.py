# functions are first class objects
# it is possible to assign a function to a variable.

def fun():
    i = int(input("enter a number: "))
    return i

x=fun()
print(x)

# it is possible to define a function inside another function
def message(str):
    def fun():
        return "Hello "

    res = fun()+str
    return res

print(message("Python!!!!!"))

# it is possible to pass a functions as parameter to another function
def display(fun):
    return "Hello "+fun

def call():
    return "python!!!!"

print(display(call()))



# it is possible that a fucntion can return another function
def myfun():
    def anotherfun():
        return "Hello Moto!!!!!"
    
    return anotherfun

x=myfun()
# when myfun is assigned over "x" then x also becomes a new function
print(x())