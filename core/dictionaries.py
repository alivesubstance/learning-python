__author__ = 'mdzhachvadze'

dict = {}
l = 'l'
dict[l] = 1
print dict



m = 'mirik'
rec = {
    'name': [m, 'dani'],
    'age': {m: 22}
}

d = {'a': 1, 'b': 2, 'c': 3}
keys = d.keys()
print keys
keys.sort()
print keys

for key in d:
    print key, "=>", d[key]

if d.has_key('r'):
    print 'hit'
else:
    print 'miss'


