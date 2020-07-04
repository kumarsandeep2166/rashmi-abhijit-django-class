def display(lst):
    for i in lst:
        print(i)

print("enter group of strings")
lst = [x for x in input().split(',')]
display(lst)