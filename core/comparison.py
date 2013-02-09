__author__ = 'mdzhachvadze'

d1 = {"a":1}
d2 = {"a":1, }

print d1 < d2

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print L1 < L2, L1 == L2, L1 > L2

print 1 > 'spam' # error in python 3+