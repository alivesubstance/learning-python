__author__ = 'mdzhachvadze'

x = set([1,2,3])
y = set((1,2))

print x - y
print y - x

z = set(['1', '2'])
print x - z
print x | z