__author__ = 'jericho'

dict = {'a': 1, 'b': 2, 'v': 3, 'o': 4, 'n': 5}

keys = dict.keys()
keys.sort()
for key in keys:
    print key,'=>',dict[key],

print '\n'

for key in sorted(dict.keys()):
    print key,'=>',dict[key],
