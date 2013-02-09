from __future__ import print_function

def myzip(*seqs):
    lengths = [len(s) for s in seqs]
    minlen = min(lengths)
    return (tuple(s[i] if i < len(s) else None for s in seqs) for i in range(max(lengths)))

print(list(myzip("124", 'abcdef')))
print(zip('124', 'abcde', '!@#'))


def mymap_java_style(func, *seqs):
    res = []
    for i in range(len(seqs)):
        arr = []
        for e in seqs[i]:
            arr.append(func(e))
        res.append(arr)
    yield res

def mymap_python_style(func, *seqs):
    return [(func(e) for e in seqs[i]) for i in range(len(seqs))]

print(mymap_java_style(lambda x:x * 2, '123', 'abcdef'))
mymap_generator = mymap_python_style(lambda x: x * 2, '123', 'abcdef')

for g in iter(mymap_generator):
    print(list(g))


