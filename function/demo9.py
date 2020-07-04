# local and global variable
def local_var():
    a=1
    a+=1
    print(a)

local_var()
# print(a) error beacuse there is no "a" available outside the function
# when a variable is declared inside the function only then that fucntion is recognized as local varible
# the scope of local varible is limited within that function only.
# but when the varible is called outside then it becomes unrecognisable


# global varible
# it is the varible which can be declared outside the fucntion and can be used throughout the program.
# the scope of this varible is highest and another varible in the samme name cannot be used again.
# it can be accessed outside the function
a=1
def global_var():
    b=2 # local and cannot be accessed outside this function
    print('a = ',a)
    print('b = ',b)

global_var()
print('a = ',a)
# print('b = ',b) error beacuse it is not available

