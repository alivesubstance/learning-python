from copy import deepcopy

__author__ = 'mdzhachvadze'

l = [1, '2', 3.14]
print l + [3, 4]

print l[-1]

m = [[1, 2, 3], [4, 5, 6], [7, 8]]
col2 = [col[0] for col in m]
print col2

m = [c * 2 for c in 'spam']
print m

l2 = [1, 2, 3]
l3 = l2 * 3
l4 = [l2] * 3
l4_orig = deepcopy(l4)
l2[0] = 0
print l3
print l4_orig, l4

l5 = [1, 2, 3, 4]
print "map(lambda x: 2 ** x, l5)=", map(lambda x: 2 ** x, l5)

l5_sqr = [(lambda x: 2 ** x)(x) for x in l5]
print "len(l5_sqr)=", len(l5_sqr)
for i in l5_sqr:
    print i