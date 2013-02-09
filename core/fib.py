__author__ = 'mdzhachvadze'

def fib(n):
    rezult = []
    a, b = 0, 1
    while a < n:
#        print a,
        a, b = b, a + b
        rezult.append(a)
    return rezult

fib100 = fib(321)
print fib100
