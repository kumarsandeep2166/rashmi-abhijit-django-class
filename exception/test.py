# try:
#     date = eval(input('enter a date:'))

# except SyntaxError:
#     print('invalid date entered')

# else:
#     print('you have entered:', date)
try:
    name = input('enter file name:')
    f = open(name, 'r')
except IOError as ie:
    print('file not found')
else:
    n = len(f.readlines())
    print(name ,'has', n, 'lines')
finally:
    print('file is closed')
    f.close()