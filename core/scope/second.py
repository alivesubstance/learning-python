__author__ = 'mdzhachvadze'

var = 9

def glob1():
    global var
    var += 1

def glob2():
    var = 0

    import second
    second.var += 1

def glob3():
    var = 0

    import sys
    module = sys.modules["second"]
    module.var += 1

def test():
    print "orginal ", var
    glob1()
    print "after glob1() ", var
    glob2()
    print "after glob2() ", var
    glob3()
    print "after glob3() ", var
    print "result ", var
