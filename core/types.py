__author__ = 'mdzhachvadze'

import types

print type([1]) == type([])
print type([1]) == list
isinstance([1], list)

def f():
    pass

print type(f) == types.FunctionType


print type((4))
print type((4,))