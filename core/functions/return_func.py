__author__ = 'mdzhachvadze'

def f1():
    x = 8
    def f2():
        print x
    return f2

action = f1()
print action
action()