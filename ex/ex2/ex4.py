import math

__author__ = 'jericho'

x = 5
l = [1, 2, 4, 8, 16, 32, 64]

sqr = 2 ** x
for i in l:
    if sqr == i:
        print "at index", l.index(sqr)
        break
else:
    print sqr, "not found"


l2 = [2**i for i in range(6)]
print 'at index ' + str(l.index(sqr)) if sqr in l2 else str(sqr) + ' not found'

l3 = map(lambda x: 2 ** x, range(7))
print l3


