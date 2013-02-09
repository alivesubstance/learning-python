__author__ = 'mdzhachvadze'

l1 = [None]
l2 = []

if l2:
    print "true"
else:
    print "false"

if l1:
    print "true"
else:
    print "false"


n1 = None
n2 = None
print n1 == n2, n1 is n2, n1 < n2, n1 > n2

print 1 + True
print 1 - False

tru = bool(1)
false_ = bool({})
print tru, false_

print type(tru)
print type(type(tru))