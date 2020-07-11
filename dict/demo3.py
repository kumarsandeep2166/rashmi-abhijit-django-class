# write a program to create a dictionary of players and their runs
# and retrieve run scored by players
x =   {}
n = int(input('enter howmany element:'))
for i in range(n):
    k = input('Enter players name:')
    v = int(input('Enter score:'))
    x.update({k:v})

print('the players are:', list(x.keys()))
name = input('enter player name:')
runs = x.get(name, -1)
if(runs==-1):
    print('player not found')
else:
    print('{} made {} runs'.format(name, runs))
    

