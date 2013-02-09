from __future__ import print_function

def seq(a, b=2, *seq):
    print("a=", a)
    print("b=", b)
    for idx, i in enumerate(seq):
        print("seq[", idx, "]=", i)

seq("a", 1, 2, 3)

def dict_func(**dict):
    for key in dict:
        print(key, "=>", dict[key])

