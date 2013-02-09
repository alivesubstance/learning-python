from __future__ import print_function

__author__ = 'jericho'

def minmax(test, *args):
    rez = args[0]
    for arg in args[0:]:
        if test(rez, arg):
            rez = arg
    return rez


def lessthan(res, arg): return res < arg


def greaterthan(res, arg): return res > arg

print(minmax(lambda x, y: x < y, 1, 4, 2, 3))
print(minmax(lambda x, y: y < x, 1, 4, 2, 3))