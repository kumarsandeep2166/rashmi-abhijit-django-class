import Emp, pickle
f = open('emp.dat', 'rb')
print('employee data')
print('---------------')
while True:
    try:
        obj = pickle.load(f)
        obj.display()
    except EOFError:
        print('end of file reached')
        break
f.close()
