# storing different element into list by taking inputs

emp = []
n = int(input('howmany employees: '))

for i in range(n):
    print('enter id: ')
    emp.append(int(input()))
    print('enter name: ')
    emp.append(input())
    print('enter salary: ')
    emp.append(input())

print('the list is: ', emp)
id = int(input('enter the id: '))
for i in range(len(emp)):
    if id == emp[i]:
        print('id= {}, name is: {}, sal is:{}'.format(emp[i], emp[i+1], emp[i+2]))