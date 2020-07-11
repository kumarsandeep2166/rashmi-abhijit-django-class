# how to update elements into dictionary
d = {}
n = int(input('how many elements: '))
for i in range(n):
    k = input('enter the key : ')
    v = input('enter the value: ')
    d.update({k:v})


print('the new dictionary is')
print('-----------------------')
for k,v in d.items():
    print('key = {} value = {}'.format(k,v))

print(d)
print('-----------------------')
print('the keys are:')
for k in d.keys():
    print(k)
print('-----------------------')
print('the values are:')
for v in d.values():
    print(v)