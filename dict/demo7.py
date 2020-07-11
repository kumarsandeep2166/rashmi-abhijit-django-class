# ordered dictionary
from collections import OrderedDict
d= OrderedDict()
d[12]='a'
d[13]='b'
d[14]='c'
d[15]='d'
d[16]='e'
for k,v in d.items():
    print(k, '----',v)
