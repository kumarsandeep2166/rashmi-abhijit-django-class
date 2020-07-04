# use of 'global' keyword
a=1
def myfun():
    a=2
    print('a = ',a)

myfun()
print(a)

c=1
def display():
    global c
    print('global value c=',c) # 1
    c=2
    print('after modification value of c is: ', c) # 2

display()
print('outside function value of c is: ', c) # 2
# when a varible is declared with global keyword and after any modification the value is changd to 
# currently assigned value. or to the changed value.
