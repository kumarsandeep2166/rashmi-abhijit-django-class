import Emp, pickle
f = open('emp.dat', 'wb')
n = int(input('how many number of employees: '))
for i in range(n):
    id = int(input('enter id: '))
    name = input('enter name: ')
    sal = float(input('enter sal: '))

    e = Emp.Emp(id, name, sal)
    pickle.dump(e, f)
f.close()