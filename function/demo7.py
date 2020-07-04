# call by reference
lst=[12,23,34,45,67]
print("the length and id of list before modifying is: ", len(lst), id(lst))

def modify(lst):
    lst.append(90)
    print(lst)
    print("the length and id of list after modifying is: ", len(lst), id(lst))

modify(lst)
