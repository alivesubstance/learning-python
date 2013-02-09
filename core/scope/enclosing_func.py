__author__ = 'mdzhachvadze'

x = 1

print "global before ", x

def main_func():
    x = 2

    def encl1():
        print "encl1() ", x

    encl1()

    def encl2():
        global x
        x += 3
        print "encl2() ", x

        def encl2_1():
            print "encl2_1() ", x

        encl2_1()

    encl2()
    print "main_func() ", x

main_func()

print "global after ", x