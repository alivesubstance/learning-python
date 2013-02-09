__author__ = 'mdzhachvadze'

def func():
    x = 4
    return lambda n: x ** n

x = func()
print x(2)