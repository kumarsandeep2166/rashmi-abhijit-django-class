# passing dictionaries into functions
def display(dictionary):
    for k, v in dictionary.items():
        print('key--{} value--- {}'.format(k,v))

d = {'a': '12', 'b': '23', '5': 'y', '3': 'z', 'c': '15'}
display(d)