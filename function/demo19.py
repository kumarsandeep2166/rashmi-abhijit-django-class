# a program to create 2 decorators

def decor(fun):
    def inner():
        value = fun()
        return value+2
    return inner

def decor1(fun):
    def inner():
        value = fun()
        return value*2
    return inner

@decor1
@decor
def num():
    return 10

print(num())
# result = decor(decor1(num))
# print(result())
# modified_result = decor1(decor(num))
# print(modified_result())

